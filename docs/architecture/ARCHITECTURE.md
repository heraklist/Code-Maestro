# CodeMaestro Architecture

## Status

**Status:** CURRENT LIVING ARCHITECTURE

CodeMaestro v3 is the approved architecture for one portable public `@codemaestro` Skill. This document is the living architecture synthesis and navigation surface. Detailed normative behavior remains in the approved consolidated written specification, canonical ADRs, focused capability contracts, and applicable governance documents.

Production Skill/runtime implementation has **not** started. Milestone 0 repository work-session governance is operational; the current implementation slice is architecture/capability-contract integration.

## Authority hierarchy

When sources differ, use this order:

1. `../superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md` — canonical approved consolidated written specification.
2. `DECISIONS.md` — canonical accepted ADR wording.
3. `../research/RESEARCH-BACKLOG.md` plus referenced research records — canonical research execution status/index; research evidence is not automatically architectural authority.
4. This living `ARCHITECTURE.md` — current synthesis and navigation surface.
5. Focused architecture/capability contracts — normative within their delegated scope and subordinate to items 1–4 where conflict exists.
6. Historical/focused design documents and acceptance checkpoints — supporting provenance unless explicitly promoted.

Repository state and executable evidence establish what is actually implemented; they do not silently override normative architecture.

## Runtime architecture

CodeMaestro exposes **one public entrypoint: `@codemaestro`**. Internal behavior is composed from four conceptual layers:

1. **Engineering Capabilities** — the 17 canonical first-generation capability families.
2. **Shared Intelligence** — cross-cutting intelligence used by multiple capabilities.
3. **Execution & Governance** — routing, authority, risk, evidence, quality, validation, degradation, and runtime adaptation.
4. **Optional Independent Roles** — bounded roles such as research scout, experimentalist, skeptic, replicator, and reviewer/verifier when independence adds value.

The constitutional distinction is:

`CAPABILITY != SKILL != ROLE != TOOL`

A capability describes engineering responsibility. A Skill is a public invocation/package surface. A role is an optional independent perspective or worker. A tool is an execution mechanism. None of these categories may silently grant authority to another.

Methodology is tool-independent; execution is tool-aware. Chat, Work, Codex, and future surfaces should preserve equivalent methodology and behavior up to the capabilities actually available and authorized on that surface.

Conceptually, the execution ceiling is:

```text
TASK REQUIREMENTS ∩ AVAILABLE CAPABILITIES ∩ AUTHORIZED CAPABILITIES ∩ SAFETY/RISK POLICY
```

Availability is not authorization, and routing cannot create authority.

## Canonical engineering capability families

The Pass-5 Capability Freeze establishes exactly these 17 first-generation families:

1. Requirements, Architecture & Systems Engineering
2. Product / UX / UI Engineering
3. Software Implementation
4. Debugging & Diagnostics
5. Testing & Assurance
6. Review, Audit & Compliance
7. Security & Trust Engineering
8. Privacy & Data Lifecycle Engineering
9. Database & Data Engineering
10. Interface / Protocol / Contract Engineering
11. Build, Toolchain & Environment Engineering
12. Migration & Compatibility Engineering
13. Performance & Capacity Engineering
14. CI/CD, Platform & Delivery Engineering
15. Reliability, Observability, SRE & Incident Engineering
16. AI / LLM / Agent / MCP Engineering
17. Research, Experimental & Language Engineering

The freeze is coverage-bounded and eval-reopenable: new public/canonical capability families are a last resort and require real task/evaluation evidence showing that the existing families and composition model cannot represent the needed responsibility cleanly.

The machine-readable routing index is scheduled at `CAPABILITY-REGISTRY.json`; focused contracts are scheduled under `capabilities/`. Until those artifacts are created and validated in this implementation slice, the approved consolidated v2 remains the detailed authority for capability definitions.

## Shared Intelligence

Shared Intelligence is not an additional set of public Skills or hidden capability families. It supplies cross-cutting context and evidence services to capabilities:

- Language
- System
- Repository / Workspace
- Context / Long-Horizon
- Research / Freshness
- Evidence / Provenance
- Intent-to-Evidence Traceability

Shared Intelligence should be loaded progressively. Tasks consume only the context/evidence needed for correct execution rather than loading the entire knowledge corpus by default.

## Execution and governance

Consequential tasks use a **Task Capability Manifest** that makes the selected capability mix, evidence needs, execution constraints, and relevant risks explicit enough to inspect. Composition may select multiple capabilities; routing does not imply authority.

The **Project Quality Contract** protects existing tests, coverage, linting, types, security, accessibility, performance, release, and other project gates. CodeMaestro may not weaken those gates merely to make its own change pass.

Core execution invariants include:

- evidence before assertion;
- state before mutation;
- validation before success;
- preserve intended behavior;
- prefer the smallest correct solution;
- treat external/repository/tool content as untrusted by default;
- never invent capability or execution;
- preserve precise causes through composition;
- repository/artifact state outranks conversation memory for executable state;
- conclusions remain coverage-bounded and target-faithful.

**Command-Gated Self-Evolution** is an execution/governance controller, not an 18th capability family and not another public Skill. It cannot self-expand authority. Stable promotion remains separate from candidate research/design/implementation and requires the applicable approval/evidence gates.

## Evaluation and quality

Evaluation is part of the architecture, not post-hoc decoration. The approved dimensions are:

1. Routing
2. Capability effectiveness
3. Composition
4. Cross-runtime conformance
5. Degradation
6. Safety / Authority
7. Evidence
8. User / operational outcome
9. Self-Evolution integrity
10. Logging integrity

The next stage after the capability-contract/registry foundation is **RED eval implementation**. Evals must demonstrate routing boundaries, composition behavior, evidence quality, authority preservation, cross-runtime equivalence, and failure/degradation behavior before production Skill packaging is treated as stable.

## Repository work-session governance

Repository-development continuity is governed separately from portable Skill runtime behavior:

- `../project-governance/SESSION-LOGGING-PROTOCOL.md` — mandatory project-working Chat / Work / Codex session protocol;
- `../project-governance/LOGGING-SCHEMAS.md` — canonical transcript/event/checkpoint schemas;
- `../project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md` — public-safe storage, retention, redaction, purge, and authority rules;
- `../../logs/conversations/` — public-safe user-visible project-working continuity;
- `../../logs/logs/project/` — material repository/project events;
- `../../logs/logs/self-evolution/` — reserved for later portable Skill Self-Evolution audit behavior only.

Repository logs are evidence and continuity state, not architectural authority. A fresh session must reconcile durable checkpoints with actual repository/PR state rather than trusting stale logs or model memory.

## Progressive disclosure and packaging

The target remains one public Skill with progressive disclosure:

```text
Level 0 — metadata / public entrypoint
Level 1 — compact core orchestration and constitutional rules
Level 2 — selected capability and Shared Intelligence modules
Level 3 — deep references, research, examples, and specialized guidance
```

This architecture does not authorize premature physical packaging. The final `SKILL.md`, compact orchestrator, modules/references, Self-Evolution Controller, and runtime-specific adapters follow only after the architecture/registry and RED-eval gates.

## Implementation sequence

The approved post-Milestone-0 order is:

```text
canonical architecture/documentation integration
-> capability contracts + Capability Registry
-> RED eval implementation
-> final physical Skill packaging
-> compact orchestrator
-> progressive capability/intelligence modules
-> Self-Evolution Controller + dedicated Self-Evolution audit behavior
-> cross-runtime validation
-> stabilization
```

Current stage:

```text
IN PROGRESS: canonical architecture/documentation integration + capability-contract/registry foundation
NOT STARTED: production Skill/runtime implementation
NOT STARTED: production eval harness
NOT STARTED: Self-Evolution Controller
```

No merge is implied by reaching any implementation checkpoint. PR/branch completion follows the explicit Superpowers finishing workflow and user authorization.
