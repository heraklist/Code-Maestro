# CodeMaestro Context, Repository, and Evidence Hardening Design

**Status:** Accepted design checkpoint
**Date:** 2026-09-04
**Scope:** Architecture and research only. No production Skill implementation is authorized by this document.

## 1. Purpose

This design records the accepted conclusions from the second comparative research pass across agent-skill, evaluation, context-engineering, security-audit, orchestration, and repository-analysis systems.

The objective is not to add more Skills by enumeration. The objective is to strengthen CodeMaestro's core operating model with a small set of reusable mechanisms that improve long-horizon reliability, repository understanding, evidence quality, third-party skill safety, and evaluation rigor.

## 2. Accepted architecture extensions

### 2.1 Context & Long-Horizon Intelligence

CodeMaestro requires an explicit context-engineering layer for long-running engineering and research work.

It must reason about:

- what belongs in active context;
- what should be loaded just-in-time;
- what can be compacted or discarded;
- what must survive compaction;
- what belongs in durable files rather than conversation history;
- what raw evidence must not be replaced by a lossy summary;
- what state is shared across agents and what must remain isolated;
- when context has become stale, poisoned, contradictory, or too large to use reliably.

Durable state must be preferred over chat-only memory for work that must survive context loss, handoff, resumption, replication, or audit.

### 2.2 Harness surface model

Autonomous and experimental workflows should classify control surfaces as:

- **LOCKED** — evaluators, acceptance criteria, normative tests, safety rules, merge policy, or other surfaces the active optimizer must not change and then use to approve itself;
- **EDITABLE** — the code, prompt, skill, configuration, experiment, or candidate artifact intentionally under change;
- **APPEND-ONLY** — results, failures, rejected hypotheses, lineage, experiment ledgers, and evidence histories;
- **HUMAN-CONTROLLED** — merge, production promotion, credential/permission expansion, evaluator changes, semantic authority changes, or other decisions reserved for explicit human authorization.

The exact enforcement mechanism is environment-dependent, but the reasoning boundary is part of CodeMaestro methodology.

### 2.3 Lowest-rung improvement principle

Recurring failures should be corrected at the lowest architectural layer capable of expressing the fix.

The improvement ladder is:

1. instruction/prompt;
2. structured context/reference;
3. context mechanism or routing;
4. workflow;
5. harness/control system;
6. optimizer/self-improvement mechanism.

CodeMaestro must not redesign a workflow or harness when a narrower freshness, context, or reference correction resolves the failure.

Self-modification is not accepted merely because the system reports improvement. Promotion requires external evidence and protected evaluators.

### 2.4 Repository Comprehension before judgment

CodeMaestro must distinguish repository comprehension from review, audit, debugging, refactoring, or remediation.

For unfamiliar or materially complex codebases, the preferred sequence is:

```text
UNDERSTAND
→ MODEL ASSUMPTIONS / BOUNDARIES / FLOWS
→ IDENTIFY OPEN QUESTIONS
→ ONLY THEN JUDGE, CHANGE, OR HUNT FOR DEFECTS
```

Repository comprehension may map:

- topology and modules;
- entry points and execution flows;
- state/data ownership;
- public and internal boundaries;
- invariants and assumptions;
- callers/callees and dependency relations;
- tests and validation paths;
- build/CI/deployment paths;
- external systems;
- unresolved ambiguities.

A comprehension-only pass should not manufacture findings, severities, fixes, or redesign proposals unless the user requested those phases as well.

### 2.5 Impact / blast-radius gate

Before consequential changes to shared or high-connectivity behavior, CodeMaestro should inspect downstream and upstream impact using the strongest available evidence.

High-value triggers include:

- shared/public APIs;
- schemas and migrations;
- central abstractions;
- dependency/toolchain upgrades;
- concurrency/transaction behavior;
- authentication/authorization boundaries;
- widely reused functions or types;
- configuration or deployment interfaces.

The method is tool-independent. Graph analysis may improve navigation when available, but current source, executable behavior, tests, and verified configuration remain stronger evidence than derived repository graphs.

### 2.6 Finding verification and refutation lifecycle

A candidate finding is not a confirmed finding.

For material findings, especially security, correctness, concurrency, specification, migration, and high-severity review findings, use a lifecycle such as:

```text
CANDIDATE CLAIM
→ EXACT FAILURE/DEFECT CLAIM
→ SUPPORTING EVIDENCE
→ COUNTER-EVIDENCE SEARCH
→ REFUTATION ATTEMPT
→ REPRODUCTION / VERIFICATION WHEN POSSIBLE
→ VERIFIED / REJECTED / UNDECIDABLE / PARTIAL
→ REPORT
```

Pattern resemblance is not proof. Similar vulnerabilities elsewhere are not proof. Severity is consequence under the actual threat/execution model, not how dangerous a line looks.

Independent or fresh-context verification should be preferred when the cost is justified and the environment supports it.

### 2.7 Spec-to-Code Compliance capability

When an authoritative specification, design contract, protocol, requirement set, or normative project document exists, CodeMaestro should be able to compare intended behavior against implementation explicitly.

Useful per-requirement verdicts include:

- `IMPLEMENTED`
- `PARTIAL`
- `CONTRADICTED`
- `STRONGER_THAN_SPEC`
- `ABSENT`
- `UNDECIDABLE`
- `NOT_CHECKED`

The reverse direction also matters: implementation behavior may exist without documentation or normative authority.

This capability is especially important for experimental-language engineering, protocol work, schema/contracts, migrations, and Cusp specification/conformance work.

### 2.8 Third-party Skill / Plugin Supply-Chain Gate

External Skills, plugins, prompts, scripts, repositories, and marketplaces are untrusted research inputs until reviewed.

Before importing or materially reproducing third-party behavior, CodeMaestro should consider:

1. provenance and repository identity;
2. license and reuse constraints;
3. prompt-injection / instruction-hijacking content;
4. scripts and executable code;
5. file-system and network behavior;
6. credential/secrets access;
7. dependency and package risks;
8. obfuscation or hidden payloads;
9. declared tool/permission scope;
10. behavioral quality and eval evidence;
11. what to adopt, adapt, reject, or research further.

The default migration method is mechanism extraction and independent redesign, not copy-paste composition.

### 2.9 Agent Role Contract

Every optional runtime agent role should define:

- purpose;
- capabilities;
- knowledge scope;
- authority;
- explicit boundaries/non-goals;
- inputs;
- outputs;
- success criteria;
- verification responsibility;
- escalation path.

Candidate roles such as `research-scout`, `experimentalist`, `skeptic`, and `replicator` remain roles under study, not automatically standalone Skills.

### 2.10 Handoff Contract

Every material agent/phase handoff should define:

- trigger;
- source;
- destination;
- payload;
- evidence/provenance included;
- acknowledgement or completion signal;
- unresolved risks/open questions;
- user-visible behavior where relevant.

Recovery strategies include retry, fallback, escalation, graceful degradation, and compensation/rollback where meaningful.

## 3. Evaluation architecture extension

CodeMaestro Skill evaluation should be layered rather than reduced to one score.

### Stage A — Structural / Skill Health

Deterministic checks where possible:

- valid frontmatter and identity;
- line/context budget;
- internal references resolve;
- required contracts/sections exist where applicable;
- stale/unsupported claims are flagged;
- eval fixtures exist for claimed high-risk behavior.

### Stage B — Routing / Activation

Measure whether the correct Skill or capability activates:

- positive activation cases;
- near-neighbor confusion cases;
- explicit negative controls;
- top-1/top-k routing where relevant;
- routing regressions after description changes.

Skill descriptions are treated as executable routing surfaces, not merely documentation.

### Stage C — Behavioral Effectiveness

Compare with and without the Skill/capability on representative tasks.

Measure, where meaningful:

- task success;
- correctness;
- evidence honesty;
- safety;
- token/context cost;
- runtime/cost;
- unnecessary tool calls;
- regression rate.

Use negative controls to detect tests that reward generic verbosity or irrelevant guidance.

### Stage D — Composition

Evaluate pairs and groups of Skills/capabilities:

- additive vs conflicting behavior;
- ordering effects;
- duplicated guidance;
- context overload;
- cross-skill handoff quality;
- whether one Skill suppresses or contaminates another.

### Evaluation rules

- deterministic verification before LLM judgment;
- human review is valid when the target property is inherently subjective;
- thresholds follow baseline/calibration rather than arbitrary green numbers;
- every automated metric should have at least one deliberately broken case proving it can fail;
- goldens and schemas should avoid silent drift;
- evaluator changes require revalidation and should not be silently modified by the artifact under evaluation;
- important benchmark claims preserve configs, versions, seeds/replications where relevant, raw outputs, and repository state.

## 4. Capability-risk extension

Read-only does not always mean consequence-free.

CodeMaestro should distinguish at least:

- read-only/local/no material cost;
- read-only but privacy-sensitive;
- read-only but compute/cost-bearing;
- reversible mutation;
- consequential/irreversible mutation;
- authority-changing actions.

Large model evaluations, cloud experiments, GPU workloads, broad repository scans, and other expensive operations may require explicit cost awareness even when they do not mutate production state.

Exact confirmation policy remains environment-specific and under capability/tool governance research.

## 5. New research tracks

The accepted design opens four P0 research tracks:

- **CM-R-021 — Context Engineering & Long-Horizon State**
- **CM-R-022 — Repository Comprehension, Impact & Architecture Drift**
- **CM-R-023 — Skill/Plugin Security & Capability Supply Chain**
- **CM-R-024 — Finding Verification, Refutation & Spec-to-Code Compliance**

Existing tracks are extended:

- **CM-R-012** adds skill health, routing, effectiveness, composition, negative controls, ablation, calibration, and deterministic-first evaluation.
- **CM-R-018** adds formal agent-role, handoff, recovery, and authority contracts.
- **CM-R-020** remains the provenance/evidence foundation for durable context, research, findings, and evaluation artifacts.

## 6. Reference projects promoted for deeper study

High-value references from this pass include:

- `muratcankoylan/Agent-Skills-for-Context-Engineering`
- `trailofbits/skills`
- `gohypergiant/agent-skills`
- `google/skills`
- `abhigyanpatwari/GitNexus`
- the previously tracked OpenAI, Superpowers, Microsoft, Cusp, language-governance, research-lab, and grounded-evidence references.

These remain research references, not dependencies or automatic authority.

## 7. Non-decisions

This checkpoint does **not** decide:

- the final number of physical Skills;
- the final filesystem/package layout;
- whether Repository Intelligence is a Skill, reference layer, or composable capability;
- whether Context Intelligence is a standalone Skill;
- the exact evidence-ledger schema;
- the exact subagent runtime configuration;
- a self-improvement implementation;
- a mandatory repository graph/indexing dependency;
- a universal LLM-judge framework;
- adoption of any third-party code or text.

Those remain research/eval-driven decisions.

## 8. Acceptance boundary

This document accepts the architectural **mechanisms and research directions** above.

It does not authorize implementation. Production Skill authoring remains gated behind completion/synthesis of the relevant P0 research, baseline RED evals, and a subsequent approved implementation design/plan.
