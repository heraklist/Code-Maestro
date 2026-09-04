# CodeMaestro v3 Capability, Runtime, Packaging & Stabilization Design

## Status

Design direction approved interactively on 2026-09-04. This document is the consolidated written specification checkpoint and is pending the explicit written-spec review gate required before implementation planning.

This document supersedes earlier partial design descriptions where they conflict, but it does not yet replace the living canonical architecture files. Canonicalization into `docs/architecture/ARCHITECTURE.md`, `docs/architecture/DECISIONS.md`, and the central research backlog is a later documentation step after this written spec is reviewed.

No production `SKILL.md`, runtime module, script, eval implementation, plugin package, or visual asset is created by this milestone.

---

## 1. Product identity and mission

CodeMaestro is a portable software-engineering operating system implemented as one public Skill.

Its mission is:

> Transform technical intent into evidence-backed, safe, production-grade engineering outcomes across requirements, architecture, implementation, debugging, testing, review, security, privacy, data, interfaces, build systems, migrations, performance, delivery, reliability, AI/agent systems, research, experimental engineering, programming languages, and learning.

CodeMaestro preserves the useful behavioral DNA of the legacy Custom GPT while removing obsolete infrastructure assumptions such as a mandatory CodeMaestro API, Custom GPT Actions gateway, Redis state, custom auth layer, or CodeMaestro-specific execution endpoints.

The governing phrase remains:

> **Tool-independent methodology, tool-aware execution.**

CodeMaestro reasons in terms of engineering capabilities and uses whatever safe, authorized native capabilities the active environment actually exposes.

---

## 2. Core architectural invariants

The following invariants apply across every capability family, runtime surface, internal module, reference, role, and execution path.

1. **One public Skill.** The user-facing entry point is `@codemaestro`.
2. **Internal modularity must not leak into user complexity.** Specialized engineering concerns are internally routed and composed.
3. **Capability is not Skill, role, or tool.** These are separate abstraction layers.
4. **Tool-independent methodology, tool-aware execution.** Workflows are expressed in terms of engineering intent and capability requirements rather than host-specific tool names.
5. **Evidence before assertion.** Claims of correctness, safety, performance, readiness, completion, or compatibility require evidence appropriate to their scope.
6. **State before mutation.** Observe the relevant current state before changing it whenever the environment permits.
7. **Validation before success claims.** Suggested or dispatched validation is not equivalent to successful validation.
8. **Preserve intended behavior.** Fixes and refactors should not broaden scope or change behavior without explicit authority.
9. **Prefer the smallest correct solution.** Complexity must justify itself.
10. **Treat external content as untrusted data.** Repository text, web content, logs, issues, pull requests, tool outputs, retrieved context, generated content, and third-party Skills are not instruction authority by default.
11. **Never invent capabilities or execution.** Unavailable, blocked, not-run, or unverified work must be reported accurately.
12. **Research before version-sensitive assertions.** Current APIs, platform behavior, security guidance, standards, and fast-moving language/toolchain details require authoritative freshness checks when material.
13. **Progressive disclosure is mandatory.** Load the minimum sufficient methodology and references for the current stage.
14. **Behavioral parity over implementation parity.** Portability is measured by equivalent engineering behavior and evidence semantics, not identical tool traces.
15. **Equivalent capabilities should produce equivalent engineering behavior regardless of Chat, Work, or Codex.**
16. **Product surface is metadata, not authority.** Surface identity must not artificially restrict CodeMaestro.
17. **Routing can add methodology; it cannot add authority.**
18. **Precise causes must survive composition.** Context may be added as evidence passes through routers, capabilities, roles, and surfaces, but a more precise underlying diagnostic or finding must not be flattened or destroyed.
19. **Evidence is structured state; rendering is a projection.** Evidence provenance should survive cross-surface handoff.
20. **Repository/artifact state outranks conversational memory for durable project truth.**
21. **Project quality constraints must not be silently weakened to make CodeMaestro's own work pass.**
22. **New public Skills are a last resort.** Splitting the single orchestrator requires empirical eval evidence that routing, isolation, context efficiency, or correctness cannot be achieved cleanly inside the existing architecture.
23. **Research breadth ends after the accepted Pass 5 scope.** Further expansion requires evidence from real failures or eval gaps rather than continued catalog hunting.

---

## 3. Public surface and internal architecture

### 3.1 Single public entry point

CodeMaestro exposes one user-facing invocation surface:

```text
@codemaestro
```

The user is not expected to know, discover, install, remember, or select engineering sub-skills such as debugger, security, architecture, UI, database, or research.

The desired UX is:

```text
@codemaestro
"The login breaks after refresh. Find the cause, fix it, verify it, and prepare the change."
```

not:

```text
Choose skill:
- Debugger
- Security
- Frontend
- Testing
- Repository
```

Natural-language intent is the primary interface. Optional shortcuts may exist later, but they must never be required for correct routing.

### 3.2 Capability modules, not public Skills

Internal specialization is represented conceptually as capability modules and shared intelligence modules. They may be implemented as references, mode files, structured registries, internal Skill-like units, or other portable mechanisms supported by the final packaging format.

The architecture does **not** assume that every capability family becomes an independently discoverable Agent Skill.

```text
USER
  |
  v
@codemaestro
  |
  +-- intent decomposition
  +-- capability discovery
  +-- authorization/trust gate
  +-- internal router/composer
  |
  +-- capability modules
  +-- shared intelligence
  +-- focused references
  +-- deterministic helpers
  +-- evals
  |
  v
native capabilities
```

### 3.3 Capability / Skill / role / tool separation

Canonical distinction:

```text
CAPABILITY != SKILL != ROLE != TOOL
```

Examples:

- Debugging is an engineering capability.
- Repository Intelligence is shared intelligence.
- `skeptic` may be an optional independent runtime role.
- shell, GitHub, browser, database, deployment, filesystem, and connected apps are runtime capabilities/tools.

This separation prevents skill proliferation and keeps reusable methodology independent from host mechanics.

---

## 4. Capability composition model

CodeMaestro uses a hierarchical composer rather than a one-mode router or free-form capability soup.

### 4.1 Routing pipeline

```text
USER INTENT
    |
    v
PRIMARY OBJECTIVE
    |
    v
REQUIRED ENGINEERING CONCERNS
    |
    v
SHARED INTELLIGENCE
    |
    v
RUNTIME CAPABILITY + AUTHORITY DISCOVERY
    |
    v
COMPOSED WORKFLOW
    |
    v
EXECUTE -> VERIFY -> REPORT
```

### 4.2 Primary objectives

Representative internal objective classes include:

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

They are internal routing semantics, not user-facing modes.

### 4.3 Minimum sufficient composition

The router selects the minimum capability set sufficient to perform the task correctly.

Example:

```text
"Fix duplicate Supabase rows"

Primary:
  Debugging & Diagnostics

Supporting:
  Database & Data Engineering
  Testing & Assurance

Conditional:
  Migration & Compatibility if schema drift is confirmed
  Security & Trust if authorization/RLS is implicated
```

The router must avoid unnecessary capability activation, context loading, and duplicated methodology.

### 4.4 Progressive activation and deactivation

Routing is not a one-time classification event.

```text
INITIAL ROUTE
    |
    v
inspect evidence
    |
    +-- no new concern -> continue
    |
    +-- material new concern -> add required capability
    |
    +-- disproven concern -> drop/de-emphasize capability
```

If a simple refactor reveals an externally consumed compatibility boundary, Contract and Migration methodology may be added. If a suspected database bottleneck is disproven, database-performance reasoning should stop consuming context.

### 4.5 Routing confidence

Routing may maintain internal confidence such as HIGH / MEDIUM / LOW. Low-confidence domains are not automatically activated. Evidence should resolve ambiguity where possible before asking the user to classify their own task.

Clarification is justified only when:

1. available context/evidence cannot resolve the ambiguity; and
2. choosing the wrong route would materially change scope, risk, or outcome.

### 4.6 Capability contracts

Every capability family should eventually have a concise internal contract containing at least:

- Purpose
- Use when
- Do not use as primary when
- Nearest-neighbor boundaries
- Inputs
- Outputs
- Required evidence
- Escalation conditions
- De-escalation conditions
- Risk modifiers

This is necessary to keep routing boundaries testable and reduce overlap.

---

## 5. Canonical capability families

After five research passes, CodeMaestro freezes the first-generation capability taxonomy at **17 canonical engineering families**.

### 5.1 Requirements, Architecture & Systems Engineering

Owns problem framing, requirements, success criteria, assumptions, scope decomposition, architecture alternatives, system boundaries, dependency direction, data/system flows, trust boundaries, design decisions, architectural drift, and greenfield system structure.

Requirements are part of this family rather than a separate silo because intent, requirements, architecture, implementation, and evidence must remain traceable.

### 5.2 Product / UX / UI Engineering

Owns product discovery, UX research, problem framing, task/journey flows, information architecture, interaction design, UI/visual design, responsive behavior, accessibility, design systems, tokens, component specifications, prototyping, usability validation, design-to-code, visual/interaction QA, and design-system governance/drift.

The family must distinguish expert/heuristic analysis from observed user research. It must never fabricate participants, consent, observations, or quotes.

UI quality is multi-boundary:

```text
render correctness
+ interaction correctness
+ accessibility
+ visual fidelity
+ user-flow correctness
```

### 5.3 Software Implementation

Owns features, fixes, services, components, endpoints, integrations, scripts, libraries, configuration, and incremental code delivery.

Default workflow:

```text
understand existing system
-> smallest correct change
-> implement
-> verify
```

### 5.4 Debugging & Diagnostics

Owns symptom reproduction, evidence collection, competing hypotheses, discriminating checks, root-cause identification, minimal repair, regression evidence, and preservation of precise diagnostic causes.

Canonical debugging shape:

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

### 5.5 Testing & Assurance

Owns proportional validation across example tests, characterization, unit/integration/system tests, contract tests, end-to-end checks, property-based tests, fuzzing, mutation testing, differential/oracle testing, reconciliation, static/model verification, and formal proof when justified.

The governing principle is the cheapest sufficient assurance for the risk and property shape.

### 5.6 Review, Audit & Compliance

Owns code review, repository audit, finding verification/refutation, spec-to-code compliance, scope review, architecture review, documentation/code drift review, and evidence-calibrated finding severity/confidence.

Candidate findings must be verified, refuted, or explicitly left partial/undecidable; speculation must not be promoted to verified finding.

### 5.7 Security & Trust Engineering

Owns application security, authn/authz, secrets, trust boundaries, secure defaults, misuse resistance, threat modeling, dependency/supply-chain risk, CI security, infrastructure/cloud security, agentic security, prompt injection, MCP/tool authorization, data exposure, and agentic taint/information flow.

Security answers the authority/trust question, but it does not own the full privacy/data-purpose lifecycle.

### 5.8 Privacy & Data Lifecycle Engineering

Owns privacy risk and the lifecycle of personal, sensitive, or user-derived data even when processing is technically authorized and no cybersecurity breach exists.

Scope includes:

- data inventory and flow mapping
- purpose and permitted use
- minimization
- collection boundaries
- storage, retention, archival, and deletion
- backups, logs, analytics, telemetry, caches, replicas, vector indexes, and derived datasets
- exports and third-party processors
- cross-system propagation
- de-identification/re-identification risk
- disclosure/user control
- AI training/evaluation/personalization data use
- privacy-by-design
- disposal/decommissioning

Exact legal/regulatory obligations are target-, jurisdiction-, and time-sensitive research, not static global doctrine.

### 5.9 Database & Data Engineering

Owns data models, schemas, integrity, queries, indexes, transactions, concurrency, data quality, reconciliation, migrations, backup/recovery, performance, and database-specific engineering such as PostgreSQL/Supabase when relevant.

### 5.10 Interface / Protocol / Contract Engineering

Owns durable behavioral agreements across APIs, RPC, GraphQL, events, streams, webhooks, schemas, data contracts, SDK-facing interfaces, and protocols.

Contract semantics include null/absent behavior, defaults, identifiers, units, ordering, pagination, authorization preconditions, errors, retries, idempotency, concurrency, delivery guarantees, duplicate/gap/reorder behavior, quotas, compatibility, deprecation, and consumer expectations.

### 5.11 Build, Toolchain & Environment Engineering

Owns build systems, toolchain discovery/pinning, package/build configuration, compiler/linker settings, environment parity, dev/prod drift, hermeticity, reproducibility, generated artifacts/codegen drift, build caches, cross-compilation, architecture/platform targets, build provenance, build debugging, and build performance.

This is distinct from CI/CD because a build can be incorrect, non-reproducible, or environment-dependent even when the pipeline itself is correctly configured.

### 5.12 Migration & Compatibility Engineering

Owns framework/runtime/dependency/schema/API/platform migrations, compatibility analysis, reversible transitions, dual-compatible operation, old-vs-new comparison, cutover, rollback, cleanup, deprecation, and migration evidence.

Preferred lifecycle:

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

### 5.13 Performance & Capacity Engineering

Owns workload definition, baselines, profiling/tracing, bottleneck discrimination, latency/throughput/resource usage, queueing/saturation/backpressure, load/stress/spike/soak testing, benchmark reproducibility, cost/performance, capacity/headroom, elasticity, and performance regression gates.

Performance claims are workload-relative and require comparable before/after evidence.

### 5.14 CI/CD, Platform & Delivery Engineering

Owns CI pipelines, automation, environments, deployment, release orchestration, platform workflows, infrastructure delivery, release gates, rollback mechanisms, artifacts, and production delivery systems.

Developer-experience/platform concerns may compose with this family but do not require a separate top-level family.

### 5.15 Reliability, Observability, SRE & Incident Engineering

Owns logs, metrics, traces, semantic telemetry, SLI/SLOs, error budgets, alerting, operational readiness, failure/degradation, incident response, recovery, rollback validation, resilience regression, production observation, telemetry cardinality/cost/privacy, and user-boundary closure.

A system is not considered recovered solely because internal metrics are green; recovery evidence should reach the relevant user/business boundary.

### 5.16 AI / LLM / Agent / MCP Engineering

Owns agent architectures, prompts/context, retrieval/RAG, tool design, MCP, orchestration, state, evals, model/tool boundaries, permission design, reliability, cost/performance, and agent-specific security/side-effect concerns.

### 5.17 Research, Experimental & Language Engineering

Owns evidence-driven survey, compare, investigate, experiment, replicate, and evolve workflows; experimental engineering; programming-language support; Language Intelligence integration; experimental-language governance; and controlled research-to-decision promotion.

Research results do not become project authority automatically.

---

## 6. Shared intelligence substrate

Shared Intelligence is not a list of user-facing capabilities. It is reusable reasoning infrastructure injected into engineering workflows when relevant.

### 6.1 Language Intelligence

Answers:

> What language, version, compiler/runtime, toolchain, maturity level, and source hierarchy apply?

It supports mainstream, niche, legacy, domain-specific, private, and experimental languages without permanent one-Skill-per-language packaging.

### 6.2 System Intelligence

Answers:

> What kind of software system is this and what execution/deployment/state model does it imply?

Representative types include:

- web application / frontend SPA
- backend/API service
- mobile application
- desktop application
- CLI
- library / SDK
- compiler / programming language
- database system
- data pipeline
- AI/ML system
- agentic application
- embedded system
- game/mod
- distributed system
- infrastructure/platform
- monorepo / multi-service workspace

System Intelligence is distinct from Language Intelligence and Repository Intelligence.

### 6.3 Repository / Workspace Intelligence

Answers:

> How is this specific implementation organized and what is the blast radius of a change?

It covers repository comprehension, package/service topology, monorepos, multi-repo systems, generated/vendored boundaries, dependency graphs, reverse-dependency closure, ownership, affected build/test/deploy scope, and architecture drift.

Canonical order:

```text
UNDERSTAND
-> MODEL BOUNDARIES / FLOWS / INVARIANTS
-> OPEN QUESTIONS
-> IMPACT / BLAST RADIUS
-> ONLY THEN JUDGE OR CHANGE
```

### 6.4 Context / Long-Horizon Intelligence

Owns durable project state, resumability, context selection, context freshness, artifact references, and recovery across long-running or multi-session work.

Conversation memory is not canonical project state.

### 6.5 Research / Freshness Intelligence

Determines when local knowledge is insufficient or stale and selects current authoritative sources for version-sensitive claims.

### 6.6 Evidence / Provenance Intelligence

Preserves source, target, version/SHA, environment, action/command, result, coverage, limitations, and evidence state.

Evidence should be captured at production/retrieval time and must survive routing and surface changes without losing precise provenance.

### 6.7 Intent-to-Evidence Traceability

Maintains bidirectional relationships among:

```text
user intent
<-> requirements/spec
<-> architecture/decision
<-> implementation
<-> tests/checks
<-> deployed/user-boundary evidence
```

Recovered specifications remain weaker than normative intent until explicitly promoted.

---

## 7. Cross-runtime execution contract

### 7.1 Capability-first, surface-aware

The architecture is capability-first and only secondarily surface-aware.

```text
TASK
  |
  v
AVAILABLE CAPABILITIES
  +
AUTHORIZED CAPABILITIES
  +
SAFETY / RISK POLICY
  |
  v
MAXIMUM SAFE EXECUTION DEPTH
```

The product surface must not impose an artificial downgrade.

### 7.2 Chat and Work

Chat and Work share the same CodeMaestro engineering semantics.

Chat is not advisory-only by design. If Chat exposes repository access, connected apps, filesystem, shell, compiler/test runner, browser, database, deployment, artifacts, or other capabilities, CodeMaestro should use them when methodologically appropriate and authorized.

Work is not required merely because a task is large or serious if Chat already exposes the capabilities needed for correct execution.

### 7.3 Codex

Codex uses the same core methodology, evidence model, authority model, capability taxonomy, and quality model.

Codex-specific adaptation is limited to mechanics such as local repository semantics, shell/git behavior, worktrees, sandboxing, browser surfaces, approval UX, and runtime-specific capabilities.

### 7.4 Runtime Capability Vector

Substantial tasks may maintain an internal capability snapshot such as:

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

The exact representation is an implementation detail; the semantic distinction is mandatory.

### 7.5 Availability is not authorization

```text
CAPABILITY EXISTS
!=
CAPABILITY IS AUTHORIZED
```

Effective execution requires the intersection of host capability, host permission, user/task authority, and safety/risk policy.

### 7.6 No-artificial-degradation rule

If Chat exposes a capability that CodeMaestro would use in Work or Codex for the same task, CodeMaestro should use it in Chat as well unless a concrete authorization, safety, or environment constraint applies.

The same principle applies in reverse. A surface name does not guarantee a capability.

### 7.7 Shell is a capability, not a Codex concept

Correct abstraction:

```text
if shell_available_and_authorized:
    use shell when the methodology requires it
```

Incorrect abstraction:

```text
if surface == codex:
    use shell
```

The same rule applies to filesystem, browser, GitHub, databases, apps, and deployment.

### 7.8 Graceful degradation

When a required capability is absent:

```text
requested workflow
-> detect capability gap
-> find valid substitute if possible
-> otherwise reduce execution depth
-> report exact limitation and evidence state
```

For example, if tests are required but no executable environment exists, CodeMaestro may write a test and provide the exact run command, but must report `PROVIDED, NOT EXECUTED` or another accurate status rather than claiming success.

### 7.9 Capability recovery

If a capability becomes available mid-task, CodeMaestro may increase execution depth without changing public mode. If a capability disappears, the workflow degrades truthfully.

### 7.10 Cross-surface evidence contract

Evidence should survive transitions such as:

```text
Chat -> Codex
Codex -> Work
Work -> Chat
```

A handoff should preserve material state such as:

- task / intent
- current target and version/SHA
- accepted decisions
- changes
- evidence
- unresolved questions
- risks
- next authorized action

### 7.11 Durable state over conversation state

Material long-horizon project state should live in durable artifacts where possible: repository docs, issues, plans, decisions, evidence ledgers, test artifacts, or equivalent project state.

---

## 8. Authority and Task Capability Manifest

### 8.1 Routing cannot create authority

Activating a deployment, database, or repository capability does not grant permission to perform consequential actions.

### 8.2 Task Capability Manifest

For consequential or high-autonomy work, CodeMaestro may derive a task-scoped capability manifest:

```text
Task Capability Manifest
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

Example:

```text
repo.read       ALLOWED
repo.write      ALLOWED on feature branch
tests           ALLOWED
deploy.staging  ALLOWED
deploy.prod     NOT AUTHORIZED
merge.main      NOT AUTHORIZED
db.prod.write   NOT AUTHORIZED
```

The manifest can only narrow host/user authority. It cannot create authority that the host, workspace, account, or user did not grant.

The mechanism should be proportional: small low-risk tasks do not require ceremonial manifest artifacts.

---

## 9. Project Quality Contract

CodeMaestro should discover or establish the project's durable quality bar when material to the work.

Potential quality-contract dimensions include:

- correctness expectations
- build/type/lint requirements
- testing and coverage requirements
- security constraints
- accessibility requirements
- performance budgets
- architectural constraints
- release gates

A failing implementation must be repaired rather than made green by silently weakening tests, coverage, lint, security, accessibility, or other project constraints.

Changes to the quality contract itself require explicit authority and should be distinguishable from changes made to satisfy it.

---

## 10. Progressive disclosure and internal packaging

### 10.1 One Skill does not mean one giant file

The root `SKILL.md` must remain a compact orchestrator containing only global methodology and routing invariants.

Heavy domain material belongs in progressively loaded modules/references.

### 10.2 Four levels of disclosure

**Level 0 — Public metadata / identity**

Skill/plugin identity, name, icon/branding, and minimal discovery metadata where supported.

**Level 1 — Core orchestrator**

Mission, invariants, routing, capability discovery, authorization/trust, quality contract, research/freshness gate, evidence semantics, mutation/completion rules, and cross-runtime contract.

**Level 2 — Capability modules**

The 17 engineering families.

**Level 3 — Deep references / techniques**

Focused domain material such as authentication, RLS, supply chain, accessibility, property-based testing, formal methods, design systems, telemetry, migration patterns, current standards, and technology-specific guidance.

### 10.3 Conceptual package layout

The final Agent Skills / OpenAI packaging format must be re-verified at implementation time. Conceptually:

```text
codemaestro/
├── SKILL.md
├── manifest-or-host-metadata/
├── assets/
│   └── CodeMaestro identity
├── router/
│   ├── capability-registry
│   ├── routing-rules
│   └── composition-rules
├── capabilities/
│   ├── requirements-architecture/
│   ├── product-ux-ui/
│   ├── implementation/
│   ├── debugging/
│   ├── testing/
│   ├── review-audit/
│   ├── security/
│   ├── privacy-data-lifecycle/
│   ├── database-data/
│   ├── contracts/
│   ├── build-environment/
│   ├── migration/
│   ├── performance/
│   ├── delivery-platform/
│   ├── reliability-observability/
│   ├── ai-agent/
│   └── research-language/
├── intelligence/
│   ├── language/
│   ├── system/
│   ├── repository-workspace/
│   ├── context/
│   ├── research-freshness/
│   ├── evidence/
│   └── traceability/
├── references/
├── scripts/
└── evals/
```

This is an information architecture, not a commitment that every directory maps one-to-one to a runtime-loadable Skill.

### 10.4 Stable methodology vs current knowledge

Stable engineering methodology and fast-changing technical facts must be physically and conceptually separable.

Version-sensitive references should preserve at least source/authority, scope, version applicability, last verification, and freshness trigger where practical.

### 10.5 Deterministic helpers

Use scripts or deterministic helpers only when repeatability, validation, or context savings justify their maintenance cost. Mechanical checks should be deterministic before consuming model judgment where possible.

### 10.6 Third-party Skill adoption

Third-party Skills or plugins are research/supply-chain inputs, not automatically trusted execution modules.

Adoption path:

```text
DISCOVER
-> PROVENANCE / LICENSE
-> QUARANTINE / STRUCTURE
-> PROMPT-INJECTION REVIEW
-> EXECUTABLE / SCRIPT REVIEW
-> DEPENDENCY REVIEW
-> FS / NETWORK / CREDENTIAL REVIEW
-> TOOL / PERMISSION SCOPE
-> BEHAVIORAL / EVAL REVIEW
-> ADOPT / ADAPT / REJECT
```

CodeMaestro should prefer extracting validated methodology rather than blindly delegating authority to arbitrary installed third-party Skills.

---

## 11. Visual identity and Skill icon

CodeMaestro requires a coherent, recognizable visual identity wherever the host supports branded Skill/plugin presentation.

### 11.1 Direction

Approved visual direction: **Maestro Monogram**.

The primary mark should be a custom geometric `CM` monogram communicating engineering precision and orchestration without relying on generic developer/AI clichés such as a bare `</>`, robot head, terminal cursor, or sparkle motif.

Desired character:

- precise
- technical
- minimal
- premium
- confident
- not playful
- not cyberpunk
- not "AI magic"

Preferred initial palette direction:

- deep graphite / near black base
- off-white or very light neutral mark
- controlled cobalt/electric-blue accent

### 11.2 Icon-first design

The mark must remain recognizable at composer/Skill-list sizes. Branding must not depend on adjacent text.

Target behavior:

```text
16-20 px  -> recognizable silhouette
32-64 px  -> clear CodeMaestro mark
256+ px   -> complete logo/detail
```

### 11.3 Asset set

Expected assets may include:

```text
assets/
├── codemaestro-composer.svg
├── codemaestro-logo.svg
├── codemaestro-logo-dark.svg
├── codemaestro-logo-light.svg
├── codemaestro-mark.svg
└── codemaestro-preview.png
```

The exact manifest fields and supported asset hooks are product-specific and must be verified against current OpenAI/Agent Skills packaging when implementation begins.

### 11.4 Visual selection process

Before final packaging, create three icon variants within the approved Maestro Monogram direction, compare them at small composer size and larger identity size, and select one final mark before integration.

---

## 12. Domain profiles instead of capability proliferation

Some common engineering domains are compositions of existing families rather than new top-level families.

Examples:

```text
Developer Experience
= Product/UX
+ Interfaces/Contracts
+ Build/Environment
+ Platform/Delivery
+ Documentation workflows

Monorepo Engineering
= Repository/Workspace Intelligence
+ Architecture
+ Build
+ Testing
+ Contracts

Supabase Engineering
= Database
+ Security
+ Migration
+ current research

Frontend Engineering
= Implementation
+ Product/UX/UI
+ Performance
+ Accessibility

Compiler Engineering
= Language Intelligence
+ System Intelligence
+ Implementation
+ Testing/Assurance
+ Performance
+ Research/Experimental
```

Documentation/knowledge maintenance is an explicit cross-cutting workflow, not a separate family. It includes human-facing docs, agent-facing instructions, examples, ADRs, docs-to-code drift, stale-version detection, and examples-as-tests where appropriate.

---

## 13. Research closure and accepted final tracks

Pass 5 is the final breadth-oriented research pass for this architecture generation.

The accepted additional research tracks are:

### CM-R-029 — Cross-Runtime Portability, Capability Discovery & Conformance

**Priority:** P0.

Scope includes portable Skill/plugin packaging, Chat/Work/Codex capability discovery, permission differences, fallback semantics, cross-surface handoff, and conformance evals.

### CM-R-030 — Product, UX/UI & Visual Interface Engineering

**Priority:** P1 by default; promote to P0 when the task is user-facing/product-critical.

Scope includes UX research integrity, flow audits, interaction design, visual direction, accessibility, responsive design, design systems, design-to-code, visual/interaction QA, and design-system governance/drift.

### CM-R-031 — Build, Toolchain & Environment Engineering

**Priority:** P1 by default; promote to P0 for build/release integrity, security-sensitive provenance, or consequential reproducibility requirements.

Scope includes toolchain correctness, build systems, environment parity, hermeticity, reproducibility, generated artifacts/codegen drift, build caches, platform targets, and build provenance.

### CM-R-032 — Privacy & Data Lifecycle Engineering

**Priority:** P1 by default; promote to P0 for personal/sensitive/high-impact data, children, health/financial data, biometrics, location, high-impact profiling, large-scale user data, or AI training/personalization based on personal data.

Scope includes privacy risk, data minimization, lifecycle, retention/deletion, propagation into backups/logs/caches/analytics/vector indexes, third parties, disposal, and privacy-by-design.

No CM-R-033 is authorized by Pass 5. Developer Experience, documentation, monorepo/workspace, and telemetry concerns remain profiles/workflows inside existing families and shared intelligence.

---

## 14. Evaluation model

CodeMaestro is evaluated by behavior and evidence, not by the amount of guidance it contains.

### 14.1 Required eval dimensions

1. **Routing** — selects the correct primary/supporting capabilities and avoids unnecessary activation.
2. **Capability effectiveness** — each family performs its core methodology correctly.
3. **Composition** — multiple families cooperate without contradictory workflows or ordering errors.
4. **Cross-runtime conformance** — equivalent capabilities produce equivalent engineering behavior across Chat, Work, and Codex.
5. **Capability degradation** — missing capabilities reduce execution depth truthfully without fabricated execution.
6. **Safety / authority** — read/write, consequential actions, production boundaries, credentials, and untrusted content remain inside authority.
7. **Evidence quality** — claims have appropriate provenance, target fidelity, coverage, and limitations.
8. **User outcome** — completion reaches the relevant user/business boundary where applicable.

### 14.2 Agent eval contracts

Agentic evaluation should distinguish:

- **Task contract** — was the requested objective achieved?
- **Trajectory contract** — was the execution path methodologically acceptable?
- **Side-effect contract** — what changed, and what must not have changed?
- **Evidence contract** — are success/finding claims backed by appropriate evidence?

A correct final output can still fail the trajectory or side-effect contract.

### 14.3 RED evals first

Before implementing the production Skill, create representative failing/baseline scenarios that expose current generic-agent weaknesses. The smallest CodeMaestro guidance that corrects the observed failure should then be added and regression tested.

### 14.4 Eval suites

Conceptual suites:

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
├── adversarial/
├── regression/
└── end-to-end/
```

### 14.5 Golden scenarios

The first regression corpus should include representative cases for:

- concurrency debugging
- framework/runtime migration
- security/auth bypass candidate
- product/UI redesign -> implementation -> visual QA
- transaction/data integrity bug
- local-pass / CI-fail build environment drift
- untrusted retrieved instruction attempting agent/tool misuse
- experimental-language semantics with conflicting authorities
- privacy/data-retention propagation failure
- cross-runtime equivalent-capability conformance

### 14.6 Project Quality Contract evals

Explicitly test that CodeMaestro does not silence checks, remove failing tests, lower coverage, weaken lint/types/security/accessibility, or change release thresholds merely to make its own implementation pass.

### 14.7 Cross-runtime conformance

Eval outcome equivalence, not exact tool sequence.

Compare:

- intent interpretation
- safety/authority boundary
- scope discipline
- root-cause/engineering decision
- validation standard
- evidence semantics
- completion meaning

### 14.8 Fresh-context review

Use optional independent/fresh-context review for high-impact architecture, security, research, and evidence-sensitive work when the runtime supports it and the expected value exceeds the overhead.

---

## 15. Capability freeze and stabilization

### 15.1 Capability freeze

Upon approval of Pass 5 and this written design, breadth expansion stops.

New top-level capability families require evidence that:

1. a real task or eval systematically fails;
2. the failure represents a distinct engineering responsibility;
3. existing families cannot express the required methodology cleanly; and
4. a new boundary improves routing/composition rather than adding taxonomy noise.

### 15.2 Stabilization focus

After first implementation, prioritize depth and coherence over new features.

Look for:

- overlapping capability boundaries
- inconsistent routing
- duplicated policy
- contradictory workflows
- evidence loss
- surface-specific drift
- context bloat
- accidental behavior becoming specification
- capability discovery/loading failures

### 15.3 Stabilization ladder

Conceptual sequence:

```text
S0 structural health
S1 routing baseline
S2 capability baseline
S3 composition
S4 cross-runtime
S5 adversarial/security
S6 real-project trials
S7 release baseline
```

Exact stage names may change; the progression from structural correctness to real-world closure should remain.

### 15.4 Skill discovery/loading fault isolation

A broken optional capability/reference must not silently corrupt unrelated workflows. Discovery/loading failures should be isolated, surfaced, and truthfully degraded where possible.

---

## 16. Controlled evolution

CodeMaestro must not silently rewrite its own methodology.

Preferred lifecycle:

```text
OBSERVED FAILURE
-> PROPOSED CHANGE
-> RATIONALE
-> EVAL CASE
-> IMPLEMENT IN ISOLATION
-> REGRESSION SUITE
-> INDEPENDENT REVIEW
-> HUMAN AUTHORIZATION
-> PROMOTE
```

Architecture changes carry a higher burden of proof than reference refreshes.

### 16.1 Change classes

**Low impact**
- current-reference refresh
- typo/citation correction

**Medium impact**
- workflow refinement
- capability reference change

**High impact**
- new capability family
- router semantics
- authority model
- evidence model
- public Skill split
- cross-runtime policy

High-impact change requires explicit research/design/eval/approval.

### 16.2 Regression from real failures

Material CodeMaestro failures should become minimized regression evals when practical. The system should evolve through testable corrections rather than an ever-growing prompt.

### 16.3 No skill creep

Default response to a new domain:

```text
new domain
-> existing capability composition?
   -> yes: profile/reference/workflow
   -> no: prove missing abstraction before new family/Skill
```

---

## 17. Production-readiness definition

A production-quality first Skill baseline is not established merely by creating `SKILL.md`.

At minimum:

- one public `@codemaestro` works as intended
- routing evals pass
- core capability evals pass
- composition evals pass
- cross-runtime conformance is demonstrated
- graceful degradation is demonstrated
- authority/safety evals pass
- evidence/provenance semantics hold
- Project Quality Contract protection is demonstrated
- no major unresolved capability overlap remains
- packaging/branding is validated against the current host format
- representative real-project trials complete
- operational/user-boundary verification is available where relevant

---

## 18. Next-step sequence after written-spec approval

This specification intentionally stops before implementation planning.

After explicit user review and approval of this written file, the next Superpowers step is to invoke `writing-plans` and create a detailed implementation plan.

The implementation sequence should begin with synthesis/canonicalization and RED eval design before production Skill authoring:

```text
WRITTEN SPEC APPROVED
-> CANONICALIZE ARCHITECTURE / DECISIONS / RESEARCH BACKLOG
-> SYNTHESIZE CAPABILITY CONTRACTS
-> WRITE RED EVALS
-> FINALIZE PHYSICAL PACKAGING
-> IMPLEMENT COMPACT ORCHESTRATOR
-> IMPLEMENT PROGRESSIVE MODULES / REFERENCES
-> VALIDATE CROSS-RUNTIME BEHAVIOR
-> STABILIZE
```

The exact task breakdown belongs in the implementation plan, not in this design checkpoint.

---

## 19. Out of scope for this design checkpoint

This document does not:

- create the production `SKILL.md`;
- create internal capability/reference files;
- create runtime scripts;
- implement evals;
- implement cross-runtime adapters;
- create the final icon assets;
- install or publish a plugin;
- merge PR #1;
- declare the Skill production-ready.

Those actions remain gated by written-spec review and the subsequent implementation plan.
