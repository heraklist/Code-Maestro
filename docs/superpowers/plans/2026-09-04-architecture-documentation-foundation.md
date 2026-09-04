# Architecture Documentation Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Execution status:** COMPLETE for the original Foundation v0.1 scope.

**Scope note:** This plan governed only the initial five-file documentation foundation and its consistency review. It does **not** retroactively claim to have planned the later comparative research passes, research records, acceptance checkpoints, consolidated v3 design, Self-Evolution design, or logging-governance amendments. Those later artifacts were produced through subsequent approved architectural/research iterations and are reviewed through the current consolidated written-spec gate. A new implementation plan will be created with `writing-plans` only after that gate passes.

**Goal:** Establish the canonical documentation foundation for CodeMaestro v3 before any production Skill implementation begins.

**Architecture:** Keep the dated Superpowers design spec as a historical checkpoint and maintain separate living documents for architecture, migration inventory, decisions, and research. The repository remains implementation-free for this milestone except for documentation scaffolding.

**Tech Stack:** Markdown, GitHub repository.

**Spec:** `docs/superpowers/specs/2026-09-04-codemaestro-v3-architecture-design.md`

## Global Constraints

- Do not create `SKILL.md`, runtime references, eval implementations, scripts, or application code in this milestone.
- Do not copy secrets, `.env` values, legacy API credentials, deployment tokens, or private runtime configuration into this public repository.
- The target architecture is zero-custom-infrastructure by default.
- Preserve behavioral intent from the legacy CodeMaestro, not API parity.
- `docs/architecture/ARCHITECTURE.md` is the living architecture gateway/source-of-truth entrypoint.
- `docs/architecture/MIGRATION-INVENTORY.md` is the canonical legacy disposition ledger.
- `docs/architecture/DECISIONS.md` is the architectural decision log.
- `docs/research/RESEARCH-BACKLOG.md` is the canonical research queue/index.

---

### Task 1: Establish the living architecture source of truth

**Files:**
- Create: `docs/architecture/ARCHITECTURE.md`

**Interfaces:**
- Consumes: the approved design spec.
- Produces: the continuously maintained architectural model used by all later design and implementation work.

- [x] Write the document with product purpose, target runtime model, core principles, capability domains, evidence model, state/mutation rules, research policy, security boundaries, Skill packaging direction, evaluation strategy, and repository documentation contract.
- [x] Verify that it contains no legacy endpoint names as required runtime dependencies.
- [x] Verify that all statements marked as architectural decisions agree with the dated design spec for this milestone.
- [x] Commit the document.

**Post-plan note:** Later architecture expansion made the original body stale. During written-spec review it was converted into a canonical gateway that points to the current consolidated v2 design until full post-review canonicalization.

### Task 2: Create the migration inventory

**Files:**
- Create: `docs/architecture/MIGRATION-INVENTORY.md`

**Interfaces:**
- Consumes: legacy ZIP analysis and the repositories `GPT_CodeMaesto_API`, `codemaestro-sbox`, and `Custom-ChatGPT---Code-maesto-v2`.
- Produces: one canonical KEEP / UPGRADE / REFACTOR / RESEARCH / RETIRE ledger.

- [x] Record the disposition of the 20 legacy runtime knowledge modules.
- [x] Record the disposition of custom API, Vercel, Redis/Upstash, OpenAPI Actions, authentication, route-specific write gates, deployment packs, duplicated snapshots, and historical artifacts.
- [x] Record the behavioral safeguards that survive the infrastructure retirement.
- [x] Record legacy eval categories that should become environment-independent scenarios.
- [x] Commit the document.

### Task 3: Create the architectural decision log

**Files:**
- Create: `docs/architecture/DECISIONS.md`

**Interfaces:**
- Consumes: approved architecture discussions.
- Produces: chronological record of decisions that constrain future work.

- [x] Record the initial decisions: Skill-first architecture, zero custom infrastructure, behavioral parity over API parity, single orchestrator Skill initially, progressive disclosure, native-tool execution, evidence-before-assertion, state-before-mutation, dynamic authoritative research, and public-repository secret hygiene.
- [x] Give every decision a stable ID and status.
- [x] Record rationale and consequences, not just the chosen option.
- [x] Commit the document.

**Post-plan note:** The decision log was subsequently extended through CM-ADR-030. The dated Pass-3 checkpoint is explicitly marked historical/absorbed where it shares IDs with the canonical log.

### Task 4: Create the research backlog

**Files:**
- Create: `docs/research/RESEARCH-BACKLOG.md`

**Interfaces:**
- Consumes: unresolved design areas identified during migration analysis.
- Produces: prioritized research queue whose findings can later change architecture or references through explicit decisions.

- [x] Add research areas for Agent Skills/Codex workflows, secure software-development standards, OWASP application and agentic security, CI/CD security, software supply-chain assurance, modern testing, PostgreSQL/Supabase, MCP/tool authorization, observability/SRE, frontend accessibility/performance, cloud/container/IaC security, and coding-agent eval methodologies.
- [x] Give every item a priority, status, expected output, and authority preference.
- [x] Mark research as not yet canonical engineering guidance until reviewed and accepted.
- [x] Commit the document.

**Post-plan note:** The canonical backlog was subsequently expanded through CM-R-032 and now indexes the later accepted research records and Pass-5 Capability Freeze evidence.

### Task 5: Make the repository entrypoint useful

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: the four canonical living documents.
- Produces: concise public entrypoint pointing contributors and future agents to the actual sources of truth.

- [x] Explain CodeMaestro's new purpose without claiming unfinished capabilities.
- [x] Link the architecture, migration inventory, decisions, research backlog, and dated design spec.
- [x] State that production Skill implementation has not started yet.
- [x] State the public-repository secret rule.
- [x] Commit the update.

### Task 6: Documentation consistency verification

**Files:**
- Review: all files created or changed in Tasks 1-5.

**Interfaces:**
- Consumes: the complete documentation foundation.
- Produces: internally consistent Architecture Documentation Foundation v0.1.

- [x] Search for `TBD`, `TODO`, `implement later`, placeholder URLs, and unresolved template language; remove any occurrence that is not deliberately describing a future research status.
- [x] Verify that legacy custom infrastructure is described only as retired/reference material, never as a target dependency.
- [x] Verify that the living architecture and decision log agree on the target model for the original foundation scope.
- [x] Verify that research items are not presented as already accepted standards without review.
- [x] Verify all README links created by this milestone resolve to repository paths.
- [x] Open a draft pull request from `docs/architecture-foundation-v0.1` to `main` for review.

## Execution evidence

The initial foundation tasks are evidenced by the committed files and the open Draft PR #1. Later review identified documentation drift introduced by subsequent same-day architecture expansion; those findings are being repaired in the written-spec review phase rather than retroactively rewriting this plan as if it had covered work it did not plan.
