# CodeMaestro Architecture Decision Checkpoint — Comparative Research Pass 3

**Date:** 2026-09-04
**Status:** ABSORBED INTO `DECISIONS.md` — historical checkpoint, non-canonical wording
**Relationship to `DECISIONS.md`:** This dated checkpoint preserves the wording recorded when comparative research pass 3 was accepted. CM-ADR-019 through CM-ADR-022 have since been absorbed into the canonical `DECISIONS.md`. Where wording differs, **`DECISIONS.md` is authoritative**. This checkpoint must not be interpreted as a second active definition of the same ADR IDs.

---

## CM-ADR-019 — Intent-to-evidence traceability is a cross-cutting architecture layer

**Status:** ABSORBED INTO `DECISIONS.md` — canonical ADR ID CM-ADR-019

**Historical checkpoint decision:** CodeMaestro will preserve bidirectional traceability among material user intent, requirements, decisions/specifications, implementation plans, code, tests/evals, and observed evidence when the maintenance value justifies the rigor.

**Rationale:** Forward-only documentation cannot detect when implementation reality makes earlier approvals stale. Reliable long-horizon engineering requires both intent-to-code traceability and code/evidence-to-spec back-propagation.

**Historical consequences:**

- stale approvals may be explicitly invalidated when evidence changes;
- orphan requirements, tests, implementation behaviors, findings, or plans become detectable classes;
- traceability claims should bind to repository/provenance state when material;
- the mechanism uses proportional rigor and must not force heavyweight artifact chains onto trivial work;
- detailed research continues under CM-R-025.

**Canonical wording:** See `DECISIONS.md` → CM-ADR-019.

---

## CM-ADR-020 — Assurance is selected through an escalation ladder

**Status:** ABSORBED INTO `DECISIONS.md` — canonical ADR ID CM-ADR-020

**Historical checkpoint decision:** CodeMaestro will select assurance techniques according to risk, property structure, specification quality, tool maturity, and verification cost rather than prescribing one test technique universally.

**Rationale:** Example tests, characterization, differential/oracle testing, property-based testing, fuzzing, mutation testing, model/static verification, and machine-checked proof answer different classes of engineering questions. Using a stronger method only helps when the target exposes an appropriate invariant/oracle and the result can actually be verified.

**Historical consequences:**

- CM-R-006 expands into an Assurance Ladder;
- property-based or formal techniques are used selectively rather than by fashion;
- generated proof-like text never counts as formal verification unless accepted by the actual checker/prover;
- the cheapest method that establishes the required confidence is preferred.

**Canonical wording:** See `DECISIONS.md` → CM-ADR-020.

---

## CM-ADR-021 — Machine-generated counterexamples are first-class repair evidence

**Status:** ABSORBED INTO `DECISIONS.md` — canonical ADR ID CM-ADR-021

**Historical checkpoint decision:** Compiler/typechecker failures, theorem-prover counterexamples, fuzz/property counterexamples, schema-validator failures, model-checker output, static-analysis evidence, and conformance failures may be treated as structured evidence that directly seeds the next debugging or repair hypothesis.

**Rationale:** A checker failure is more than a red status; it is often the most discriminating evidence available for the next repair step. Preserving it improves reproducibility and reduces repeated investigation.

**Historical consequences:**

- counterexamples remain linked to the resulting fix and regression evidence when practical;
- CM-R-013 expands to cover counterexample-driven repair;
- CM-R-020 defines provenance requirements for these artifacts;
- repeated repair loops must still respect independent validation and may not redefine the evaluator to manufacture success.

**Canonical wording:** See `DECISIONS.md` → CM-ADR-021.

---

## CM-ADR-022 — Migration is a first-class workflow concern with reversible cutover discipline

**Status:** ABSORBED INTO `DECISIONS.md` — canonical ADR ID CM-ADR-022

**Historical checkpoint decision:** CodeMaestro will treat migration, compatibility, and cutover as a coherent engineering workflow across languages, runtimes, frameworks, schemas, APIs/protocols, infrastructure, and platforms. This does not yet require a standalone physical Skill.

**Rationale:** Migration failures commonly arise from missing compatibility inventory, irreversible batching, premature cutover, weak old-vs-new comparison, or cleanup before evidence stabilizes. These concerns recur across otherwise unrelated domains.

**Historical consequences:**

- migrations prefer characterization before change, reversible or dual-compatible transition when appropriate, small batches, explicit cutover criteria, rollback triggers, observation, and delayed cleanup;
- default research priority is P1, escalating to P0 for data-integrity, auth/security-boundary, or irreversible external-interface migrations;
- detailed methodology is tracked under CM-R-026;
- physical Skill packaging remains eval-driven.

**Canonical wording:** See `DECISIONS.md` → CM-ADR-022.

---

## Related accepted extensions

This checkpoint also records the following Pass-3 extensions to existing research tracks. Their current status and canonical queue entries are maintained in `../research/RESEARCH-BACKLOG.md` and their individual research records.

- **CM-R-012:** routing, effectiveness, composition, traceability preservation, and artifact-invalidation evals.
- **CM-R-020:** requirement/test/finding IDs and machine-generated counterexamples bind to provenance.
- **CM-R-021:** phase fingerprints, fresh-context resumption, and no-replay recovery.
- **CM-R-022:** architecture drift is bidirectional — design constrains code, while accepted code reality can invalidate stale design documentation.
- **CM-R-024:** verified findings may escalate into variant, property, fuzz, mutation, or formal assurance when justified.

## Explicit non-decisions

This checkpoint does not create standalone Skills for:

- traceability;
- every testing or formal method;
- resume routing;
- architecture drift;
- each migration subtype.

Those boundaries remain subject to routing, effectiveness, composition, and context-cost evals.
