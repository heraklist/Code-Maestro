# Pass 4 Acceptance & Canonicalization Checkpoint

**Date:** 2026-09-04
**Status:** ACCEPTED

## Authority

This checkpoint records explicit user approval of all Candidate groups A–H in `../research/2026-09-04-comparative-research-pass-4.md`.

It supersedes the earlier `REVIEW` status line in that research-pass document. The research evidence remains unchanged; the architectural disposition is now accepted.

## Accepted Pass 4 directions

1. **Interface / Protocol / Contract Engineering** — open `CM-R-027`.
2. **Performance / Benchmarking / Capacity Engineering** — open `CM-R-028`.
3. **Evidence Coverage & Target Fidelity** — extend CM-R-020/025.
4. **Recovered Specification** — extend CM-R-022/025 with `RECOVERED / OBSERVED SPECIFICATION`.
5. **Operational Assurance & Resilience Closure** — extend CM-R-006/009/013/015/020/026.
6. **System Invariants, Misuse Resistance & Agentic Taint Flow** — extend CM-R-002/003/004/008/014/023 and CM-R-027 where relevant.
7. **Agent Eval Contract Hardening** — extend CM-R-012/020.
8. **Skill Registry Fault Isolation** — extend CM-R-001/018/023.

## New research records

- `../research/CM-R-027-interface-protocol-contract-engineering.md`
- `../research/CM-R-028-performance-benchmarking-capacity-engineering.md`

## Canonical decision mapping

The accepted directions are recorded in `DECISIONS.md` as:

- CM-ADR-023 — Interface and protocol contracts are first-class engineering agreements
- CM-ADR-024 — Performance engineering is evidence-driven and workload-relative
- CM-ADR-025 — Evidence conclusions are coverage-bounded and target-faithful
- CM-ADR-026 — Recovered specifications have weaker authority than normative intent
- CM-ADR-027 — Operational closure requires user/business-boundary evidence
- CM-ADR-028 — Security analysis includes misuse resistance and agentic taint flow
- CM-ADR-029 — Agent evals distinguish task, trajectory, side-effect, and evidence contracts
- CM-ADR-030 — Skill discovery and loading must be fault-isolated

## Canonicalization repair discovered during acceptance

State inspection before mutation found that several previously accepted Pass 3 decisions and research items existed as research records but were not yet reflected in the canonical decision log/backlog/living architecture.

The decision-log portion is repaired in the same acceptance change:

- CM-ADR-019 — Intent-to-evidence traceability is bidirectional
- CM-ADR-020 — Assurance is selected by risk and property shape
- CM-ADR-021 — Machine-generated counterexamples are repair evidence
- CM-ADR-022 — Migrations require compatibility-aware, reversible cutover discipline

The existing research records CM-R-021 through CM-R-026 remain authoritative working records. Their absence from the older backlog snapshot is documentation drift, not evidence that those tracks were unapproved.

## Architecture synthesis

The accepted architecture now includes these cross-cutting systems/concepts:

```text
User intent
    ↓
CodeMaestro orchestrator
    ├─ Research Lab
    ├─ Language Intelligence
    ├─ Repository Intelligence
    ├─ Context / long-horizon state
    ├─ Engineering sub-skills
    ├─ Interface & Contract methodology
    ├─ Migration methodology
    └─ Performance & Capacity methodology
           ↓
Intent-to-Evidence Traceability
           ↓
Evidence Model
    ├─ authority
    ├─ target/source fidelity
    ├─ provenance
    ├─ assessed coverage
    ├─ reproducibility
    ├─ uncertainty
    └─ epistemic status
           ↓
Assurance / Verification
    ├─ tests
    ├─ differential/oracle checks
    ├─ property/fuzz/mutation
    ├─ reconciliation/control evidence
    ├─ model/formal verification where justified
    └─ user-boundary operational closure
           ↓
Decision / authorization gates
           ↓
Authorized execution
```

## Physical packaging boundary

Acceptance of these mechanisms does **not** authorize one Skill per domain or immediate production implementation.

The project remains in architecture/research preparation. Physical Skill boundaries, scripts, eval harnesses, and runtime role packaging remain gated by research synthesis, baseline RED evals, approved implementation design, and implementation planning.
