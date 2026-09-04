# Comparative Research Pass 4 — Contracts, Operational Assurance, Performance, and Evidence Boundaries

**Date:** 2026-09-04
**Status:** REVIEW — research findings recorded; architectural adoption requires explicit approval.

## Objective

Run a fourth, deliberately selective comparative pass over current Skill and agent repositories, looking only for mechanisms that materially extend CodeMaestro beyond the already accepted architecture.

This pass rejects duplication by default. Generic expert personas, technology-specific checklists, arbitrary static thresholds, and workflows already covered by Language Intelligence, Research Lab, Repository/Context Intelligence, Traceability, Assurance, Refutation, Migration, or Orchestration are not treated as new capabilities merely because they appear in another repository.

## Source set sampled

High-signal sources included:

- `magnus919/agent-skills`
  - API design and evolution
  - contract verification
  - verification methodology
  - release engineering
  - site reliability engineering
  - agent evals and observability
- `trailofbits/skills`
  - supply-chain risk auditor
  - sharp-edges / misuse-resistance analysis
  - agentic GitHub Actions auditor
- `vaquarkhan/data-engineering-agent-skills`
  - data quality and contract testing
  - reconciliation and financial controls
  - incident triage and recovery
  - resiliency testing and failure injection
  - schema evolution and contract migrations
  - safe replay/backfill orchestration
  - observability/SLA management
- `microsoft/amplifier-bundle-systems-design`
  - architecture primitives
  - distributed systems
  - web-service/system scaling patterns
- `google/skills`
  - Well-Architected performance optimization
- `Jeffallan/claude-skills`
  - spec mining / legacy reverse specification
- `openai/codex`
  - current Skill loading and invocation mechanics
- marketplace/community catalogs were used only for discovery and were not treated as correctness authorities.

---

## High-signal finding 1 — Reconciliation is an assurance technique, not merely a data-engineering task

For high-trust systems, a passing test suite or successful job does not prove that real operational or business quantities remain correct.

Reconciliation-oriented workflows introduce a separate evidence class:

```text
control objective
→ source / target or before / after populations
→ acceptable variance
→ timing / cutoff semantics
→ reconciliation rule
→ exception ownership
→ retained evidence
```

Examples include:

- row-count/volume parity;
- control totals;
- aggregate balance checks;
- record-level matching;
- business-key duplicate checks;
- referential-integrity controls;
- freshness/completeness controls;
- source-to-target metric reconciliation.

The important distinction is:

```text
code executed successfully
≠ transformation is correct
≠ business state reconciles
```

### Recommendation

Do **not** create a standalone Reconciliation Skill at this stage.

Extend **CM-R-006 — Modern Testing Strategy / Assurance Ladder** and **CM-R-020 — Evidence & Provenance** with a class of **control/reconciliation evidence** for domains where correctness is defined by conserved totals, balances, expected populations, or source-to-target invariants.

Also connect this evidence to CM-R-026 migration/cutover verification.

---

## High-signal finding 2 — Operational closure must be proved at the user/business boundary

Several SRE/recovery systems distinguish internal signal recovery from actual service recovery.

A cleared alert, green health endpoint, successful deployment, or completed rerun is evidence — not sufficient closure.

A stronger operational closure sequence is:

```text
bound recovery action
→ execute within blast-radius limit
→ verify critical user journey / business outcome
→ verify data/state correctness
→ verify dependency health
→ observe stability window / backlog recovery / secondary effects
→ only then close
```

The active state should remain `MITIGATING`, `MONITORING`, or equivalent when required user-boundary evidence is absent.

### Recommendation

Extend:

- **CM-R-009 — Observability and SRE readiness**
- **CM-R-015 — Release and production readiness**
- **CM-R-020 — Evidence/provenance**

with an explicit **operational closure gate**.

No new research track is required.

---

## High-signal finding 3 — Every valuable incident should be eligible to become a resilience regression

Production incidents expose failure modes that ordinary happy-path testing misses.

A strong lifecycle is:

```text
incident
→ containment
→ live-state observation
→ impact classification
→ safe recovery
→ validated closure
→ root cause / contributing conditions
→ guardrail
→ bounded failure-injection or resilience regression
```

Failure drills should define:

- the exact failure mode;
- safe environment and blast radius;
- acceptable data loss / availability behavior;
- recovery-time and backlog expectations;
- replay/idempotency guarantees;
- publish/quarantine behavior;
- alert/escalation expectation;
- recovery evidence.

Random breakage is not resilience testing. The drill must be controlled and falsifiable.

### Recommendation

Extend **CM-R-006**, **CM-R-009**, **CM-R-013**, and **CM-R-015** with **incident-to-resilience-case learning**.

No separate Chaos/Resilience Skill decision is justified yet.

---

## High-signal finding 4 — Evidence needs target/source fidelity, not only source authority

Existing CodeMaestro research already ranks evidence by authority. This pass reveals an independent property: **identity fidelity**.

If a claim concerns a particular repository, deployment, tenant, service, branch, database, compiler, contract version, or configured local system, evidence about an adjacent public project or a similar environment is not interchangeable.

Example:

```text
claim: production deployment X currently behaves Y

strong official docs about product X
≠ evidence that deployment X currently behaves Y
```

Rules:

1. Use the exact target/source when accessible.
2. Record failure if the exact source cannot be queried.
3. Substitute evidence only as explicitly secondary/contextual evidence.
4. Never silently upgrade secondary evidence into current-target state.

### Recommendation

Extend **CM-R-020** and **CM-R-025** with a **source/target fidelity field** in the evidence model.

Potential future invariant:

> Verification conclusions must be both authoritative enough for the claim and faithful to the identity/state the claim is about.

No new research track is required.

---

## High-signal finding 5 — Clean conclusions require an explicit evidence-coverage denominator

Supply-chain and audit systems repeatedly expose a subtle failure mode:

```text
no findings returned
→ falsely reported as
system is clean
```

A trustworthy negative finding must state the assessed surface.

Useful evidence states include:

- assessed-clean;
- assessed-flagged;
- unassessable-with-reason;
- not assessed;
- incomplete/partial coverage.

Principles:

- unavailable data is not evidence of risk;
- unavailable data is also not evidence of safety;
- absence from findings is not endorsement;
- “none found” is meaningful only relative to what was actually measured;
- coverage limitations are part of the result, not report footnotes to omit.

### Recommendation

Extend **CM-R-020** with **coverage-bounded evidence**.

Candidate evidence metadata:

```text
claim
source identity
source state/version
assessed surface / denominator
assessed subset
unassessed or unassessable subset
measurement method
result
uncertainty / limitations
```

This should also inform audits, security reviews, repository comprehension, test coverage claims, migration validation, and research synthesis.

---

## High-signal finding 6 — Legacy systems need recovered specifications with a weaker authority status

Repository Comprehension explains what a system contains and how it behaves. Spec-to-Code Compliance checks implementation against an existing authoritative specification.

A third case exists:

> the implementation survives, but original requirements/specification have been lost or are incomplete.

A useful reverse-engineering workflow is:

```text
scope
→ inspect implementation and observable behavior
→ trace flows and boundaries
→ recover behavior statements / inferred requirements
→ bind each statement to code/runtime evidence
→ record uncertainty and gaps
```

The critical epistemic rule is:

```text
recovered behavior
≠ original intent
≠ normative specification
```

A recovered specification describes what the current implementation appears to require or do. It cannot silently become the authority that justifies itself.

### Recommendation

Extend:

- **CM-R-022 — Repository Comprehension**
- **CM-R-025 — Intent-to-Evidence Traceability**

with a **Recovered Specification** state/category.

Candidate label:

- `RECOVERED / OBSERVED SPECIFICATION`

A later explicit project decision may promote recovered behavior into normative intent, but that promotion must be visible and authorized.

No separate Reverse Engineering Skill decision is justified yet.

---

## High-signal finding 7 — Interface, protocol, and contract engineering is a distinct cross-cutting domain

This pass found a gap not fully covered by general architecture or migration methodology.

Consumer-facing and system-to-system interfaces are durable behavioral agreements. Their correctness depends on semantics beyond route/schema shape.

Relevant interface families include:

- REST/HTTP;
- GraphQL;
- RPC/gRPC;
- events/messages;
- webhooks;
- streams;
- data schemas/contracts;
- protocol boundaries.

Important contract dimensions include:

- consumer job and domain meaning;
- source/authority ownership;
- null vs absent semantics;
- defaults;
- identifiers and units;
- ordering;
- pagination/filtering;
- authorization expectations;
- preconditions;
- idempotency scope and equivalence;
- retries and deadlines;
- concurrency behavior;
- partial outcomes;
- error semantics;
- quotas/resource limits;
- duplicate/gap/reordering behavior;
- compatibility/deprecation policy.

A key finding is that compatibility is **consumer-relative**. An additive schema/API change is not automatically safe when consumers use strict decoders, generated clients, signatures, caches, quotas, or assumptions not visible in the provider schema.

### Multi-boundary contract verification

Contract readiness should distinguish:

1. **Contract boundary** — schema/reference/examples/negative examples/semantics.
2. **Provider boundary** — implementation conformance, errors, authorization, limits, concurrency, side effects.
3. **Consumer boundary** — actual consumer expectations and client behavior.
4. **Compatibility boundary** — change diff under consumer-specific assumptions.
5. **Deployed boundary** — end-to-end behavior at the intended environment plus telemetry/rollback evidence.

A mock, generated document, or schema linter does not prove deployed integration.

### Recommendation

Propose a new research track:

## CM-R-027 — Interface, Protocol & Contract Engineering

**Proposed priority:** P1

Research should produce:

- interface/contract design methodology;
- semantic contract template;
- provider/consumer ownership model;
- sync/async delivery semantics;
- error/idempotency/retry/concurrency contract model;
- consumer-aware compatibility assessment;
- multi-boundary verification strategy;
- deprecation/evolution integration with CM-R-026;
- security/misuse-resistance integration;
- protocol/API eval scenarios.

This does **not** pre-decide a physical standalone Skill.

---

## High-signal finding 8 — Secure interface design includes misuse resistance, not only implementation security

Traditional review often asks whether the implementation has a vulnerability.

A separate question is whether the API/configuration makes unsafe use easy.

Misuse-resistance review looks for:

- dangerous defaults;
- zero/empty/null magic values;
- algorithm/mode selection footguns;
- type-confusable primitives;
- stringly typed security choices;
- configuration cliffs;
- silent security failures;
- error handling that encourages insecure use;
- high-level secure paths that are harder than unsafe low-level paths.

“Documented correctly” is not sufficient if normal developer usage remains easy to misuse.

### Recommendation

Extend:

- **CM-R-002 — Secure software development**
- **CM-R-003 — Application/LLM/agent security**
- proposed **CM-R-027 — Interface/Contract Engineering**

with **misuse-resistance / pit-of-success analysis**.

No separate Skill or research track is required.

---

## High-signal finding 9 — Agentic CI/security review needs end-to-end untrusted-input dataflow

Static agentic CI auditing shows that prompt injection and unsafe execution are not limited to visibly interpolated prompt strings.

Relevant sources of untrusted input include:

- issue/PR bodies and titles;
- comments;
- branch/file content;
- workflow inputs;
- build/test/error logs;
- environment-variable intermediaries;
- CLI-fetched remote content;
- outputs of earlier AI/model steps.

The critical path is:

```text
untrusted input
→ prompt/context/tool instruction
→ agent capability
→ tool/shell/network/repository action
→ side effect / exfiltration / authority use
```

Tool allowlists and sandboxes reduce attack surface but are not proof when allowed tools can indirectly execute, expand shells, access credentials, or reach dangerous side effects.

### Recommendation

Extend:

- **CM-R-003**
- **CM-R-004 — CI/CD security**
- **CM-R-008 — MCP/tool authorization**
- **CM-R-023 — Skill/Plugin Supply Chain**

with an explicit **agentic taint/dataflow model**.

No new track is required.

---

## High-signal finding 10 — Agent evaluation needs task contracts and trajectory contracts

Agent output quality alone is insufficient when tools, side effects, intermediate state, recovery, and authorization matter.

Evaluation should distinguish:

- **task contract** — what outcome is required;
- **trajectory contract** — what paths/actions are allowed, required, or forbidden;
- **side-effect contract** — what state changes may occur;
- **evidence contract** — what proves the outcome.

Strong eval methodology also requires:

- immutable/versioned datasets;
- dataset provenance and changelog;
- rights/consent and retention where production data is used;
- contamination awareness;
- explicit slices;
- comparable baseline/candidate conditions;
- stochastic repeats where variability matters;
- preserved failures/timeouts rather than survivorship filtering;
- multidimensional profiles rather than one scalar score;
- hard safety/privacy/authorization invariants that cannot be averaged away by better quality scores;
- verified incidents/near misses promoted into regression cases after review.

### Recommendation

Deepen **CM-R-012 — Skill/Agent Evaluation Methodology** and **CM-R-020**.

No new track is required.

---

## High-signal finding 11 — Distributed-system references should be invariant-driven

The distributed-systems corpus reinforces a useful form for CodeMaestro domain references.

Rather than encyclopedic descriptions of technologies, high-value guidance should ask:

- what consistency is actually required per data class;
- who owns and enforces each invariant;
- where final/durable effects occur;
- whether every retryable operation is safely repeatable;
- who owns retries and deadlines;
- whether backlogs/queues are bounded;
- how derived state is reconstructed;
- what source of truth exists;
- what happens during partial failure;
- how retry amplification behaves under overload;
- what failure domain and RPO/RTO apply to authoritative stores.

### Recommendation

Extend **CM-R-014 — Concurrency & Distributed-System Review** with a formal **System Invariant Contract**.

Also adopt a documentation-writing principle across CodeMaestro references:

> Store decision criteria, guarantees, failure modes, and “when this pattern is wrong” before storing encyclopedic pattern summaries.

No new track is required.

---

## High-signal finding 12 — General performance and capacity engineering is missing from the backlog

Current CodeMaestro research includes frontend performance and SRE, but lacks a general method for diagnosing and validating performance across languages, runtimes, databases, services, compilers, data pipelines, and infrastructure.

Useful methodology converges on:

```text
performance requirement / workload model
→ representative baseline
→ profiling / tracing / measurement
→ identify actual bottleneck or saturation point
→ competing hypotheses
→ targeted optimization or capacity decision
→ same-condition comparison
→ regression budget/gate
→ production observation where relevant
```

Important dimensions include:

- latency distributions rather than averages alone;
- throughput;
- CPU/memory/allocation;
- storage and I/O;
- network;
- queueing and saturation;
- database pool/connection constraints;
- concurrency/lock contention;
- cold-start behavior;
- load/stress/soak behavior;
- capacity/headroom;
- elasticity/autoscaling lag;
- retry amplification under stress;
- cost-performance trade-offs;
- benchmark variance and reproducibility.

Static platform-specific “good values” should not become timeless CodeMaestro rules unless they are stable standards. Current thresholds belong to authoritative dynamic research.

### Recommendation

Propose a new research track:

## CM-R-028 — Performance, Benchmarking & Capacity Engineering

**Proposed priority:** P1; promote to P0 for performance-critical or resource-critical systems.

Expected output:

- general performance investigation methodology;
- workload/baseline contract;
- profiler/tool selection principles;
- benchmark reproducibility model;
- load/stress/soak strategy;
- latency/throughput/resource analysis;
- capacity/headroom/elasticity reasoning;
- cost-performance model;
- performance regression gates;
- language/runtime/platform research handoff rules;
- performance-specific eval scenarios.

This does **not** pre-decide a physical standalone Skill.

---

## High-signal finding 13 — Skill ecosystems need fault-isolated discovery/loading

Current Codex runtime mechanics provide a useful scaling lesson:

- ordered Skill roots;
- explicit read/parse/validation errors;
- filtering by environment/product;
- snapshot reuse/caching;
- implicit invocation signals associated with reading Skill resources or executing Skill scripts.

The generalizable CodeMaestro principle is not to duplicate Codex runtime implementation. It is:

> A large Skill ecosystem must tolerate partial catalog failure.

One broken, stale, untrusted, or unreadable third-party Skill should not make the entire CodeMaestro capability catalog unusable or silently disappear without diagnostic evidence.

### Recommendation

Extend **CM-R-001**, **CM-R-018**, and **CM-R-023** with:

- fault-isolated discovery;
- per-Skill load/validation status;
- precedence/conflict policy;
- stale snapshot/cache policy;
- diagnostic reporting;
- safe exclusion of broken/untrusted entries.

No new track is required.

---

## High-signal finding 14 — Replay/backfill semantics are not ordinary execution semantics

Historical replay/backfill work is a useful stress case for the accepted migration and operational-safety architecture.

Required distinctions include:

- bounded time/partition window;
- target grain;
- replay/merge/overwrite semantics;
- idempotency proof at target grain;
- separate incremental vs historical cursor/watermark semantics;
- publish pause/quarantine;
- downstream notification;
- rollback strategy defined before mutation;
- single-slice/dry-run proof before broad expansion;
- reconciliation thresholds defined before execution;
- publish reopening only after reconciliation evidence.

### Recommendation

Extend **CM-R-026**, **CM-R-009**, **CM-R-015**, and the Assurance Ladder.

No dedicated Backfill Skill decision is justified in the architecture at this stage.

---

## Rejected / low-value patterns from this pass

### Generic technical-debt scoring by arbitrary code-size thresholds

Rules such as “file > 500 lines = debt,” “function > 50 lines = refactor,” or generic `impact / effort` scoring are too context-blind to become CodeMaestro canon.

Code size may be a signal, not a verdict. Debt should be tied to demonstrated cost, risk, change friction, defect history, ownership, architecture/invariant impact, or operational burden.

### Technology-specific performance quick-win lists

Caching, lazy loading, compression, autoscaling, or microservices are not universal optimizations. Performance guidance must begin with measurement and workload evidence.

### One Skill per interface/test/reliability technique

No evidence yet justifies separate Skills for REST, GraphQL, gRPC, event contracts, PBT, fuzzing, chaos tests, reconciliation, backfills, or spec mining. These should first exist as composable methodology/reference domains unless routing/composition evals prove otherwise.

### Marketplace popularity as architectural evidence

Marketplace counts, stars, and repeated personas remain discovery signals only.

---

# Candidate architecture/research changes requiring approval

## Candidate A — Interface / Protocol / Contract Engineering

Create:

**CM-R-027 — Interface, Protocol & Contract Engineering**

Default priority P1.

This owns cross-cutting contract semantics, consumer-aware compatibility, async delivery contracts, and multi-boundary verification. It composes with CM-R-026 migration/evolution, CM-R-002/003 security, and CM-R-020 evidence.

---

## Candidate B — Performance / Benchmarking / Capacity Engineering

Create:

**CM-R-028 — Performance, Benchmarking & Capacity Engineering**

Default priority P1; promote to P0 for performance/resource-critical projects.

This owns evidence-driven profiling, representative benchmarks, load/capacity reasoning, and regression methodology rather than vendor-specific optimization recipes.

---

## Candidate C — Evidence Coverage & Target Fidelity

Extend **CM-R-020** and **CM-R-025** with two invariants:

1. negative/clean conclusions are coverage-bounded;
2. evidence must match the identity/state the claim is about, or be labeled secondary/substitute evidence.

Potential future evidence metadata includes assessed surface, unassessable surface, and source-target fidelity.

---

## Candidate D — Recovered Specification

Extend **CM-R-022** and **CM-R-025** with `RECOVERED / OBSERVED SPECIFICATION` for legacy/undocumented systems.

Recovered behavior must remain epistemically weaker than original intent or an accepted normative specification until explicitly promoted by project authority.

---

## Candidate E — Operational Assurance & Resilience Closure

Extend **CM-R-006**, **CM-R-009**, **CM-R-013**, **CM-R-015**, **CM-R-020**, and **CM-R-026** with:

- reconciliation/control evidence;
- user-boundary recovery closure;
- stability windows;
- incident-to-resilience regression;
- bounded replay/backfill proof;
- explicit reopen/promotion gates.

No new track required.

---

## Candidate F — System Invariants, Misuse Resistance, and Agentic Taint Flow

Extend:

- **CM-R-014** with a System Invariant Contract;
- **CM-R-002/003** with misuse-resistant API/configuration review;
- **CM-R-003/004/008/023** with untrusted-input → agent → tool/side-effect dataflow analysis.

No new track required.

---

## Candidate G — Agent Eval Contract Hardening

Extend **CM-R-012** and **CM-R-020** with:

- task vs trajectory vs side-effect contracts;
- immutable dataset manifests;
- consent/rights/retention/contamination metadata;
- comparable candidate/baseline runs;
- statistical uncertainty and slices;
- hard invariants that cannot be averaged away;
- incident/near-miss promotion into reviewed regression cases.

No new track required.

---

## Candidate H — Skill Registry Fault Isolation

Extend **CM-R-001**, **CM-R-018**, and **CM-R-023** with fault-isolated Skill discovery/loading, explicit validation status, precedence/conflict handling, and safe exclusion of broken/untrusted entries.

No new track required.

---

# Recommended new research items

## CM-R-027 — Interface, Protocol & Contract Engineering

**Proposed priority:** P1

**Question:** How should CodeMaestro design, review, evolve, and verify consumer-facing and system-to-system contracts across APIs, RPC, events, streams, webhooks, and data/schema boundaries?

**Expected output:** semantic contract model; ownership/authority model; sync/async delivery semantics; error/idempotency/retry/concurrency guidance; consumer-aware compatibility methodology; multi-boundary contract verification; deprecation/evolution integration; misuse-resistance review; baseline eval scenarios.

**Preferred authorities:** protocol/API standards and official specifications; OpenAPI/AsyncAPI/GraphQL/gRPC primary sources where applicable; primary platform and language ecosystem guidance; mature contract-testing/evolution sources.

---

## CM-R-028 — Performance, Benchmarking & Capacity Engineering

**Proposed priority:** P1; P0 for performance/resource-critical workloads

**Question:** How should CodeMaestro measure, diagnose, optimize, benchmark, and capacity-plan software systems without relying on premature optimization or stale platform-specific thresholds?

**Expected output:** performance investigation workflow; workload/baseline contract; profiler selection model; benchmark reproducibility and statistics; load/stress/soak methodology; capacity/headroom/elasticity analysis; cost-performance reasoning; regression gates; dynamic-source policy; baseline eval scenarios.

**Preferred authorities:** language/runtime/platform profiler documentation; current official performance guidance; systems/performance engineering literature and primary tooling; workload-specific standards where applicable.

---

# Existing tracks to extend if approved

- **CM-R-001** — fault-isolated Skill discovery/loading and catalog diagnostics.
- **CM-R-002** — misuse-resistant secure API/config design.
- **CM-R-003** — agentic taint flow and unsafe-interface review.
- **CM-R-004** — AI-agent CI/CD input-flow risks.
- **CM-R-006** — reconciliation/control evidence and resilience/failure-injection rung selection.
- **CM-R-008** — end-to-end untrusted context → tool authorization reasoning.
- **CM-R-009** — operational closure at user boundary, stability windows, incident-to-drill loop.
- **CM-R-012** — task/trajectory/side-effect eval contracts and dataset governance.
- **CM-R-013** — incident/counterexample evidence into regression prevention.
- **CM-R-014** — System Invariant Contract.
- **CM-R-015** — production/readiness gates based on user-boundary and resilience evidence.
- **CM-R-018** — fault-isolated Skill composition/loading consequences.
- **CM-R-020** — source fidelity, evidence coverage denominator, reconciliation/run evidence.
- **CM-R-022** — recovered/observed specifications for undocumented systems.
- **CM-R-023** — broken/untrusted Skill isolation and agentic CI supply-chain paths.
- **CM-R-025** — recovered-spec links and source-target fidelity.
- **CM-R-026** — replay/backfill, contract cutover, reconciliation and consumer migration.

---

# Current synthesis

Pass 4 produced fewer genuinely new domains than earlier passes, which is a useful convergence signal.

The two strongest uncovered domain gaps are:

1. **Interface / Protocol / Contract Engineering**
2. **General Performance / Benchmarking / Capacity Engineering**

Most other high-value findings are better treated as hardening of already accepted mechanisms rather than new Skills or subsystems.

The architectural trend remains:

```text
fewer stable capability boundaries
+
strong contracts
+
progressively disclosed domain references
+
explicit evidence semantics
+
selective optional roles/tools
>
large catalog of overlapping expert personas
```

## Approval boundary

This document records research findings only.

No Candidate A–H is accepted architecture until explicit user review/approval.
No production Skill implementation is authorized by this pass.
Physical Skill boundaries remain eval-driven.
