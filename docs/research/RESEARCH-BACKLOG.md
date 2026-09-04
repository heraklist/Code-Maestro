# CodeMaestro Research Backlog

## Purpose

This backlog tracks research that must be completed before related guidance becomes canonical CodeMaestro architecture or Skill reference material.

Research findings are evidence, not automatic project decisions. Material changes to the architecture must be recorded in `docs/architecture/DECISIONS.md` and incorporated into `docs/architecture/ARCHITECTURE.md` after review.

## Status values

- `QUEUED` — identified but not started.
- `IN RESEARCH` — active evidence collection.
- `SYNTHESIS` — sources gathered; conclusions being compared.
- `REVIEW` — recommendation ready for architectural review.
- `ACCEPTED` — findings incorporated into canonical architecture/reference guidance.
- `REJECTED` — researched but not adopted.

## Authority preference

For all research:

1. official specifications and standards;
2. official product/project documentation;
3. primary repositories, release notes, advisories, and maintainers;
4. high-quality secondary technical sources where primary evidence is insufficient.

Fast-changing claims should be date/version scoped.

---

## CM-R-001 — Agent Skills and Codex engineering workflows

**Priority:** P0
**Status:** QUEUED

**Question:** What are the current authoritative design, packaging, progressive-disclosure, testing, tool-use, and workflow patterns for Agent Skills and Codex-oriented engineering work?

**Expected output:** Recommended Skill structure, trigger design, reference-loading strategy, script boundaries, eval strategy, and portability constraints for CodeMaestro.

**Preferred authorities:** OpenAI official documentation and specifications; Agent Skills specification where applicable.

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

**Expected output:** Decision framework spanning unit, integration, contract, property-based, fuzz, mutation, end-to-end, regression, and environment-specific validation without dogmatically requiring every test type everywhere.

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

**Question:** What production-readiness and observability methodology should CodeMaestro apply across logging, metrics, traces, alerting, SLOs, error budgets, incident response, rollback, and release verification?

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

**Question:** How should CodeMaestro evaluate an engineering Skill for instruction following, safety, coding quality, debugging, research, tool use, evidence honesty, and regression resistance?

**Expected output:** Eval taxonomy, baseline methodology, scoring approach, pressure scenarios, and regression suite design.

**Preferred authorities:** OpenAI official eval guidance, Agent Skills guidance/specifications, primary research where useful.

---

## CM-R-013 — Systematic debugging and root-cause analysis

**Priority:** P0
**Status:** QUEUED

**Question:** What general debugging methodology best supports evidence-first root-cause analysis across software stacks, including reproduction, hypothesis discrimination, tracing, concurrency issues, and regression prevention?

**Expected output:** Debugging workflow suitable for a core engineering reference and evaluation scenarios.

**Preferred authorities:** primary debugger/runtime guidance, established engineering literature, high-quality primary technical material.

---

## CM-R-014 — Concurrency and distributed-system review

**Priority:** P2
**Status:** QUEUED

**Question:** How should CodeMaestro identify and reason about race conditions, idempotency, ordering, retries, consistency, leases/locks, distributed transactions, queues, and failure modes?

**Expected output:** Review checklist driven by system invariants rather than technology-specific recipes.

**Preferred authorities:** primary platform documentation and established distributed-systems literature.

---

## CM-R-015 — Release and production-readiness engineering

**Priority:** P1
**Status:** QUEUED

**Question:** What evidence should CodeMaestro require or recommend before calling software release-ready or production-ready?

**Expected output:** Release-readiness model covering validation, security, migrations, observability, rollback, dependency/supply chain, configuration, and operational ownership.

**Preferred authorities:** relevant official platform guidance and established production engineering practices.

---

## CM-R-016 — Universal Language Intelligence and Experimental Language Support

**Priority:** P0
**Status:** IN RESEARCH

**Question:** How should CodeMaestro provide reliable engineering support across mainstream, niche, legacy, domain-specific, private, and experimental languages without using one permanently installed Skill per language?

**Expected output:** Language Intelligence architecture, language-profile contract, language taxonomy, maturity model, reliability levels, source hierarchy, unknown-language protocol, standalone language-skill promotion criteria, representative coverage matrix, and baseline eval design.

**Preferred authorities:** official language specifications and documentation; primary language/toolchain repositories; vendor-maintained Agent Skills where available; GitHub Linguist for discovery metadata; other catalogs only as discovery aids rather than correctness authorities.

**Working record:** `docs/research/CM-R-016-universal-language-intelligence.md`

## Prioritization principle

P0 research should be resolved before the first production-quality CodeMaestro Skill is considered stable. P1 areas should be resolved before the corresponding specialized references are declared canonical. P2 areas may be added incrementally as the Skill expands.
