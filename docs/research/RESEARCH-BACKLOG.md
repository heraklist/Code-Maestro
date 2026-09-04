# CodeMaestro Research Backlog

## Purpose

This backlog is the canonical queue/index for CodeMaestro research tracks. It tracks research that must be completed before related guidance becomes canonical CodeMaestro architecture or Skill reference material and records accepted working tracks that remain active inputs to implementation/evals.

Research findings are evidence, not automatic project decisions. Material changes to the architecture must be recorded in `docs/architecture/DECISIONS.md` and incorporated into `docs/architecture/ARCHITECTURE.md` after review.

## Status values

- `QUEUED` — identified but not started.
- `IN RESEARCH` — active evidence collection.
- `SYNTHESIS` — sources gathered; conclusions being compared.
- `REVIEW` — recommendation ready for architectural review.
- `ACCEPTED` — findings/direction accepted into architecture or an accepted working track exists.
- `REJECTED` — researched but not adopted.

## Authority preference

For all research:

1. official specifications and standards;
2. official product/project documentation;
3. primary repositories, release notes, advisories, and maintainers;
4. high-quality secondary technical sources where primary evidence is insufficient.

Fast-changing claims should be date/version scoped. Where pre-CM-ADR-018 research lacks exact SHA/version/timestamp provenance, that limitation must be stated rather than reconstructed from memory.

---

## CM-R-001 — Agent Skills and Codex engineering workflows

**Priority:** P0
**Status:** IN RESEARCH

**Question:** What are the current authoritative design, packaging, progressive-disclosure, testing, tool-use, agent-role, and workflow patterns for Agent Skills and Codex-oriented engineering work?

**Expected output:** Recommended Skill structure, trigger design, reference-loading strategy, script boundaries, eval strategy, subagent-role boundary, plugin evolution path, and portability constraints for CodeMaestro.

**Preferred authorities:** OpenAI official Codex repository/documentation, OpenAI plugin examples, Agent Skills specification where applicable.

---

## CM-R-002 — Secure software-development standards

**Priority:** P0
**Status:** QUEUED

**Question:** Which current standards should anchor CodeMaestro's general secure-development methodology without making the Skill dependent on stale tool-specific checklists?

**Expected output:** Stable security principles, review taxonomy, confidence model, and guidance on what must remain dynamically researched.

**Preferred authorities:** NIST, OWASP, CISA, language/platform primary security guidance.

---

## CM-R-003 — OWASP application, LLM, and agentic security

**Priority:** P0
**Status:** QUEUED

**Question:** How should CodeMaestro modernize security review for conventional applications and AI/LLM/agent systems, including prompt injection, tool abuse, RAG trust, excessive agency, insecure output handling, and data exposure?

**Expected output:** Updated threat/review domains and reusable review methodology.

**Preferred authorities:** OWASP primary projects and current official guidance.

---

## CM-R-004 — GitHub Actions and CI/CD security

**Priority:** P1
**Status:** QUEUED

**Question:** What current CI/CD security and reliability practices should replace legacy static assumptions in the GitHub CI review playbook?

**Expected output:** Current guidance for permissions, third-party actions, pinning/provenance, secrets, untrusted PRs, runners, artifacts, caching, environments, and validation evidence.

**Preferred authorities:** GitHub official documentation/security guidance; relevant supply-chain standards.

---

## CM-R-005 — Software supply-chain assurance

**Priority:** P1
**Status:** QUEUED

**Question:** How should CodeMaestro review and recommend SBOMs, provenance, signing, attestations, dependency integrity, build integrity, and release evidence in current software projects?

**Expected output:** Modern supply-chain review playbook and risk model.

**Preferred authorities:** SLSA, Sigstore, SPDX/CycloneDX, CISA/NIST, ecosystem primary documentation.

---

## CM-R-006 — Modern testing strategy

**Priority:** P0
**Status:** QUEUED

**Question:** What testing methodology should CodeMaestro use across bug fixes, features, refactors, distributed systems, APIs, databases, and agentic software?

**Expected output:** Decision framework spanning unit, integration, contract, property-based, fuzz, mutation, end-to-end, regression, reconciliation/control evidence, resilience regression, and environment-specific validation without dogmatically requiring every test type everywhere.

**Preferred authorities:** primary framework documentation, established testing literature, standards and project guidance where applicable.

---

## CM-R-007 — PostgreSQL and Supabase current practices

**Priority:** P1
**Status:** QUEUED

**Question:** What current PostgreSQL and Supabase guidance should anchor schema, migration, RLS, auth, functions, edge/runtime, performance, backup, and production-safety review?

**Expected output:** Updated database/Supabase reference and migration-safety methodology.

**Preferred authorities:** PostgreSQL and Supabase official documentation.

---

## CM-R-008 — MCP and tool authorization security

**Priority:** P0
**Status:** QUEUED

**Question:** How should CodeMaestro reason about MCP servers, tool trust, authorization, least privilege, confused-deputy risks, prompt injection across tool boundaries, and consequential actions?

**Expected output:** Tool authorization and agentic execution security model suitable for the Skill core and AI-agent reference.

**Preferred authorities:** MCP/OpenAI official documentation, primary security guidance, relevant standards.

---

## CM-R-009 — Observability and SRE readiness

**Priority:** P1
**Status:** QUEUED

**Question:** What production-readiness and observability methodology should CodeMaestro apply across logging, metrics, traces, alerting, SLOs, error budgets, incident response, rollback, release verification, telemetry semantics, and user-boundary closure?

**Expected output:** Observability/SRE review domain and operational handoff criteria.

**Preferred authorities:** OpenTelemetry, major platform primary docs, established SRE literature.

---

## CM-R-010 — Frontend accessibility and performance

**Priority:** P2
**Status:** QUEUED

**Question:** Which current accessibility and performance standards should CodeMaestro apply to frontend reviews and implementations?

**Expected output:** Practical review methodology tied to current WCAG/platform guidance and measurable web/application performance evidence.

**Preferred authorities:** W3C/WCAG, browser/platform primary documentation.

---

## CM-R-011 — Cloud, container, and infrastructure-as-code security

**Priority:** P1
**Status:** QUEUED

**Question:** How should CodeMaestro review container images, runtime isolation, cloud permissions, secrets, networking, IaC, environment separation, and deployment safety across providers without becoming vendor-bound?

**Expected output:** Provider-agnostic core methodology plus rules for dynamic provider-specific research.

**Preferred authorities:** NIST/CISA, OCI/Kubernetes/Terraform and cloud-provider primary documentation as applicable.

---

## CM-R-012 — Coding-agent and Skill evaluation methodology

**Priority:** P0
**Status:** QUEUED

**Question:** How should CodeMaestro evaluate an engineering Skill for instruction following, safety, coding quality, debugging, research, tool use, evidence honesty, side effects, trajectory constraints, and regression resistance?

**Expected output:** Eval taxonomy, baseline methodology, scoring approach, pressure scenarios, task/trajectory/side-effect/evidence contracts, dataset governance, and regression suite design.

**Preferred authorities:** OpenAI official eval guidance, Agent Skills guidance/specifications, primary research where useful.

---

## CM-R-013 — Systematic debugging and root-cause analysis

**Priority:** P0
**Status:** QUEUED

**Question:** What general debugging methodology best supports evidence-first root-cause analysis across software stacks, including reproduction, hypothesis discrimination, tracing, concurrency issues, counterexample-driven repair, and regression prevention?

**Expected output:** Debugging workflow suitable for a core engineering reference and evaluation scenarios.

**Preferred authorities:** primary debugger/runtime guidance, established engineering literature, high-quality primary technical material.

---

## CM-R-014 — Concurrency and distributed-system review

**Priority:** P2
**Status:** QUEUED

**Question:** How should CodeMaestro identify and reason about race conditions, idempotency, ordering, retries, consistency, leases/locks, distributed transactions, queues, and failure modes?

**Expected output:** Review checklist and System Invariant Contract driven by system invariants rather than technology-specific recipes.

**Preferred authorities:** primary platform documentation and established distributed-systems literature.

---

## CM-R-015 — Release and production-readiness engineering

**Priority:** P1
**Status:** QUEUED

**Question:** What evidence should CodeMaestro require or recommend before calling software release-ready or production-ready?

**Expected output:** Release-readiness model covering validation, security, migrations, observability, user/business-boundary closure, rollback, dependency/supply chain, configuration, and operational ownership.

**Preferred authorities:** relevant official platform guidance and established production engineering practices.

---

## CM-R-016 — Universal Language Intelligence and Experimental Language Support

**Priority:** P0
**Status:** IN RESEARCH

**Question:** How should CodeMaestro provide reliable engineering support across mainstream, niche, legacy, domain-specific, private, and experimental languages without using one permanently installed Skill per language?

**Expected output:** Language Intelligence architecture, language-profile contract, language taxonomy, maturity model, reliability levels, source hierarchy, unknown-language protocol, standalone language-skill promotion criteria, representative coverage matrix, and baseline eval design.

**Preferred authorities:** official language specifications and documentation; primary language/toolchain repositories; vendor-maintained Agent Skills where available; GitHub Linguist for discovery metadata; other catalogs only as discovery aids rather than correctness authorities.

**Working record:** `CM-R-016-universal-language-intelligence.md`

---

## CM-R-017 — Research & Experimental Engineering

**Priority:** P0
**Status:** ACCEPTED

**Question:** What evidence-driven research lifecycle should CodeMaestro use for surveys, comparisons, investigations, bounded experiments, replication, and experimental technical evolution?

**Expected output:** Research Lab operating model, epistemic state machine, proportional-rigor rules, hypothesis/experiment/decision workflow, stopping criteria, durable artifact model, and baseline eval scenarios.

**Preferred authorities:** primary research-method sources where relevant; rigorous agent-research systems; Cusp experimental engineering records; reproducible software-engineering practice.

**Accepted direction:** Autonomous Research Lab capability with durable evidence state and explicit separation between research result and project authority.

**Design record:** `../superpowers/specs/2026-09-04-research-experimental-engineering-design.md`

---

## CM-R-018 — Subagent and Skill Orchestration

**Priority:** P0
**Status:** IN RESEARCH

**Question:** How should CodeMaestro divide responsibility among the orchestrator, internal capability modules, shared knowledge/intelligence systems, optional runtime roles, subagents, plugins, and native tools without duplicating policy or introducing hidden dependencies?

**Expected output:** Skill-vs-role-vs-agent-vs-tool model, role contract, delegation policy, parallelism rules, fresh-context patterns, result-review rules, failure propagation, and portability strategy.

**Preferred authorities:** OpenAI Codex and plugin architecture; Superpowers; Microsoft skill/agent patterns; other portable agent systems with explicit evals and evidence models.

**Candidate roles under study:** research-scout, experimentalist, skeptic, replicator.

---

## CM-R-019 — Programming-Language Evolution & Specification Governance

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro research and assist the evolution of experimental languages while preserving clear separation among ideas, observations, characterization, proposals, accepted design, normative specification, implementation, and stable/released behavior?

**Expected output:** Language Evolution Protocol, proposal template, authority/state taxonomy, comparative language-study method, compatibility/security/resource review requirements, and promotion/acceptance gates.

**Preferred authorities:** Cusp project records; Rust RFCs; Swift Evolution; Carbon proposals/governance; Python PEPs; Kotlin KEEP; Go proposals; TC39 proposals; other mature or experimental language projects where useful.

**Primary stress case:** Cusp.

---

## CM-R-020 — Evidence, Provenance, Citations & Reproducibility

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro bind research and engineering claims to retrievable sources, repository snapshots, experiment conditions, validation runs, and reproducible artifacts?

**Expected output:** Claim/evidence model, provenance ledger, source capture rules, target/source fidelity, coverage-bounded conclusions, reconciliation/run evidence, uncertainty representation, evidence verification rules, and report integration.

**Preferred authorities:** reproducible research/software practices; source-ledger systems; Cusp snapshot/evidence model; deterministic citation/evidence workflows; primary tooling where applicable.

---

## CM-R-021 — Context Engineering & Long-Horizon State

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro preserve useful project state, resume safely across long tasks/sessions, manage context freshness, and avoid replay/stale-context failures?

**Expected output:** durable-state hierarchy, phase fingerprints, resumability protocol, fresh-context recovery, context-loading rules, and baseline evals.

**Working record:** `CM-R-021-context-engineering-long-horizon-state.md`

---

## CM-R-022 — Repository Comprehension, Impact & Architecture Drift

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro understand repository/system structure, dependency topology, behavioral boundaries, blast radius, recovered specifications, and bidirectional architecture drift before judgment or mutation?

**Expected output:** repository-comprehension workflow, dependency/impact model, recovered-spec semantics, architecture-drift detection, and affected-validation methodology.

**Working record:** `CM-R-022-repository-comprehension-impact-drift.md`

---

## CM-R-023 — Skill / Plugin Security & Supply Chain

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro evaluate third-party Skills/plugins/repositories before adoption, including provenance, prompt injection, executable scripts, dependencies, filesystem/network/credential access, permissions, and catalog fault isolation?

**Expected output:** quarantine/adoption gate, risk model, permission review, dependency/supply-chain checks, untrusted-content analysis, and adopt/adapt/reject criteria.

**Working record:** `CM-R-023-skill-plugin-security-supply-chain.md`

---

## CM-R-024 — Finding Refutation & Spec-to-Code Compliance

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro verify or refute candidate findings and compare implementation with normative specifications without promoting speculation to fact?

**Expected output:** finding state machine, counter-evidence workflow, verification/refutation rules, spec-to-code verdict vocabulary, and assurance escalation.

**Working record:** `CM-R-024-finding-refutation-spec-compliance.md`

---

## CM-R-025 — Intent-to-Evidence Traceability

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro preserve bidirectional traceability among intent, requirements, specifications, decisions, plans, implementation, tests/evals, and observed outcomes?

**Expected output:** traceability model, stale-artifact invalidation, orphan detection, recovered-spec links, source-target fidelity integration, and proportional-rigor rules.

**Working record:** `CM-R-025-intent-to-evidence-traceability.md`

---

## CM-R-026 — Migration, Compatibility & Cutover Engineering

**Priority:** P1; P0 for consequential/irreversible migrations
**Status:** ACCEPTED

**Question:** How should CodeMaestro plan and validate migrations across runtimes, frameworks, schemas, APIs/protocols, infrastructure, and platforms while preserving compatibility and rollback capability?

**Expected output:** inventory, characterization, reversible/dual-compatible transition, old/new comparison, cutover/rollback gates, replay/backfill semantics, reconciliation, and delayed cleanup.

**Working record:** `CM-R-026-migration-compatibility-cutover.md`

---

## CM-R-027 — Interface, Protocol & Contract Engineering

**Priority:** P1
**Status:** ACCEPTED

**Question:** How should CodeMaestro design, review, evolve, and verify consumer-facing and system-to-system contracts across APIs, RPC, events, streams, webhooks, and data/schema boundaries?

**Expected output:** semantic contract model, ownership/authority, sync/async delivery semantics, error/idempotency/retry/concurrency guidance, consumer-aware compatibility, multi-boundary verification, deprecation/evolution, misuse resistance, and eval scenarios.

**Working record:** `CM-R-027-interface-protocol-contract-engineering.md`

---

## CM-R-028 — Performance, Benchmarking & Capacity Engineering

**Priority:** P1; P0 for performance/resource-critical workloads
**Status:** ACCEPTED

**Question:** How should CodeMaestro measure, diagnose, optimize, benchmark, and capacity-plan software systems without relying on premature optimization or stale platform-specific thresholds?

**Expected output:** workload/baseline contract, profiling, benchmark reproducibility, load/stress/soak methodology, capacity/headroom/elasticity, cost-performance reasoning, regression gates, and eval scenarios.

**Working record:** `CM-R-028-performance-benchmarking-capacity-engineering.md`

---

## CM-R-029 — Cross-Runtime Portability, Capability Discovery & Conformance

**Priority:** P0
**Status:** ACCEPTED

**Question:** How should CodeMaestro preserve equivalent engineering behavior across Chat, Work, Codex, and future surfaces while capability availability, permission, execution mechanics, and connected-app support differ?

**Expected output:** runtime capability discovery, availability-vs-authorization contract, graceful degradation/recovery, handoff/evidence semantics, and cross-runtime conformance evals.

**Working record:** `CM-R-029-cross-runtime-portability-conformance.md`

---

## CM-R-030 — Product, UX/UI & Visual Interface Engineering

**Priority:** P1 by default; P0 for user-facing/product-critical work
**Status:** ACCEPTED

**Question:** How should CodeMaestro design, audit, implement, and validate user-facing software across product framing, UX, interaction, visual design, accessibility, responsive behavior, design systems, and visual/interaction QA without fabricating user research?

**Expected output:** product/UX workflow, research-integrity boundary, interaction/visual design guidance, accessibility, design-system governance, design-to-code, visual/interaction QA, and eval scenarios.

**Working record:** `CM-R-030-product-ux-ui-visual-interface-engineering.md`

---

## CM-R-031 — Build, Toolchain & Environment Engineering

**Priority:** P1 by default; P0 for consequential build/release integrity or reproducibility
**Status:** ACCEPTED

**Question:** How should CodeMaestro reason about build systems, compilers/toolchains, environment parity, reproducibility, generated artifacts, caches, cross-compilation, target platforms, and build provenance independently from CI/CD orchestration?

**Expected output:** build/toolchain discovery, pinning, environment parity, hermeticity/reproducibility, codegen/cache correctness, target-platform reasoning, provenance, debugging/performance, and eval scenarios.

**Working record:** `CM-R-031-build-toolchain-environment-engineering.md`

---

## CM-R-032 — Privacy & Data Lifecycle Engineering

**Priority:** P1 by default; P0 for personal/sensitive/high-impact data
**Status:** ACCEPTED

**Question:** How should CodeMaestro reason about privacy risk and the lifecycle of personal, sensitive, or user-derived data even where access is authorized and no cybersecurity compromise exists?

**Expected output:** data inventory/flows, purpose/use, minimization, collection boundaries, retention/deletion, backups/logs/telemetry/caches/replicas, derived/training/eval datasets, third parties, user control, privacy-by-design, and disposal.

**Working record:** `CM-R-032-privacy-data-lifecycle-engineering.md`

---

## Comparative research passes and acceptance checkpoints

- Pass 3: `2026-09-04-comparative-research-pass-3.md`
- Pass 4: `2026-09-04-comparative-research-pass-4.md`
- Pass 4 acceptance: `../architecture/2026-09-04-pass-4-acceptance-and-canonicalization.md`
- Pass 5: `2026-09-04-comparative-research-pass-5.md`
- Pass 5 acceptance / Capability Freeze: `../architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md`

## Comparative reference registry

The external reference set and study priorities are maintained in:

`COMPARATIVE-REFERENCE-REGISTRY.md`

References are research inputs, not CodeMaestro dependencies or automatic architectural authority.

## Prioritization principle

P0 research must be sufficiently resolved for the affected behaviors before the first production-quality CodeMaestro Skill is considered stable. P1 areas must be sufficiently resolved before the corresponding specialized capability/reference guidance is declared canonical for consequential use. P2 areas may be added incrementally as the Skill stabilizes.

Accepted tracks may still contain implementation-time freshness work; `ACCEPTED` means the architectural direction/track is accepted, not that every future version-sensitive question is permanently answered.
