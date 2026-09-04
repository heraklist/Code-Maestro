# Comparative Research Pass 3 — Traceability, Assurance, Migration, and Autonomous Engineering

**Date:** 2026-09-04
**Status:** ACCEPTED — Candidate A–D accepted as architecture/research direction. Physical Skill boundaries remain eval-driven.

## Objective

Run a third comparative pass over skills and agent repositories, looking only for mechanisms that materially extend CodeMaestro beyond the already accepted architecture.

This pass deliberately deprioritized generic role/persona skills and duplicate senior-engineer prompts.

## High-signal findings

### 1. Bidirectional SDLC traceability is a distinct mechanism

Several systems preserve explicit chains such as:

```text
user intent / issue
↔ requirements
↔ specification
↔ architecture / plan
↔ tasks
↔ tests
↔ code
↔ operational evidence
```

The important new idea is not merely writing those artifacts. It is **back-propagating reality upstream** when code, tests, or behavior changes so that previously approved artifacts can become stale and lose their approved status.

Relevant patterns:

- `tomzx/agents` `backpropagate-sdlc`: walks code/tests back through tasks, plan, specification, requirements, and issue, checking adjacent and end-to-end consistency.
- traceability-led documentation systems: assign durable requirement/test/change identifiers and maintain bidirectional links rather than treating docs as prose snapshots.

### Accepted direction

Open a new cross-cutting capability/research track:

**CM-R-025 — Intent-to-Evidence Traceability & Drift Propagation**

Candidate responsibilities:

- stable IDs for material requirements/decisions/tests when warranted;
- forward traceability: intent → design → implementation → verification;
- backward traceability: actual implementation/test behavior → affected plans/specs/requirements;
- drift detection and invalidation of stale approvals;
- explicit orphan detection (requirement with no implementation/test, test with no current requirement, code behavior with no documented authority where one is required);
- provenance binding to repository state.

This is broader than documentation drift and narrower than general repository comprehension.

---

### 2. Assurance should be selected by property shape, not by testing fashion

Trail of Bits property-based testing guidance provides a strong decision principle: use property-based testing when the code has an algebraic or invariant structure rather than as a universal replacement for example tests.

Useful property shapes include:

- roundtrip;
- inverse;
- oracle/reference equivalence;
- idempotence;
- invariants;
- commutativity/associativity/identity;
- cheap checker for expensive computation.

A valuable quality distinction is also explicit:

```text
no crash
< type preservation
< invariant
< idempotence
< roundtrip / oracle
```

Formal-verification projects add a further layer: important properties can be translated into theorem statements and mechanically proved when the semantics and stakes justify that cost.

### Accepted direction

Do **not** create a generic mandatory Formal Methods Skill.

Extend **CM-R-006 — Modern Testing Strategy** into an **Assurance Ladder**:

```text
example regression tests
→ characterization / differential tests
→ property-based tests
→ fuzz / mutation / adversarial tests
→ model checking / static proof obligations where suitable
→ formal specification / theorem proving for selected invariants
```

The correct rung is selected by:

- consequence of failure;
- property/invariant structure;
- availability of a stable specification;
- cost of creating and maintaining the oracle/proof;
- toolchain maturity;
- ability to verify the result mechanically.

Formal proof should never be claimed from a generated theorem/proof sketch that was not accepted by the actual prover/checker.

---

### 3. Proof failure can become structured repair evidence

`facebookresearch/repoprover` and related formalization systems show a useful orchestration pattern:

```text
source/spec
→ formal sketch/specification
→ proof attempt
→ proof/compiler failure
→ repair task
→ independent review
→ merge only while canonical branch remains buildable
```

The significant mechanism for CodeMaestro is **checker feedback as repair evidence**, not the Lean-specific implementation.

This generalizes to:

- compiler/typechecker errors;
- theorem-prover counterexamples;
- schema validators;
- model checkers;
- static analyzers;
- protocol conformance suites;
- fuzz/property counterexamples.

### Accepted direction

Extend the Evidence/Debugging model with a class of **machine-generated counterexample evidence**. A counterexample should seed the next hypothesis/repair step directly and remain attached to the resulting fix and regression test.

---

### 4. Migration engineering deserves a first-class workflow, but probably not yet a first-class Skill

Migration-focused skills consistently converge on several mechanisms:

- compatibility inventory before mutation;
- dual-run / dual-read / dual-write or expand-contract strategies when applicable;
- old-vs-new output comparison for semantic changes;
- small reversible batches;
- explicit cutover gate;
- rollback trigger defined before cutover;
- delayed cleanup of shims/old paths until evidence stabilizes.

This is relevant across:

- language/runtime upgrades;
- framework upgrades;
- database/schema migrations;
- APIs/protocols;
- infrastructure/platform changes.

### Accepted direction

Open a new research item rather than deciding a physical Skill:

**CM-R-026 — Migration, Compatibility & Cutover Engineering**

It should unify the migration concerns currently spread across language intelligence, database, release readiness, dependencies, and architecture.

Default priority is P1, promoted to P0 for migrations touching data integrity, authentication/security boundaries, or irreversible external interfaces.

---

### 5. Persisted blueprint/state is a strong anti-context-rot pattern

`iannil/skills` reinforces a pattern already emerging elsewhere: long project chains recover from fresh sessions by reading persisted blueprints and state fingerprints rather than continuing indefinitely in one conversation.

Useful distinction:

```text
orchestrator state ≠ model memory
```

A resume router can inspect durable artifacts and decide which phase is actually incomplete without replaying earlier phases.

### Accepted direction

Fold this into CM-R-021. Add explicit study of:

- phase fingerprints;
- resumption without replay;
- completion evidence per phase;
- stale/contradictory state recovery;
- fresh-context restart criteria.

No separate Resume Skill is justified yet.

---

### 6. Architecture-drift control benefits from two directions

Existing CodeMaestro thinking mostly asks whether implementation drifted from the accepted architecture.

This pass strengthens the reverse direction too:

```text
accepted design → code conformity
actual code reality → design/spec freshness
```

When implementation legitimately changes, architecture documentation and earlier approvals may need to be invalidated or revised.

### Accepted direction

CM-R-022 covers **bidirectional architecture drift**, while CM-R-025 owns artifact-chain traceability and invalidation semantics.

---

## Reference classification updates

### Promote for deep study

- `trailofbits/skills` — assurance, property testing, mutation testing, spec compliance, false-positive resistance, code-context building.
- `facebookresearch/repoprover` — formalization orchestration, durable shared repository, checker-driven repair, merge-gated verified state.
- `tomzx/agents` — bidirectional SDLC traceability, artifact invalidation/back-propagation, explicit assumptions/questions/decisions.
- `muratcankoylan/Agent-Skills-for-Context-Engineering` — long-horizon state and eval methodology.

### Selective extraction

- `iannil/skills` — persisted blueprint/state fingerprints, resume routing, acceptance-before-advance, context resets.
- migration-specialized skill collections — dual compatibility, cutover/rollback, semantic output diffing.
- product/document traceability skills — stable IDs and bidirectional links where they demonstrate concrete maintenance behavior.

### Keep as discovery only

Large persona catalogs and marketplace entries whose primary distinction is title/domain wording without unique methodology, deterministic tooling, evidence contracts, or evaluable behavior.

## Accepted architecture changes

### Candidate A — Intent-to-Evidence Traceability — ACCEPTED

Add a cross-cutting traceability layer capable of connecting user intent, requirements, decisions, specifications, implementation, tests, and observed outcomes, with explicit drift/invalidation behavior.

### Candidate B — Assurance Ladder — ACCEPTED

Extend the testing/evidence architecture so CodeMaestro deliberately chooses the cheapest assurance technique that provides the required confidence, escalating to property/fuzz/formal methods only when justified.

### Candidate C — Counterexample-Driven Repair — ACCEPTED

Treat compiler/prover/fuzzer/schema/model-checker counterexamples as durable evidence that can directly seed debugging, repair, regression tests, and provenance.

### Candidate D — Migration/Compatibility research track — ACCEPTED

Add CM-R-026 for phased, reversible, compatibility-aware migration engineering.

## New research items

### CM-R-025 — Intent-to-Evidence Traceability & Drift Propagation

**Priority:** P0

Research stable identifiers, bidirectional artifact links, orphan detection, approval invalidation, code-to-spec back-propagation, and traceability evals.

### CM-R-026 — Migration, Compatibility & Cutover Engineering

**Priority:** P1 by default; P0 when data integrity, auth/security boundaries, or irreversible external interfaces are materially involved.

Research compatibility matrices, expand-contract/dual-run patterns, data and semantic diffing, staged cutover, rollback triggers, reversible batching, and cleanup gates.

## Existing tracks extended by this decision

- **CM-R-006** — add Assurance Ladder and formal/property/fuzz/mutation selection criteria.
- **CM-R-012** — add evals for traceability preservation and artifact invalidation.
- **CM-R-013** — add counterexample-driven debugging/repair.
- **CM-R-020** — bind requirement/test/finding IDs and counterexamples to provenance.
- **CM-R-021** — add phase fingerprints, fresh-context resumption, no-replay recovery.
- **CM-R-022** — add bidirectional architecture drift.
- **CM-R-024** — connect verified findings to variant/property/formal assurance when warranted.

## Rejected over-expansion

This pass does **not** recommend standalone Skills for:

- every formal method/tool;
- every testing technique;
- resume routing;
- architecture drift alone;
- every migration subtype;
- generic requirements writing;
- generic senior-engineer/reviewer personas.

These mechanisms should be composed behind stable CodeMaestro contracts unless later evals demonstrate a real routing/context benefit from physical separation.

## Acceptance result

Candidate A–D are accepted as CodeMaestro architecture/research direction as of 2026-09-04.

This acceptance does not decide physical Skill boundaries or authorize production implementation. Those remain gated by research synthesis, baseline RED evals, and later implementation design.
