# CodeMaestro Research & Experimental Engineering Design

**Status:** Accepted architecture extension — 2026-09-04  
**Scope:** Research methodology, experimental engineering, programming-language evolution, evidence/provenance, and optional subagent roles.

## 1. Goal

CodeMaestro must operate not only as a software-engineering executor but also as a disciplined technical researcher and experimental engineering partner.

This capability is intended for work such as:

- surveying unfamiliar technical domains;
- comparing architectures, languages, runtimes, libraries, and tools;
- investigating uncertain behavior;
- designing and running bounded experiments;
- reproducing technical claims independently;
- evolving experimental programming languages and DSLs;
- turning evidence into reviewable design proposals without silently creating authority.

The Cusp language project is a primary stress case for this design because it requires semantic research, characterization, experimental compiler work, governance, reproducibility, and explicit separation between proposals and normative language authority.

## 2. Architectural decision

Use an autonomous **Research Lab** capability alongside shared **Language Intelligence**, with optional scoped runtime subagent roles where the host environment supports them.

Do not model every research role as a permanently installed Skill. Skills own reusable methodology and domain guidance; runtime agent roles may provide temporary independent contexts for focused research, experimentation, criticism, or replication.

Conceptually:

```text
CodeMaestro
├── orchestrator
├── Research Lab
│   ├── survey
│   ├── compare
│   ├── investigate
│   ├── experiment
│   ├── replicate
│   └── evolve
├── Language Intelligence
├── engineering sub-skills
└── optional runtime roles
    ├── research-scout
    ├── experimentalist
    ├── skeptic
    └── replicator
```

## 3. Research is not search-and-summarize

A research workflow must preserve epistemic state. It must distinguish at minimum:

- hypothesis;
- source-supported claim;
- observation;
- characterization;
- reproduced result;
- supported or contradicted hypothesis;
- accepted project decision;
- normative rule/specification;
- implementation;
- validated implementation.

These states are not interchangeable. A prototype that runs once is not automatically a validated design. Observed compiler behavior is not automatically normative semantics. A feature found in another language is not automatically a recommendation for the target language.

## 4. Research lifecycle

For substantial work, the default lifecycle is:

```text
Question / problem
→ constraints and non-goals
→ current state / baseline
→ source landscape
→ hypotheses
→ alternatives
→ experiment design
→ bounded experiments
→ evidence capture
→ adversarial review
→ replication when material
→ comparison
→ decision
→ proposal/specification when applicable
→ implementation
→ validation
→ regression or reopening when evidence changes
```

The rigor is proportional to consequence and uncertainty. Small factual or technical questions should not pay the cost of a full laboratory workflow.

## 5. Research modes

### Survey
Map the current technical landscape, authorities, terminology, major approaches, maturity, and gaps.

### Compare
Evaluate alternatives under a shared criterion matrix rather than independent descriptions.

### Investigate
Explain an observed behavior through competing hypotheses and discriminating evidence.

### Experiment
Test a bounded hypothesis under recorded conditions with explicit success/failure criteria.

### Replicate
Attempt to reproduce a result in a fresh context using only the procedure, inputs, and artifacts needed for the claim.

### Evolve
Convert research pressure into a reviewable design or semantic proposal, followed by explicit project/governance acceptance before normative status.

## 6. Durable research state

Research that must survive context loss, be audited, or be reproduced must use durable artifacts instead of model memory alone.

A representative structure is:

```text
research/<topic>/
├── question.md
├── state.md
├── hypotheses.md
├── source-map.md
├── evidence-ledger.json
├── experiments/
│   └── <run-id>/
│       ├── plan.md
│       ├── metadata.json
│       ├── results.md
│       └── artifacts/
├── comparison.md
├── decision.md
└── report.md
```

The final implementation may use a different physical layout, but the information responsibilities must remain.

## 7. Evidence and provenance contract

Material research claims should be traceable to the exact state that produced them.

Depending on the work, provenance may include:

- source URL or repository path;
- repository and commit SHA;
- language/compiler/runtime/tool version;
- operating system and architecture;
- command line and flags;
- configuration and dependency state;
- input or artifact hashes;
- test suite / experiment definition version;
- random seed where relevant;
- timestamp and run identifier;
- result classification.

Source provenance should be captured when evidence is retrieved or produced, not reconstructed later from model memory.

## 8. Adversarial and independent review

For consequential or uncertain research, CodeMaestro should actively search for evidence that could falsify the leading explanation or design.

A skeptic pass should:

- identify hidden assumptions;
- find counterexamples;
- seek contrary primary sources;
- identify missing measurements;
- distinguish correlation from causation;
- identify cases that would change the decision.

Independent replication should use a fresh context where available and should not receive the intended conclusion unless required to reproduce the procedure.

## 9. Optional runtime roles

### Research Scout
Find and classify authoritative sources and unresolved gaps. Does not make the final decision.

### Experimentalist
Design and execute a bounded experiment, capture metadata, and report results. Does not grant normative status.

### Skeptic
Challenge the leading claim, design, or interpretation using counterevidence and alternate explanations.

### Replicator
Attempt an independent reproduction using the declared procedure and artifacts.

The main Research Lab workflow remains responsible for synthesis, conflict resolution, and handoff to project authority.

## 10. Authority boundary

Research does not become authority merely because CodeMaestro generated it.

For an experimental language such as Cusp:

```text
CodeMaestro research
→ evidence / characterization / proposal

Cusp governance and accepted decisions
→ project decision authority

Normative Cusp specification
→ semantic authority

Compiler/tests/evidence
→ implementation and conformance evidence
```

The invariant is:

> Research may discover, characterize, challenge, experiment, and propose. It may not silently create semantic authority.

## 11. Language Evolution Protocol

For substantive experimental-language changes:

```text
Problem / pressure
→ current normative state
→ observed behavior
→ design constraints and non-goals
→ comparative language study
→ hypotheses and alternatives
→ minimal experimental design
→ prototype
→ characterization
→ negative / property / fuzz tests as appropriate
→ performance and resource analysis
→ compatibility impact
→ security impact
→ independent challenge
→ replication when material
→ decision proposal
→ human/project acceptance
→ normative specification
→ implementation
→ conformance validation
```

The protocol must distinguish idea, proposal, accepted design, implementation, and stable feature.

## 12. Sub-skill epistemic contract

Every autonomous CodeMaestro sub-skill should eventually define:

- what kinds of claims it produces;
- what evidence each claim type requires;
- which claims may remain observations or inferences;
- which claims require current external authority;
- when research is mandatory;
- when independent review materially improves confidence;
- how uncertainty and unverified claims are reported;
- what validation can upgrade the evidence state.

This extends the existing autonomous sub-skill contract.

## 13. Reference projects and patterns

The comparative research registry is maintained in `docs/research/COMPARATIVE-REFERENCE-REGISTRY.md`.

Key patterns already identified include:

- progressive-disclosure and skill-authoring principles from OpenAI Codex;
- composable development methodology from Superpowers;
- research decomposition, parallelism, resumability, and structured validation from Deep-Research-skills;
- durable ledgers, fresh-context review, and external verification from rigorous engineering-skill repositories;
- source/evidence ledgers from grounded-citation workflows;
- skills-vs-commands / knowledge-vs-workflow separation from large skill catalogs;
- explicit skills / custom-agent / tool separation from mature agent ecosystems;
- RFC/proposal governance and state separation from mature and experimental programming-language projects.

These repositories are design references, not runtime dependencies or authorities for CodeMaestro behavior.

## 14. Open research questions

The following remain research work rather than accepted implementation details:

1. Exact physical packaging of Research Lab relative to the main orchestrator.
2. Which research roles merit optional agent-role definitions in Codex-capable environments.
3. Exact durable artifact schemas and minimum metadata fields.
4. Claim/evidence ledger representation and citation integration.
5. Stopping criteria and research-budget policy.
6. Criteria that require replication or adversarial review.
7. Language-proposal template and promotion rules for experimental semantics.
8. How research outputs feed automatically or manually into ADR/spec/eval workflows.

These are tracked through CM-R-017 to CM-R-020.
