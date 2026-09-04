# Architecture & Capability Registry Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the approved consolidated written specification into a durable living architecture plus a machine-checkable registry and explicit contracts for all 17 canonical CodeMaestro engineering capability families, without starting production Skill/runtime implementation.

**Architecture:** `ARCHITECTURE.md` becomes the current living architecture gateway/synthesis rather than a stale-review pointer. Capability contracts live as focused Markdown files under `docs/architecture/capabilities/`, while `docs/architecture/CAPABILITY-REGISTRY.json` provides the minimal machine-readable routing index required by the approved v2 design. A dependency-free validator extends the existing repository consistency gate so capability-family count, IDs, registry fields, contract paths, and contract/registry identity cannot drift silently.

**Tech Stack:** Python 3.12 standard library (`json`, `pathlib`, `re`, `unittest`), JSON, Markdown, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md`

## Global Constraints

- One public entrypoint remains `@codemaestro`; this slice must not create production `SKILL.md` or multiple public Skills.
- `CAPABILITY != SKILL != ROLE != TOOL` remains normative.
- Capability Freeze remains 17 canonical engineering families unless reopened by real task/eval evidence.
- Registry metadata is routing/packaging metadata only; it cannot grant authority or override root policy/user/system authority.
- Each capability contract must define: Purpose, Use when, Do not use as primary when, Nearest-neighbor boundaries, Inputs, Outputs, Required evidence, Escalation conditions, De-escalation conditions, Risk modifiers.
- Each registry entry must define: `id`, `name`, `purpose`, `trigger_signals`, `exclusion_signals`, `nearest_neighbors`, `risk_modifiers`, `evidence_requirements`, `contract_path`.
- Registry IDs must be stable lowercase kebab-case identifiers and unique.
- `contract_path` values must resolve inside the repository and point to the matching capability contract.
- The registry must contain exactly the 17 approved capability families and no hidden/public-Skill aliases.
- Existing documentation/logging consistency checks remain mandatory and may not be weakened to make this slice pass.
- No production router, runtime capability loading, host/plugin packaging, Self-Evolution Controller, or production eval harness is implemented in this plan.
- PR #1 remains Draft and unmerged unless separately authorized.
- Repository session/project logging remains event-time under `docs/project-governance/SESSION-LOGGING-PROTOCOL.md`.

---

## File Structure

Create or modify:

```text
docs/architecture/
├── ARCHITECTURE.md
├── CAPABILITY-REGISTRY.json
└── capabilities/
    ├── README.md
    ├── requirements-architecture-systems.md
    ├── product-ux-ui.md
    ├── software-implementation.md
    ├── debugging-diagnostics.md
    ├── testing-assurance.md
    ├── review-audit-compliance.md
    ├── security-trust.md
    ├── privacy-data-lifecycle.md
    ├── database-data.md
    ├── interface-protocol-contract.md
    ├── build-toolchain-environment.md
    ├── migration-compatibility.md
    ├── performance-capacity.md
    ├── cicd-platform-delivery.md
    ├── reliability-observability-sre-incident.md
    ├── ai-llm-agent-mcp.md
    └── research-experimental-language.md

tools/
├── doc_consistency.py
└── capability_registry.py

tests/
├── test_doc_consistency.py
└── test_capability_registry.py

README.md
logs/conversations/...                         # event-time append only
logs/logs/project/...                          # event-time append only
```

`tools/capability_registry.py` public interfaces:

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass(frozen=True)
class CapabilityFinding:
    code: str
    path: str
    message: str


def load_registry(root: Path) -> dict[str, Any]: ...
def check_capability_registry(root: Path) -> list[CapabilityFinding]: ...
```

The existing `tools/doc_consistency.py::check_repository()` must compose the capability-registry findings so the normal CI gate protects this architecture layer.

---

### Task 1: Canonicalize the living architecture document

**Files:**
- Modify: `docs/architecture/ARCHITECTURE.md`
- Modify: `tests/test_doc_consistency.py`

**Interfaces:**
- Consumes: approved consolidated v2, canonical ADRs, research backlog, operational Milestone 0 governance.
- Produces: current living architecture summary and navigation surface for later registry/eval/runtime work.

- [ ] **Step 1: Add a failing architecture-canonicalization test**

Add a test requiring `ARCHITECTURE.md` to no longer contain `detailed canonicalization pending written-spec approval` and to contain these headings/tokens:

```python
class LivingArchitectureTests(unittest.TestCase):
    def test_architecture_is_current_living_synthesis(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / "docs/architecture/ARCHITECTURE.md").read_text(encoding="utf-8")
        self.assertNotIn("detailed canonicalization pending written-spec approval", text.lower())
        for token in (
            "**Status:** CURRENT LIVING ARCHITECTURE",
            "## Authority hierarchy",
            "## Runtime architecture",
            "## Canonical engineering capability families",
            "## Shared Intelligence",
            "## Execution and governance",
            "## Evaluation and quality",
            "## Repository work-session governance",
            "## Implementation sequence",
        ):
            self.assertIn(token, text)
```

- [ ] **Step 2: Run the focused test and confirm RED**

Run:

```bash
python -m unittest tests.test_doc_consistency.LivingArchitectureTests -v
```

Expected: FAIL because the current gateway still states canonicalization is pending.

- [ ] **Step 3: Replace the stale gateway with the living architecture synthesis**

Write `ARCHITECTURE.md` so it:

- declares `**Status:** CURRENT LIVING ARCHITECTURE`;
- preserves the authority order headed by consolidated v2 and `DECISIONS.md`;
- defines one public `@codemaestro` entrypoint;
- summarizes the four conceptual layers: Engineering Capabilities, Shared Intelligence, Execution & Governance, Optional Independent Roles;
- lists all 17 canonical capability-family names exactly;
- names all seven Shared Intelligence layers exactly;
- summarizes capability-first cross-runtime execution and `TASK REQUIREMENTS ∩ AVAILABLE ∩ AUTHORIZED ∩ SAFETY/RISK = EXECUTION CEILING`;
- preserves Task Capability Manifest and Project Quality Contract;
- links repository logging governance and keeps it separate from portable Self-Evolution audit behavior;
- points to `CAPABILITY-REGISTRY.json` and `capabilities/README.md` once created;
- records the approved post-Milestone-0 sequence;
- explicitly states that production Skill/runtime implementation has not yet started.

Do not duplicate the entire consolidated v2; this is a living synthesis/navigation authority, with detailed normative behavior remaining in v2/ADRs/contracts.

- [ ] **Step 4: Run focused and full consistency tests**

Run:

```bash
python -m unittest tests.test_doc_consistency.LivingArchitectureTests -v
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: all PASS.

- [ ] **Step 5: Append the architecture-canonicalization project event and commit**

Record the mutation under the active repository project log, including before/after authority state and exact test evidence.

Commit message:

```text
docs: canonicalize living architecture after milestone zero
```

---

### Task 2: Establish the capability-registry schema and validator

**Files:**
- Create: `docs/architecture/CAPABILITY-REGISTRY.json`
- Create: `docs/architecture/capabilities/README.md`
- Create: `tools/capability_registry.py`
- Create: `tests/test_capability_registry.py`
- Modify: `tools/doc_consistency.py`

**Interfaces:**
- Consumes: the 17 approved capability-family names and the v2 §5.2/§5.3 capability/registry contracts.
- Produces: stable machine-readable registry contract and repository consistency validation.

- [ ] **Step 1: Write failing registry shape tests**

Create `tests/test_capability_registry.py` with tests that require:

```python
EXPECTED_IDS = {
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

class CapabilityRegistryTests(unittest.TestCase):
    def test_registry_has_exactly_canonical_ids(self):
        root = Path(__file__).resolve().parents[1]
        registry = load_registry(root)
        ids = {item["id"] for item in registry["capabilities"]}
        self.assertEqual(ids, EXPECTED_IDS)
        self.assertEqual(len(registry["capabilities"]), 17)

    def test_registry_validator_accepts_repository(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(check_capability_registry(root), [])
```

- [ ] **Step 2: Run and confirm RED**

Run:

```bash
python -m unittest tests.test_capability_registry -v
```

Expected: import/file failure because registry/validator do not exist.

- [ ] **Step 3: Implement minimal registry loader/validator**

`tools/capability_registry.py` validates:

```text
REGISTRY_MISSING
REGISTRY_JSON_INVALID
REGISTRY_CAPABILITIES_INVALID
CAPABILITY_COUNT_INVALID
CAPABILITY_ID_DUPLICATE
CAPABILITY_FIELD_MISSING
CAPABILITY_FIELD_EMPTY
CAPABILITY_CONTRACT_MISSING
CAPABILITY_CONTRACT_ID_MISMATCH
CAPABILITY_NEIGHBOR_UNKNOWN
```

Required registry top-level shape:

```json
{
  "schema_version": 1,
  "public_entrypoint": "@codemaestro",
  "capability_freeze_count": 17,
  "capabilities": []
}
```

Required fields per capability are exactly those in Global Constraints. `nearest_neighbors` must contain only known registry IDs and may be empty only when explicitly justified by the contract; all first-generation entries should declare at least one neighbor.

- [ ] **Step 4: Create registry skeleton with all 17 canonical entries**

Populate exact `id`, `name`, `purpose`, routing signals, neighbors, risk modifiers, evidence requirements, and expected `contract_path`. Contract paths may initially point to files created in Tasks 3–6; until those files exist the validator should fail with `CAPABILITY_CONTRACT_MISSING`, proving the remaining work is visible.

- [ ] **Step 5: Wire registry validation into `check_repository()`**

Import `check_capability_registry` and append its findings to the existing aggregate consistency result without weakening ADR/CM-R/link/log checks.

- [ ] **Step 6: Run and confirm expected partial RED**

Run:

```bash
python -m unittest tests.test_capability_registry -v
python tools/doc_consistency.py
```

Expected: registry structure tests pass far enough to expose missing contract files; repository checker FAILS only on the intentionally missing capability contracts.

- [ ] **Step 7: Commit schema/validator foundation**

Commit message:

```text
feat: add canonical capability registry contract
```

Record the RED state in the project ledger; do not claim registry completion yet.

---

### Task 3: Author capability contracts 1–5

**Files:**
- Create:
  - `docs/architecture/capabilities/requirements-architecture-systems.md`
  - `docs/architecture/capabilities/product-ux-ui.md`
  - `docs/architecture/capabilities/software-implementation.md`
  - `docs/architecture/capabilities/debugging-diagnostics.md`
  - `docs/architecture/capabilities/testing-assurance.md`
- Modify: `tests/test_capability_registry.py`

**Interfaces:**
- Consumes: registry IDs/names and consolidated v2 §§6.1–6.5.
- Produces: five normative capability contracts matching registry identity.

- [ ] **Step 1: Add contract-schema tests for the first five IDs**

For each contract require:

```text
Capability ID: `<id>`
## Purpose
## Use when
## Do not use as primary when
## Nearest-neighbor boundaries
## Inputs
## Outputs
## Required evidence
## Escalation conditions
## De-escalation conditions
## Risk modifiers
```

- [ ] **Step 2: Run tests and confirm RED because files are absent**

Run the focused contract test class and verify all five expected missing-file failures.

- [ ] **Step 3: Write the five contracts from the approved v2 semantics**

Each contract must be concise and routing-oriented. Preserve explicit boundaries, for example:

- Requirements/Architecture vs Implementation;
- Product/UX/UI vs implementation-only frontend work;
- Implementation vs root-cause debugging;
- Debugging vs broad audit/review;
- Testing/Assurance vs Review/Audit findings.

Do not introduce new capability responsibilities beyond approved v2/supporting authority.

- [ ] **Step 4: Run focused tests**

Expected: first five contracts pass; registry still reports remaining missing contracts.

- [ ] **Step 5: Log and commit**

Commit message:

```text
docs: add core delivery capability contracts
```

---

### Task 4: Author capability contracts 6–10

**Files:**
- Create:
  - `docs/architecture/capabilities/review-audit-compliance.md`
  - `docs/architecture/capabilities/security-trust.md`
  - `docs/architecture/capabilities/privacy-data-lifecycle.md`
  - `docs/architecture/capabilities/database-data.md`
  - `docs/architecture/capabilities/interface-protocol-contract.md`
- Modify: `tests/test_capability_registry.py`

**Interfaces:**
- Consumes: consolidated v2 §§6.6–6.10 and existing focused research/ADRs.
- Produces: assurance/trust/data/contract capability boundaries.

- [ ] **Step 1: Add failing schema/identity tests for IDs 6–10**
- [ ] **Step 2: Run and confirm RED**
- [ ] **Step 3: Write the five contracts**

Boundary requirements include:

- Review/Audit verifies/refutes findings and spec compliance but does not replace Testing/Assurance or Security methodology;
- Security owns authorization/trust/misuse resistance while Privacy owns purpose/minimization/retention/deletion harms including authorized processing;
- Database/Data owns persistent-data integrity/query/transaction concerns while Interface/Protocol/Contract owns inter-component agreement semantics.

- [ ] **Step 4: Run focused tests and registry checker**
- [ ] **Step 5: Log and commit**

Commit message:

```text
docs: add assurance trust and data capability contracts
```

---

### Task 5: Author capability contracts 11–15

**Files:**
- Create:
  - `docs/architecture/capabilities/build-toolchain-environment.md`
  - `docs/architecture/capabilities/migration-compatibility.md`
  - `docs/architecture/capabilities/performance-capacity.md`
  - `docs/architecture/capabilities/cicd-platform-delivery.md`
  - `docs/architecture/capabilities/reliability-observability-sre-incident.md`
- Modify: `tests/test_capability_registry.py`

**Interfaces:**
- Consumes: consolidated v2 §§6.11–6.15.
- Produces: build/change/performance/delivery/operations contracts.

- [ ] **Step 1: Add failing schema/identity tests for IDs 11–15**
- [ ] **Step 2: Run and confirm RED**
- [ ] **Step 3: Write the five contracts**

Boundary requirements include:

- Build/Toolchain/Environment vs CI/CD delivery;
- Migration/Compatibility vs ordinary implementation/refactor;
- Performance/Capacity vs reliability symptoms without measured workload evidence;
- CI/CD/Platform/Delivery vs build correctness;
- Reliability/Observability/SRE/Incident vs isolated debugging and generic deployment.

- [ ] **Step 4: Run focused tests and registry checker**
- [ ] **Step 5: Log and commit**

Commit message:

```text
docs: add platform performance and reliability capability contracts
```

---

### Task 6: Author capability contracts 16–17 and close registry validation

**Files:**
- Create:
  - `docs/architecture/capabilities/ai-llm-agent-mcp.md`
  - `docs/architecture/capabilities/research-experimental-language.md`
- Modify: `tests/test_capability_registry.py`
- Modify: `docs/architecture/capabilities/README.md`

**Interfaces:**
- Consumes: consolidated v2 §§6.16–6.17, §7, §8, and accepted Research/Experimental supporting design.
- Produces: complete 17-contract registry layer.

- [ ] **Step 1: Add failing schema/identity tests for IDs 16–17**
- [ ] **Step 2: Run and confirm RED**
- [ ] **Step 3: Write both contracts**

The Research/Experimental/Language contract must preserve that Language/System/Repository/Context/Freshness/Evidence/Traceability remain Shared Intelligence or supporting intelligence, not hidden extra capability families.

- [ ] **Step 4: Complete `capabilities/README.md`**

Document:

- registry vs contract vs public Skill distinction;
- authority hierarchy;
- how nearest-neighbor boundaries are used;
- that registry data cannot grant authority;
- Capability Freeze rule;
- next consumer: RED routing/capability/composition evals.

- [ ] **Step 5: Run full capability validation**

Run:

```bash
python -m unittest tests.test_capability_registry -v
python -m unittest tests.test_doc_consistency -v
python tools/doc_consistency.py
```

Expected: PASS, with exactly 17 registry entries and zero missing contracts.

- [ ] **Step 6: Log and commit**

Commit message:

```text
docs: complete canonical capability contract registry
```

---

### Task 7: Integrate navigation, CI evidence, and execution handoff

**Files:**
- Modify: `README.md`
- Modify: `docs/architecture/ARCHITECTURE.md`
- Create: `docs/superpowers/plans/2026-09-04-architecture-capability-registry-integration-execution.md`
- Append: active conversation/project logs

**Interfaces:**
- Consumes: completed living architecture, registry, 17 contracts, validator results.
- Produces: durable next-stage handoff for RED eval planning.

- [ ] **Step 1: Add failing navigation assertions**

Require README and living architecture to link to:

```text
docs/architecture/CAPABILITY-REGISTRY.json
docs/architecture/capabilities/README.md
```

- [ ] **Step 2: Run and confirm RED if navigation is missing**
- [ ] **Step 3: Update README/architecture navigation and current phase**

Current phase after this task must say capability-contract/registry foundation is operational and the next unstarted stage is RED eval implementation; do not claim production Skill implementation.

- [ ] **Step 4: Create immutable execution record**

Record each Task 1–7 result and exact commit/CI evidence without rewriting the original plan checkboxes as retrospective execution history.

- [ ] **Step 5: Run final exact-branch gate**

Run through GitHub Actions on the real PR checkout:

```text
python -m unittest tests.test_doc_consistency -v
python -m unittest tests.test_capability_registry -v
python tools/doc_consistency.py
```

Expected: all PASS.

- [ ] **Step 6: Append final project checkpoint**

Checkpoint must contain:

- current branch/SHA;
- registry count `17`;
- exact final CI run/result;
- PR Draft/unmerged state;
- unresolved research status remains unchanged;
- next authorized stage: write/execute RED eval implementation plan.

- [ ] **Step 7: Commit**

Commit message:

```text
docs: close architecture capability registry integration
```

---

## Completion Gate

This slice is complete only when all are true:

```text
ARCHITECTURE.md is CURRENT LIVING ARCHITECTURE
AND
CAPABILITY-REGISTRY.json contains exactly 17 approved canonical families
AND
all registry entries have required non-empty routing/evidence fields
AND
all nearest-neighbor IDs resolve
AND
all 17 contract paths exist and match their registry IDs
AND
repository consistency checker composes capability-registry validation
AND
existing ADR/CM-R/link/logging checks remain green
AND
README/architecture navigation points to registry/contracts
AND
execution record + live project checkpoint exist
AND
fresh exact-branch GitHub Actions run is success
```

If any condition fails, do not begin RED eval implementation.
