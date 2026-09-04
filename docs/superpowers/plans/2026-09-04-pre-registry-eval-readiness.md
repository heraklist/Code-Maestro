# Pre-Registry Eval Readiness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Challenge the provisional 17-family capability taxonomy with real-derived routing tasks, a minimal evaluable skeleton, deterministic grading, and repeated runtime/model runs before any full capability contract is authored.

**Architecture:** Eval Readiness is independent of Repository Hardening and is the only pre-registry gate that authorizes capability-contract authoring. Start with a 10-case real-derived pilot—one case per ambiguity cluster—to maximize information early. If the pilot exposes a structural taxonomy failure, stop and reopen the taxonomy before investing in the 100-case corpus, registry, or contracts.

**Tech Stack:** Python 3.12 standard library, JSON, `unittest`, Markdown provenance records, current authorized Chat/Work/Codex model/runtime execution surfaces when available.

**Spec:** `docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md`

## Global Constraints

- The current 17 capability families are a **Provisional First-Generation Capability Freeze**, not an empirically proven taxonomy.
- No production `SKILL.md` or full capability contract may be authored before this plan's Eval Readiness gate passes.
- Structural registry tests are necessary but not sufficient and are outside this plan until Eval Readiness passes.
- Corpus expectations are committed before routing outputs are generated.
- At least one third of the final corpus must be traceable to real historical legacy requests/issues/evals rather than newly invented examples.
- Never copy secrets, private credentials, or sensitive user content from legacy repositories into eval fixtures. Normalize/redact task text while preserving the engineering decision boundary.
- The 10-case pilot must be real-derived where sufficient source material exists; any synthetic pilot case must carry `source_kind: synthetic` and a justification.
- The full corpus contains **at least 100 cases: at least 10 cases in each of the 10 ambiguity clusters**.
- Each full-corpus cluster includes positive-primary, negative/not-primary, multi-capability, no-clarification, and clarification-required cases.
- Each full-corpus capability contract later must reference at least two negative/not-primary routing examples; those contracts are not authored in this plan.
- Routing result generation may be stochastic. Every candidate evaluation uses **n >= 3 independent runs per runtime/model configuration**.
- Record runtime surface, provider/model identifier as exposed by the environment, model/configuration version when available, date/time, corpus SHA, skeleton SHA, grader version, run ID, and result artifact path.
- Do not invent unavailable model/version metadata; record `NOT AVAILABLE` explicitly.
- GREEN is judged on the **worst complete run**, never the best run or average alone.
- Full-corpus GREEN thresholds per run: primary accuracy >= 90%; supporting exact-set accuracy >= 80%; clarification accuracy >= 90%; unknown capability IDs = 0; malformed results = 0; high-risk fail-closed cases = 100%.
- Per-cluster primary gate: **at least 9/10 primary cases correct** for every ambiguity cluster in every qualifying run. If a cluster has more than 10 cases, it may have at most one primary failure unless the spec is explicitly amended before execution.
- Record min/max/mean and population standard deviation across repeated runs for primary, supporting, and clarification metrics; these descriptive statistics do not replace the worst-run GREEN rule.
- If the minimal skeleton unexpectedly passes every GREEN threshold on the challenge corpus, treat that as a corpus-quality warning and review case difficulty/provenance before accepting the taxonomy.
- Eval Readiness can progress while Repository Hardening is incomplete. Repository Hardening failures do not block pilot learning unless they compromise eval evidence integrity.

---

## File Structure

Create:

```text
evals/routing/
├── README.md
├── schema.json
├── pilot-real-derived.json
├── corpus-v1.json
├── skeleton-v0.json
├── results/
│   ├── README.md
│   └── .gitkeep
└── reports/
    └── .gitkeep

tools/
├── routing_eval.py
└── routing_skeleton.py

tests/
├── test_routing_eval.py
└── test_routing_skeleton.py

docs/evals/
├── ROUTING-EVAL-PROTOCOL.md
└── ROUTING-CORPUS-PROVENANCE.md

docs/superpowers/plans/
└── 2026-09-04-pre-registry-eval-readiness-execution.md

logs/logs/project/2026/2026-09-04-pre-registry.log
```

The legacy source inventory is `docs/architecture/MIGRATION-INVENTORY.md`. Source repositories named there are historical/reference inputs only and do not regain runtime authority.

---

### Task B1: Define machine-readable routing case and result contracts

**Files:**
- Create: `evals/routing/schema.json`
- Create: `evals/routing/README.md`
- Create: `docs/evals/ROUTING-EVAL-PROTOCOL.md`
- Create: `tools/routing_eval.py`
- Create: `tests/test_routing_eval.py`

**Interfaces:**
- Produces:

```python
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
```

Canonical provisional capability IDs used by eval fixtures:

```text
requirements-architecture-systems
product-ux-ui
software-implementation
debugging-diagnostics
testing-assurance
review-audit-compliance
security-trust
privacy-data-lifecycle
database-data
interface-protocol-contract
build-toolchain-environment
migration-compatibility
performance-capacity
cicd-platform-delivery
reliability-observability-sre-incident
ai-llm-agent-mcp
research-experimental-language
```

- [ ] **Step 1: Write RED parser/validation tests**

Tests must reject:

```text
missing case id
unknown cluster
unknown expected capability id
duplicate case id
empty source_ref for source_kind != synthetic
malformed result case_id
unknown actual capability id
```

Also verify supporting IDs are canonicalized to sorted unique tuples before exact-set comparison.

- [ ] **Step 2: Run focused tests and confirm RED**

Run:

```bash
python -m unittest tests.test_routing_eval -v
```

Expected: FAIL because parser/grader implementation does not exist.

- [ ] **Step 3: Implement JSON schema and Python loaders**

`schema.json` requires case fields:

```json
{
  "id": "cluster-slug-001",
  "cluster": "build-ci-debug",
  "prompt": "...",
  "expected_primary": "build-toolchain-environment",
  "expected_supporting": ["cicd-platform-delivery", "debugging-diagnostics"],
  "clarification_required": false,
  "high_risk": false,
  "source_kind": "legacy-request",
  "source_ref": "heraklist/Custom-ChatGPT---Code-maesto-v2:<stable-reference>",
  "source_transform": "Normalized names and removed environment-specific identifiers."
}
```

Allowed `source_kind` values:

```text
legacy-request
legacy-issue
legacy-eval
current-project-task
synthetic
```

- [ ] **Step 4: Implement deterministic single-run grading**

Expose:

```python
def load_cases(path: Path) -> list[RoutingCase]: ...
def load_results(path: Path) -> list[RoutingResult]: ...
def grade_run(cases: Sequence[RoutingCase], results: Sequence[RoutingResult]) -> RunMetrics: ...
def is_green(metrics: RunMetrics) -> bool: ...
```

`is_green()` implements the full-corpus thresholds from Global Constraints, including 9/10 per cluster and 100% high-risk.

- [ ] **Step 5: Add deterministic grader tests**

Use fixed fixtures to prove:

```text
same inputs -> equal RunMetrics
90/100 primary passes
89/100 primary fails
8/10 in one cluster fails even if global primary >=90%
9/10 in every cluster may pass cluster gate
one malformed result fails
one unknown capability ID fails
one failed high-risk case fails
supporting comparison is exact set, not order-sensitive list equality
```

- [ ] **Step 6: Run tests**

Run:

```bash
python -m unittest tests.test_routing_eval -v
```

Expected: PASS.

- [ ] **Step 7: Document protocol**

`ROUTING-EVAL-PROTOCOL.md` must state that expectations are precommitted, grader is deterministic, result generation may be stochastic, n>=3 repeated runs are required, worst run determines GREEN, and corpus provenance is part of evidence.

- [ ] **Step 8: Commit**

```bash
git add evals/routing/schema.json evals/routing/README.md docs/evals/ROUTING-EVAL-PROTOCOL.md tools/routing_eval.py tests/test_routing_eval.py logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: define deterministic routing evaluation contract"
```

---

### Task B2: Build the first 10 real-derived pilot cases before more taxonomy work

**Files:**
- Create: `evals/routing/pilot-real-derived.json`
- Create: `docs/evals/ROUTING-CORPUS-PROVENANCE.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes: `docs/architecture/MIGRATION-INVENTORY.md` and accessible historical/reference material from:
  - `heraklist/GPT_CodeMaesto_API`
  - `heraklist/codemaestro-sbox`
  - `heraklist/Custom-ChatGPT---Code-maesto-v2`
  - real current CodeMaestro engineering tasks when they expose a routing boundary.
- Produces: exactly 10 precommitted pilot cases, one per ambiguity cluster, preferably all real-derived.

- [ ] **Step 1: Search legacy sources for real task/eval/issue candidates**

For each of the ten clusters, retrieve at least two candidate historical tasks when available. Prefer user requests, issues, failing tests/evals, and concrete review findings over explanatory documentation.

Do not use retired endpoint mechanics as the routing target; normalize them to the underlying engineering responsibility.

- [ ] **Step 2: Select one pilot case per cluster**

The ten pilot clusters are:

```text
build-ci-debug
implementation-debug
testing-review
security-privacy
database-interface
migration-implementation
performance-reliability
product-frontend
research-language-freshness
ai-interface-security
```

Each case must contain a stable `source_ref` and `source_transform`.

- [ ] **Step 3: Precommit expected routing labels before running the skeleton**

For each case, record `expected_primary`, exact `expected_supporting`, and `clarification_required` based on the approved architecture—not on observed skeleton output.

At least one pilot case must require clarification if a genuine historical case supports that boundary. Do not manufacture clarification solely to satisfy coverage.

- [ ] **Step 4: Validate pilot structure**

Run:

```bash
python tools/routing_eval.py validate evals/routing/pilot-real-derived.json
```

Expected: PASS, exactly 10 cases, exactly one case per cluster.

- [ ] **Step 5: Write provenance ledger**

For every case record:

```text
case id
source repository/current project
source artifact/issue/eval/request reference
why it is representative
normalization/redaction performed
whether the source is real-derived or synthetic
```

- [ ] **Step 6: Commit the pilot expectations before any skeleton output exists**

```bash
git add evals/routing/pilot-real-derived.json docs/evals/ROUTING-CORPUS-PROVENANCE.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: precommit real-derived routing pilot corpus"
```

This commit boundary is evidence that expectations preceded results.

---

### Task B3: Implement the minimal evaluable routing skeleton

**Files:**
- Create: `evals/routing/skeleton-v0.json`
- Create: `tools/routing_skeleton.py`
- Create: `tests/test_routing_skeleton.py`

**Interfaces:**
- Consumes: a routing prompt plus only minimal architecture-derived signals; it must not consume full capability contracts because they do not exist yet.
- Produces:

```python
@dataclass(frozen=True)
class SkeletonDecision:
    primary: str
    supporting: tuple[str, ...]
    clarification_required: bool


def route_with_skeleton(prompt: str) -> SkeletonDecision: ...
```

- [ ] **Step 1: Define minimal skeleton signal table**

`skeleton-v0.json` contains only provisional capability IDs plus compact trigger/exclusion phrases derived from the Living Architecture and existing accepted taxonomy. Keep it intentionally minimal; no ten-section capability contracts.

- [ ] **Step 2: Write RED skeleton tests**

Tests verify only mechanical properties:

```text
returns canonical primary ID
returns canonical supporting IDs
never duplicates supporting IDs
primary is not repeated in supporting
returns boolean clarification_required
same prompt and same skeleton config -> same decision
```

Do **not** encode all pilot expected answers as unit tests; that would train the skeleton directly against the challenge set.

- [ ] **Step 3: Run tests and confirm RED**

Run:

```bash
python -m unittest tests.test_routing_skeleton -v
```

Expected: FAIL until skeleton exists.

- [ ] **Step 4: Implement deterministic minimal routing skeleton**

Use explicit normalized keyword/signal scoring with deterministic tie-breaking. The skeleton is an evaluable baseline, not the production router.

Tie behavior:

```text
if top two materially different capability scores are tied and choosing between them changes task scope/risk -> clarification_required=True
otherwise use stable capability-order tie break and retain the runner-up as supporting when appropriate
```

Document exact scoring in code comments and `evals/routing/README.md`.

- [ ] **Step 5: Run mechanical tests**

Run:

```bash
python -m unittest tests.test_routing_skeleton -v
```

Expected: PASS.

- [ ] **Step 6: Commit skeleton before pilot execution**

```bash
git add evals/routing/skeleton-v0.json tools/routing_skeleton.py tests/test_routing_skeleton.py evals/routing/README.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "feat: add minimal pre-contract routing skeleton"
```

---

### Task B4: Run the 10-case pilot and make the first taxonomy decision

**Files:**
- Create: `evals/routing/results/pilot-skeleton-v0.json`
- Create: `evals/routing/reports/pilot-skeleton-v0.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes: committed pilot corpus and committed skeleton v0.
- Produces: deterministic pilot outputs, grader metrics, taxonomy decision `CONTINUE | REOPEN TAXONOMY`.

- [ ] **Step 1: Generate skeleton results without editing corpus or skeleton**

Run a command implemented in `tools/routing_skeleton.py`:

```bash
python tools/routing_skeleton.py \
  --cases evals/routing/pilot-real-derived.json \
  --output evals/routing/results/pilot-skeleton-v0.json
```

- [ ] **Step 2: Grade the pilot**

Run:

```bash
python tools/routing_eval.py grade \
  --cases evals/routing/pilot-real-derived.json \
  --results evals/routing/results/pilot-skeleton-v0.json \
  --report evals/routing/reports/pilot-skeleton-v0.md
```

Pilot metrics are diagnostic only; the 100-case GREEN thresholds do not apply to this 10-case pilot.

- [ ] **Step 3: Inspect failures by boundary, not only count**

For every failed case classify:

```text
SKELETON SIGNAL GAP
EXPECTED LABEL QUESTIONABLE
TAXONOMY BOUNDARY AMBIGUOUS
CASE UNDER-SPECIFIED
CASE PROVENANCE/TRANSFORM DISTORTED
```

Do not change expected labels merely because the skeleton disagreed.

- [ ] **Step 4: Apply early taxonomy-stop rule**

Set `REOPEN TAXONOMY` if either condition holds:

```text
>= 3 of 10 cases are classified TAXONOMY BOUNDARY AMBIGUOUS
OR
>= 2 distinct clusters reveal no defensible primary owner even after reviewing source provenance and approved architecture
```

Otherwise set `CONTINUE` and carry observed ambiguity into full-corpus design.

- [ ] **Step 5: If `REOPEN TAXONOMY`, stop this plan before B5**

Record the exact cases and open an architecture amendment. Do not create the 100-case corpus or Capability Registry until that review resolves.

- [ ] **Step 6: If `CONTINUE`, commit pilot evidence**

```bash
git add evals/routing/results/pilot-skeleton-v0.json evals/routing/reports/pilot-skeleton-v0.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: record first routing taxonomy challenge"
```

---

### Task B5: Expand to a 100-case provenance-balanced corpus

**Files:**
- Create: `evals/routing/corpus-v1.json`
- Modify: `docs/evals/ROUTING-CORPUS-PROVENANCE.md`
- Modify: `tests/test_routing_eval.py`

**Interfaces:**
- Consumes: pilot findings and legacy/current real-task sources.
- Produces: >=100 precommitted cases, >=10 per cluster, >=1/3 real-derived overall.

- [ ] **Step 1: Add corpus-composition tests before writing cases**

Add validator tests enforcing:

```text
case count >= 100
each of 10 clusters count >= 10
real-derived count / total >= 1/3
unique case IDs
all source_kind/source_ref requirements satisfied
```

Define real-derived as:

```text
legacy-request
legacy-issue
legacy-eval
current-project-task
```

- [ ] **Step 2: Run composition test and confirm RED**

Expected: FAIL because `corpus-v1.json` does not exist.

- [ ] **Step 3: Build cases cluster-by-cluster**

For each cluster create at least 10 cases including:

```text
>=2 clear positive-primary cases
>=2 negative/not-primary cases
>=2 multi-capability composition cases
>=1 evidence-resolved no-clarification case
>=1 genuine clarification-required case
remaining cases chosen to stress the boundary exposed by pilot failures
```

A single case may satisfy more than one category.

- [ ] **Step 4: Meet provenance floor**

At least 34 of the first 100 cases must be real-derived. Prefer a higher proportion when historical sources provide suitable tasks.

Record every source and normalization in the provenance document.

- [ ] **Step 5: Freeze corpus expectations before model/runtime runs**

Validate and commit:

```bash
python tools/routing_eval.py validate evals/routing/corpus-v1.json
git add evals/routing/corpus-v1.json docs/evals/ROUTING-CORPUS-PROVENANCE.md tests/test_routing_eval.py logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: freeze provenance-balanced routing corpus v1"
```

After this commit, expectation changes require an explicit corpus-version bump or correction record; do not silently edit labels after seeing results.

---

### Task B6: Add repeated-run manifest and aggregation semantics

**Files:**
- Modify: `tools/routing_eval.py`
- Modify: `tests/test_routing_eval.py`
- Create: `evals/routing/results/README.md`

**Interfaces:**
- Produces:

```python
@dataclass(frozen=True)
class RunManifest:
    run_id: str
    runtime_surface: str
    provider: str
    model_id: str
    model_version: str
    configuration: str
    corpus_sha256: str
    skeleton_sha256: str
    grader_version: str
    started_at: str
    result_path: str

@dataclass(frozen=True)
class AggregateMetrics:
    run_count: int
    worst_run_id: str
    primary_min: float
    primary_max: float
    primary_mean: float
    primary_pstdev: float
    supporting_min: float
    supporting_max: float
    supporting_mean: float
    supporting_pstdev: float
    clarification_min: float
    clarification_max: float
    clarification_mean: float
    clarification_pstdev: float
    green: bool
```

- [ ] **Step 1: Write RED aggregation tests**

Prove:

```text
<3 runs -> not eligible for GREEN
best run green but worst run red -> aggregate red
all 3 runs green -> aggregate green
statistics use all complete runs
missing model metadata may be literal NOT AVAILABLE but fields cannot be absent
corpus/skeleton/grader identity mismatch across runs -> aggregate invalid
```

- [ ] **Step 2: Run tests and confirm RED**

Run:

```bash
python -m unittest tests.test_routing_eval -v
```

Expected: FAIL until aggregation exists.

- [ ] **Step 3: Implement aggregation**

Expose:

```python
def aggregate_runs(
    manifests: Sequence[RunManifest],
    metrics: Sequence[RunMetrics],
) -> AggregateMetrics: ...
```

Use `statistics.mean` and `statistics.pstdev`. GREEN requires `len(runs) >= 3` and every complete run independently passes `is_green()`.

- [ ] **Step 4: Add manifest validation**

Reject aggregation when corpus SHA, skeleton SHA, or grader version differs between supposedly repeated runs of one configuration.

- [ ] **Step 5: Run tests**

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add tools/routing_eval.py tests/test_routing_eval.py evals/routing/results/README.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: add repeated-run routing aggregation contract"
```

---

### Task B7: Execute the pre-contract RED baseline across repeated runs

**Files:**
- Create: `evals/routing/results/<configuration>-run-01.json`
- Create: `evals/routing/results/<configuration>-run-01.manifest.json`
- Create: corresponding run 02 and 03 artifacts
- Create: `evals/routing/reports/pre-contract-baseline.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes: frozen `corpus-v1.json`, frozen skeleton v0, deterministic grader.
- Produces: at least three complete runs for each runtime/model configuration actually evaluated, dispersion report, worst-run verdict.

- [ ] **Step 1: Record exact evaluation configuration before each run**

Manifest fields:

```text
runtime_surface
provider
model_id
model_version
configuration
corpus_sha256
skeleton_sha256
grader_version
started_at
```

Use actual environment metadata. If unavailable, write `NOT AVAILABLE`; never guess a model build identifier.

- [ ] **Step 2: Run the same frozen corpus at least three independent times per configuration**

Do not edit expectations, skeleton, or grader between repeated runs.

If the evaluated surface cannot directly execute a machine-readable routing prompt batch, use the narrowest authorized harness that preserves identical case text and output schema and record the adapter mechanics in the manifest.

- [ ] **Step 3: Grade each run independently**

Produce one `RunMetrics` record/report per run.

- [ ] **Step 4: Aggregate runs**

Produce min/max/mean/pstdev and identify the worst run. GREEN is false if any qualifying run fails any threshold.

- [ ] **Step 5: Apply the inverse-safeguard**

If the minimal pre-contract skeleton passes every threshold on every run:

```text
RESULT = CORPUS CHALLENGE REVIEW REQUIRED
```

Review provenance, ambiguous boundaries, and adversarial difficulty before accepting the result. Do not proceed merely because the skeleton scored unexpectedly well.

- [ ] **Step 6: Record expected baseline state**

A legitimate outcome is RED. The purpose is to learn which boundaries/contracts need work.

Classify failures by cluster and reason; do not weaken thresholds after observing scores.

- [ ] **Step 7: Commit baseline evidence**

```bash
git add evals/routing/results evals/routing/reports/pre-contract-baseline.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: record repeated pre-contract routing baseline"
```

---

### Task B8: Decide whether the 17-family taxonomy survives the baseline

**Files:**
- Create: `docs/evals/ROUTING-TAXONOMY-DECISION.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes: pilot and full baseline evidence.
- Produces: `TAXONOMY SURVIVES — CONTRACT WORK AUTHORIZED` or `REOPEN TAXONOMY`.

- [ ] **Step 1: Review every persistent failure across repeated runs**

A persistent failure appears in at least two of the three required runs for the same case/configuration.

Classify each as:

```text
ROUTER/SKELETON LIMITATION
CONTRACT BOUNDARY NEEDS CLARIFICATION
EXPECTED LABEL DEFECT
CASE DEFECT
TAXONOMY DEFECT
RUNTIME VARIANCE
```

Expectation/case defects require a versioned corpus correction with rationale; do not silently mutate corpus v1.

- [ ] **Step 2: Apply taxonomy reopen criteria**

Reopen if evidence shows a responsibility cannot be cleanly owned/composed by the existing 17 without persistent ambiguity, duplicated methodology, or evidence loss. Cite exact case IDs and repeated-run evidence.

- [ ] **Step 3: If taxonomy survives, identify contract-driving failures**

Produce a table:

```text
case id | cluster | observed failure | primary contract to clarify | neighboring contract(s) | required boundary statement
```

This table becomes input to Capability Registry/contracts.

- [ ] **Step 4: Commit decision**

```bash
git add docs/evals/ROUTING-TAXONOMY-DECISION.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "docs: decide provisional capability taxonomy from routing evidence"
```

If result is `REOPEN TAXONOMY`, stop before B9 and open an architecture amendment.

---

### Task B9: Establish Eval Readiness gate

**Files:**
- Create: `docs/superpowers/plans/2026-09-04-pre-registry-eval-readiness-execution.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes: Tasks B1–B8.
- Produces: independent authorization state for capability-contract work.

- [ ] **Step 1: Verify Eval Readiness acceptance conditions**

Require:

```text
machine-readable case/result schema exists
10-case real-derived pilot completed
pilot taxonomy decision = CONTINUE
full corpus >=100 cases
>=10 cases per cluster
>=1/3 real-derived corpus provenance
expectations frozen before outputs
minimal skeleton frozen before baseline outputs
deterministic grader tests PASS
n>=3 repeated runs per evaluated configuration
runtime/model/configuration metadata recorded or NOT AVAILABLE explicitly
variance statistics recorded
worst-run rule applied
pre-contract baseline recorded
inverse-safeguard applied if skeleton unexpectedly green
taxonomy decision = TAXONOMY SURVIVES
contract-driving failure table exists
```

- [ ] **Step 2: Write execution record**

Record all corpus/skeleton/grader hashes, commits, run artifacts, metrics, dispersion, taxonomy decision, and known limitations.

- [ ] **Step 3: Append Eval Readiness checkpoint**

Result vocabulary:

```text
PASS — capability registry/contracts may begin
BLOCKED — missing evidence/infrastructure
REOPEN TAXONOMY — architecture review required
```

Explicitly state that Repository Hardening is a parallel gate and its completion state does not change the empirical taxonomy decision.

- [ ] **Step 4: Run fresh repository validation applicable at current head**

At minimum:

```bash
python -m unittest discover -s tests -v
python tools/doc_consistency.py
```

Also run any Repository Hardening quality gates that already exist on the branch; do not wait for unfinished unrelated hardening work solely to obtain Eval Readiness evidence.

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/plans/2026-09-04-pre-registry-eval-readiness-execution.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "docs: close pre-registry eval readiness gate"
```

---

## Post-Plan Handoff

Only if Task B9 result is `PASS`:

```text
Eval Readiness PASS
-> amend/supersede the old Capability Registry plan
-> create registry skeleton + structural validator
-> write capability contracts specifically against the contract-driving failure table
-> run the same frozen corpus at n>=3 after contract-informed routing changes
-> require worst-run GREEN before claiming routing/composition readiness
```

The first post-contract GREEN does **not** authorize changing corpus expectations to fit implementation. Corpus corrections remain versioned evidence changes.
