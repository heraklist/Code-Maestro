# Comparative Research Pass 5 — Capability Closure, Runtime Portability, Product/UI, Build, and Privacy

**Date:** 2026-09-04
**Status:** ACCEPTED — architectural findings were explicitly approved before the written-spec review.

## Purpose

Pass 5 was the final breadth-oriented comparative research pass for the first-generation CodeMaestro v3 capability model. Its purpose was not to keep expanding the taxonomy, but to test whether material engineering responsibilities remained uncovered after Passes 1–4 and to identify the smallest justified additions before Capability Freeze.

This record exists to make the previously conversation-only Pass 5 evidence durable and reviewable.

## Scope and stopping rule

The pass asked four questions:

1. Does cross-runtime portability require its own research contract beyond generic tool independence?
2. Is Product/UX/UI engineering sufficiently distinct to remain a canonical capability family?
3. Is build/toolchain/environment correctness distinct from CI/CD and general implementation?
4. Is privacy/data-lifecycle engineering distinct enough from security to require a separate capability family?

It also tested whether Developer Experience, documentation, monorepo/workspace engineering, telemetry, or further public Skills justified additional top-level families.

Stopping rule:

> If remaining concerns can be expressed cleanly as composed domain profiles, shared intelligence, or cross-cutting workflows, breadth expansion stops and the architecture moves to eval-driven stabilization.

---

## Authoritative source set

The architectural conclusions below are grounded primarily in current authoritative sources. Source identity and retrieval date are captured here because CM-ADR-018 requires provenance at retrieval/production time.

### OpenAI / Agent Skills portability and surface capability

1. OpenAI — Build skills
   - URL: https://learn.chatgpt.com/docs/build-skills
   - Legacy redirect observed from: https://developers.openai.com/codex/skills
   - Accessed: 2026-09-04
   - Relevance: current Skill construction and OpenAI Skill surface guidance.

2. Agent Skills specification
   - URL: https://agentskills.io/specification
   - Accessed: 2026-09-04
   - Relevance: portable Skill structure and progressive disclosure baseline.

3. OpenAI — Plugins in ChatGPT and Codex
   - URL: https://help.openai.com/en/articles/20001256-plugins-in-codex/
   - Accessed: 2026-09-04
   - Relevance: plugins can package skills/apps/app templates; availability depends on plan, workspace, role, region, surface, and included capabilities; installation does not bypass app/provider/workspace authorization.

4. OpenAI — Apps in ChatGPT
   - URL: https://help.openai.com/en/articles/11487775
   - Accessed: 2026-09-04
   - Relevance: Plugin Directory migration and separation between packaged workflow capability and connected-app authorization.

### Build / reproducibility

5. Reproducible Builds — Definition
   - URL: https://reproducible-builds.org/docs/definition/
   - Accessed: 2026-09-04
   - Relevance: reproducible builds require the same source code, relevant build environment, and build instructions to recreate bit-for-bit identical specified artifacts.

### Privacy engineering

6. NIST — Privacy Engineering
   - URL: https://www.nist.gov/privacy-engineering
   - Accessed: 2026-09-04
   - Relevance: privacy engineering is treated as a systems-engineering discipline addressing privacy risk, distinct from merely preventing cybersecurity compromise.

7. NIST — About Privacy Engineering
   - URL: https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/about
   - Accessed: 2026-09-04
   - Relevance: privacy engineering focuses on removing conditions that create problems for people when systems process their information.

8. NISTIR 8062 — An Introduction to Privacy Engineering and Risk Management in Federal Information Systems
   - URL: https://www.nist.gov/publications/introduction-privacy-engineering-and-risk-management-federal-information-systems
   - DOI: https://doi.org/10.6028/NIST.IR.8062
   - Accessed: 2026-09-04
   - Relevance: privacy engineering objectives and privacy-risk modeling.

9. NIST CSRC Glossary — systems privacy engineering
   - URL: https://csrc.nist.gov/glossary/term/systems_privacy_engineering
   - Accessed: 2026-09-04
   - Relevance: privacy requirements are integrated into systems through purposeful design/configuration; systems privacy engineering is a specialty discipline of systems engineering.

### Product / accessibility

10. W3C WAI — WCAG 2.2 Approved as an ISO Standard
    - URL: https://www.w3.org/WAI/news/2025-10-21/wcag22-iso/
    - Accessed: 2026-09-04
    - Relevance: WCAG 2.2 is ISO/IEC 40500:2025, supporting accessibility as a current product/UI engineering requirement rather than an optional style concern.

### Observability / telemetry semantics

11. OpenTelemetry — Semantic Conventions
    - URL: https://opentelemetry.io/docs/specs/semconv/
    - Version observed: 1.44.0
    - Accessed: 2026-09-04
    - Relevance: telemetry benefits from shared semantic attributes and versioned conventions.

12. OpenTelemetry — How to write semantic conventions
    - URL: https://opentelemetry.io/docs/specs/semconv/how-to-write-conventions/
    - Accessed: 2026-09-04
    - Relevance: attributes that may contain PII/sensitive data should be explicitly identified; sensitive/expensive/verbose attributes should generally be opt-in.

13. OpenTelemetry — URL semantic conventions
    - URL: https://opentelemetry.io/docs/specs/semconv/url/
    - Accessed: 2026-09-04
    - Relevance: credentials must not be recorded; known sensitive query data should be scrubbed.

---

## Supplementary comparative sources

Pass 5 also used comparative Skill/agent repositories and user-provided/file-retrieved reference material to test boundaries and workflow composition. During the original pass, exact upstream commit SHAs were not consistently persisted before CM-ADR-018 was fully operationalized.

Those comparative materials therefore have **weaker provenance authority** than the authoritative sources above and are used only as supporting pattern evidence, not as the sole basis for a canonical claim.

Patterns sampled included:

- spec-driven development and quality-constraint workflows;
- progressive-disclosure Skill construction;
- durable state over transient context;
- fresh-context review;
- bounded capability manifests/fail-closed capability scope;
- product/design Skill structures and visual/accessibility critique.

This limitation is explicit and coverage-bounds the claims of this record.

---

# Findings

## Finding 1 — Cross-runtime portability needs an explicit conformance research track

The existing principle “tool-independent methodology, tool-aware execution” is necessary but insufficient by itself. Current OpenAI product behavior makes a second distinction material:

```text
capability packaged/discoverable
!=
capability available on this surface/account/workspace
!=
capability authorized for this task
```

A portable Skill therefore requires explicit capability discovery, graceful degradation, handoff semantics, and cross-runtime conformance testing.

### Accepted disposition

Open **CM-R-029 — Cross-Runtime Portability, Capability Discovery & Conformance** at P0.

Canonical invariant:

> Equivalent available-and-authorized capabilities should produce equivalent engineering behavior across supported surfaces; the surface label must not impose an artificial downgrade.

---

## Finding 2 — Product / UX / UI Engineering remains a real canonical family

Product/UI work has distinct correctness boundaries that are not reducible to implementation alone:

```text
render correctness
+ interaction correctness
+ accessibility
+ visual fidelity
+ user-flow correctness
```

Research integrity is also distinct: heuristic/expert critique is not observed user research, and CodeMaestro must not invent participants, observations, consent, or quotes.

### Accepted disposition

Retain **Product / UX / UI Engineering** as a canonical capability family and open **CM-R-030** for its detailed methodology.

Default priority P1, promoted to P0 for user-facing/product-critical work.

---

## Finding 3 — Build, Toolchain & Environment Engineering is distinct from CI/CD

A pipeline can be configured correctly while the build itself remains environment-dependent, non-reproducible, incorrectly pinned, cache-corrupted, or target-incompatible.

The missing responsibility includes:

- build-system discovery/configuration;
- compiler/linker/toolchain versions;
- environment parity;
- hermeticity/reproducibility;
- generated artifact/codegen drift;
- build caches and cache correctness;
- cross-compilation/target platforms;
- build provenance;
- build debugging and performance.

### Accepted disposition

Retain **Build, Toolchain & Environment Engineering** as a canonical family and open **CM-R-031**.

Default priority P1, promoted to P0 where build/release integrity or reproducibility is consequential.

---

## Finding 4 — Privacy & Data Lifecycle Engineering is distinct from Security & Trust Engineering

Security primarily asks whether access/use is authorized and protected against compromise or misuse. Privacy also asks whether data should exist in a location or flow at all, for what purpose, for how long, how it propagates, whether it can be deleted, and what harm may arise from authorized processing.

Distinct privacy/data-lifecycle responsibilities include:

- data inventory and flow mapping;
- purpose/use boundaries;
- minimization;
- collection boundaries;
- retention/deletion/archival;
- backups/logs/analytics/telemetry/caches/replicas;
- vector indexes and derived/training/eval datasets;
- exports/third parties/cross-system propagation;
- de-identification/re-identification;
- user control/selective disclosure;
- privacy-by-design and disposal.

### Accepted disposition

Add **Privacy & Data Lifecycle Engineering** as a canonical family and open **CM-R-032**.

Default priority P1; promote to P0 for personal/sensitive/high-impact data or consequential profiling/data use.

Exact legal requirements remain jurisdiction- and time-sensitive research rather than hardcoded global law.

---

## Finding 5 — System Intelligence is a real Shared Intelligence layer

Language Intelligence answers what language/toolchain applies. Repository/Workspace Intelligence answers how this implementation is organized and what its blast radius is. A separate reusable question remains:

> What kind of software system is this, and what execution/deployment/state model follows from that system type?

### Accepted disposition

Promote **System Intelligence** to Shared Intelligence.

---

## Finding 6 — Requirements belong inside the first architecture family

Requirements are not a separate public Skill/family. Intent, requirements, architecture, implementation, tests, and evidence need a continuous traceability chain.

### Accepted disposition

Rename the first family to:

**Requirements, Architecture & Systems Engineering**.

---

## Finding 7 — Workspace/monorepo engineering belongs in Repository Intelligence

Monorepo and multi-repo reasoning is primarily about dependency topology, reverse-dependency closure, affected validation scope, package/service ownership, and blast radius.

### Accepted disposition

Keep it in **Repository / Workspace Intelligence** rather than creating another family.

---

## Finding 8 — Telemetry engineering deepens Reliability/Observability rather than creating another family

Telemetry design includes semantic conventions, schema/version stability, signal selection, cardinality, cost, PII/privacy, sampling, correlation, dashboard/alert compatibility, and telemetry migration.

### Accepted disposition

Deepen **Reliability, Observability, SRE & Incident Engineering** with explicit Telemetry Engineering.

---

## Finding 9 — Developer Experience is a composed domain profile

Developer Experience commonly composes:

```text
Product/UI
+ Interfaces/Contracts
+ Build/Environment
+ Platform/Delivery
+ Documentation workflows
```

### Accepted disposition

Do not create a DX family or public Skill.

---

## Finding 10 — Documentation is a cross-cutting workflow

Human-facing docs, agent-facing instructions, API docs, ADRs, examples, docs↔code drift, stale references, and examples-as-tests are important but cut across several capability families.

### Accepted disposition

Do not create a Documentation family. Keep explicit documentation/knowledge-maintenance workflows cross-cutting.

---

## Finding 11 — A bounded Task Capability Manifest improves consequential execution

For consequential/high-autonomy tasks, an explicit task-scoped capability manifest can make effective authority inspectable:

```text
host capability
∩ host permission
∩ user/task authority
∩ safety/risk policy
=
effective authority
```

The manifest may restrict but never grant authority.

### Accepted disposition

Adopt the **Task Capability Manifest** as proportional governance machinery, not as a new Skill/family.

---

# Final capability disposition

Pass 5 closes the first-generation taxonomy at **17 canonical engineering capability families**:

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

Shared Intelligence after Pass 5:

- Language Intelligence
- System Intelligence
- Repository / Workspace Intelligence
- Context / Long-Horizon Intelligence
- Research / Freshness Intelligence
- Evidence / Provenance Intelligence
- Intent-to-Evidence Traceability

---

# Research-track disposition

```text
CM-R-029  Cross-Runtime Portability, Capability Discovery & Conformance   ACCEPT / P0
CM-R-030  Product, UX/UI & Visual Interface Engineering                  ACCEPT / P1 default
CM-R-031  Build, Toolchain & Environment Engineering                     ACCEPT / P1 default
CM-R-032  Privacy & Data Lifecycle Engineering                           ACCEPT / P1 default
```

No CM-R-033 is opened by this pass.

---

# Capability Freeze recommendation

The remaining uncovered concerns are adequately expressible as existing families, Shared Intelligence, composed domain profiles, or cross-cutting workflows.

Therefore Pass 5 recommends **Capability Freeze** for the first-generation architecture:

```text
SYNTHESIZE
-> SPECIFY
-> RED EVALS
-> IMPLEMENT
-> STABILIZE
-> VALIDATE
```

Post-freeze, a new top-level family requires evidence from a real task/eval failure showing that existing boundaries cannot express the responsibility cleanly.

This is a coverage-bounded conclusion: it applies to the source landscape and engineering responsibilities assessed through Passes 1–5 and does not claim that no future engineering domain can ever justify a new family.

---

## Limitations

1. Some supplementary comparative-repository material from the original interactive Pass 5 lacks exact upstream SHA provenance. It is therefore secondary evidence only.
2. Product/platform behavior is fast-moving and must be reverified at implementation time.
3. The pass establishes architecture and research tracks, not production Skill packaging.
4. Capability Freeze is an eval-reopenable governance rule, not a claim of permanent universal completeness.
