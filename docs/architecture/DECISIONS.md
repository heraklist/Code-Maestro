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

---

## CM-ADR-014 — Autonomous engineering sub-skills with shared Language Intelligence

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will separate autonomous engineering sub-skills from a shared Language Intelligence layer. Language coverage will be profile- and research-driven by default rather than implemented as one permanently installed Skill per language. Standalone language correction/orientation skills are promoted selectively when eval evidence shows that generic language intelligence is insufficient.

**Rationale:** CodeMaestro is intended to support mainstream, niche, legacy, domain-specific, private, and experimental languages. A skill-per-language architecture would create unnecessary discovery/context overhead, duplicated methodology, and an unbounded maintenance surface. Current official language-agent projects such as Mojo and MoonBit also demonstrate that rapidly changing languages benefit from freshness gates, correction layers, authoritative source routing, and explicit verification rather than static encyclopedic prompts.

**Consequences:**

- engineering sub-skills must define their own trigger, scope, non-goals, evidence, freshness, failure, output, and verification contracts and remain safe/correct without hidden parent behavior;
- the shared Language Intelligence subsystem will own language detection, classification, maturity, version/toolchain discovery, source-of-truth routing, reliability levels, profiles, and the unknown-language protocol;
- language profiles are references/data contracts, not automatically standalone Skills;
- standalone language skills require explicit promotion criteria and eval evidence;
- unknown languages enter a research-and-verification workflow rather than being treated as categorically unsupported;
- exact language/API/toolchain claims must not be presented at a stronger confidence level than the available local or authoritative evidence;
- the active design and open questions are tracked in `docs/research/CM-R-016-universal-language-intelligence.md`.

---

## CM-ADR-015 — Autonomous Research Lab with explicit epistemic states

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will include an autonomous Research Lab capability for technical survey, comparison, investigation, bounded experimentation, replication, and experimental evolution. Research work must preserve explicit epistemic states rather than collapsing hypotheses, observations, characterization, decisions, normative rules, implementation, and validation into one generic notion of "knowledge".

**Rationale:** Experimental engineering such as the Cusp language project requires more than web search and summarization. Reliable work needs durable hypotheses, baselines, experiment design, reproducible evidence, adversarial challenge, and a controlled path from findings to accepted project decisions.

**Consequences:**

- substantial research uses a proportional evidence-driven lifecycle;
- durable artifacts are required when results must survive context loss, be resumed, audited, reproduced, or challenged;
- research findings do not automatically become canonical CodeMaestro guidance or target-project authority;
- the Research Lab may compose with Language Intelligence and engineering sub-skills;
- exact durable artifact schemas and packaging remain research items under CM-R-017 and CM-R-020;
- the accepted design is recorded in `docs/superpowers/specs/2026-09-04-research-experimental-engineering-design.md`.

---

## CM-ADR-016 — Skills own methodology; runtime roles provide optional independent contexts

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will distinguish reusable Skills from optional runtime agent roles. Skills own methodology, decision criteria, evidence contracts, and reusable workflows. Runtime roles may be used for scoped independent work when the active environment provides safe subagent capabilities.

**Rationale:** Research scout, experimenter, skeptic, and replicator are useful independent perspectives, but modeling every role as a permanently installed Skill would conflate reusable knowledge with execution context and increase discovery/context overhead.

**Consequences:**

- candidate roles include `research-scout`, `experimentalist`, `skeptic`, and `replicator`;
- subagents provide evidence or independent judgment, not hidden project authority;
- the parent workflow reviews delegated output before accepting phase completion;
- delegation must degrade safely in environments without subagent capability;
- exact role configuration and orchestration policy remain under CM-R-018.

---

## CM-ADR-017 — Experimental-language evolution requires a distinct authority ladder

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will use a Language Evolution Protocol that explicitly separates research pressure, observed behavior, characterization, proposal, accepted project decision, normative specification, implementation, conformance validation, and stable/released behavior.

**Rationale:** Experimental languages evolve under uncertainty. Treating implementation behavior or an AI-generated proposal as semantic authority causes specification drift and can prematurely canonize accidental behavior.

**Consequences:**

- research may discover, characterize, challenge, experiment, and propose semantics but may not silently create semantic authority;
- comparative study of other languages informs alternatives and trade-offs but does not become target-language authority;
- substantive semantic proposals should include compatibility, security, resource/performance, validation, and migration considerations where material;
- Cusp is the primary stress case for this protocol;
- detailed governance research continues under CM-R-019.

---

## CM-ADR-018 — Evidence provenance is captured at production/retrieval time

**Status:** Accepted — 2026-09-04

**Decision:** Material engineering and research evidence should retain provenance to the state that produced it, and source identity should be captured when evidence is retrieved or generated rather than reconstructed later from model memory.

**Rationale:** Long-running, multi-agent, or experimental work cannot be audited reliably when source/version/run identity exists only in conversational context.

**Consequences:**

- provenance may include source URL/path, repository SHA, toolchain/runtime versions, environment, commands, configuration, input hashes, test/experiment versions, seeds, timestamps, and run IDs as relevant;
- claim strength must not exceed the evidence provenance available;
- snapshot-bound evidence from the Cusp systems is retained as a generalized design principle even though the custom APIs themselves are not migrated;
- the exact claim/evidence ledger and citation/reproducibility model remain under CM-R-020.
