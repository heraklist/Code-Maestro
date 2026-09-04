# Repository Work-Session Logging Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Milestone 0 operational by adding a status-aware documentation consistency checker, resolving the public-repository logging privacy/retention decision, creating canonical logging schemas and real-time session instructions, bootstrapping the repository logging filesystem, and validating an end-to-end work-session logging flow before any CodeMaestro Skill implementation begins.

**Architecture:** Milestone 0 is repository-development governance, not portable `@codemaestro` behavior. A dependency-free Python checker protects documentation authority/status consistency; Markdown governance artifacts define privacy, schemas, and the real-time session protocol; repository `logs/` directories hold sanitized user-visible session history and project-event history. `logs/logs/self-evolution/` is only reserved structurally here; Skill-owned Self-Evolution logging behavior is implemented later with the Self-Evolution Controller.

**Tech Stack:** Python 3 standard library (`unittest`, `pathlib`, `re`, `urllib.parse`), Markdown, Git/GitHub.

**Spec:** `docs/superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md`

## Global Constraints

- Milestone 0 is the **first implementation milestone** after written-spec approval.
- The documentation-consistency checker is the **first Milestone 0 deliverable**.
- `logs/conversations/` and `logs/logs/project/` are repository work-session governance for the user's Chat / Work / Codex sessions developing CodeMaestro; they are not generic portable Skill behavior.
- `logs/logs/self-evolution/` belongs to the later CodeMaestro Self-Evolution contract; Milestone 0 may reserve the path but must not implement the Self-Evolution Controller.
- Research execution `Status` and architectural `Disposition` are separate; `ACCEPTED` is reserved for sufficiently completed/reviewed/incorporated research.
- The consistency checker must reject multiple active/canonical ADR definitions while allowing historical `ABSORBED`, `SUPERSEDED`, or otherwise non-canonical occurrences.
- The checker must verify that referenced CM-R tracks have required backlog entries and working records, and that backlog `Status` equals record `Status` where a record exists.
- Internal repository Markdown links must resolve.
- Conversation/project logs are semantic append-only under ordinary operation; corrections/supersessions are appended, not silently rewritten.
- Public-repository transcript completeness is subordinate to privacy/security. Secrets and non-public sensitive data must not be committed.
- The canonical secret-redaction marker is `[REDACTED SECRET — not persisted]`.
- Milestone 0 is **not operational** until the CM-R-032 retention/deletion/public-sanitization policy is researched, decided, recorded, and the end-to-end logging validation passes.
- Do not create production `SKILL.md`, capability modules, Self-Evolution Controller, production plugin/package, or unrelated implementation in this plan.
- Do not merge PR #1 unless separately and explicitly authorized.

---

## File Structure

Create or modify the following focused units:

```text
tools/
└── doc_consistency.py
    # Dependency-free repository documentation consistency checker.

tests/
└── test_doc_consistency.py
    # Unit/regression tests for status-aware ADR, CM-R, and link validation.

docs/project-governance/
├── LOGGING-PRIVACY-RETENTION-POLICY.md
│   # Milestone-0-specific CM-R-032 decision for public/private logging lifecycle.
├── LOGGING-SCHEMAS.md
│   # Canonical transcript header, project event, correction, redaction, checkpoint schemas.
└── SESSION-LOGGING-PROTOCOL.md
    # Real-time Chat/Work/Codex repository work-session behavior.

logs/
├── conversations/
│   ├── README.md
│   └── <year>/<session-file>.md
└── logs/
    ├── project/
    │   ├── README.md
    │   └── <year>/<date>.log
    └── self-evolution/
        └── README.md
        # Reserved namespace only; later Skill-owned behavior.

docs/research/
├── CM-R-032-privacy-data-lifecycle-engineering.md
└── RESEARCH-BACKLOG.md
    # Record the Milestone-0 sub-question disposition without falsely completing all CM-R-032 research.

README.md
    # Point contributors/agents to the operational session protocol once validated.
```

Interfaces shared between tasks:

```python
# tools/doc_consistency.py
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def check_repository(root: Path) -> list[Finding]: ...
def check_adr_authority(root: Path) -> list[Finding]: ...
def check_research_index(root: Path) -> list[Finding]: ...
def check_markdown_links(root: Path) -> list[Finding]: ...
def main(argv: list[str] | None = None) -> int: ...
```

CLI contract:

```text
python tools/doc_consistency.py
```

- exit `0`: no findings;
- exit `1`: one or more consistency findings;
- output: one line per finding as `CODE path: message`, followed by `PASS` or `FAIL (<n> findings)`.

---

### Task 1: Build the status-aware documentation consistency checker

**Files:**
- Create: `tools/doc_consistency.py`
- Create: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: repository Markdown under `docs/` and `README.md`.
- Produces: `check_repository(root: Path) -> list[Finding]` and CLI exit status used by all later Milestone 0 verification.

- [ ] **Step 1: Write the failing ADR-authority tests**

Create `tests/test_doc_consistency.py` with temporary repositories proving that one canonical ADR plus one absorbed historical duplicate is valid, while two active definitions fail:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.doc_consistency import check_adr_authority


class AdrAuthorityTests(unittest.TestCase):
    def test_absorbed_duplicate_is_allowed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture").mkdir(parents=True)
            (root / "docs/architecture/DECISIONS.md").write_text(
                "## CM-ADR-019 — Canonical\n\n**Status:** Accepted — 2026-09-04\n",
                encoding="utf-8",
            )
            (root / "docs/architecture/PASS3.md").write_text(
                "## CM-ADR-019 — Historical\n\n**Status:** ABSORBED INTO `DECISIONS.md`\n",
                encoding="utf-8",
            )
            self.assertEqual(check_adr_authority(root), [])

    def test_two_active_definitions_fail(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs/architecture").mkdir(parents=True)
            (root / "docs/architecture/A.md").write_text(
                "## CM-ADR-019 — A\n\n**Status:** Accepted — 2026-09-04\n",
                encoding="utf-8",
            )
            (root / "docs/architecture/B.md").write_text(
                "## CM-ADR-019 — B\n\n**Status:** Accepted — 2026-09-04\n",
                encoding="utf-8",
            )
            findings = check_adr_authority(root)
            self.assertEqual([f.code for f in findings], ["ADR_DUPLICATE_ACTIVE"])
```

- [ ] **Step 2: Run the focused tests and confirm RED**

Run:

```bash
python -m unittest tests.test_doc_consistency.AdrAuthorityTests -v
```

Expected: import/error failure because `tools/doc_consistency.py` does not yet exist.

- [ ] **Step 3: Implement minimal ADR parsing**

Create `tools/doc_consistency.py` with:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ADR_RE = re.compile(r"^##\s+(CM-ADR-\d{3})\b", re.MULTILINE)
STATUS_RE = re.compile(r"^\*\*Status:\*\*\s*(.+)$", re.MULTILINE)
NON_CANONICAL_MARKERS = ("ABSORBED", "SUPERSEDED", "HISTORICAL", "NON-CANONICAL")


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def _markdown_files(root: Path):
    yield from sorted((root / "docs").rglob("*.md"))


def _sections(text: str, pattern: re.Pattern[str]):
    matches = list(pattern.finditer(text))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        yield match.group(1), text[match.start():end]


def _status(section: str) -> str:
    match = STATUS_RE.search(section)
    return match.group(1).strip() if match else ""


def _is_active(status: str) -> bool:
    upper = status.upper()
    return not any(marker in upper for marker in NON_CANONICAL_MARKERS)


def check_adr_authority(root: Path) -> list[Finding]:
    occurrences: dict[str, list[tuple[Path, str]]] = {}
    for path in _markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for adr_id, section in _sections(text, ADR_RE):
            occurrences.setdefault(adr_id, []).append((path, _status(section)))

    findings: list[Finding] = []
    for adr_id, items in sorted(occurrences.items()):
        active = [(path, status) for path, status in items if _is_active(status)]
        if len(active) > 1:
            paths = ", ".join(str(path.relative_to(root)) for path, _ in active)
            findings.append(Finding("ADR_DUPLICATE_ACTIVE", paths, f"{adr_id} has {len(active)} active definitions"))
    return findings
```

- [ ] **Step 4: Run ADR tests and confirm GREEN**

Run:

```bash
python -m unittest tests.test_doc_consistency.AdrAuthorityTests -v
```

Expected: 2 tests pass.

- [ ] **Step 5: Add failing CM-R status parity tests**

Append tests that create a backlog entry `CM-R-032` with `Status: IN RESEARCH`, a matching record with the same status, and then a mismatch with `Status: ACCEPTED`:

```python
from tools.doc_consistency import check_research_index


class ResearchIndexTests(unittest.TestCase):
    def _write_backlog(self, root: Path, status: str):
        research = root / "docs/research"
        research.mkdir(parents=True, exist_ok=True)
        (research / "RESEARCH-BACKLOG.md").write_text(
            f"## CM-R-032 — Privacy\n\n**Status:** {status}\n\n"
            "**Working record:** `CM-R-032-privacy.md`\n",
            encoding="utf-8",
        )
        (research / "CM-R-032-privacy.md").write_text(
            "# CM-R-032 — Privacy\n\n**Status:** IN RESEARCH\n",
            encoding="utf-8",
        )

    def test_matching_status_is_allowed(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_backlog(root, "IN RESEARCH")
            self.assertEqual(check_research_index(root), [])

    def test_mismatched_status_fails(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_backlog(root, "ACCEPTED")
            findings = check_research_index(root)
            self.assertIn("RESEARCH_STATUS_MISMATCH", [f.code for f in findings])
```

- [ ] **Step 6: Run the research tests and confirm RED**

Run:

```bash
python -m unittest tests.test_doc_consistency.ResearchIndexTests -v
```

Expected: failure because `check_research_index` is not defined.

- [ ] **Step 7: Implement CM-R existence and status parity**

Add to `tools/doc_consistency.py`:

```python
RESEARCH_HEADING_RE = re.compile(r"^##\s+(CM-R-\d{3})\b", re.MULTILINE)
WORKING_RECORD_RE = re.compile(r"\*\*Working record:\*\*\s*`([^`]+)`")


def check_research_index(root: Path) -> list[Finding]:
    research_dir = root / "docs/research"
    backlog = research_dir / "RESEARCH-BACKLOG.md"
    if not backlog.exists():
        return [Finding("RESEARCH_BACKLOG_MISSING", str(backlog.relative_to(root)), "canonical backlog missing")]

    text = backlog.read_text(encoding="utf-8")
    findings: list[Finding] = []
    indexed_ids: set[str] = set()

    for research_id, section in _sections(text, RESEARCH_HEADING_RE):
        indexed_ids.add(research_id)
        backlog_status = _status(section)
        record_match = WORKING_RECORD_RE.search(section)
        if record_match:
            record_path = research_dir / record_match.group(1)
            if not record_path.exists():
                findings.append(Finding("RESEARCH_RECORD_MISSING", str(record_path.relative_to(root)), f"{research_id} working record missing"))
                continue
            record_status = _status(record_path.read_text(encoding="utf-8"))
            if backlog_status != record_status:
                findings.append(Finding(
                    "RESEARCH_STATUS_MISMATCH",
                    str(record_path.relative_to(root)),
                    f"{research_id}: backlog={backlog_status!r} record={record_status!r}",
                ))

    for path in sorted(research_dir.glob("CM-R-*.md")):
        match = re.match(r"(CM-R-\d{3})", path.name)
        if match and match.group(1) not in indexed_ids:
            findings.append(Finding("RESEARCH_BACKLOG_ENTRY_MISSING", str(path.relative_to(root)), f"{match.group(1)} missing from backlog"))
    return findings
```

- [ ] **Step 8: Run research tests and confirm GREEN**

Run:

```bash
python -m unittest tests.test_doc_consistency.ResearchIndexTests -v
```

Expected: 2 tests pass.

- [ ] **Step 9: Add failing Markdown-link tests**

Add:

```python
from tools.doc_consistency import check_markdown_links


class MarkdownLinkTests(unittest.TestCase):
    def test_missing_relative_markdown_link_fails(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "README.md").write_text("[missing](docs/missing.md)\n", encoding="utf-8")
            findings = check_markdown_links(root)
            self.assertEqual([f.code for f in findings], ["LINK_TARGET_MISSING"])
```

- [ ] **Step 10: Run link test and confirm RED**

Run:

```bash
python -m unittest tests.test_doc_consistency.MarkdownLinkTests -v
```

Expected: failure because `check_markdown_links` is not defined.

- [ ] **Step 11: Implement local Markdown-link validation and CLI composition**

Add:

```python
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check_markdown_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    files = [root / "README.md", *_markdown_files(root)]
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                findings.append(Finding("LINK_OUTSIDE_REPO", str(path.relative_to(root)), raw_target))
                continue
            if not candidate.exists():
                findings.append(Finding("LINK_TARGET_MISSING", str(path.relative_to(root)), raw_target))
    return findings


def check_repository(root: Path) -> list[Finding]:
    return [
        *check_adr_authority(root),
        *check_research_index(root),
        *check_markdown_links(root),
    ]


def main(argv: list[str] | None = None) -> int:
    root = Path.cwd()
    findings = check_repository(root)
    for finding in findings:
        print(f"{finding.code} {finding.path}: {finding.message}")
    if findings:
        print(f"FAIL ({len(findings)} findings)")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

- [ ] **Step 12: Run all checker unit tests**

Run:

```bash
python -m unittest tests.test_doc_consistency -v
```

Expected: all tests pass.

- [ ] **Step 13: Run the checker against the actual branch**

Run:

```bash
python tools/doc_consistency.py
```

Expected: `PASS`. If the checker finds pre-existing drift, repair the documentation inconsistency rather than weakening the checker; rerun until `PASS`.

- [ ] **Step 14: Commit the checker**

```bash
git add tools/doc_consistency.py tests/test_doc_consistency.py docs README.md
git commit -m "test: add documentation consistency gate"
```

---

### Task 2: Resolve the Milestone-0 CM-R-032 logging privacy and retention policy

**Files:**
- Create: `docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md`
- Modify: `docs/research/CM-R-032-privacy-data-lifecycle-engineering.md`
- Modify: `docs/research/RESEARCH-BACKLOG.md`
- Test: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: v2 §17.4, CM-R-032, public-repository secret hygiene, current authoritative privacy sources.
- Produces: a concrete repository logging lifecycle decision required by Tasks 3–6 and Milestone-0 operational status.

- [ ] **Step 1: Add a failing policy-presence regression test**

Append:

```python
class LoggingPolicyTests(unittest.TestCase):
    REQUIRED_HEADINGS = (
        "## Scope",
        "## Storage classes",
        "## Public-safe transcript rule",
        "## Retention",
        "## Deletion and purge",
        "## Redaction",
        "## Access and authority",
        "## Review trigger",
    )

    def test_logging_privacy_policy_has_required_contract(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for heading in self.REQUIRED_HEADINGS:
            self.assertIn(heading, text)
```

- [ ] **Step 2: Run the policy test and confirm RED**

```bash
python -m unittest tests.test_doc_consistency.LoggingPolicyTests -v
```

Expected: failure because the policy file does not exist.

- [ ] **Step 3: Research the narrow policy question from current authoritative sources**

Use current primary/authoritative privacy guidance, starting with the NIST sources already recorded in CM-R-032, and answer only the Milestone-0 repository logging questions:

```text
What may be committed publicly?
What remains private/local only?
What is the retention rule for each storage class?
Who may authorize deletion/purge/history rewrite?
How are redactions represented?
How are backups/copies/digests handled?
What event is retained after an authorized purge?
What triggers policy re-review?
```

Capture source URLs, access date, scope, and limitations in the policy's `## Evidence basis` section.

- [ ] **Step 4: Write the concrete policy decision**

Create `docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md` with these exact semantic requirements:

```text
Public repository:
- only sanitized/public-safe conversation and project-event records;
- never persist secrets or non-public sensitive payloads;
- use explicit redaction markers;
- sanitized history may be retained as project audit history while useful and authorized.

Private/local raw transcript class:
- optional, not required for normal CodeMaestro repository operation;
- only when a real continuity/evidence need justifies it;
- never implied by the public repository;
- retention must be explicit and revocable by project authority.

Deletion/purge:
- legitimate privacy/security/legal deletion overrides ordinary semantic append-only behavior;
- authorized purge may rewrite repository history when necessary;
- retain only a non-sensitive purge event after removal;
- never preserve the removed secret/private payload in the purge record.
```

Also include the required headings from Step 1 and an `## Evidence basis` section with actual sources used.

- [ ] **Step 5: Update CM-R-032 without falsely closing the full track**

Keep:

```text
**Status:** IN RESEARCH
**Disposition:** DIRECTION ACCEPTED
```

Add a Milestone-0 sub-question result pointing to the new policy and explicitly state that the narrow logging lifecycle prerequisite is resolved while broader CM-R-032 methodology remains `IN RESEARCH`.

- [ ] **Step 6: Update the backlog's CM-R-032 Milestone-0 note**

Replace the unresolved Milestone-0 note with a pointer to `../project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md`, while keeping `Status: IN RESEARCH` and `Disposition: DIRECTION ACCEPTED`.

- [ ] **Step 7: Run policy and repository consistency tests**

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: all unit tests pass; repository checker prints `PASS`.

- [ ] **Step 8: Commit the policy decision**

```bash
git add docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md docs/research/CM-R-032-privacy-data-lifecycle-engineering.md docs/research/RESEARCH-BACKLOG.md tests/test_doc_consistency.py
git commit -m "docs: define repository logging privacy lifecycle"
```

---

### Task 3: Create canonical logging schemas

**Files:**
- Create: `docs/project-governance/LOGGING-SCHEMAS.md`
- Test: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: v2 §17 normative logging artifacts and Task 2 privacy policy.
- Produces: exact schema templates consumed by the session protocol and initial log files.

- [ ] **Step 1: Add failing schema-contract tests**

Add a test asserting `LOGGING-SCHEMAS.md` contains:

```python
class LoggingSchemaTests(unittest.TestCase):
    REQUIRED_TOKENS = (
        "Session started:",
        "Surface:",
        "Repository:",
        "Initial branch:",
        "Initial SHA:",
        "Transcript policy:",
        "TIMESTAMP",
        "SESSION",
        "EVENT / TYPE",
        "TARGET",
        "ACTION",
        "REASON",
        "BEFORE",
        "AFTER",
        "EVIDENCE",
        "AUTHORITY",
        "RESULT",
        "RELATED COMMIT / ARTIFACT",
        "CORRECTION / SUPERSEDES EVENT",
        "[REDACTED SECRET — not persisted]",
        "CHECKPOINT",
    )

    def test_logging_schema_contains_normative_contract(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "docs/project-governance/LOGGING-SCHEMAS.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for token in self.REQUIRED_TOKENS:
            self.assertIn(token, text)
```

- [ ] **Step 2: Run and confirm RED**

```bash
python -m unittest tests.test_doc_consistency.LoggingSchemaTests -v
```

Expected: failure because the schema file does not exist.

- [ ] **Step 3: Write `LOGGING-SCHEMAS.md`**

Include exact copy-ready templates for:

1. conversation session header;
2. `STATE CHANGE` entry;
3. project event with the 12 canonical fields;
4. `CORRECTION / SUPERSEDES EVENT <event-id>`;
5. typed redaction including the exact secret marker;
6. session `CHECKPOINT` containing branch/SHA, last action, decisions, mutations, evidence, unresolved items, and next authorized action.

State the timestamp format as:

```text
YYYY-MM-DD HH:mm:ss ±HH:MM
```

and state that UTC may additionally be stored for cross-runtime correlation.

- [ ] **Step 4: Run schema and full consistency tests**

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add docs/project-governance/LOGGING-SCHEMAS.md tests/test_doc_consistency.py
git commit -m "docs: define work-session logging schemas"
```

---

### Task 4: Define the canonical real-time session logging protocol

**Files:**
- Create: `docs/project-governance/SESSION-LOGGING-PROTOCOL.md`
- Modify: `README.md`
- Test: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: Task 2 privacy policy and Task 3 schemas.
- Produces: one repository instruction for every Chat / Work / Codex session working on CodeMaestro.

- [ ] **Step 1: Add a failing protocol test**

Test for these mandatory phase tokens:

```python
class SessionProtocolTests(unittest.TestCase):
    REQUIRED_TOKENS = (
        "SESSION ADMISSION GATE",
        "EVENT-TIME LOGGING",
        "PROGRESSIVE HISTORY LOADING",
        "PRIVACY / REDACTION GATE",
        "CHECKPOINT / HANDOFF GATE",
        "LOG WRITE FAILURE",
    )

    def test_session_protocol_has_required_gates(self):
        root = Path(__file__).resolve().parents[1]
        path = root / "docs/project-governance/SESSION-LOGGING-PROTOCOL.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for token in self.REQUIRED_TOKENS:
            self.assertIn(token, text)
```

- [ ] **Step 2: Run and confirm RED**

```bash
python -m unittest tests.test_doc_consistency.SessionProtocolTests -v
```

Expected: failure because the protocol file does not exist.

- [ ] **Step 3: Write the session admission gate**

Define this mandatory sequence for project-working sessions with authorized repository write capability:

```text
SESSION ADMISSION GATE
1. identify CodeMaestro repository and current branch/SHA;
2. read this protocol and the logging privacy policy;
3. locate or create the current session transcript;
4. read only recent/relevant project history needed for continuity;
5. append the session-start record;
6. only then begin material project work.
```

If write capability is unavailable, the session must state that repository logging is unavailable and must not claim the history was persisted.

- [ ] **Step 4: Define event-time logging triggers**

Require an append near the event for:

```text
user/design/research approval
file mutation
branch/SHA change
commit/PR change
eval/test failure or pass
scope/state change
correction/refutation
rollback/recovery
consequential external mutation
```

Do not rely on end-of-session retrospective reconstruction as the primary logging method.

- [ ] **Step 5: Define progressive history loading and privacy gates**

Require:

```text
load current state + relevant recent history first;
do not ingest all historical conversations by default;
apply the public-safe policy before persistence;
never commit secrets/private payloads for transcript completeness;
use canonical redaction markers when omission occurs.
```

- [ ] **Step 6: Define log-write failure behavior**

Use explicit status:

```text
LOG WRITE FAILED
```

For consequential work, pause further consequential mutation until the audit/continuity write is restored or the user explicitly authorizes a safe alternative. For low-risk analysis, work may continue only with an explicit continuity limitation and without claiming repository logging succeeded.

- [ ] **Step 7: Define checkpoint/handoff behavior**

Before session end or surface transfer, require the canonical checkpoint from `LOGGING-SCHEMAS.md`.

- [ ] **Step 8: Link the protocol from README**

Add a `Repository work-session protocol` link under the current authority/operations section. Make clear it governs chats developing this repository, not arbitrary projects using the future Skill.

- [ ] **Step 9: Run protocol, link, and full consistency tests**

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: all pass.

- [ ] **Step 10: Commit**

```bash
git add docs/project-governance/SESSION-LOGGING-PROTOCOL.md README.md tests/test_doc_consistency.py
git commit -m "docs: define real-time work-session protocol"
```

---

### Task 5: Bootstrap the actual repository logging filesystem and first live records

**Files:**
- Create: `logs/conversations/README.md`
- Create: `logs/logs/project/README.md`
- Create: `logs/logs/self-evolution/README.md`
- Create: `logs/conversations/<YYYY>/<session-file>.md`
- Create: `logs/logs/project/<YYYY>/<YYYY-MM-DD>.log`
- Test: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: privacy policy, logging schemas, session protocol, current branch/SHA/session state.
- Produces: operational repository directories plus the first real-time sanitized session and project-event records.

- [ ] **Step 1: Add failing filesystem-contract tests**

Use directory/path assertions rather than `.gitkeep`:

```python
class LoggingFilesystemTests(unittest.TestCase):
    def test_logging_roots_exist(self):
        root = Path(__file__).resolve().parents[1]
        required = (
            root / "logs/conversations/README.md",
            root / "logs/logs/project/README.md",
            root / "logs/logs/self-evolution/README.md",
        )
        for path in required:
            self.assertTrue(path.exists(), path)
```

- [ ] **Step 2: Run and confirm RED**

```bash
python -m unittest tests.test_doc_consistency.LoggingFilesystemTests -v
```

Expected: failure because the directories/files do not yet exist.

- [ ] **Step 3: Create the three directory README files**

`logs/conversations/README.md` states:

```text
Owner: repository project-working sessions.
Content: sanitized/public-safe user-visible session history.
Protocol: docs/project-governance/SESSION-LOGGING-PROTOCOL.md.
Not authority: transcripts are continuity evidence, not canonical project authority.
```

`logs/logs/project/README.md` states:

```text
Owner: repository project-working sessions.
Content: material project mutation/state events.
Semantic rule: append corrections/supersessions; do not silently rewrite ordinary history.
```

`logs/logs/self-evolution/README.md` states:

```text
Reserved owner: future CodeMaestro Self-Evolution Controller.
Milestone 0 does not implement Self-Evolution behavior.
Do not let ordinary project sessions use this stream as a substitute for project-event logging.
```

- [ ] **Step 4: Create the first live sanitized conversation record**

Resolve an offset-aware timestamp at execution time. Filename rule:

```text
logs/conversations/YYYY/YYYY-MM-DDTHHMMSS±HHMM_<surface>_<short-session-slug>.md
```

Use the canonical session header. Append **only user-visible content and observable action summaries available to the executing session**; do not fabricate missing earlier transcript content and do not persist hidden reasoning. If prior conversation material is unavailable, state the exact coverage boundary in the header/checkpoint rather than claiming completeness.

Apply Task 2 privacy policy before writing.

- [ ] **Step 5: Create the first project event log**

Create:

```text
logs/logs/project/YYYY/YYYY-MM-DD.log
```

Append events for Milestone-0 bootstrap using the canonical project-event schema, including current branch/SHA and related commits/artifacts as actually observed.

- [ ] **Step 6: Add an explicit checkpoint to the conversation record**

Append the canonical checkpoint after the filesystem/bootstrap work and before handing off to Task 6.

- [ ] **Step 7: Run filesystem and consistency tests**

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: all pass.

- [ ] **Step 8: Commit**

```bash
git add logs tests/test_doc_consistency.py
git commit -m "chore: bootstrap repository work-session logs"
```

---

### Task 6: Validate append, correction, redaction, resume, and handoff behavior end to end

**Files:**
- Modify: `tests/test_doc_consistency.py`
- Modify: active `logs/conversations/<YYYY>/<session-file>.md`
- Modify: active `logs/logs/project/<YYYY>/<YYYY-MM-DD>.log`
- Modify: `README.md` only if validation reveals documentation mismatch

**Interfaces:**
- Consumes: all Milestone 0 deliverables.
- Produces: verified Milestone-0 operational evidence and a clean handoff for the next implementation plan.

- [ ] **Step 1: Add format-level validation helpers/tests**

Add tests that read the real bootstrap records and verify:

```text
conversation file contains required session-header fields;
project event contains the canonical event fields used for that event;
timestamps match an offset-aware ISO-like form;
no literal test secret fixture is persisted;
checkpoint exists;
self-evolution directory contains no fabricated Self-Evolution run.
```

Use a harmless sentinel such as `CM_TEST_SECRET_DO_NOT_PERSIST` in an in-memory/test fixture and assert it never appears under `logs/` after the redaction formatter/path is exercised.

- [ ] **Step 2: Run the new tests and confirm RED for missing validation behavior**

```bash
python -m unittest tests.test_doc_consistency -v
```

Expected: the new tests expose any missing schema/checkpoint/redaction behavior before repair.

- [ ] **Step 3: Perform a real append event**

Append a new project event describing the validation start, using a fresh timestamp and current branch/SHA. Do not edit the earlier event in place.

- [ ] **Step 4: Perform a correction/supersession drill**

Append a harmless intentionally superseded test event, then append:

```text
CORRECTION / SUPERSEDES EVENT <test-event-id>
Previous statement: <bounded harmless statement>
Corrected state: <correct harmless statement>
Evidence: validation drill
```

Confirm the original event remains present.

- [ ] **Step 5: Perform a redaction drill without committing a secret**

Generate only the canonical marker in the durable test record:

```text
[REDACTED SECRET — not persisted]
```

Never place an actual credential or realistic secret value in the repository, test fixture, shell history, or commit.

- [ ] **Step 6: Perform a resume/handoff drill**

From a fresh process/context if available, read:

```text
SESSION-LOGGING-PROTOCOL.md
current transcript header/checkpoint
current project log tail
current branch/SHA
```

Verify that the next authorized action can be reconstructed without loading all historical conversations.

- [ ] **Step 7: Run the complete verification suite**

```bash
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: all unit/regression tests pass and checker prints `PASS`.

- [ ] **Step 8: Append the Milestone-0 validation result**

Append project and session records with actual results. Use `PASS` only for checks that actually ran successfully. Record any limitation explicitly.

- [ ] **Step 9: Verify the actual branch/PR state before completion claim**

Run/inspect:

```text
current branch
current HEAD SHA
dirty state
PR #1 head/status
```

Confirm the recorded checkpoint matches the actual state.

- [ ] **Step 10: Commit final Milestone-0 validation**

```bash
git add tests logs README.md
git commit -m "test: validate work-session logging foundation"
```

- [ ] **Step 11: Milestone-0 completion gate**

Milestone 0 may be marked operational only if all are true:

```text
doc consistency checker PASS
status-aware ADR rule PASS
CM-R backlog/record parity PASS
internal links PASS
logging privacy/retention policy exists and narrow CM-R-032 prerequisite is resolved
canonical schemas exist
session protocol exists
real logs filesystem exists
first sanitized session/project records exist
append/correction/redaction/checkpoint drill PASS
resume/handoff drill PASS
no Skill-owned Self-Evolution behavior was prematurely implemented
```

If any item is false, report Milestone 0 as `BLOCKED` or `PARTIALLY VERIFIED`, not complete.

---

## Self-Review Results

### 1. Spec coverage

Covered by this plan:

- v2 §17 repository logging ownership and real-time/event-time behavior — Tasks 3–6.
- v2 §17 canonical session header, project-event fields, timestamps, correction format, redaction marker, progressive history loading, checkpoint/handoff — Tasks 3–6.
- v2 §17 privacy boundary and CM-R-032 operational prerequisite — Task 2.
- v2 §15 Logging Integrity eval dimension and `evals/logging/` intent — Tasks 1, 3–6 provide the initial executable regression surface; the later full Skill eval plan can migrate/extend these tests into the final `evals/logging/` harness after Skill packaging exists.
- v2 §21 checker-first ordering — Task 1 is first.
- status-aware ADR uniqueness — Task 1.
- CM-R record/backlog existence and status parity — Task 1.
- internal-link validation — Task 1.
- actual logging filesystem and real-time session/project records — Task 5.
- Self-Evolution ownership separation — Tasks 4–6.

Intentionally not covered here because they belong to later independent plans:

- canonical capability-module implementation;
- production `SKILL.md`;
- full CodeMaestro eval harness beyond Milestone-0 repository governance;
- Self-Evolution Controller and its live audit implementation;
- final plugin/branding/package publication.

### 2. Placeholder scan

The plan contains no `TBD`, `TODO`, “implement later”, placeholder URLs, or unspecified code steps. Runtime-derived values such as timestamp, current SHA, session filename, and event ID use explicit generation rules rather than invented fixed values.

### 3. Type consistency

The checker interface is consistent across tasks:

```python
Finding(code: str, path: str, message: str)
check_adr_authority(root: Path) -> list[Finding]
check_research_index(root: Path) -> list[Finding]
check_markdown_links(root: Path) -> list[Finding]
check_repository(root: Path) -> list[Finding]
main(argv: list[str] | None = None) -> int
```

All tests import these exact names.
