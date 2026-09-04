# CM-R-026 — Migration, Compatibility & Cutover Engineering

**Priority:** P1 by default; promote to P0 when data integrity, authentication/security boundaries, or irreversible external interfaces are materially involved.
**Status:** IN RESEARCH
**Accepted:** 2026-09-04

## Research question

How should CodeMaestro plan, execute, verify, and roll back migrations across languages, runtimes, frameworks, APIs, schemas, protocols, infrastructure, and platforms while preserving compatibility and minimizing irreversible risk?

## Accepted direction

Migration engineering is a first-class workflow concern, but not yet a guaranteed standalone Skill.

Preferred conceptual lifecycle:

```text
INVENTORY
→ COMPATIBILITY ANALYSIS
→ CURRENT-BEHAVIOR CHARACTERIZATION
→ MIGRATION DESIGN
→ REVERSIBLE / DUAL-COMPATIBLE TRANSITION
→ SMALL BATCHES
→ OLD-vs-NEW COMPARISON
→ CUTOVER GATE
→ OBSERVATION
→ CLEANUP GATE
```

## Research scope

Study and define:

- dependency/runtime/framework compatibility matrices;
- schema and data migration safety;
- expand-contract patterns;
- dual-read / dual-write / shadow / dual-run patterns where appropriate;
- old-vs-new semantic/output comparison;
- reversible batching;
- feature flags and compatibility shims;
- cutover readiness evidence;
- rollback triggers and rollback feasibility;
- observability during transition;
- migration sequencing across dependent components;
- cleanup timing and deprecation/removal gates;
- migration-specific security and supply-chain risks;
- handling irreversible external contracts;
- traceability from migration intent to validation evidence.

## Risk escalation

Treat the migration as P0 research/design when it materially touches:

- irreversible or hard-to-recover data transformations;
- authentication, authorization, credentials, or trust boundaries;
- externally published protocols or APIs with compatibility obligations;
- financial or security-sensitive state;
- one-way vendor/platform cutovers;
- production systems without tested rollback.

## Evidence expectations

A migration should not be called successful solely because the new system starts or a test suite is green.

Depending on the target, stronger evidence may include:

- old/new output comparison;
- production-like replay;
- data reconciliation;
- compatibility/conformance tests;
- rollback rehearsal;
- shadow traffic comparison;
- schema validation;
- observability and error-budget checks;
- explicit proof that deprecated paths are no longer required before cleanup.

## Related CodeMaestro tracks

- CM-R-005 — supply-chain assurance;
- CM-R-006 — Assurance Ladder / testing strategy;
- CM-R-007 — PostgreSQL/Supabase practices;
- CM-R-015 — release and production readiness;
- CM-R-016 — language/toolchain intelligence;
- CM-R-020 — evidence/provenance;
- CM-R-022 — repository impact/drift;
- CM-R-025 — intent-to-evidence traceability.

## Expected output

- migration risk taxonomy;
- compatibility matrix contract;
- migration/cutover workflow;
- reversible-transition patterns;
- validation and reconciliation strategy;
- rollback/cutover gate contract;
- cleanup/deprecation gate;
- baseline eval scenarios.

## Non-decision

No physical `migration` Skill is required yet. Packaging remains contingent on routing/effectiveness/composition evals.
