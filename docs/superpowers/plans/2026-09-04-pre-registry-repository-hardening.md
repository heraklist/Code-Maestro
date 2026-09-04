# Pre-Registry Repository Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close repository-governance drift and harden CodeMaestro's checker, CI, append-only history, secret handling, and main-branch controls without blocking the independent Eval Readiness track.

**Architecture:** This plan is one of two parallel pre-registry plans. It hardens repository truth and enforcement only. The companion plan `docs/superpowers/plans/2026-09-04-pre-registry-eval-readiness.md` owns routing corpus, skeleton, grader, repeated model/runtime runs, and the gate that actually unlocks capability-contract authoring.

**Tech Stack:** Python 3.12 standard library, `unittest`, GitHub Actions, Ruff 0.16.6, mypy 2.3.1, Gitleaks 8.30.1, Markdown, Git.

**Spec:** `docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md`

## Global Constraints

- Repository target visibility is private; do not assume or purchase a paid GitHub tier implicitly.
- While the repository remains public, use available free mechanical controls on `main` immediately.
- If private visibility later disables required branch protection on the available plan, record `PROCESS-ENFORCED` degradation explicitly rather than claiming mechanical enforcement.
- `main` push validation is authoritative post-merge evidence and must never be cancelled by a newer `main` push.
- PR validation is authoritative pre-merge evidence for PR work.
- Existing project ledgers and conversation transcripts are append-only except through an explicitly authorized privacy/security purge path.
- Do not rewrite historical `PENDING` events; close them with new resolution events.
- Do not weaken `tools/check_append_only_logs.py` or existing documentation consistency tests to make new work pass.
- Repository logging remains event-time and public-safe until visibility actually changes; visibility-dependent wording is reconciled only when the transition happens.
- No production `SKILL.md`, router, Capability Registry, capability contracts, or Self-Evolution Controller are created by this plan.
- This plan and Eval Readiness may execute in parallel. Completion of this plan is not a prerequisite for authoring capability contracts once the Eval Readiness gate passes.

---

## File Structure

Create or modify:

```text
.github/
├── workflows/
│   ├── documentation-consistency.yml
│   └── security-quality.yml
└── pull_request_template.md

.gitignore
.gitleaks.toml
pyproject.toml
requirements-dev.txt
README.md
docs/architecture/ARCHITECTURE.md
docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md
docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md
logs/logs/project/2026/2026-09-04-pre-registry.log

tools/
├── check_append_only_logs.py
├── doc_consistency.py
└── check_spec_reachability.py

tests/
├── test_append_only_logs.py
├── test_doc_consistency.py
└── test_spec_reachability.py
```

Repository settings touched during execution:

```text
main branch protection / ruleset
required status check: documentation-consistency
repository visibility state record
```

---

### Task A1: Close durable governance state and make the approved amendment reachable

**Files:**
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`
- Modify: `docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md`
- Modify: `docs/architecture/ARCHITECTURE.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: merged foundation SHA `6bb21fff2279584979ba8bee7ab61d57edcb5425`, successful pre-merge CI run `33870305620`, successful post-merge main run `33871555735`, approved v2 amendment.
- Produces: explicit resolution events, approved-spec status, inbound navigation links, current checkpoint.

- [ ] **Step 1: Add failing tests for approved-spec reachability and unresolved historical PENDING events**

Append tests to `tests/test_doc_consistency.py`:

```python
class PreRegistryGovernanceTests(unittest.TestCase):
    SPEC = "docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md"

    def test_pre_registry_spec_is_reachable_from_architecture_or_readme(self):
        root = Path(__file__).resolve().parents[1]
        haystack = "\n".join(
            (root / path).read_text(encoding="utf-8")
            for path in ("README.md", "docs/architecture/ARCHITECTURE.md")
        )
        self.assertIn(self.SPEC, haystack)

    def test_pre_registry_spec_is_approved(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / self.SPEC).read_text(encoding="utf-8")
        self.assertIn("**Status:** WRITTEN SPEC — APPROVED", text)
```

Add a focused repository test that requires resolution-event IDs for both historical pending events:

```python
class PendingEventResolutionTests(unittest.TestCase):
    def test_known_pending_events_have_resolution_records(self):
        root = Path(__file__).resolve().parents[1]
        text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (root / "logs/logs/project").rglob("*.log")
        )
        for event_id in (
            "CM-EVENT-20260904T133229+0300-state-sync-001",
            "CM-EVENT-20260904T144900+0300-log-correction-001",
        ):
            self.assertIn(f"RESOLVES EVENT {event_id}", text)
```

- [ ] **Step 2: Run focused tests and confirm RED**

Run:

```bash
python -m unittest \
  tests.test_doc_consistency.PreRegistryGovernanceTests \
  tests.test_doc_consistency.PendingEventResolutionTests -v
```

Expected: FAIL because the v2 spec is not yet marked approved/reachable and the two pending events have no resolution records.

- [ ] **Step 3: Append resolution events and post-merge checkpoint**

Append three new events to `logs/logs/project/2026/2026-09-04-pre-registry.log` with exact evidence:

```text
EVENT / TYPE: RESOLUTION
...
RESOLVES EVENT CM-EVENT-20260904T133229+0300-state-sync-001
EVIDENCE: pre-merge exact-head run 33870305620 success; post-merge main run 33871555735 success; merge SHA 6bb21fff2279584979ba8bee7ab61d57edcb5425.
RESULT: PASS
```

```text
EVENT / TYPE: RESOLUTION
...
RESOLVES EVENT CM-EVENT-20260904T144900+0300-log-correction-001
EVIDENCE: restoration commit chain plus run 33870305620 success and main run 33871555735 success.
RESULT: PASS
```

```text
EVENT / TYPE: CHECKPOINT
TARGET: Foundation -> Pre-Registry Hardening/Eval Readiness handoff
AFTER: main=6bb21fff2279584979ba8bee7ab61d57edcb5425; foundation merged; post-merge documentation consistency PASS; append-only guard operational; next authorized stages are Repository Hardening and Eval Readiness in parallel.
RESULT: PASS
```

Use event-time timestamps at execution; do not reuse the examples as timestamps.

- [ ] **Step 4: Mark the v2 amendment approved and link it from current navigation**

Change the status line in the v2 spec to:

```text
**Status:** WRITTEN SPEC — APPROVED — 2026-09-04
```

Add direct Markdown links from both `README.md` and `docs/architecture/ARCHITECTURE.md` to:

```text
docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md
```

State that it governs pre-registry ordering, budgets, hardening, and eval-first requirements.

- [ ] **Step 5: Run focused and full checks**

Run:

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
python tools/check_append_only_logs.py HEAD^
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add README.md docs/architecture/ARCHITECTURE.md \
  docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md \
  logs/logs/project/2026/2026-09-04-pre-registry.log tests/test_doc_consistency.py
git commit -m "docs: close foundation governance and approve pre-registry design"
```

---

### Task A2: Protect `main` now while the repository is public

**Files:**
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`
- Modify: `docs/project-governance/SESSION-LOGGING-PROTOCOL.md` only if a protection-state recording field is needed

**Interfaces:**
- Consumes: current repository visibility, current GitHub plan capabilities, existing `documentation-consistency` check.
- Produces: mechanical branch protection now when available; explicit protection state record and future private-visibility degradation rule.

- [ ] **Step 1: Read current visibility and protection/ruleset state before mutation**

Record:

```text
visibility = public | private
rulesets = current ruleset list
traditional branch protection = readable state or NOT AVAILABLE
```

Do not infer billing tier from visibility alone.

- [ ] **Step 2: If the repository is still public, configure `main` protection immediately**

Required policy:

```text
require pull request before merge
require status checks before merge
required check = documentation-consistency
prevent force pushes
prevent branch deletion
```

Do not enable a rule that would prevent the repository owner from recovering from a broken configuration without first validating GitHub's exact behavior for this personal repository.

- [ ] **Step 3: Verify the protection state through a fresh read**

Expected when supported:

```text
main protection = mechanically enforced
required check includes documentation-consistency
```

If the connector cannot read or write the relevant protection API, record `NOT AVAILABLE` for the connector operation and configure through an authorized GitHub surface if available in the execution environment.

- [ ] **Step 4: Record future private-visibility policy without changing visibility in this task**

Append a governance event that says:

```text
Target visibility: private.
Paid upgrade: not assumed.
Before any visibility transition, re-read protection capability.
If private-on-current-tier disables required checks, record PROTECTION MODE: PROCESS-ENFORCED and do not claim mechanical enforcement.
```

- [ ] **Step 5: Commit only repository-file changes, if any**

```bash
git add logs/logs/project/2026/2026-09-04-pre-registry.log docs/project-governance/SESSION-LOGGING-PROTOCOL.md
git commit -m "governance: record main protection and visibility policy"
```

If only GitHub settings changed, record the settings mutation in the project ledger; do not create an empty commit.

---

### Task A3: Fix documentation checker false negatives and authority parsing

**Files:**
- Modify: `tools/doc_consistency.py`
- Modify: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: current `Finding` structure and `check_repository(root)` interface.
- Produces: per-occurrence CM-R negation, explicit ADR-status semantics, anchored event-field validation, fragment-aware Markdown links, location-aware ADR definitions.

- [ ] **Step 1: Add RED tests for all confirmed checker bugs**

Add tests equivalent to:

```python
class ResearchReferenceOccurrenceTests(unittest.TestCase):
    def test_negative_occurrence_does_not_hide_positive_occurrence(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            research = root / "docs/research"
            research.mkdir(parents=True)
            (research / "RESEARCH-BACKLOG.md").write_text(
                "## CM-R-032 — Existing\n\n**Status:** IN RESEARCH\n",
                encoding="utf-8",
            )
            (root / "docs/mixed.md").write_text(
                "No CM-R-033 is opened here.\n\nLater, CM-R-033 defines the next stage.\n",
                encoding="utf-8",
            )
            findings = check_research_references(root)
            self.assertEqual([f.code for f in findings], ["RESEARCH_REFERENCE_UNINDEXED"])
```

```python
class AdrStatusTests(unittest.TestCase):
    def test_not_superseded_is_not_noncanonical_by_substring(self):
        self.assertTrue(_is_active("NOT SUPERSEDED"))
```

```python
class EventFieldAnchoringTests(unittest.TestCase):
    def test_field_name_inside_action_does_not_satisfy_required_field(self):
        # Build a synthetic event missing EVIDENCE but mentioning "EVIDENCE:" inside ACTION.
        ...
        self.assertIn("LOG_EVENT_FIELD_MISSING", [f.code for f in findings])
```

Use actual complete fixture code in the test file; do not leave ellipses in implementation.

Add fragment tests:

```python
class MarkdownAnchorTests(unittest.TestCase):
    def test_missing_cross_file_fragment_fails(self): ...
    def test_existing_cross_file_fragment_passes(self): ...
    def test_missing_local_fragment_fails(self): ...
```

Add ADR-location tests:

```python
class AdrLocationAuthorityTests(unittest.TestCase):
    def test_active_adr_definition_outside_authorized_architecture_file_fails(self): ...
    def test_adr_reference_in_readme_does_not_count_as_definition(self): ...
```

- [ ] **Step 2: Run focused checker tests and confirm RED**

Run:

```bash
python -m unittest \
  tests.test_doc_consistency.ResearchReferenceOccurrenceTests \
  tests.test_doc_consistency.AdrStatusTests \
  tests.test_doc_consistency.EventFieldAnchoringTests \
  tests.test_doc_consistency.MarkdownAnchorTests \
  tests.test_doc_consistency.AdrLocationAuthorityTests -v
```

Expected: FAIL for the newly exposed behaviors.

- [ ] **Step 3: Implement per-occurrence research-reference classification**

Replace file-level set subtraction with occurrence-level logic. Use the match span and inspect the immediately preceding lexical context on the same sentence/line for `no`, `not`, or `without` applying to that occurrence only.

Expose a helper:

```python
def _is_negated_research_reference(text: str, match: re.Match[str]) -> bool:
    ...
```

`check_research_references()` must iterate every `RESEARCH_REFERENCE_RE.finditer(text)` occurrence and only suppress the specific negated match.

- [ ] **Step 4: Implement explicit ADR status semantics**

Replace generic substring matching with exact normalized authority markers. Keep active-by-default compatibility for existing accepted statuses, but classify non-active only when the normalized status is one of the documented non-canonical forms or starts with an explicit marker form such as `ABSORBED INTO `.

- [ ] **Step 5: Anchor all required event fields**

Add:

```python
def _field_line_present(section: str, field: str) -> bool:
    return re.search(rf"^{re.escape(field)}(?:\s*.*)$", section, re.MULTILINE) is not None
```

Use it for every `REQUIRED_PROJECT_EVENT_FIELDS` item.

- [ ] **Step 6: Implement deterministic Markdown heading/fragment normalization**

Add helpers:

```python
def _markdown_anchor(text: str) -> set[str]: ...
def _normalize_markdown_heading(heading: str) -> str: ...
```

Normalize GitHub-style headings deterministically for the subset used by this repository: lowercase, strip inline Markdown emphasis/backticks, remove punctuation except spaces/hyphens, convert whitespace to `-`, collapse repeated hyphens. Support explicit HTML anchors if present.

Validate `#local` and `file.md#fragment` targets after file existence checks.

- [ ] **Step 7: Restrict active ADR definitions to authorized decision artifacts**

Define an explicit authorized-path predicate, initially:

```python
AUTHORIZED_ADR_DEFINITION_PATHS = {
    Path("docs/architecture/DECISIONS.md"),
    Path("docs/architecture/DECISIONS-2026-09-04-PASS3.md"),
}
```

Historical file entries must remain non-active by status. References elsewhere are scanned as references, not definitions.

- [ ] **Step 8: Run focused and full checks**

Run:

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add tools/doc_consistency.py tests/test_doc_consistency.py logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "fix: harden documentation authority and reference checks"
```

---

### Task A4: Extend append-only protection across the full branch range and transcripts

**Files:**
- Modify: `tools/check_append_only_logs.py`
- Create: `tests/test_append_only_logs.py`
- Modify: `.github/workflows/documentation-consistency.yml`

**Interfaces:**
- Consumes: Git repository with a base ref/merge base and current HEAD.
- Produces: full-range append-only verification for project `*.log` ledgers and conversation `*.md` transcripts.

- [ ] **Step 1: Write RED unit tests for multi-commit truncation and transcript truncation**

Refactor `tools/check_append_only_logs.py` so the core comparison is testable without shelling out for every assertion:

```python
@dataclass(frozen=True)
class AppendOnlyFinding:
    path: str
    reason: str


def compare_append_only_bytes(base: bytes, head: bytes, path: str) -> list[AppendOnlyFinding]: ...
```

Tests must cover:

```python
def test_project_log_truncation_fails(): ...
def test_project_log_append_passes(): ...
def test_transcript_truncation_fails(): ...
def test_transcript_append_passes(): ...
def test_new_append_only_file_passes(): ...
def test_deleted_append_only_file_fails(): ...
```

- [ ] **Step 2: Run unit tests and confirm RED**

Run:

```bash
python -m unittest tests.test_append_only_logs -v
```

Expected: FAIL because the core interface/full-scope behavior does not yet exist.

- [ ] **Step 3: Expand protected paths**

Protect both:

```text
logs/logs/project/**/*.log
logs/conversations/**/*.md    # excluding README.md
```

Do not include the self-evolution namespace until it contains actual run records; when it does, it must adopt the same append-only contract in the Self-Evolution implementation slice.

- [ ] **Step 4: Change CLI semantics from `HEAD^` to explicit base..HEAD range**

CLI:

```text
python tools/check_append_only_logs.py <base-ref> [<head-ref>]
```

Default `<head-ref>` to `HEAD`.

For CI PR execution, compute:

```bash
git fetch --no-tags origin main
git merge-base origin/main HEAD
```

and pass that merge-base to the tool.

For main push execution, compare against `${{ github.event.before }}` when it is a valid non-zero SHA; if unavailable, compute the nearest previous main commit explicitly. Never rely only on `HEAD^` for a multi-commit push.

- [ ] **Step 5: Set checkout history sufficient for full-range comparison**

Change checkout to:

```yaml
with:
  fetch-depth: 0
```

- [ ] **Step 6: Run local regression suite**

Run:

```bash
python -m unittest tests.test_append_only_logs -v
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Then run the append-only tool against the real branch merge-base with `main`.

Expected: PASS on the current valid history.

- [ ] **Step 7: Commit**

```bash
git add tools/check_append_only_logs.py tests/test_append_only_logs.py .github/workflows/documentation-consistency.yml logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "fix: enforce append-only history across branch range and transcripts"
```

---

### Task A5: Make CI evidence unambiguous and broaden change coverage

**Files:**
- Modify: `.github/workflows/documentation-consistency.yml`
- Modify: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: current Documentation Consistency workflow.
- Produces: authoritative-run semantics, concurrency cancellation off `main`, broad `tools/**` and `tests/**` path coverage.

- [ ] **Step 1: Add RED workflow-structure tests**

Add assertions:

```python
class WorkflowSemanticsTests(unittest.TestCase):
    def test_workflow_uses_broad_tool_and_test_paths(self):
        text = self._workflow()
        self.assertIn("- 'tools/**'", text)
        self.assertIn("- 'tests/**'", text)

    def test_main_runs_are_never_cancelled(self):
        text = self._workflow()
        self.assertIn("cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}", text)
```

- [ ] **Step 2: Run focused test and confirm RED**

Run:

```bash
python -m unittest tests.test_doc_consistency.WorkflowSemanticsTests -v
```

Expected: FAIL on current workflow.

- [ ] **Step 3: Update path filters**

Replace individual tool/test entries with:

```yaml
- 'tools/**'
- 'tests/**'
```

Keep `README.md`, `docs/**`, `logs/**`, and workflow paths.

- [ ] **Step 4: Add concurrency without cancelling main evidence**

Use:

```yaml
concurrency:
  group: documentation-consistency-${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```

Document in a workflow comment or governance doc:

```text
PR event = authoritative pre-merge run.
main push event = authoritative post-merge run.
```

- [ ] **Step 5: Run full workflow tests/checker**

Run:

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/documentation-consistency.yml tests/test_doc_consistency.py logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "ci: define authoritative documentation validation runs"
```

---

### Task A6: Add deterministic secret, lint, type, and local-artifact gates

**Files:**
- Create: `.github/workflows/security-quality.yml`
- Create: `.gitleaks.toml`
- Create: `.gitignore`
- Create: `pyproject.toml`
- Create: `requirements-dev.txt`
- Modify: `README.md`

**Interfaces:**
- Consumes: Python `tools/` and `tests/` sources plus entire repository history/worktree.
- Produces: Gitleaks, Ruff, and mypy gates with pinned tool versions.

- [ ] **Step 1: Create pinned development dependencies**

`requirements-dev.txt`:

```text
ruff==0.16.6
mypy==2.3.1
```

`pyproject.toml`:

```toml
[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F", "I", "UP"]

[tool.mypy]
python_version = "3.12"
strict = true
files = ["tools", "tests"]
```

If strict mypy exposes legitimate typing debt, fix the code rather than weakening `strict = true` unless a specific incompatibility is documented with evidence.

- [ ] **Step 2: Add minimal `.gitignore`**

Use:

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
venv/
.env
.env.*
!.env.example
.DS_Store
.idea/
.vscode/
```

Do not ignore repository evidence, docs, eval artifacts, or source-controlled configuration.

- [ ] **Step 3: Add Gitleaks configuration**

Create `.gitleaks.toml` extending the default scanner rules, with only narrowly justified repository-specific allowlists. Do not add blanket path exclusions for `logs/`, `docs/`, or test fixtures.

Never commit a real secret to prove the scanner works.

- [ ] **Step 4: Create `security-quality.yml`**

Use Python 3.12 and install `requirements-dev.txt`, then run:

```bash
ruff check tools tests
mypy tools tests
```

Run Gitleaks 8.30.1 pinned to that version. Prefer the official binary/container or official action version supported at execution time; record the exact implementation and version in the workflow.

The scan must cover the checked-out repository and relevant Git history. Use full checkout history.

- [ ] **Step 5: Run Ruff and mypy locally and fix only actual findings**

Run:

```bash
python -m pip install -r requirements-dev.txt
ruff check tools tests
mypy tools tests
```

Expected: PASS after necessary targeted fixes.

- [ ] **Step 6: Run Gitleaks against the real repository**

Expected: PASS with no real secret findings. If findings appear, classify them individually; do not suppress them globally.

- [ ] **Step 7: Document developer verification commands**

Add to README:

```text
python -m unittest discover -s tests -v
python tools/doc_consistency.py
ruff check tools tests
mypy tools tests
gitleaks detect ...
```

Use the exact final Gitleaks command from the implemented workflow.

- [ ] **Step 8: Commit**

```bash
git add .github/workflows/security-quality.yml .gitleaks.toml .gitignore pyproject.toml requirements-dev.txt README.md tools tests logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "ci: add secret lint and type quality gates"
```

---

### Task A7: Add machine-checkable spec reachability

**Files:**
- Create: `tools/check_spec_reachability.py`
- Create: `tests/test_spec_reachability.py`
- Modify: `.github/workflows/documentation-consistency.yml`

**Interfaces:**
- Consumes: canonical navigation roots `README.md` and `docs/architecture/ARCHITECTURE.md` plus approved/current spec metadata.
- Produces: orphan-spec findings for current/approved authoritative specs.

- [ ] **Step 1: Define a narrow reachability contract**

Do not require every historical spec to be linked from README.

The checker only requires inbound navigation for specs whose status line contains one of:

```text
WRITTEN SPEC — APPROVED
CURRENT
ACTIVE
```

and excludes files explicitly marked historical/superseded/absorbed.

- [ ] **Step 2: Write RED tests**

Expose:

```python
@dataclass(frozen=True)
class ReachabilityFinding:
    path: str
    message: str


def check_spec_reachability(root: Path) -> list[ReachabilityFinding]: ...
```

Tests:

```python
def test_active_spec_without_inbound_link_fails(): ...
def test_active_spec_linked_from_architecture_passes(): ...
def test_historical_spec_may_be_unlinked(): ...
```

- [ ] **Step 3: Run tests and confirm RED**

Run:

```bash
python -m unittest tests.test_spec_reachability -v
```

Expected: FAIL until implementation exists.

- [ ] **Step 4: Implement reachability checker**

Parse active spec paths under `docs/superpowers/specs/`. Build inbound Markdown link targets from `README.md` and `docs/architecture/ARCHITECTURE.md`. Report any active/approved spec absent from both navigation roots.

- [ ] **Step 5: Wire into Documentation Consistency workflow**

Add:

```yaml
- name: Check active spec reachability
  run: python tools/check_spec_reachability.py
```

- [ ] **Step 6: Run complete repository hardening verification**

Run:

```bash
python -m unittest discover -s tests -v
python tools/doc_consistency.py
python tools/check_spec_reachability.py
ruff check tools tests
mypy tools tests
```

Run the final append-only command using the actual merge base rather than `HEAD^`, then run Gitleaks with the exact workflow command.

Expected: all PASS.

- [ ] **Step 7: Commit**

```bash
git add tools/check_spec_reachability.py tests/test_spec_reachability.py .github/workflows/documentation-consistency.yml logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "ci: require reachability for active architecture specs"
```

---

### Task A8: Repository Hardening gate and handoff

**Files:**
- Create: `docs/superpowers/plans/2026-09-04-pre-registry-repository-hardening-execution.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes: Tasks A1–A7 evidence.
- Produces: independent `REPOSITORY HARDENING: PASS | PROCESS-ENFORCED | BLOCKED` state.

- [ ] **Step 1: Verify each hardening acceptance condition**

Record individually:

```text
governance resolutions present
approved amendment reachable
main protection state explicitly known
doc checker hardening tests PASS
full-range project-log + transcript append-only guard PASS
PR/main CI authoritative-run semantics active
secret scan PASS
Ruff PASS
mypy PASS
minimal .gitignore present
active-spec reachability PASS
```

- [ ] **Step 2: Classify branch protection separately from code quality**

Allowed outcomes:

```text
MECHANICALLY ENFORCED
PROCESS-ENFORCED
BLOCKED
```

`PROCESS-ENFORCED` is acceptable only when mechanical enforcement is unavailable on the chosen private-plan combination and the limitation is durably recorded.

- [ ] **Step 3: Write execution record**

Create the execution record with exact commit SHAs, CI run IDs, tool versions, and any accepted degradation.

- [ ] **Step 4: Run fresh exact-head GitHub Actions**

Require successful current-head runs for both Documentation Consistency and Security/Quality workflows before claiming this gate passed.

- [ ] **Step 5: Append hardening checkpoint**

Record branch/SHA, gate result, unresolved limitations, and note explicitly:

```text
Eval Readiness is a separate gate and may already be executing or complete.
Repository Hardening does not by itself authorize capability-contract authoring.
```

- [ ] **Step 6: Commit**

```bash
git add docs/superpowers/plans/2026-09-04-pre-registry-repository-hardening-execution.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "docs: close pre-registry repository hardening gate"
```
