from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Sequence


CAPABILITY_IDS = frozenset(
    {
        "requirements-architecture-systems",
        "product-ux-ui",
        "software-implementation",
        "debugging-diagnostics",
        "testing-assurance",
        "review-audit-compliance",
        "security-trust",
        "privacy-data-lifecycle",
        "database-data",
        "interface-protocol-contract",
        "build-toolchain-environment",
        "migration-compatibility",
        "performance-capacity",
        "cicd-platform-delivery",
        "reliability-observability-sre-incident",
        "ai-llm-agent-mcp",
        "research-experimental-language",
    }
)

CLUSTERS = frozenset(
    {
        "build-ci-debug",
        "implementation-debug",
        "testing-review",
        "security-privacy",
        "database-interface",
        "migration-implementation",
        "performance-reliability",
        "product-frontend",
        "research-language-freshness",
        "ai-interface-security",
    }
)

SOURCE_KINDS = frozenset(
    {"legacy-request", "legacy-issue", "legacy-eval", "current-project-task", "synthetic"}
)


@dataclass(frozen=True)
class RoutingCase:
    id: str
    cluster: str
    prompt: str
    expected_primary: str
    expected_supporting: tuple[str, ...]
    clarification_required: bool
    high_risk: bool
    source_kind: str
    source_ref: str
    source_transform: str


@dataclass(frozen=True)
class RoutingResult:
    case_id: str
    primary: str
    supporting: tuple[str, ...]
    clarification_required: bool


@dataclass(frozen=True)
class RunMetrics:
    primary_correct: int
    primary_total: int
    supporting_exact_correct: int
    supporting_total: int
    clarification_correct: int
    clarification_total: int
    unknown_capability_ids: int
    malformed_results: int
    high_risk_correct: int
    high_risk_total: int
    per_cluster_primary: dict[str, tuple[int, int]]


def _load_json_list(path: Path) -> list[dict]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot load JSON from {path}: {exc}") from exc
    if not isinstance(payload, list):
        raise ValueError(f"expected JSON array in {path}")
    if not all(isinstance(item, dict) for item in payload):
        raise ValueError(f"expected array of objects in {path}")
    return payload


def _required_string(item: dict, field: str) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")
    return value.strip()


def _required_bool(item: dict, field: str) -> bool:
    value = item.get(field)
    if not isinstance(value, bool):
        raise ValueError(f"{field} must be a boolean")
    return value


def _canonical_capability_tuple(value: object, field: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{field} must be an array of capability IDs")
    normalized = tuple(sorted(set(value)))
    unknown = [item for item in normalized if item not in CAPABILITY_IDS]
    if unknown:
        raise ValueError(f"{field} contains unknown capability IDs: {unknown}")
    return normalized


def load_cases(path: Path) -> list[RoutingCase]:
    rows = _load_json_list(path)
    cases: list[RoutingCase] = []
    seen: set[str] = set()
    for row in rows:
        case_id = _required_string(row, "id")
        if case_id in seen:
            raise ValueError(f"duplicate case id: {case_id}")
        seen.add(case_id)
        cluster = _required_string(row, "cluster")
        if cluster not in CLUSTERS:
            raise ValueError(f"unknown cluster: {cluster}")
        primary = _required_string(row, "expected_primary")
        if primary not in CAPABILITY_IDS:
            raise ValueError(f"unknown expected capability id: {primary}")
        source_kind = _required_string(row, "source_kind")
        if source_kind not in SOURCE_KINDS:
            raise ValueError(f"unknown source_kind: {source_kind}")
        source_ref = row.get("source_ref", "")
        if not isinstance(source_ref, str):
            raise ValueError("source_ref must be a string")
        if source_kind != "synthetic" and not source_ref.strip():
            raise ValueError("source_ref is required for real-derived cases")
        cases.append(
            RoutingCase(
                id=case_id,
                cluster=cluster,
                prompt=_required_string(row, "prompt"),
                expected_primary=primary,
                expected_supporting=_canonical_capability_tuple(
                    row.get("expected_supporting"), "expected_supporting"
                ),
                clarification_required=_required_bool(row, "clarification_required"),
                high_risk=_required_bool(row, "high_risk"),
                source_kind=source_kind,
                source_ref=source_ref.strip(),
                source_transform=_required_string(row, "source_transform"),
            )
        )
    return cases


def load_results(path: Path) -> list[RoutingResult]:
    rows = _load_json_list(path)
    results: list[RoutingResult] = []
    seen: set[str] = set()
    for row in rows:
        case_id = _required_string(row, "case_id")
        if case_id in seen:
            raise ValueError(f"duplicate result case_id: {case_id}")
        seen.add(case_id)
        primary = _required_string(row, "primary")
        if primary not in CAPABILITY_IDS:
            raise ValueError(f"unknown actual capability id: {primary}")
        results.append(
            RoutingResult(
                case_id=case_id,
                primary=primary,
                supporting=_canonical_capability_tuple(row.get("supporting"), "supporting"),
                clarification_required=_required_bool(row, "clarification_required"),
            )
        )
    return results


def grade_run(cases: Sequence[RoutingCase], results: Sequence[RoutingResult]) -> RunMetrics:
    by_id = {result.case_id: result for result in results}
    case_ids = {case.id for case in cases}
    malformed = len(set(by_id) - case_ids) + sum(1 for case in cases if case.id not in by_id)
    primary_correct = 0
    supporting_correct = 0
    clarification_correct = 0
    high_risk_correct = 0
    high_risk_total = 0
    per_cluster: dict[str, list[int]] = {}

    for case in cases:
        result = by_id.get(case.id)
        bucket = per_cluster.setdefault(case.cluster, [0, 0])
        bucket[1] += 1
        if case.high_risk:
            high_risk_total += 1
        if result is None:
            continue
        primary_ok = result.primary == case.expected_primary
        if primary_ok:
            primary_correct += 1
            bucket[0] += 1
        if result.supporting == case.expected_supporting:
            supporting_correct += 1
        if result.clarification_required == case.clarification_required:
            clarification_correct += 1
        if case.high_risk and primary_ok and result.clarification_required == case.clarification_required:
            high_risk_correct += 1

    return RunMetrics(
        primary_correct=primary_correct,
        primary_total=len(cases),
        supporting_exact_correct=supporting_correct,
        supporting_total=len(cases),
        clarification_correct=clarification_correct,
        clarification_total=len(cases),
        unknown_capability_ids=0,
        malformed_results=malformed,
        high_risk_correct=high_risk_correct,
        high_risk_total=high_risk_total,
        per_cluster_primary={key: (value[0], value[1]) for key, value in sorted(per_cluster.items())},
    )


def _ratio(correct: int, total: int) -> float:
    return correct / total if total else 1.0


def is_green(metrics: RunMetrics) -> bool:
    if metrics.unknown_capability_ids or metrics.malformed_results:
        return False
    if _ratio(metrics.primary_correct, metrics.primary_total) < 0.90:
        return False
    if _ratio(metrics.supporting_exact_correct, metrics.supporting_total) < 0.80:
        return False
    if _ratio(metrics.clarification_correct, metrics.clarification_total) < 0.90:
        return False
    if metrics.high_risk_total and metrics.high_risk_correct != metrics.high_risk_total:
        return False
    for correct, total in metrics.per_cluster_primary.values():
        if total < 10 or correct < total - 1:
            return False
    return True


def _metrics_payload(metrics: RunMetrics) -> dict:
    return {
        "primary_correct": metrics.primary_correct,
        "primary_total": metrics.primary_total,
        "supporting_exact_correct": metrics.supporting_exact_correct,
        "supporting_total": metrics.supporting_total,
        "clarification_correct": metrics.clarification_correct,
        "clarification_total": metrics.clarification_total,
        "unknown_capability_ids": metrics.unknown_capability_ids,
        "malformed_results": metrics.malformed_results,
        "high_risk_correct": metrics.high_risk_correct,
        "high_risk_total": metrics.high_risk_total,
        "per_cluster_primary": metrics.per_cluster_primary,
        "green": is_green(metrics),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and grade CodeMaestro routing evals")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("cases", type=Path)
    grade = sub.add_parser("grade")
    grade.add_argument("--cases", required=True, type=Path)
    grade.add_argument("--results", required=True, type=Path)
    grade.add_argument("--report", type=Path)
    args = parser.parse_args()

    if args.command == "validate":
        cases = load_cases(args.cases)
        print(f"PASS: {len(cases)} routing cases valid")
        return 0

    cases = load_cases(args.cases)
    results = load_results(args.results)
    metrics = grade_run(cases, results)
    payload = json.dumps(_metrics_payload(metrics), indent=2, sort_keys=True)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if is_green(metrics) else 1


if __name__ == "__main__":
    raise SystemExit(main())
