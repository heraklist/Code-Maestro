# CodeMaestro Comparative Research Registry

## Purpose

This registry tracks external projects that may inform CodeMaestro architecture, sub-skill design, subagent orchestration, research methodology, evaluation, and experimental-language engineering.

A registry entry is a **reference target**, not an adopted dependency or authority. Useful ideas must survive CodeMaestro's own research, compatibility, licensing, safety, and eval review before adoption.

## Tier model

- **Tier A — Deep study:** high-value primary/reference projects whose architecture or methodology is directly relevant.
- **Tier B — Selective extraction:** useful patterns or examples, but not strong enough to drive architecture alone.
- **Tier C — Discovery only:** useful for taxonomy, ecosystem discovery, naming, or user-intent signals; not treated as correctness authority.

## Tier A — Deep study

### OpenAI Codex

**Repositories / sources**
- `openai/codex`
- `openai/plugins`
- official Codex skill-creator sample

**Study themes**
- Skill packaging and progressive disclosure
- skill discovery and routing
- agent roles and runtime orchestration
- plugins, skills, agents, commands, MCP/tool boundaries
- validation and authoring patterns

**Current extraction hypothesis**
CodeMaestro should keep methodology in skills and use runtime agent roles only when the host environment supports scoped independent contexts.

---

### Agent Skills specification and reference collections

**Repositories / sources**
- Agent Skills specification
- `anthropics/skills`

**Study themes**
- portable skill contract
- metadata and discovery cost
- progressive disclosure
- reference/resource boundaries
- cross-harness portability

---

### Superpowers

**Repository**
- `obra/superpowers`

**Study themes**
- brainstorm → design → plan → implementation lifecycle
- hard approval gates
- TDD
- isolated workspaces
- independent review
- subagent decomposition
- anti-rationalization patterns

**Adoption posture**
Extract proven workflow invariants rather than embed the full methodology unchanged.

---

### Microsoft Skills

**Repository**
- `microsoft/skills`

**Study themes**
- large skill catalog architecture
- router skills
- skill / custom-agent / MCP separation
- language-specific vs language-agnostic skills
- eval and test harnesses
- context-rot avoidance

---

### Addy Osmani Agent Skills

**Repository**
- `addyosmani/agent-skills`

**Study themes**
- source-driven development
- doubt-driven / adversarial verification
- constraint-driven development
- context engineering
- lifecycle decomposition
- proportional autonomy and quality gates

---

### Steve Vitali Agent Skills

**Repository**
- `SteveVitali/agent-skills`

**Study themes**
- durable state over context
- evidence over self-assessment
- multi-session orchestration
- fresh-context review
- deterministic-before-LLM mechanics
- resumable build ledgers

---

### Research Lab reference

**Repository**
- `pbi-agent/skills`

**Focus**
- `research-lab`

**Study themes**
- prepare/specify/baseline/explore/compare/decide/apply/review lifecycle
- durable research artifacts
- resumable research state
- phase delegation

**CodeMaestro extension target**
Add explicit epistemic states, experimental-language semantics, adversarial challenge, replication, snapshot provenance, and authority separation.

---

### Grounded research / citation evidence

**Repository**
- `NousResearch/hermes-agent`

**Focus**
- grounded citations and evidence ledgers

**Study themes**
- capture provenance at retrieval time
- deterministic source IDs
- source → evidence → claim linkage
- explicit unverified claims
- verification before delivery

---

### Cusp language system

**Repositories**
- `heraklist/Cusp`
- `heraklist/cusp-steward`
- `heraklist/GPT_cusp-steward_API`

**Study themes**
- experimental language design
- semantic authority separation
- design constitution
- normative vs characterization evidence
- snapshot-bound evidence
- self-maintenance / self-improvement / language-evolution separation
- controlled AI proposal and human authorization
- compiler, grammar, project-model, and roadmap evolution

**Special role**
Primary CodeMaestro stress case for Research Lab + Language Intelligence + Language Evolution Protocol.

---

### Programming-language evolution governance

**Repositories / processes**
- `rust-lang/rfcs`
- `swiftlang/swift-evolution`
- `carbon-language/carbon-lang`
- Python PEP process
- Kotlin KEEP process
- Go proposal process
- TC39 ECMAScript proposal process

**Study themes**
- substantial-change threshold
- pre-proposal exploration
- alternatives and drawbacks
- open questions and blocking issues
- accepted proposal vs implementation vs release distinction
- normative specification and compatibility evolution

## Tier B — Selective extraction

### Deep Research Skills

**Repository**
- `Weizhena/Deep-Research-skills`

**Useful patterns**
- research-outline decomposition
- per-item field contracts
- parallel independent research
- resumability
- structured uncertainty
- deterministic result validation

**Do not copy blindly**
- fixed prompt reproduction as a universal method
- search-to-JSON as sufficient for experimental engineering

---

### Agent Rules Books

**Repository**
- `ciembor/agent-rules-books`

**Useful patterns**
- multi-resolution guidance (`full` / `mini` / `nano`)
- operational distillation of engineering principles
- testing whether explicit rules change agent behavior

**Caution**
Books and derived rules are design perspectives, not CodeMaestro authority.

---

### Designer Skills

**Repository**
- `Owl-Listener/designer-skills`

**Useful patterns**
- skills as reusable knowledge units
- commands/workflows as compositional actions
- large domain taxonomy
- index/discovery strategy
- specialization without one monolithic prompt

---

### Claude Skills product-designer example

**Repository**
- `borghei/Claude-Skills`

**Useful patterns**
- explicit prerequisites
- scope and limitations
- staged workflows
- integration boundaries
- measurable deliverables

**Caution**
Avoid copying universal hardcoded thresholds when they are contextual, version-sensitive, or domain-dependent.

---

### Official / vendor language skills

**Examples**
- Mojo official Agent Skills
- MoonBit official Agent Skills

**Useful patterns**
- fast-moving syntax correction layers
- official freshness guidance
- narrow language-orientation skills
- validation against current toolchain

## Tier C — Discovery only

### LobeHub skills catalog

**Use**
- discover repeated user intents
- survey ecosystem naming and taxonomy
- identify capability gaps
- find candidate repositories for deeper verification

**Not authority for**
- security
- software correctness
- skill quality
- architecture decisions

---

### Generic prompt/skill marketplaces and large collections

Use only as discovery inputs unless a specific project demonstrates authoritative sourcing, reproducible evals, strong governance, or unusually relevant architecture.

## Evaluation dimensions for each reference

When studying a project, record:

1. Problem it solves.
2. Unit of abstraction: prompt, rule, skill, workflow, role, agent, plugin, tool, or runtime.
3. Trigger and routing design.
4. Context-loading strategy.
5. State/persistence model.
6. Evidence and verification model.
7. Tool authorization model.
8. Failure and uncertainty behavior.
9. Parallelism/subagent model.
10. Eval/regression methodology.
11. Portability constraints.
12. Maintenance/freshness model.
13. Licensing implications.
14. What CodeMaestro should adopt, adapt, reject, or investigate further.

## Current priority sequence

1. OpenAI Codex / plugins / skill creator
2. Agent Skills specification
3. Cusp / Cusp Steward experimental-governance model
4. Superpowers
5. Microsoft Skills
6. Steve Vitali + Addy Osmani engineering-skill systems
7. Research Lab + grounded-evidence systems
8. Rust / Swift / Carbon language-evolution governance
9. Deep Research / design / rules repositories
10. discovery catalogs such as LobeHub
