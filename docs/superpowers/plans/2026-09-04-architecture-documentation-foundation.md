# Architecture Documentation Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish the canonical documentation foundation for CodeMaestro v3 before any production Skill implementation begins.

**Architecture:** Keep the dated Superpowers design spec as a historical checkpoint and maintain separate living documents for architecture, migration inventory, decisions, and research. The repository remains implementation-free for this milestone except for documentation scaffolding.

**Tech Stack:** Markdown, GitHub repository.

**Spec:** `docs/superpowers/specs/2026-09-04-codemaestro-v3-architecture-design.md`

## Global Constraints

- Do not create `SKILL.md`, runtime references, eval implementations, scripts, or application code in this milestone.
- Do not copy secrets, `.env` values, legacy API credentials, deployment tokens, or private runtime configuration into this public repository.
- The target architecture is zero-custom-infrastructure by default.
- Preserve behavioral intent from the legacy CodeMaestro, not API parity.
- `docs/architecture/ARCHITECTURE.md` is the living architecture source of truth.
- `docs/architecture/MIGRATION-INVENTORY.md` is the canonical legacy disposition ledger.
- `docs/architecture/DECISIONS.md` is the architectural decision log.
- `docs/research/RESEARCH-BACKLOG.md` is the canonical queue for unresolved research questions.

---

### Task 1: Establish the living architecture source of truth

**Files:**
- Create: `docs/architecture/ARCHITECTURE.md`

**Interfaces:**
- Consumes: the approved design spec.
- Produces: the continuously maintained architectural model used by all later design and implementation work.

- [ ] Write the document with product purpose, target runtime model, core principles, capability domains, evidence model, state/mutation rules, research policy, security boundaries, Skill packaging direction, evaluation strategy, and repository documentation contract.
- [ ] Verify that it contains no legacy endpoint names as required runtime dependencies.
- [ ] Verify that all statements marked as architectural decisions agree with the dated design spec.
- [ ] Commit the document.

### Task 2: Create the migration inventory

**Files:**
- Create: `docs/architecture/MIGRATION-INVENTORY.md`

**Interfaces:**
- Consumes: legacy ZIP analysis and the repositories `GPT_CodeMaesto_API`, `codemaestro-sbox`, and `Custom-ChatGPT---Code-maesto-v2`.
- Produces: one canonical KEEP / UPGRADE / REFACTOR / RESEARCH / RETIRE ledger.

- [ ] Record the disposition of the 20 legacy runtime knowledge modules.
- [ ] Record the disposition of custom API, Vercel, Redis/Upstash, OpenAPI Actions, authentication, route-specific write gates, deployment packs, duplicated snapshots, and historical artifacts.
- [ ] Record the behavioral safeguards that survive the infrastructure retirement.
- [ ] Record legacy eval categories that should become environment-independent scenarios.
- [ ] Commit the document.

### Task 3: Create the architectural decision log

**Files:**
- Create: `docs/architecture/DECISIONS.md`

**Interfaces:**
- Consumes: approved architecture discussions.
- Produces: chronological record of decisions that constrain future work.

- [ ] Record the initial decisions: Skill-first architecture, zero custom infrastructure, behavioral parity over API parity, single orchestrator Skill initially, progressive disclosure, native-tool execution, evidence-before-assertion, state-before-mutation, dynamic authoritative research, and public-repository secret hygiene.
- [ ] Give every decision a stable ID and status.
- [ ] Record rationale and consequences, not just the chosen option.
- [ ] Commit the document.

### Task 4: Create the research backlog

**Files:**
- Create: `docs/research/RESEARCH-BACKLOG.md`

**Interfaces:**
- Consumes: unresolved design areas identified during migration analysis.
- Produces: prioritized research queue whose findings can later change architecture or references through explicit decisions.

- [ ] Add research areas for Agent Skills/Codex workflows, secure software-development standards, OWASP application and agentic security, CI/CD security, software supply-chain assurance, modern testing, PostgreSQL/Supabase, MCP/tool authorization, observability/SRE, frontend accessibility/performance, cloud/container/IaC security, and coding-agent eval methodologies.
- [ ] Give every item a priority, status, expected output, and authority preference.
- [ ] Mark research as not yet canonical engineering guidance until reviewed and accepted.
- [ ] Commit the document.

### Task 5: Make the repository entrypoint useful

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: the four canonical living documents.
- Produces: concise public entrypoint pointing contributors and future agents to the actual sources of truth.

- [ ] Explain CodeMaestro's new purpose without claiming unfinished capabilities.
- [ ] Link the architecture, migration inventory, decisions, research backlog, and dated design spec.
- [ ] State that production Skill implementation has not started yet.
- [ ] State the public-repository secret rule.
- [ ] Commit the update.

### Task 6: Documentation consistency verification

**Files:**
- Review: all files created or changed in Tasks 1-5.

**Interfaces:**
- Consumes: the complete documentation foundation.
- Produces: internally consistent Architecture Documentation Foundation v0.1.

- [ ] Search for `TBD`, `TODO`, `implement later`, placeholder URLs, and unresolved template language; remove any occurrence that is not deliberately describing a future research status.
- [ ] Verify that legacy custom infrastructure is described only as retired/reference material, never as a target dependency.
- [ ] Verify that the living architecture and decision log agree on the target model.
- [ ] Verify that research items are not presented as already accepted standards.
- [ ] Verify all README links resolve to repository paths.
- [ ] Open a draft pull request from `docs/architecture-foundation-v0.1` to `main` for review.
