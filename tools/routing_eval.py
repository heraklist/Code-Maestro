from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path
from statistics import mean, pstdev
from typing import Sequence


CAPABILITY_IDS = frozenset({"requirements-architecture-systems","product-ux-ui","software-implementation","debugging-diagnostics","testing-assurance","review-audit-compliance","security-trust","privacy-data-lifecycle","database-data","interface-protocol-contract","build-toolchain-environment","migration-compatibility","performance-capacity","cicd-platform-delivery","reliability-observability-sre-incident","ai-llm-agent-mcp","research-experimental-language"})
CLUSTERS = frozenset({"build-ci-debug","implementation-debug","testing-review","security-privacy","database-interface","migration-implementation","performance-reliability","product-frontend","research-language-freshness","ai-interface-security"})
SOURCE_KINDS = frozenset({"legacy-request", "legacy-issue", "legacy-eval", "current-project-task", "synthetic"})
REAL_DERIVED_SOURCE_KINDS = frozenset({"legacy-request", "legacy-issue", "legacy-eval", "current-project-task"})


@dataclass(frozen=True)
class RoutingCase:
    id: str; cluster: str; prompt: str; expected_primary: str; expected_supporting: tuple[str, ...]; clarification_required: bool; high_risk: bool; source_kind: str; source_ref: str; source_transform: str

@dataclass(frozen=True)
class RoutingResult:
    case_id: str; primary: str; supporting: tuple[str, ...]; clarification_required: bool

@dataclass(frozen=True)
class RunMetrics:
    primary_correct: int; primary_total: int; supporting_exact_correct: int; supporting_total: int; clarification_correct: int; clarification_total: int; unknown_capability_ids: int; malformed_results: int; high_risk_correct: int; high_risk_total: int; per_cluster_primary: dict[str, tuple[int, int]]

@dataclass(frozen=True)
class RunManifest:
    run_id: str; runtime_surface: str; provider: str; model_id: str; model_version: str; configuration: str; corpus_sha256: str; skeleton_sha256: str; grader_version: str; started_at: str; result_path: str

@dataclass(frozen=True)
class AggregateMetrics:
    run_count: int; worst_run_id: str; primary_min: float; primary_max: float; primary_mean: float; primary_pstdev: float; supporting_min: float; supporting_max: float; supporting_mean: float; supporting_pstdev: float; clarification_min: float; clarification_max: float; clarification_mean: float; clarification_pstdev: float; green: bool


def _load_json_list(path: Path) -> list[dict]:
    try: payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc: raise ValueError(f"cannot load JSON from {path}: {exc}") from exc
    if not isinstance(payload, list): raise ValueError(f"expected JSON array in {path}")
    if not all(isinstance(item, dict) for item in payload): raise ValueError(f"expected array of objects in {path}")
    return payload

def _required_string(item: dict, field: str) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value.strip(): raise ValueError(f"{field} must be a non-empty string")
    return value.strip()

def _required_bool(item: dict, field: str) -> bool:
    value = item.get(field)
    if not isinstance(value, bool): raise ValueError(f"{field} must be a boolean")
    return value

def _canonical_capability_tuple(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value): raise ValueError(f"{field} must be an array of capability IDs")
    normalized = tuple(sorted(set(value))); unknown = [item for item in normalized if item not in CAPABILITY_IDS]
    if unknown: raise ValueError(f"{field} contains unknown capability IDs: {unknown}")
    return normalized

def load_cases(path: Path) -> list[RoutingCase]:
    rows = _load_json_list(path); cases=[]; seen=set()
    for row in rows:
        case_id=_required_string(row,"id")
        if case_id in seen: raise ValueError(f"duplicate case id: {case_id}")
        seen.add(case_id); cluster=_required_string(row,"cluster")
        if cluster not in CLUSTERS: raise ValueError(f"unknown cluster: {cluster}")
        primary=_required_string(row,"expected_primary")
        if primary not in CAPABILITY_IDS: raise ValueError(f"unknown expected capability id: {primary}")
        source_kind=_required_string(row,"source_kind")
        if source_kind not in SOURCE_KINDS: raise ValueError(f"unknown source_kind: {source_kind}")
        source_ref=row.get("source_ref","")
        if not isinstance(source_ref,str): raise ValueError("source_ref must be a string")
        if source_kind != "synthetic" and not source_ref.strip(): raise ValueError("source_ref is required for real-derived cases")
        cases.append(RoutingCase(case_id,cluster,_required_string(row,"prompt"),primary,_canonical_capability_tuple(row.get("expected_supporting"),"expected_supporting"),_required_bool(row,"clarification_required"),_required_bool(row,"high_risk"),source_kind,source_ref.strip(),_required_string(row,"source_transform")))
    return cases

def validate_corpus_composition(cases: Sequence[RoutingCase]) -> dict:
    case_count=len(cases)
    if case_count < 100: raise ValueError(f"full routing corpus requires at least 100 cases; got {case_count}")
    ids=[case.id for case in cases]
    if len(ids)!=len(set(ids)): raise ValueError("full routing corpus contains duplicate case IDs")
    cluster_counts=Counter(case.cluster for case in cases); missing={cluster:cluster_counts.get(cluster,0) for cluster in CLUSTERS if cluster_counts.get(cluster,0)<10}
    if missing: raise ValueError(f"every ambiguity cluster requires at least 10 cases: {dict(sorted(missing.items()))}")
    real=sum(case.source_kind in REAL_DERIVED_SOURCE_KINDS for case in cases)
    if real*3 < case_count: raise ValueError(f"at least one third of the corpus must be real-derived; got {real}/{case_count}")
    return {"case_count":case_count,"real_derived_count":real,"cluster_counts":dict(sorted(cluster_counts.items()))}

def load_results(path: Path) -> list[RoutingResult]:
    rows=_load_json_list(path); results=[]; seen=set()
    for row in rows:
        case_id=_required_string(row,"case_id")
        if case_id in seen: raise ValueError(f"duplicate result case_id: {case_id}")
        seen.add(case_id); primary=_required_string(row,"primary")
        if primary not in CAPABILITY_IDS: raise ValueError(f"unknown actual capability id: {primary}")
        results.append(RoutingResult(case_id,primary,_canonical_capability_tuple(row.get("supporting"),"supporting"),_required_bool(row,"clarification_required")))
    return results

def grade_run(cases: Sequence[RoutingCase], results: Sequence[RoutingResult]) -> RunMetrics:
    by_id={r.case_id:r for r in results}; case_ids={c.id for c in cases}; malformed=len(set(by_id)-case_ids)+sum(c.id not in by_id for c in cases); pc=sc=cc=hrc=hrt=0; per={}
    for case in cases:
        result=by_id.get(case.id); bucket=per.setdefault(case.cluster,[0,0]); bucket[1]+=1
        if case.high_risk: hrt+=1
        if result is None: continue
        primary_ok=result.primary==case.expected_primary
        if primary_ok: pc+=1; bucket[0]+=1
        if result.supporting==case.expected_supporting: sc+=1
        if result.clarification_required==case.clarification_required: cc+=1
        if case.high_risk and primary_ok and result.clarification_required==case.clarification_required: hrc+=1
    return RunMetrics(pc,len(cases),sc,len(cases),cc,len(cases),0,malformed,hrc,hrt,{k:(v[0],v[1]) for k,v in sorted(per.items())})
def _ratio(correct:int,total:int)->float: return correct/total if total else 1.0
def is_green(m:RunMetrics)->bool:
    if m.unknown_capability_ids or m.malformed_results: return False
    if _ratio(m.primary_correct,m.primary_total)<.90 or _ratio(m.supporting_exact_correct,m.supporting_total)<.80 or _ratio(m.clarification_correct,m.clarification_total)<.90: return False
    if m.high_risk_total and m.high_risk_correct!=m.high_risk_total: return False
    return all(total>=10 and correct>=total-1 for correct,total in m.per_cluster_primary.values())

def _validate_manifest(manifest: RunManifest) -> None:
    for field in RunManifest.__dataclass_fields__:
        value=getattr(manifest,field)
        if not isinstance(value,str) or not value.strip(): raise ValueError(f"manifest {field} must be a non-empty string; use NOT AVAILABLE when metadata is unavailable")

def aggregate_runs(manifests: Sequence[RunManifest], metrics: Sequence[RunMetrics]) -> AggregateMetrics:
    if len(manifests)!=len(metrics) or not manifests: raise ValueError("manifests and metrics must be non-empty and have equal length")
    for manifest in manifests: _validate_manifest(manifest)
    for field in ("corpus_sha256","skeleton_sha256","grader_version"):
        if len({getattr(m,field) for m in manifests})!=1: raise ValueError(f"repeated runs have mismatched {field}")
    prim=[_ratio(m.primary_correct,m.primary_total) for m in metrics]; supp=[_ratio(m.supporting_exact_correct,m.supporting_total) for m in metrics]; clar=[_ratio(m.clarification_correct,m.clarification_total) for m in metrics]
    # Worst run is the lexicographically weakest threshold vector; deterministic run_id breaks exact ties.
    worst_idx=min(range(len(metrics)), key=lambda i:(prim[i],supp[i],clar[i],manifests[i].run_id))
    stat=lambda xs:(min(xs),max(xs),mean(xs),pstdev(xs))
    p=stat(prim); s=stat(supp); c=stat(clar)
    return AggregateMetrics(len(metrics),manifests[worst_idx].run_id,*p,*s,*c,len(metrics)>=3 and all(is_green(m) for m in metrics))

def _metrics_payload(m:RunMetrics)->dict:
    return {"primary_correct":m.primary_correct,"primary_total":m.primary_total,"supporting_exact_correct":m.supporting_exact_correct,"supporting_total":m.supporting_total,"clarification_correct":m.clarification_correct,"clarification_total":m.clarification_total,"unknown_capability_ids":m.unknown_capability_ids,"malformed_results":m.malformed_results,"high_risk_correct":m.high_risk_correct,"high_risk_total":m.high_risk_total,"per_cluster_primary":m.per_cluster_primary,"green":is_green(m)}
def main()->int:
    parser=argparse.ArgumentParser(description="Validate and grade CodeMaestro routing evals"); sub=parser.add_subparsers(dest="command",required=True); validate=sub.add_parser("validate"); validate.add_argument("cases",type=Path); grade=sub.add_parser("grade"); grade.add_argument("--cases",required=True,type=Path); grade.add_argument("--results",required=True,type=Path); grade.add_argument("--report",type=Path); args=parser.parse_args()
    if args.command=="validate":
        cases=load_cases(args.cases)
        if args.cases.name=="corpus-v1.json": summary=validate_corpus_composition(cases); print(f"PASS: {summary['case_count']} routing cases valid; {summary['real_derived_count']} real-derived")
        else: print(f"PASS: {len(cases)} routing cases valid")
        return 0
    cases=load_cases(args.cases); results=load_results(args.results); metrics=grade_run(cases,results); payload=json.dumps(_metrics_payload(metrics),indent=2,sort_keys=True)
    if args.report: args.report.parent.mkdir(parents=True,exist_ok=True); args.report.write_text(payload+"\n",encoding="utf-8")
    print(payload); return 0 if is_green(metrics) else 1
if __name__=="__main__": raise SystemExit(main())
