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

**Rationale:** CodeMaestro is intended to support mainstream, niche, legacy, domain-specific, private, and experimental languages. A skill-per-language architecture would create unnecessary discovery/context overhead, duplicated methodology, and an unbounded maintenance surface.

**Consequences:** Engineering sub-skills remain independently safe and evidence-aware; Language Intelligence owns detection, version/toolchain discovery, maturity, source routing, profiles, reliability levels, and the unknown-language protocol; standalone language Skills require eval justification.

---

## CM-ADR-015 — Autonomous Research Lab with explicit epistemic states

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will include an autonomous Research Lab capability for technical survey, comparison, investigation, bounded experimentation, replication, and experimental evolution. Research work must preserve explicit epistemic states rather than collapsing hypotheses, observations, characterization, decisions, normative rules, implementation, and validation into one generic notion of knowledge.

**Rationale:** Experimental engineering such as the Cusp language project requires more than web search and summarization.

**Consequences:** Research findings do not automatically become canonical guidance or target-project authority; durable research artifacts and reproducible evidence are first-class when results must survive context loss or be challenged.

---

## CM-ADR-016 — Skills own methodology; runtime roles provide optional independent contexts

**Status:** Accepted — 2026-09-04

**Decision:** Reusable Skills own methodology, decision criteria, evidence contracts, and workflows. Optional runtime agent roles may provide scoped independent work when the environment safely supports subagents.

**Rationale:** Research scout, experimenter, skeptic, and replicator are useful independent perspectives, but turning every role into a permanently installed Skill would conflate reusable knowledge with execution context.

**Consequences:** Delegated output is evidence or independent judgment, not hidden authority; parent workflows review it; the design degrades safely without subagents.

---

## CM-ADR-017 — Experimental-language evolution requires a distinct authority ladder

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will use a Language Evolution Protocol that separates research pressure, observed behavior, characterization, proposal, accepted project decision, normative specification, implementation, conformance validation, and stable/released behavior.

**Rationale:** Experimental languages evolve under uncertainty, and implementation behavior or AI proposals must not silently become semantic authority.

**Consequences:** Comparative research can inform proposals but not create target-language authority. Cusp is the primary stress case for this protocol.

---

## CM-ADR-018 — Evidence provenance is captured at production/retrieval time

**Status:** Accepted — 2026-09-04

**Decision:** Material engineering and research evidence should retain provenance to the state that produced it, and source identity should be captured when evidence is retrieved or generated rather than reconstructed later from model memory.

**Rationale:** Long-running, multi-agent, or experimental work cannot be audited reliably when source/version/run identity exists only in conversational context.

**Consequences:** Provenance may include URL/path, repository SHA, tool/runtime versions, environment, commands, configuration, hashes, seeds, timestamps, and run IDs as relevant; claim strength must not exceed available provenance.

---

## CM-ADR-019 — Intent-to-evidence traceability is bidirectional

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will preserve traceability across user intent, requirements, decisions/specifications, plans, implementation, tests/evals, and observed outcomes, and may propagate implementation reality upstream when prior artifacts become stale.

**Rationale:** Forward traceability alone cannot detect specifications or approvals that no longer describe accepted code reality.

**Consequences:** Material orphaned requirements/tests, undocumented authority-sensitive behavior, and stale approved artifacts should be detectable. Stable identifiers and exact storage format remain research under CM-R-025.

---

## CM-ADR-020 — Assurance is selected by risk and property shape

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro will use an Assurance Ladder rather than requiring every testing or formal method everywhere. It chooses the least costly technique that provides the required confidence and escalates when risk, invariants, or failure consequences justify stronger assurance.

**Rationale:** Example tests, differential checks, properties, fuzzing, mutation testing, model checking, reconciliation, and formal proof observe different classes of correctness.

**Consequences:** Formal verification is never claimed unless an actual prover/checker accepts the artifact. Business/control reconciliation may serve as assurance where code execution alone cannot prove operational correctness.

---

## CM-ADR-021 — Machine-generated counterexamples are repair evidence

**Status:** Accepted — 2026-09-04

**Decision:** Compiler, type-checker, prover, fuzzer, schema-validator, model-checker, static-analysis, and conformance counterexamples are first-class evidence that can seed the next debugging or repair hypothesis.

**Rationale:** Treating machine failures only as terminal status discards high-value diagnostic evidence.

**Consequences:** Counterexamples should remain traceable to the repair and regression evidence they produce when material.

---

## CM-ADR-022 — Migrations require compatibility-aware, reversible cutover discipline

**Status:** Accepted — 2026-09-04

**Decision:** Migration work should begin with compatibility inventory and use phased, reversible, evidence-backed transition mechanisms such as expand-contract, dual-run/read/write, semantic comparison, bounded batches, explicit cutover gates, rollback triggers, and delayed cleanup when applicable.

**Rationale:** Runtime, schema, API, platform, and protocol changes often fail at compatibility and cutover boundaries rather than in isolated implementation units.

**Consequences:** CM-R-026 owns migration methodology. Replay/backfill and consumer cutover are special cases requiring explicit semantics and reconciliation where material.

---

## CM-ADR-023 — Interface and protocol contracts are first-class engineering agreements

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro treats APIs, RPC, events, streams, webhooks, schemas, and protocol boundaries as durable behavioral agreements whose semantics, ownership, failure behavior, compatibility, and deployed verification require explicit engineering treatment.

**Rationale:** Route or schema validity is insufficient to establish consumer correctness or safe evolution.

**Consequences:** CM-R-027 is opened. Contract verification distinguishes contract, provider, consumer, compatibility, and deployed boundaries. Physical Skill packaging remains eval-driven.

---

## CM-ADR-024 — Performance engineering is evidence-driven and workload-relative

**Status:** Accepted — 2026-09-04

**Decision:** Performance and capacity claims must be grounded in representative workload evidence, baseline measurements, profiling/tracing, bottleneck or saturation analysis, comparable before/after conditions, and regression evidence where material.

**Rationale:** Generic optimization recipes and isolated microbenchmarks often fail to predict end-to-end system behavior.

**Consequences:** CM-R-028 is opened. Static vendor thresholds are not canonical unless they are stable standards; current thresholds remain dynamically researched.

---

## CM-ADR-025 — Evidence conclusions are coverage-bounded and target-faithful

**Status:** Accepted — 2026-09-04

**Decision:** Evidence must record both what target/state it actually describes and what surface was actually assessed. Negative or clean conclusions apply only to the assessed surface, and substitute evidence must not be silently presented as current-target state.

**Rationale:** Authoritative information about the wrong deployment or a partial audit can otherwise be overstated into a false current-state or clean-bill-of-health claim.

**Consequences:** CM-R-020 and CM-R-025 will include target/source fidelity, assessed/unassessed/unassessable coverage, and explicit limitations in the evidence model.

---

## CM-ADR-026 — Recovered specifications have weaker authority than normative intent

**Status:** Accepted — 2026-09-04

**Decision:** When original requirements are missing, CodeMaestro may recover observed behavior/specification from implementation and runtime evidence, but it must label that artifact `RECOVERED / OBSERVED SPECIFICATION` and must not treat it as original intent or normative authority without explicit promotion by project authority.

**Rationale:** Legacy systems often preserve behavior after design intent and documentation disappear.

**Consequences:** CM-R-022 and CM-R-025 incorporate recovered-spec workflows and authority status.

---

## CM-ADR-027 — Operational closure requires user/business-boundary evidence

**Status:** Accepted — 2026-09-04

**Decision:** An alert clearing, process completion, deployment success, health endpoint, or rerun is not by itself sufficient evidence that an incident or recovery is resolved. Closure requires appropriate user/business-boundary, state/data, dependency, and stability evidence.

**Rationale:** Internal signals can recover while externally observable correctness remains degraded.

**Consequences:** CM-R-006, CM-R-009, CM-R-013, CM-R-015, CM-R-020, and CM-R-026 incorporate reconciliation/control evidence, stability windows, incident-to-resilience regression, and bounded replay/reopen gates where relevant.

---

## CM-ADR-028 — Security analysis includes misuse resistance and agentic taint flow

**Status:** Accepted — 2026-09-04

**Decision:** Secure engineering must consider whether interfaces/configuration make unsafe use easy and must trace untrusted inputs through prompts/context, agent capabilities, tools, and side effects rather than checking only direct prompt interpolation or implementation bugs.

**Rationale:** Dangerous defaults, configuration cliffs, indirect environment/log flows, and tool-mediated side effects create security failures invisible to conventional local code review.

**Consequences:** CM-R-002/003/004/008/014/023 and CM-R-027 incorporate misuse-resistance, system-invariant, and agentic taint/dataflow analysis as appropriate.

---

## CM-ADR-029 — Agent evals distinguish task, trajectory, side-effect, and evidence contracts

**Status:** Accepted — 2026-09-04

**Decision:** CodeMaestro agent/Skill evaluation will distinguish required task outcome, allowed/required trajectory, permitted side effects, and evidence required for the verdict. Hard safety/privacy/authorization invariants cannot be averaged away by higher aggregate quality scores.

**Rationale:** Final-answer quality alone cannot evaluate tool use, state mutation, authorization, recovery, or safety behavior.

**Consequences:** CM-R-012 and CM-R-020 incorporate versioned datasets, provenance, slices, comparable baselines, uncertainty, failures/timeouts, hard gates, and reviewed incident/near-miss regression cases.

---

## CM-ADR-030 — Skill discovery and loading must be fault-isolated

**Status:** Accepted — 2026-09-04

**Decision:** A future CodeMaestro Skill ecosystem must tolerate broken, stale, unreadable, conflicting, or untrusted individual Skills without making the entire capability catalog unusable.

**Rationale:** Large Skill ecosystems require explicit validation status, precedence, diagnostics, and safe exclusion rather than assuming every discovered Skill is healthy.

**Consequences:** CM-R-001, CM-R-018, and CM-R-023 study per-Skill load/validation status, precedence/conflicts, cache/snapshot freshness, diagnostics, and safe exclusion. This decision does not require CodeMaestro to reimplement the Codex loader.

---

## CM-ADR-031 — Zero paid external dependency

**Status:** Accepted — 2026-09-05

**Decision:** CodeMaestro development governance uses only capabilities included in the project's existing ChatGPT / Codex / Work subscriptions; it does not depend on paid external services or API billing. As a product property, CodeMaestro **does not require** paid API access to operate. This is not a prohibition on API use: when an authorized user or runtime already exposes additional API capability, capability discovery may use it rather than artificially degrading execution.

**Rationale:** The project must remain reproducible and operable without creating a second paid infrastructure dependency, while preserving the constitutional rule that available and authorized capability must not be ignored merely to maintain artificial parity with a weaker surface.

**Consequences:**

1. **Development governance vs product property:** repository development is constrained to subscription-provided surfaces, while the portable Skill remains tool-aware and may use optional authorized API access when present. Availability still does not imply authorization.
2. **Eval split:** deterministic checks execute in CI; model-based evals execute only in an authorized interactive session. Model inference and model grading are never CI requirements. `evals/` must make this separation explicit.
3. **Deterministic grading only:** CodeMaestro eval verdicts must not depend on an LLM-as-judge. Model-produced outputs may be inputs to evals, but acceptance grading remains deterministic and inspectable.
4. **Self-Evolution is interactive:** because material Self-Evolution requires inference, it cannot be a background or scheduled process under project governance. It is command-gated and must run inside an authorized interactive session.
5. **Quota is first-class:** invocation allowance is a design budget alongside context. Every model-based eval suite declares an invocation budget and may be distributed across quota windows without reducing corpus size, run count, or thresholds.
6. **Cross-runtime conformance is manual per surface:** Chat, Work, Codex, and future target surfaces are evaluated separately in authorized sessions; results are not averaged across surfaces.
7. **No artificial degradation:** optional capability exposed by the active authorized environment remains usable. This ADR forbids paid dependency, not capability discovery.
