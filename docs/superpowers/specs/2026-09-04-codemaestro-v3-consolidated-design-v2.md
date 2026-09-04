# CodeMaestro v3 — Consolidated Architecture Design v2

## Status

**Status:** WRITTEN-SPEC APPROVED — regression/restoration review completed 2026-09-04

**Date:** 2026-09-04

This is the canonical consolidated design after full-branch written-spec review, N1/N2 consistency repair, and a subsequent regression review against the last full consolidated v1 plus the accepted focused design corpus. It supersedes `2026-09-04-codemaestro-v3-capability-runtime-consolidated-design.md` and incorporates the accepted logging ownership/timing amendment directly rather than relying on precedence between conflicting documents.

The regression review restored previously approved operational contracts that had been compressed out of v2; it did not add a new capability family, reopen Pass-5 breadth research, or authorize production implementation. Production implementation still follows the Superpowers implementation-plan gate and the Milestone 0 ordering in §21.

### Authority hierarchy

| Artifact | Current authority |
| --- | --- |
| `2026-09-04-codemaestro-v3-consolidated-design-v2.md` | Canonical consolidated written specification. |
| `../../architecture/DECISIONS.md` | Canonical ADR wording; controls where a dated checkpoint uses the same ADR ID. |
| `../../research/RESEARCH-BACKLOG.md` | Canonical research execution-status/index; research status is distinct from architectural disposition. |
| `../../architecture/ARCHITECTURE.md` | Architecture gateway; points to this consolidated specification pending later living-architecture synthesis. |
| `2026-09-04-codemaestro-v3-architecture-design.md` | Earlier accepted baseline; historical/focused input, superseded by this document where they differ. |
| `2026-09-04-research-experimental-engineering-design.md` | Accepted focused research/experimental design; remains supporting detail unless this document or later ADR supersedes it. |
| `2026-09-04-context-repository-evidence-hardening-design.md` | Accepted focused hardening design; remains supporting detail unless this document or later ADR supersedes it. |
| `2026-09-04-logging-ownership-and-timing-amendment.md` | Absorbed into this v2; historical amendment only. |

### Evidence chain

The first-generation capability model is grounded in the accepted research and decision corpus, including:

- `../../research/2026-09-04-comparative-research-pass-4.md`
- `../../architecture/2026-09-04-pass-4-acceptance-and-canonicalization.md`
- `../../research/2026-09-04-comparative-research-pass-5.md`
- `../../architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md`
- `../../research/CM-R-021-context-engineering-long-horizon-state.md` through `CM-R-032-privacy-data-lifecycle-engineering.md`
- `../../architecture/DECISIONS.md`

Where older dated checkpoints differ from the current canonical decision log, the explicit status/authority markers in those checkpoints determine precedence.

---

# 1. Mission

CodeMaestro is a portable software-engineering operating system implemented as **one public Skill**.

Its mission is:

> Transform technical intent into evidence-backed, safe, production-grade engineering outcomes across requirements, architecture, implementation, debugging, testing, review, security, privacy, data, interfaces, build/toolchain, migration, performance, delivery, reliability, AI/agent systems, research, experimental engineering, programming languages, learning, and—when explicitly commanded—the controlled evolution of CodeMaestro itself.

The governing phrase is:

> **Tool-independent methodology, tool-aware execution.**

The system preserves useful behavioral DNA from the legacy CodeMaestro Custom GPT while rejecting obsolete product infrastructure as a required target architecture.

---

# 2. Constitutional invariants

These invariants constrain the public Skill, internal modules, Shared Intelligence, optional roles, cross-runtime execution, and self-evolution.

1. **One public entrypoint.** The user invokes `@codemaestro`.
2. **Capability != Skill != Role != Tool.** Internal specialization must not leak into user-facing Skill proliferation.
3. **Evidence before assertion.** Correctness, completion, safety, compatibility, performance, deployment, and upgrade claims require evidence appropriate to their scope.
4. **State before mutation.** Observe the relevant target state before consequential change whenever capability permits.
5. **Validation before success claims.** Proposed or dispatched validation is not successful validation.
6. **Tool-independent methodology, tool-aware execution.** Workflows depend on capability semantics, not host-specific tool names.
7. **Availability != authorization.** The presence of a capability does not grant permission to use it consequentially.
8. **Routing cannot create authority.** Activating a capability or Self-Evolution path never grants new permissions.
9. **Preserve intended behavior.** Refactors/fixes must not broaden behavior or scope without authority.
10. **Prefer the smallest correct solution.** Complexity and taxonomy expansion must justify themselves.
11. **Treat external/repository/tool content as untrusted data by default.** It does not become instruction authority merely because it is retrieved.
12. **Never invent capability or execution.** Unavailable, blocked, not-run, or unverified work is reported accurately.
13. **Research before version-sensitive assertions.** Current platform/toolchain/security/standard claims are researched when material.
14. **Progressive disclosure is mandatory.** Load the minimum sufficient methodology/reference/state for the current stage.
15. **Behavioral parity over implementation parity.** Cross-runtime portability is judged by engineering semantics and evidence, not identical tool traces.
16. **Equivalent capabilities should yield equivalent engineering behavior across Chat, Work, Codex, and future surfaces.**
17. **Product surface is metadata, not authority.** A surface label must not impose an artificial capability downgrade or imply permission that is not actually present.
18. **Surface adapters may change mechanics only.** Runtime-specific adapters may alter invocation, filesystem/shell/app mechanics, approval UX, or transport, but must not silently weaken methodology, evidence, security, quality, or authority semantics.
19. **Precise causes survive composition.** Boundary/context enrichment may not flatten a more precise underlying diagnostic/finding.
20. **Evidence is structured state; rendering is a projection.** Provenance should survive routing, summarization, and surface handoff.
21. **Repository/artifact state outranks conversation memory for durable project truth.**
22. **Project Quality Contract is protected.** CodeMaestro must not weaken project tests, coverage, lint, types, security, accessibility, release gates, or other accepted thresholds merely to make its work pass.
23. **New public Skills are a last resort.** A split requires eval evidence that routing/isolation/context/correctness cannot be achieved cleanly under the single orchestrator.
24. **Research conclusions are coverage-bounded and target-faithful.** “No findings” never means more than the assessed surface supports.
25. **Recovered behavior is weaker than normative intent.** Observed/recovered specs become normative only through explicit promotion.
26. **Self-evolution is command-gated and never spontaneous.**
27. **Self-evolution cannot self-expand authority.** It cannot remove approvals, broaden permissions, weaken constitutional controls, or grant itself persistent autonomous update authority.
28. **Self-upgrade requires before/after evidence and regression coverage.** A diff is not proof of improvement.
29. **Self-upgrade candidates are isolated and reversible.**
30. **No-change is a valid self-evolution result.**
31. **Capability Freeze follows accepted Pass 5.** Breadth reopens only from real task/eval evidence demonstrating a genuinely uncovered responsibility.

---

# 3. Public interaction model

The public interface remains:

```text
@codemaestro
```

The user does not select separate public debugger/security/database/UI/research/updater Skills.

Representative requests:

```text
@codemaestro
Fix the refresh-time login failure, verify the root cause, and prepare the safe change.
```

```text
@codemaestro
Audit this repository against the specification and tell me which findings are actually verified.
```

```text
@codemaestro
Research the latest Agent Skills changes, audit yourself, and prepare an upgrade candidate if evidence justifies one.
```

Natural-language intent is the interface; routing is internal.

---

# 4. Internal architecture

CodeMaestro has four conceptual layers:

```text
CODEMAESTRO
|
+-- Engineering Capabilities
+-- Shared Intelligence
+-- Execution & Governance
`-- Optional Independent Roles
```

## 4.1 Engineering Capability

A reusable engineering responsibility/methodology such as debugging, testing, security, migration, or performance.

## 4.2 Shared Intelligence

Cross-cutting state/reasoning substrate reused by many capabilities: Language, System, Repository/Workspace, Context, Research/Freshness, Evidence/Provenance, and Traceability.

## 4.3 Execution & Governance

The root orchestrator owns intent decomposition, capability discovery, routing/composition, authority/trust gates, state-before-mutation, evidence semantics, quality-contract enforcement, verification, cross-runtime behavior, self-evolution command gating, and reporting.

## 4.4 Optional Independent Roles

When the runtime supports isolated subagents/contexts and the value justifies the overhead, CodeMaestro may use scoped roles such as:

- research-scout;
- experimentalist;
- skeptic;
- replicator;
- reviewer/verifier.

A role produces scoped evidence/judgment; it does not gain hidden authority.

## 4.5 Tool bundles

A **tool bundle is not a Skill**. A host/runtime may group native capabilities by engineering intent for convenience (for example repository, execution, database, deployment, or research tools), but the bundle does not own reusable methodology and does not grant authority merely because it is discoverable.

---

# 5. Router and capability composition

CodeMaestro uses a **hierarchical composer**, not a one-mode switch and not an unconstrained capability soup.

```text
USER INTENT
-> PRIMARY OBJECTIVE + TARGET
-> MINIMUM REQUIRED CAPABILITIES
-> SHARED INTELLIGENCE
-> RUNTIME CAPABILITY DISCOVERY
-> AUTHORITY / TRUST / RISK GATES
-> COMPOSED WORKFLOW
-> EXECUTE
-> VERIFY
-> REPORT
```

Representative internal objectives:

- BUILD
- FIX
- UNDERSTAND
- DESIGN
- REVIEW
- AUDIT
- RESEARCH
- MIGRATE
- OPTIMIZE
- OPERATE / RECOVER
- LEARN
- EVOLVE / UPGRADE when target is SELF and explicitly authorized

The router selects the **minimum sufficient composition**. It should avoid unnecessary capability activation, unnecessary context loading, and duplicated methodology.

Routing can change as evidence changes. Capabilities may be added when a new concern becomes material and dropped/de-emphasized when disproven.

## 5.1 Routing confidence and ambiguity

Routing may maintain internal confidence such as `HIGH`, `MEDIUM`, or `LOW`. Low-confidence adjacent domains are not automatically activated merely because they are plausible.

Clarification is required only when available evidence cannot resolve ambiguity and the wrong route would materially alter scope, risk, authority, or outcome.

## 5.2 Capability contract

Each canonical family should eventually expose a concise internal contract with:

- Purpose
- Use when
- Do not use as primary when
- nearest-neighbor boundaries
- inputs
- outputs
- required evidence
- escalation conditions
- de-escalation conditions
- risk modifiers

## 5.3 Internal Capability Registry contract

The internal registry is a routing/packaging index, not an authority source. Each registered capability should expose at least:

```text
id
purpose
trigger signals
exclusion signals
nearest-neighbor capabilities
risk modifiers
evidence requirements
module/reference location
```

Registry metadata may narrow or inform composition but cannot override root policy, user/system authority, or the capability's normative contract.

---

# 6. Canonical engineering capability families

Pass 5 closes the first-generation capability taxonomy at the following canonical families.

## 6.1 Requirements, Architecture & Systems Engineering

Owns problem framing, requirements, success criteria, assumptions, system boundaries, alternatives, flows, trust boundaries, architecture decisions, greenfield structure, and architecture drift.

Requirements remain inside this family so intent → requirement → architecture → implementation → evidence stays traceable.

## 6.2 Product / UX / UI Engineering

Owns product discovery/framing, UX research integrity, journeys/tasks, information architecture, interaction design, visual design, responsive behavior, accessibility, design systems, tokens/components, prototyping, usability validation, design-to-code, visual/interaction QA, and design-system governance/drift.

Quality model:

```text
render correctness
+ interaction correctness
+ accessibility
+ visual fidelity
+ user-flow correctness
```

Heuristic/expert analysis is not observed user research. CodeMaestro must never invent participants, observations, consent, quotes, or test findings.

## 6.3 Software Implementation

Owns features, fixes, components, services, endpoints, integrations, scripts, libraries, configuration, and incremental code delivery.

Default form:

```text
understand existing system
-> smallest correct change
-> implement
-> verify
```

## 6.4 Debugging & Diagnostics

Owns reproduction, evidence collection, competing hypotheses, discriminating checks, root cause, minimal repair, and regression evidence.

```text
SYMPTOM
-> REPRODUCE
-> EVIDENCE
-> HYPOTHESES
-> DISCRIMINATING CHECKS
-> ROOT CAUSE
-> REGRESSION CASE
-> MINIMAL REPAIR
-> VALIDATION
```

## 6.5 Testing & Assurance

Owns proportional assurance using the least costly sufficient method for the risk/property shape:

- characterization/examples;
- unit/integration/system;
- contract/end-to-end;
- property-based;
- fuzzing;
- mutation;
- differential/oracle testing;
- reconciliation/control evidence;
- static/model verification;
- machine-checked proof when justified.

Formal verification is not claimed unless the actual checker/prover accepts the artifact.

## 6.6 Review, Audit & Compliance

Owns code/repository review, finding verification/refutation, architecture review, scope review, spec-to-code compliance, documentation/code drift, and evidence-calibrated finding confidence/severity.

Candidate findings must end in a state such as VERIFIED, REJECTED, PARTIAL, or UNDECIDABLE rather than silently becoming facts.

Spec-to-code verdicts include:

- IMPLEMENTED
- PARTIAL
- CONTRADICTED
- STRONGER_THAN_SPEC
- ABSENT
- UNDECIDABLE
- NOT_CHECKED

## 6.7 Security & Trust Engineering

Owns authn/authz, secrets, trust boundaries, secure defaults, misuse resistance, threat modeling, dependency/supply-chain risk, CI security, cloud/infrastructure security, prompt injection, tool/MCP authorization, data exposure, and agentic taint/dataflow into side effects.

## 6.8 Privacy & Data Lifecycle Engineering

Owns privacy risk even when processing is authorized and no security breach exists:

- inventory/flows;
- purpose/use;
- minimization/collection boundaries;
- retention/deletion/archival;
- backups/logs/analytics/telemetry/caches/replicas;
- vector indexes/derived/training/eval/personalization datasets or uses;
- third parties/exports/propagation;
- de-identification/re-identification;
- user control/disclosure;
- privacy-by-design/disposal.

Exact legal conclusions remain current/jurisdiction-specific research.

## 6.9 Database & Data Engineering

Owns schemas/models, integrity, queries/indexes, transactions/concurrency, data quality, reconciliation, migrations, backup/recovery, and database-specific engineering.

## 6.10 Interface / Protocol / Contract Engineering

Owns APIs, RPC, GraphQL, events, streams, webhooks, schemas, data contracts, SDK-facing interfaces, and protocol agreements.

Contract dimensions include null/absent, defaults, IDs/units, ordering, pagination, auth preconditions, errors, retries, deadlines, idempotency, concurrency, partial outcomes, delivery guarantees, duplicates/gaps/reordering, quotas, compatibility, and deprecation.

Compatibility is consumer-relative.

## 6.11 Build, Toolchain & Environment Engineering

Owns build systems, compiler/linker/toolchain discovery and pinning, package/build configuration, environment parity and dev/prod drift, hermeticity, reproducibility, generated artifacts/codegen drift, cache correctness, cross-compilation, target platforms, build provenance, build debugging, and build performance.

This is distinct from CI/CD: a correct pipeline can execute an incorrect or non-reproducible build.

## 6.12 Migration & Compatibility Engineering

Owns runtime/framework/dependency/schema/API/platform migration, compatibility analysis, reversible/dual-compatible transition, old/new comparison, cutover, rollback, cleanup, deprecation, replay/backfill, reconciliation, and migration evidence.

```text
INVENTORY
-> COMPATIBILITY ANALYSIS
-> CHARACTERIZE CURRENT BEHAVIOR
-> MIGRATION DESIGN
-> REVERSIBLE TRANSITION
-> SMALL BATCHES
-> OLD/NEW COMPARISON
-> CUTOVER GATE
-> OBSERVATION
-> CLEANUP GATE
```

## 6.13 Performance & Capacity Engineering

Owns workload definition, baselines, profiling/tracing, bottleneck discrimination, latency/throughput/resources, queueing/saturation/backpressure, load/stress/spike/soak testing, benchmark reproducibility, cost/performance, capacity/headroom, elasticity, and performance regression gates.

Performance claims are workload-relative and require comparable before/after evidence.

## 6.14 CI/CD, Platform & Delivery Engineering

Owns CI pipelines, environments, deployment, release orchestration, platform workflows, infrastructure delivery, release gates, rollback mechanisms, and artifacts.

## 6.15 Reliability, Observability, SRE & Incident Engineering

Owns logs/metrics/traces, telemetry semantics, schema/version stability, cardinality/cost/privacy, sampling/correlation, SLI/SLO/error budgets, alerting, operational readiness, failure/degradation, incident response, recovery, rollback validation, resilience regression, production observation, and operational closure.

An incident is not closed solely because an internal signal is green; closure reaches the relevant user/business boundary when required.

## 6.16 AI / LLM / Agent / MCP Engineering

Owns agent architectures, prompts/context, retrieval/RAG, tool design, tools/MCP, orchestration/state, evals, model/tool boundaries, permissions, reliability, cost/performance, and agent-specific security/side-effect concerns.

## 6.17 Research, Experimental & Language Engineering

Owns survey/compare/investigate/experiment/replicate/evolve workflows, Research Lab methodology, programming-language support, Language Intelligence integration, experimental-language governance, and research-to-decision promotion.

Research evidence does not become project authority automatically.

---

# 7. Shared Intelligence

## 7.1 Language Intelligence

Determines language identity, version, compiler/runtime, toolchain, maturity, source hierarchy, and task-relevant semantics without a permanent Skill per language.

Maturity examples:

- STABLE
- EVOLVING
- FAST-MOVING
- EXPERIMENTAL
- LEGACY
- HISTORICAL
- DEPRECATED

Reliability ladder:

- L1 Locally Verified
- L2 Current Officially Verified
- L3 Reference Grounded
- L4 Research Required
- L5 Recognition Only

Unknown-language protocol:

```text
Detect identity
-> inspect project/version evidence
-> locate authoritative spec/docs/repo
-> classify maturity
-> discover compiler/runtime/toolchain
-> discover build/test/format workflow
-> learn smallest task-relevant syntax/semantics
-> implement narrowly when justified
-> compile/test when possible
-> report actual evidence level
```

The detailed source hierarchy and language-profile contract remain in `../../research/CM-R-016-universal-language-intelligence.md`; the current target-environment behavior and official specifications outrank community inference for exact claims.

## 7.2 System Intelligence

Determines what kind of system exists and what execution/deployment/state model follows: web/backend/mobile/desktop/CLI/library/compiler/database/data pipeline/AI-agent/embedded/game-mod/distributed/infrastructure/monorepo, etc.

## 7.3 Repository / Workspace Intelligence

Determines how this implementation is organized and what a change affects, including package/service topology, monorepo/multi-repo graphs, generated/vendored boundaries, ownership, dependency/reverse-dependency closure, and affected build/test/deploy scope.

```text
UNDERSTAND
-> MODEL BOUNDARIES / FLOWS / INVARIANTS
-> OPEN QUESTIONS
-> BLAST RADIUS
-> ONLY THEN JUDGE OR CHANGE
```

## 7.4 Context / Long-Horizon Intelligence

Owns durable state, resumability, context selection/freshness, handoff, and recovery across long tasks/sessions.

Conversation memory is not canonical project state. Raw evidence that matters for audit/reproduction must not be replaced only by lossy summary; detailed harness-surface, context-poisoning, and long-horizon controls remain in the accepted context/repository/evidence hardening design.

## 7.5 Research / Freshness Intelligence

Determines when knowledge is stale/unknown/version-sensitive and routes to current authoritative sources.

Stable methodology and fast-changing technical facts should remain conceptually and, where practical, physically separable. A stale fact should normally trigger a focused reference refresh rather than an architecture rewrite.

## 7.6 Evidence / Provenance Intelligence

Preserves claim/source/target/version-SHA/environment/action/result/time/coverage/limitations and epistemic status.

Provenance is captured when evidence is produced/retrieved rather than reconstructed from model memory later.

## 7.7 Intent-to-Evidence Traceability

Maintains bidirectional links:

```text
user intent
<-> requirements/spec
<-> decisions/architecture
<-> plan
<-> implementation
<-> tests/evals
<-> observed/user-boundary evidence
```

For Self-Evolution, traceability additionally links:

```text
explicit self-evolution command
<-> observed limitation/gap
<-> research evidence
<-> proposed change
<-> eval case
<-> candidate mutation
<-> review
<-> promotion/rollback decision
```

Implementation reality may invalidate stale prior artifacts, but does not silently rewrite original intent.

---

# 8. Research Lab and epistemic states

Research modes:

- Survey
- Compare
- Investigate
- Experiment
- Replicate
- Evolve

Representative epistemic states:

- HYPOTHESIS
- SOURCE-SUPPORTED
- OBSERVED
- CHARACTERIZED
- REPRODUCED
- SUPPORTED / CONTRADICTED
- DECISION-ACCEPTED
- NORMATIVE
- IMPLEMENTED
- VALIDATED

Lifecycle:

```text
QUESTION
-> CONSTRAINTS + NON-GOALS
-> BASELINE
-> SOURCE LANDSCAPE
-> HYPOTHESES
-> ALTERNATIVES
-> EXPERIMENT DESIGN
-> BOUNDED EXPERIMENTS
-> EVIDENCE
-> ADVERSARIAL REVIEW
-> REPLICATION
-> COMPARISON
-> DECISION
-> SPEC / PROPOSAL
-> IMPLEMENTATION
-> VALIDATION
-> REGRESSION / REOPEN
```

Detailed durable research-artifact, provenance, independent-replication, Cusp Language Evolution, and optional role contracts remain normative supporting detail in `2026-09-04-research-experimental-engineering-design.md` unless superseded by this document or a later ADR.

---

# 9. Cross-runtime execution contract

CodeMaestro is capability-first and surface-aware.

```text
TASK REQUIREMENTS
∩ AVAILABLE CAPABILITIES
∩ AUTHORIZED CAPABILITIES
∩ SAFETY / RISK POLICY
=
EXECUTION CEILING
```

Representative runtime capabilities:

- repository read/write;
- filesystem read/write;
- shell;
- compiler/test runner;
- browser/web research;
- connected apps;
- database read/write;
- deployment;
- artifact generation;
- subagents;
- scheduled execution.

Chat is not advisory-only. Work is not automatically required for serious tasks. Codex is not defined by shell availability. A capability is used where it exists, is authorized, and methodology requires it.

Chat, Work, Codex, and future surface adapters may differ in mechanics, but not in the engineering methodology, evidence standard, quality contract, security model, or authority semantics applied to equivalent capabilities.

## 9.1 Runtime Capability Snapshot

For substantial/consequential tasks, CodeMaestro may maintain an internal snapshot/vector of the capabilities that matter to the task, for example:

```text
surface              chat
repo.read             yes
repo.write            yes
filesystem.read       yes
filesystem.write      yes
shell                 yes
compiler              yes
test_runner           yes
browser               yes
web_research          yes
apps                  yes
database.read         no
database.write        no
deployment            yes
artifact_generation   yes
subagents             no
```

The representation is implementation-specific; the distinction among capability existence, environment permission, task authorization, and safety eligibility is mandatory.

## 9.2 Graceful degradation and capability recovery

If a required capability is absent:

```text
requested workflow
-> identify gap
-> valid substitute if available
-> otherwise reduce execution depth
-> report exact limitation/evidence state
```

Examples of evidence statuses include:

- PROVIDED, NOT EXECUTED
- PARTIALLY VERIFIED
- VERIFIED
- BLOCKED

If a capability becomes available mid-task, CodeMaestro may increase execution depth without changing public mode. If a capability disappears or becomes unauthorized, it degrades truthfully and does not preserve a stronger success claim from an earlier state.

## 9.3 Cross-surface handoff

A durable handoff preserves at least:

- task/intent;
- target/version/SHA;
- accepted decisions;
- changes;
- evidence;
- unresolved questions;
- risks;
- next authorized action.

A Self-Evolution handoff additionally preserves the baseline CodeMaestro version/SHA, evolution/candidate identifier, eval/regression state, rollback target, and promotion status.

---

# 10. Authority and Task Capability Manifest

Routing/capability discovery never grants authority.

For consequential/high-autonomy tasks, CodeMaestro may derive a proportional Task Capability Manifest:

```text
- target
- available capabilities
- authorized capabilities
- read scope
- write scope
- consequential actions
- approval requirements
- forbidden actions
- validity/session
- fallback/degradation behavior
```

Effective authority is the intersection of host capability/permission, user/task authority, and safety/risk constraints.

A manifest may restrict authority. It cannot create authority.

---

# 11. Project Quality Contract

When material, CodeMaestro discovers/establishes the project's durable quality bar across dimensions such as:

- correctness;
- build/type/lint;
- testing/coverage;
- security;
- accessibility;
- performance budgets;
- architecture constraints;
- release gates.

A failing solution is repaired rather than made green by weakening the quality contract.

Changing the contract itself is distinct from satisfying it and requires appropriate authority.

For Self-Evolution, CodeMaestro's own eval/quality contract is protected by the same rule: an upgrade candidate may not lower thresholds, disable inconvenient evals, redefine success, or remove protected negative controls merely to appear improved.

---

# 12. Progressive disclosure and physical architecture

One public Skill does not mean one giant file.

## 12.1 Disclosure levels

**Level 0 — public metadata/identity**

Name, discovery metadata, branding where supported.

**Level 1 — compact core orchestrator**

Mission, invariants, routing/composition, capability discovery, authority/trust, evidence, quality contract, freshness gate, mutation/completion rules, cross-runtime contract, and Self-Evolution command gate.

**Level 2 — capability modules**

The canonical families defined in §6.

**Level 3 — deep references/techniques**

Focused domains such as auth/RLS, supply chain, accessibility, formal methods, design systems, telemetry, migrations, current standards, and technology-specific guidance.

Load the minimum sufficient context needed for the current stage; deep references are not loaded merely because they exist.

## 12.2 Methodology authority hierarchy

Reusable methodology obeys this direction of authority:

```text
USER / SYSTEM AUTHORITY
        ↓
CODEMAESTRO CORE
        ↓
CAPABILITY MODULE
        ↓
REFERENCE / TECHNIQUE
```

Lower layers may specialize or add evidence requirements but may not silently override root constitutional, authority, security, quality, or evidence rules. Global policy belongs at the root rather than being independently redefined in every module.

## 12.3 Conceptual Skill package

Final physical packaging must be reverified against the current Agent Skills/OpenAI format at implementation time.

```text
codemaestro/
├── SKILL.md                  # only public entrypoint
├── host/plugin metadata
├── assets/
├── router/
│   ├── capability registry
│   ├── routing/composition rules
│   └── self-evolution controller
├── capabilities/
├── intelligence/
├── references/
├── scripts/                  # deterministic helpers only
└── evals/
```

The exact directory/runtime-load boundary is implementation-time and eval-driven. The host/plugin shell is a distribution/branding surface, not a second public CodeMaestro Skill.

Third-party Skills/plugins remain untrusted supply-chain inputs until they pass the accepted provenance/license/injection/executable/dependency/filesystem/network/credential/permission/behavioral review gate defined in the context/repository/evidence hardening design.

---

# 13. Domain profiles instead of taxonomy expansion

Some important domains are compositions, not new canonical families.

```text
Developer Experience
= Product/UI + Contracts + Build/Environment + Platform/Delivery + Documentation

Monorepo Engineering
= Repository/Workspace Intelligence + Architecture + Build + Testing + Contracts

Supabase Engineering
= Database + Security + Migration + current authoritative research

Frontend Engineering
= Implementation + Product/UI + Performance + Accessibility

Compiler Engineering
= Language Intelligence + System Intelligence + Implementation + Assurance + Performance + Research/Experimental
```

Documentation/knowledge maintenance is an explicit cross-cutting workflow rather than a family. It includes human-facing documentation, agent-facing instructions, examples, ADRs, docs↔code drift, stale-version detection, and examples-as-tests where appropriate.

---

# 14. Pass 5 and Capability Freeze

Pass 5 is a durable research record at:

`../../research/2026-09-04-comparative-research-pass-5.md`

Acceptance/Capability Freeze is recorded at:

`../../architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md`

Pass 5 accepted the architectural directions and **opened** these tracks; it did not mark their research execution complete:

- CM-R-029 — Cross-Runtime Portability, Capability Discovery & Conformance — `IN RESEARCH`, `DIRECTION ACCEPTED`
- CM-R-030 — Product, UX/UI & Visual Interface Engineering — `IN RESEARCH`, `DIRECTION ACCEPTED`
- CM-R-031 — Build, Toolchain & Environment Engineering — `IN RESEARCH`, `DIRECTION ACCEPTED`
- CM-R-032 — Privacy & Data Lifecycle Engineering — `IN RESEARCH`, `DIRECTION ACCEPTED`

No CM-R-033 is opened by Pass 5.

Capability Freeze means:

> Do not add a new top-level capability family because another domain name exists. Reopen breadth only when a real task/eval demonstrates a distinct responsibility that existing capabilities/shared intelligence cannot express cleanly.

Freeze is coverage-bounded and eval-reopenable, not a claim of universal permanent completeness.

---

# 15. Evaluation model

CodeMaestro is evaluated by correct behavior and evidence, not the amount of prose it contains.

Required dimensions:

1. Routing
2. Capability effectiveness
3. Composition
4. Cross-runtime conformance
5. Capability degradation
6. Safety / Authority
7. Evidence quality
8. User/operational outcome
9. Self-Evolution integrity
10. **Logging integrity** — repository session/project history and Self-Evolution audit records preserve required schema, event-time updates, correction/supersession semantics, redaction/privacy boundaries, continuity/handoff evidence, and ownership separation.

Agent eval contracts distinguish:

- task contract;
- trajectory contract;
- side-effect contract;
- evidence contract.

A correct final output may still fail the trajectory or side-effect contract.

## 15.1 RED evals first

Before major production guidance is authored, create baseline cases that expose the weakness the guidance is intended to correct.

```text
CURRENT FAILURE / LIMITATION
-> encode as eval
-> reproduce baseline weakness
-> smallest justified change
-> rerun target eval
-> regression suites
```

## 15.2 Initial eval layout

```text
evals/
├── routing/
├── capabilities/
├── composition/
├── cross-runtime/
├── degradation/
├── evidence/
├── authority/
├── quality-contract/
├── logging/
├── self-evolution/
├── adversarial/
├── regression/
└── end-to-end/
```

Representative scenarios include:

- concurrency debugging;
- framework/runtime migration;
- auth bypass candidates;
- user-facing UI redesign → implementation → visual/interaction QA;
- transaction/data-integrity bugs;
- local-pass/CI-fail environment drift;
- untrusted prompt/tool misuse;
- experimental-language conflicting authorities;
- privacy/data-retention propagation;
- cross-runtime equivalent-capability conformance;
- no-change self-audit;
- a Self-Evolution candidate that improves the target eval while preserving core regression/authority/evidence/quality suites;
- adversarial self-upgrade attempts to lower the quality bar or broaden authority;
- session handoff where transcript/project logs preserve enough state to resume without relying on model memory;
- correction of a false prior log entry by appending `CORRECTION / SUPERSEDES` rather than rewriting history;
- secret or sensitive material appearing in visible content and being omitted/redacted from durable public history using the canonical marker;
- a Self-Evolution run that does not read conversations when they add no evidentiary value, and one that records the reason/scope when it does consult them.

## 15.3 Router and composition health

Routing evals should track, where meaningful:

- routing precision;
- routing recall;
- unnecessary capability activation;
- missed supporting capability;
- clarification frequency;
- wrong escalation/de-escalation.

Composition evals should examine:

- workflow completeness;
- contradictions;
- ordering effects;
- duplicated methodology;
- unnecessary context load;
- handoff/evidence loss.

Metrics are calibrated against representative baselines rather than arbitrary green numbers.

## 15.4 Project Quality Contract evals

Explicitly test that CodeMaestro does not silence or remove failing tests, lower coverage, weaken lint/types/security/accessibility, alter release thresholds, or redefine the quality contract merely to make its solution pass. The same protection applies to Self-Evolution.

## 15.5 Cross-runtime conformance contract

Cross-runtime evals compare outcome semantics, not exact tool traces. Compare at least:

- intent interpretation;
- authority/safety boundary;
- scope discipline;
- root-cause/engineering decision;
- validation standard;
- evidence semantics;
- completion meaning;
- graceful degradation/recovery;
- logging/continuity semantics when repository work-session governance applies;
- Self-Evolution command/promotion semantics when target is `SELF`.

## 15.6 Fresh-context review

For high-impact architecture, security, research, evidence-sensitive work, and Self-Evolution, use independent/fresh-context review when the runtime supports it and the expected value exceeds the overhead. Fresh review is supporting evidence, not hidden authority.

---

# 16. Command-Gated Self-Evolution

Self-Evolution is a **governance controller**, not an 18th capability family and not a second public Skill.

Target:

```text
SELF
```

It composes existing capabilities/intelligence as needed, especially Research, Repository/Workspace, System, Evidence, Testing/Assurance, Review/Audit, Security, and Build/Environment.

## 16.1 Command levels

### Self-research / self-audit

Read-only by default:

```text
inspect current CodeMaestro
-> authoritative current research
-> gap/opportunity analysis
-> report
```

### Design a self-upgrade

```text
research
-> self-audit
-> proposal
-> impact/risk class
-> proposed evals
-> upgrade design
```

No stable mutation by default.

### Prepare/perform a self-upgrade candidate

```text
BASELINE SNAPSHOT
-> SELF-COMPREHENSION
-> CURRENT RESEARCH
-> GAP / FAILURE
-> UPGRADE HYPOTHESIS
-> IMPACT CLASS
-> RED EVAL
-> ISOLATED CHANGE
-> TARGET + REGRESSION EVALS
-> ADVERSARIAL / FRESH-CONTEXT REVIEW
-> VERIFIED CANDIDATE
-> PROMOTION GATE
```

The command authorizes only the workflow inside actual host/user/task authority. It does not by itself authorize merge, publish, quality-bar changes, permission expansion, or constitutional-policy changes.

### Stable promotion

Promotion/merge/publish is a separate consequential stage governed by actual repository/runtime authority.

## 16.2 Self-model before self-change

CodeMaestro applies Repository/System Intelligence to itself before modification:

- public contract;
- architecture;
- router/composer;
- capability registry;
- Shared Intelligence;
- references;
- evals;
- packaging;
- quality contract;
- protected invariants;
- dependency/blast radius.

Conversation transcripts are not mandatory self-model input.

## 16.3 Upgrade impact classes

- **SELF-U1** — knowledge refresh
- **SELF-U2** — methodology/reference refinement
- **SELF-U3** — capability behavior/eval change
- **SELF-U4** — core router/evidence/authority-adjacent change
- **SELF-U5** — constitutional architecture change

SELF-U5 requires explicit human approval after research/design/eval evidence and cannot be self-authorized.

## 16.4 Protected constitutional layer

Self-Evolution may not silently change:

- public entrypoint policy;
- evidence-before-assertion;
- state-before-mutation;
- validation-before-success;
- no-invented-execution;
- authorization boundaries;
- untrusted-content model;
- Project Quality Contract protection;
- human authority;
- command-gated Self-Evolution;
- promotion/rollback discipline;
- append-only Self-Evolution audit history;
- the rule that conversation transcripts are optional evidence rather than mandatory Self-Evolution context.

## 16.5 Research priority for Self-Evolution

Default evidence priority:

```text
1 current executable/repository state
2 canonical architecture/ADRs/specs/protected invariants
3 current eval evidence
4 relevant repository project-event history, if available
5 relevant previous Self-Evolution records
6 current authoritative external research
7 conversation transcripts only when a specific evidentiary need justifies them
```

Conversations are optional evidence. If consulted, the Self-Evolution record states why, what scope was read, and what evidentiary result was obtained.

## 16.6 RED, non-regression, and adversarial review

A material self-change should be tied to a demonstrated weakness whenever practical:

```text
OBSERVED LIMITATION
-> exact claim
-> baseline reproduction/eval
-> candidate change
-> same target eval after change
```

A target improvement is insufficient if unrelated behavior regresses, authority expands, evidence/quality gates weaken, routing becomes noisier, or the candidate games its own evals.

Depending on impact class, validation may require:

```text
target eval
+ core regression suite
+ routing suite
+ composition suite
+ authority/safety suite
+ evidence suite
+ cross-runtime suite
+ quality-contract suite
+ Self-Evolution logging-integrity checks
```

SELF-U3 and above should use fresh-context/adversarial review where available and proportionate.

## 16.7 Isolated candidate and before/after evidence contract

Consequential Self-Evolution occurs in an isolated branch/workspace or equivalent candidate target with a known previous-good rollback baseline. Conceptual branch naming may use:

```text
self-evolution/<date>-<goal>
```

Every material upgrade candidate preserves:

```text
BEFORE
- CodeMaestro version/SHA
- target limitation/eval
- relevant baseline results

CHANGE
- triggering user instruction
- research basis
- rationale
- impact class
- affected modules/files

AFTER
- target eval result
- regression results
- new limitations
- evidence coverage
- reviewer verdict
- rollback target
```

An upgrade claim reflects this evidence, not the existence of a diff.

## 16.8 Dedicated Self-Evolution ledger

When available and authorized, each run uses a dedicated record such as:

```text
logs/logs/self-evolution/YYYY/YYYY-MM-DD_<evolution-id>.log
```

The canonical record should preserve, when applicable:

```text
evolution id
started timestamp
mode: SELF-RESEARCH / SELF-AUDIT / SELF-UPGRADE
triggering user instruction
objective
baseline version/SHA
research snapshot / sources
observed gap/failure
hypotheses/refutations
proposal
impact class
RED eval
candidate changes/state
regression evidence
conversations consulted + justification, if any
independent review
approval/promotion state
resulting version/SHA
rollback target
```

A research/audit run that makes no change still receives a Self-Evolution record; it does not fabricate a project-mutation event.

## 16.9 Fail-closed conditions

Self-Evolution must not silently downgrade into direct stable mutation when a required safety/evidence precondition fails. Examples include:

- invalid or unknown baseline;
- inability to isolate the candidate change;
- unavailable/corrupted required Self-Evolution audit record;
- unavailable critical target/regression evals for the impact class;
- missing required approval for promotion;
- inability to identify a practical rollback point for a consequential change.

The workflow may degrade to research/design/reporting if safe, but must report the limitation truthfully.

## 16.10 Rollback

Every promoted material self-upgrade has a known previous-good state and a practical rollback strategy proportional to impact. A regression discovered after promotion may trigger rollback and a new regression eval rather than uncontrolled forward-fixing.

Rollback is itself evidence/state and is appended to the relevant Self-Evolution record and, when repository state changes, the project-event stream.

## 16.11 Stopping rule

A valid outcome is:

```text
SELF-AUDIT COMPLETE
NO MATERIAL UPGRADE JUSTIFIED
```

The command to improve does not obligate CodeMaestro to manufacture change.

## 16.12 Controlled evolution lifecycle

For material CodeMaestro changes generally:

```text
OBSERVED FAILURE / JUSTIFIED GAP
-> PROPOSED CHANGE
-> RATIONALE
-> EVAL CASE
-> IMPLEMENT IN ISOLATION
-> REGRESSION SUITE
-> INDEPENDENT REVIEW
-> HUMAN / PROJECT AUTHORIZATION AS REQUIRED
-> PROMOTE
```

Architecture/constitutional changes carry a higher burden of proof than reference refreshes.

Outside an explicit Self-Evolution run, impact is still classified proportionally:

- **Low** — reference freshness, typo/citation correction;
- **Medium** — workflow refinement, capability/reference behavior;
- **High** — canonical capability family, router semantics, authority/evidence model, public Skill split, cross-runtime policy, Self-Evolution governance, or durable logging authority/integrity semantics.

High-impact changes require explicit research/design/eval/approval. Real material failures should become minimized regression evals when practical.

---

# 17. Logging ownership — two separate contracts

The logging design has **two different policy owners** and must not be conflated.

## 17.1 Repository Work-Session Logging — NOT portable Skill behavior

This exists for the user's Chat / Work / Codex sessions that **develop or maintain the CodeMaestro repository**.

It is project-development governance, not a generic behavior imposed by an installed `@codemaestro` on unrelated projects.

The user-selected repository layout intentionally uses a root `logs/` folder with two child folders named `conversations/` and `logs/`:

```text
Code-Maestro/
└── logs/
    ├── conversations/          # project-working chat session history
    └── logs/
        ├── project/            # project mutation/state-event history
        └── self-evolution/     # reserved for Skill Self-Evolution audit
```

The repeated `logs/logs/` path is **intentional, not a typo**: the outer `logs/` is the repository audit root chosen by the project owner; its `logs/` child is the event-log stream beside `conversations/`.

### Conversations

`logs/conversations/` preserves user-visible project-working dialogue and relevant observable action summaries for continuity. It never stores hidden chain-of-thought.

### Canonical session header

Each new project-working transcript begins with an immutable historical header equivalent to:

```text
# CodeMaestro Conversation Transcript

Session started: 2026-09-04 11:32:00 +03:00
Surface: Chat
Repository: heraklist/Code-Maestro
Initial branch: docs/architecture-foundation-v0.1
Initial SHA: <sha>
Purpose: <session purpose>
Transcript policy: semantic append-only / public-safe
```

If branch/SHA/scope later changes, the original header is not rewritten; append a timestamped `STATE CHANGE` record.

### Project events

`logs/logs/project/` records what actually changed in the CodeMaestro project: files, branches, commits, PRs, approvals, eval state, corrections, rollbacks, and other material state transitions.

A material project-event record uses these canonical fields when applicable:

```text
TIMESTAMP
SESSION
EVENT / TYPE
TARGET
ACTION
REASON
BEFORE
AFTER
EVIDENCE
AUTHORITY
RESULT
RELATED COMMIT / ARTIFACT
```

Fields may be omitted when genuinely not applicable, but the record must remain unambiguous and reconstructable.

### Timestamp convention

Prefer offset-aware timestamps:

```text
YYYY-MM-DD HH:mm:ss ±HH:MM
```

for example:

```text
2026-09-04 11:43:17 +03:00
```

UTC/ISO-8601 may additionally be stored for cross-runtime correlation.

### Real-time/event-time session admission rule

The repository work-session protocol must require updates **as work happens**, not reconstructed only at the end:

```text
SESSION START
-> locate/read repository work-session protocol
-> initialize/resume session transcript
-> identify relevant recent project-event state using progressive disclosure
-> capture repo/branch/SHA
-> only then begin material project work
-> append conversation history as it progresses
-> append material project event when it occurs
-> append corrections/supersessions rather than rewrite
-> checkpoint before handoff/end
```

History loading is also progressively disclosed: a session reads only the recent/relevant transcript/event material needed for continuity rather than ingesting the entire historical corpus by default.

### Correction / supersession format

Semantic append-only means a historical entry is not silently edited to make the record cleaner. A correction is appended, for example:

```text
CORRECTION / SUPERSEDES EVENT <event-id>
Previous statement: <bounded description>
Corrected state: <new state>
Evidence: <source/commit/result>
```

The old entry remains part of ordinary audit history, except where the privacy/security deletion exception below requires authorized sanitation.

### Conversation-to-event traceability

When material, conversation and project-event records cross-reference the decision/change they represent:

```text
CONVERSATION
<-> DECISION / AUTHORITY
<-> PROJECT EVENT
<-> COMMIT / ARTIFACT / EVIDENCE
```

The link improves reconstruction/provenance but does not make historical conversation text normative authority.

### Log-write failure behavior

If a required repository session/project log write fails, the session must report:

```text
LOG WRITE FAILED
```

For consequential work, further consequential mutation pauses until the audit/continuity write is restored or the user explicitly authorizes a safe alternative. Low-risk analysis may continue only with an explicit continuity limitation and without claiming repository logging succeeded.

### Checkpoint / handoff minimum

Before session end or cross-surface handoff, append a checkpoint containing when material:

- current branch/SHA;
- last completed action;
- decisions/approvals;
- mutations;
- evidence/validation state;
- unresolved issues/risks;
- next expected or authorized action.

## 17.2 Self-Evolution Audit — Skill behavior

Only `logs/logs/self-evolution/` belongs to the CodeMaestro Skill's Self-Evolution contract.

When explicitly running Self-Evolution and repository logging is available/authorized, CodeMaestro opens/resumes the dedicated Self-Evolution record defined in §16.8 **before substantive self-research/evolution work** and appends material evidence/events as they occur.

If Self-Evolution causes a real repository mutation:

- the Self-Evolution stream records **why/how** the change was researched/evaluated;
- the project stream records **what actually changed**;
- the two cross-reference by evolution ID/commit/artifact.

A no-change self-audit has a Self-Evolution record but no fabricated project-mutation event.

A required Self-Evolution audit-write failure is a fail-closed condition for consequential self-mutation as specified in §16.9.

## 17.3 Semantic append-only, not cryptographic immutability

Under ordinary operation, history is semantically append-only: old entries are not silently rewritten; corrections/refutations/rollbacks are appended as new events.

Git commit history provides version linkage, but this design does **not** claim cryptographic immutability or protection against repository-history rewriting. If future promotion gates depend on stronger tamper evidence, hash chaining/signed attestations may be evaluated under the evidence/supply-chain model rather than assumed.

## 17.4 Public-repository privacy boundary

`heraklist/Code-Maestro` is public. Therefore “complete transcript” is subordinate to Privacy & Data Lifecycle Engineering and public-repository hygiene.

Committed conversation records must be **public-safe**:

- secrets/credentials/private keys/tokens are never committed;
- non-public personal, confidential, or sensitive data is redacted/omitted from the public record;
- where preserving a raw transcript is necessary, it must live in an authorized private/local store, while the public repository may retain a sanitized transcript or digest/reference;
- redactions are explicit so the public record does not falsely claim verbatim completeness.

Canonical redaction marker for a secret that must not be persisted:

```text
[REDACTED SECRET — not persisted]
```

Equivalent typed redaction markers may be used for non-secret sensitive/private information, but must not themselves reveal the removed payload.

The ordinary append-only rule does not override a legitimate privacy/security/legal deletion requirement. If data must be purged, the project follows an authorized sanitation/history-rewrite process as required and records a non-sensitive purge event without retaining the removed payload.

Retention/deletion policy for these development records is **not yet resolved**. CM-R-032 is `IN RESEARCH`; this policy must be researched, decided, and recorded before Milestone 0 logging is declared operational.

## 17.5 Logs are evidence, not authority

Conversation/project/Self-Evolution logs do not override current user/system authority, executable state, normative specs, accepted ADRs, or more current verified evidence.

---

# 18. Visual identity

Approved direction: **Maestro Monogram**.

The primary mark is a custom geometric `CM` that communicates orchestration/engineering precision without relying on generic developer/AI clichés such as a bare `</>`, robot head, terminal cursor, or sparkle/“AI magic” motif.

Desired qualities:

- precise;
- technical;
- minimal;
- premium;
- confident;
- not playful;
- not cyberpunk;
- not “AI magic”.

Initial palette direction:

- deep graphite / near black;
- off-white/light neutral mark;
- controlled cobalt/electric-blue accent;
- avoid uncontrolled neon-gradient treatment.

## 18.1 Icon-first behavior

The mark must remain recognizable without adjacent text at small composer/Skill-list sizes.

Target behavior:

```text
16–20 px  -> recognizable silhouette
32–64 px  -> clear CodeMaestro mark
256+ px   -> complete logo/detail
```

## 18.2 Expected asset family

Expected final assets may include:

```text
assets/
├── codemaestro-composer.svg
├── codemaestro-logo.svg
├── codemaestro-logo-dark.svg
├── codemaestro-logo-light.svg
├── codemaestro-mark.svg
└── codemaestro-preview.png
```

Exact manifest fields and supported asset hooks are reverified against current OpenAI/Agent Skills/plugin packaging before integration.

## 18.3 Visual selection gate

Before final packaging, create **three Maestro Monogram variants**, compare them at small composer scale and larger identity scale, and select one final mark before integration. Branding/plugin metadata is a distribution shell around the one public Skill, not another CodeMaestro Skill.

---

# 19. Stabilization and controlled evolution

After the first implementation, optimize depth/coherence before adding breadth.

Look for:

- overlapping capability boundaries;
- routing errors/overactivation;
- duplicated or contradictory policy;
- evidence loss;
- surface drift;
- context bloat;
- architecture/code drift;
- capability discovery/loading failure;
- missing/duplicated/corrupted logging or logging that overwhelms useful context;
- self-evolution loops or upgrade churn.

Conceptual stabilization ladder:

```text
S0 structural health
S1 routing baseline
S2 capability baseline
S3 composition
S4 cross-runtime + continuity/logging
S5 adversarial/security/self-evolution
S6 real-project trials
S7 release baseline
```

Skill discovery/loading should be fault-isolated; one broken optional reference/third-party Skill must not silently corrupt unrelated workflows.

The Self-Evolution Controller fails closed rather than mutating the stable baseline when required audit, baseline, isolation, eval, approval, or rollback conditions cannot be satisfied.

Material failures should become minimized regression evals where practical.

---

# 20. Production-readiness definition

A production-quality first Skill is not established by the existence of `SKILL.md`.

At minimum:

- one public `@codemaestro` works as intended;
- routing/capability/composition evals pass;
- cross-runtime conformance is demonstrated;
- graceful degradation/recovery is demonstrated;
- authority/security/evidence contracts hold;
- Project Quality Contract protection is demonstrated;
- no major capability-overlap ambiguity remains;
- packaging/branding is validated against the current host format;
- representative real-project trials complete;
- user/business-boundary verification exists where relevant;
- Command-Gated Self-Evolution is validated before being considered production-ready;
- Self-Evolution cannot expand authority or silently promote itself;
- before/after/regression/rollback evidence contracts for Self-Evolution are validated;
- dedicated Self-Evolution audit behavior is validated when that controller is implemented.

Repository work-session conversation/project logging is a development-governance prerequisite for this repository; it is **not** a portable production-readiness requirement of the CodeMaestro Skill in unrelated projects.

---

# 21. Sequence after written-spec approval

This section is authoritative for post-review ordering.

Superpowers process requires an implementation plan before implementation:

```text
WRITTEN SPEC APPROVED
-> implementation plan
-> implementation plan MUST make Milestone 0 the first implementation milestone
```

## Milestone 0 — Repository Work-Session Logging Foundation

**Before any other implementation work:**

```text
1. create documentation-consistency checker FIRST
   - ADR ID uniqueness with status/authority awareness
   - every referenced CM-R has backlog entry and record where required
   - backlog Status equals record Status
   - internal repository links resolve
2. run checker against current branch and repair any detected drift
3. create logs/conversations/
4. create logs/logs/project/
5. create canonical transcript/project-event schemas/templates from §17
6. create canonical real-time project-working-chat instruction
7. resolve CM-R-032 retention/deletion/public-sanitization policy required for these records
8. verify append/correction/redaction/cross-reference/log-write-failure/checkpoint/handoff workflow
```

The consistency checker must understand historical/superseded/absorbed ADR occurrences: for example, CM-ADR-019…022 may legally appear in `DECISIONS-2026-09-04-PASS3.md` when that file marks them `ABSORBED INTO DECISIONS.md`. The checker rejects multiple **active/canonical** definitions, not every repeated token.

`logs/logs/self-evolution/` may be reserved structurally, but the **Skill-owned Self-Evolution logging behavior is implemented later with the Self-Evolution Controller**, not conflated with Milestone 0 project-chat governance.

Milestone 0 is not operational until its consistency checks pass and the CM-R-032 logging retention/deletion/public-sanitization decision exists.

## Only after Milestone 0 is operational

Proceed with:

```text
canonical architecture/documentation integration
-> capability contracts + Capability Registry
-> RED eval implementation including routing/composition metrics
-> final physical Skill packaging
-> compact orchestrator
-> progressive capability/intelligence modules
-> Self-Evolution Controller + dedicated Self-Evolution audit behavior
-> cross-runtime validation
-> stabilization
```

---

# 22. Out of scope before implementation planning

Before implementation begins, do not:

- create production `SKILL.md`;
- implement capability modules/references;
- implement the Self-Evolution Controller;
- perform an actual Self-Evolution upgrade;
- publish/install the final plugin/Skill;
- merge the architecture PR.

The documentation repairs required to close written-spec/regression review are part of the design-review process and do not count as production implementation.
