# CodeMaestro Architecture Decision Log

## Purpose

This file records accepted architectural decisions that constrain future CodeMaestro work.

Each decision has a stable ID, status, rationale, and consequences. If a later decision supersedes an earlier one, both remain in the log and the living `ARCHITECTURE.md` is updated to reflect the current state.

---

## CM-ADR-001 — Rebuild as a Skill-first system

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will be rebuilt as a portable software-engineering Skill rather than maintained as a Custom GPT product.

**Rationale:** The valuable part of the legacy system is its engineering methodology, safety model, validation discipline, and domain playbooks. Custom GPT packaging is no longer the desired product boundary.

**Consequences:** New work targets Skill architecture and reusable references/evals. GPT Builder-specific packaging becomes migration history only.

---

## CM-ADR-002 — Zero custom runtime infrastructure by default

**Status:** Accepted — 2026-09-04

**Decision:** The target CodeMaestro architecture will not require a CodeMaestro-specific API, Vercel gateway, Redis/Upstash store, custom Action authentication, or OpenAPI Actions contract.

**Rationale:** Native capabilities can provide repository, execution, research, and platform access without maintaining a parallel middleware product. The enduring value lies in policy and methodology, not the transport layer.

**Consequences:** `GPT_CodeMaesto_API` and `codemaestro-sbox` become reference-only systems. Their useful safeguards are absorbed or generalized at the Skill level.

---

## CM-ADR-003 — Behavioral parity over API parity

**Status:** Accepted — 2026-09-04

**Decision:** Migration success is measured by preservation or improvement of useful behavior, not by recreating legacy endpoints or operation IDs.

**Rationale:** Endpoint parity would preserve obsolete implementation constraints and reduce portability.

**Consequences:** Legacy tests must be rewritten around engineering behavior, authorization, evidence, and outcomes rather than HTTP routes.

---

## CM-ADR-004 — One orchestrator Skill initially

**Status:** Accepted — 2026-09-04

**Decision:** Start with one `codemaestro` orchestrator Skill supported by focused references rather than multiple overlapping CodeMaestro skills.

**Rationale:** A single router preserves one engineering identity, one evidence model, one safety model, and composable workflows without trigger overlap or duplicated guidance.

**Consequences:** Specialized domains live in references. Splitting into multiple skills is reconsidered only if evals show discovery, context, or routing problems that cannot be solved cleanly inside one orchestrator.

---

## CM-ADR-005 — Progressive disclosure is mandatory

**Status:** Accepted — 2026-09-04

**Decision:** `SKILL.md` will remain a concise orchestrator. Heavy, specialized, or fast-changing guidance belongs in focused references, with scripts only for deterministic helpers that justify their maintenance cost.

**Rationale:** The legacy pattern of very large instructions plus many static knowledge files is harder to maintain and wastes context.

**Consequences:** Future design work must explicitly decide whether guidance belongs in the Skill core, a reference, research, a script, or an eval.

---

## CM-ADR-006 — Tool-independent methodology, native-tool execution

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro workflows are expressed in terms of capabilities such as inspect repository state, modify files, run validation, inspect CI, or research documentation. Actual execution uses whatever authorized native tools exist in the active environment.

**Rationale:** This makes CodeMaestro portable across ChatGPT, Codex, repository connectors, uploaded artifacts, and future execution environments.

**Consequences:** The Skill must discover capability availability and degrade truthfully when a capability is absent. It must not encode CodeMaestro-specific endpoint names as workflow requirements.

---

## CM-ADR-007 — Evidence before assertion

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro may not claim current state, execution, validation, deployment, or success without corresponding evidence.

**Rationale:** Capability and validation truthfulness are core differentiators inherited from the legacy system.

**Consequences:** The evidence status vocabulary becomes a first-class contract, and evals must include pressure cases that tempt the agent to overclaim.

---

## CM-ADR-008 — State before mutation

**Status:** Accepted — 2026-09-04

**Decision:** Relevant current state should be observed with a trusted authorized capability before consequential mutation whenever possible.

**Rationale:** This protects against stale assumptions, concurrent changes, wrong targets, and unintended scope expansion.

**Consequences:** The legacy Repository State Gate is generalized to repositories, local workspaces, databases, package state, configuration, and deployment targets.

---

## CM-ADR-009 — Dynamic authoritative research for fast-changing guidance

**Status:** Accepted — 2026-09-04

**Decision:** Stable principles may be encoded locally, but version-sensitive, current, unfamiliar, or security-critical implementation guidance should be verified from authoritative sources when material.

**Rationale:** Static knowledge ages quickly and can turn previously correct guidance into unsafe or incompatible advice.

**Consequences:** Research becomes part of the operating model, not an optional add-on. Research findings that materially change architecture must flow through the decision process before becoming canonical.

---

## CM-ADR-010 — Composable intent routing

**Status:** Accepted — 2026-09-04

**Decision:** Legacy operation modes are retained as useful concepts but are no longer mutually exclusive execution modes. CodeMaestro composes workflows from the concerns present in the request.

**Rationale:** Real engineering tasks frequently combine debugging, database work, security, repository mutation, testing, and delivery.

**Consequences:** The future router must identify relevant domains and load corresponding references without forcing a single-mode classification.

---

## CM-ADR-011 — The repository is canonical project memory

**Status:** Accepted — 2026-09-04

**Decision:** Architecture, migration state, accepted decisions, research backlog, dated specs, and implementation plans are persisted in `heraklist/Code-Maestro` rather than relying on conversation history.

**Rationale:** The project is long-running and will involve multiple research and design passes.

**Consequences:** Important decisions made in conversation must be incorporated into repository documentation. `docs/architecture/ARCHITECTURE.md` remains the living source of truth.

---

## CM-ADR-012 — Public repository secret hygiene

**Status:** Accepted — 2026-09-04

**Decision:** The public CodeMaestro repository must contain no secret values, active credentials, private environment configuration, legacy tokens, or copied `.env` material.

**Rationale:** Legacy packages include deployment-oriented configuration that is irrelevant to the new Skill and unsafe to migrate into a public repository.

**Consequences:** Secret-bearing legacy artifacts are excluded from migration. Active credentials associated with retired infrastructure should be rotated or revoked during decommissioning.

---

## CM-ADR-013 — Evals are a first-class development mechanism

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro Skill behavior will be developed and upgraded against explicit baseline and regression scenarios rather than prose review alone.

**Rationale:** The legacy project already contains useful safety and capability tests, and Skill guidance is only trustworthy when it changes observed behavior reliably.

**Consequences:** Before production Skill guidance is written for major behaviors, baseline failure scenarios should be captured. Legacy endpoint-specific tests are converted to environment-independent behavioral evals.
