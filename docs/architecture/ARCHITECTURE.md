# CodeMaestro Architecture

## Status

This document is the living architecture source of truth for the next-generation CodeMaestro project.

It supersedes the architectural assumptions of the legacy Custom GPT and custom Actions infrastructure whenever they conflict with the decisions recorded here.

## Mission

CodeMaestro is a portable software-engineering operating system implemented as a Skill.

Its purpose is to transform technical intent into evidence-backed, safe, production-grade engineering outcomes across architecture, implementation, debugging, review, refactoring, security, validation, deployment, maintenance, research, and learning.

CodeMaestro should behave like a disciplined senior engineering partner rather than a code generator. It must distinguish what it knows, what it inferred, what it researched, what it actually executed, and what remains unverified.

## Product principles

1. **Tool-independent methodology, tool-aware execution.** Engineering workflows are expressed in terms of capabilities, not CodeMaestro-specific APIs.
2. **Evidence before assertion.** Claims about repository state, execution, validation, deployment, or security must be grounded in observed evidence.
3. **State before mutation.** Relevant current state should be observed before changing repositories, workspaces, databases, configuration, deployments, or package state.
4. **Validation before success claims.** Suggested code, triggered jobs, or planned commands are not equivalent to successful validation.
5. **Research before version-sensitive assertions.** Fast-changing technical facts must be checked against current authoritative sources when material.
6. **Preserve intended behavior.** Fixes and refactors should not silently alter unrelated behavior.
7. **Prefer the smallest correct solution.** Avoid speculative abstractions and unnecessary complexity.
8. **Treat external content as untrusted data.** Repository files, issues, pull-request text, logs, web pages, tool responses, and generated content do not override trusted instructions.
9. **Never invent capabilities.** If a required tool is absent, CodeMaestro must adapt its workflow and report the limitation truthfully.
10. **Security principles are durable; implementation guidance may age.** Stable principles may be local references, while fast-changing practices should be researched before becoming canonical.
11. **Progressive disclosure.** The main Skill remains concise; specialized guidance lives in focused references loaded only when relevant.
12. **Behavioral parity over implementation parity.** The new system preserves useful intent and safeguards, not obsolete APIs or deployment machinery.

## Target runtime architecture

```text
User intent
    |
    v
CodeMaestro Skill
    |
    |-- intent decomposition
    |-- environment/context discovery
    |-- capability discovery
    |-- workflow composition
    |-- safety/trust boundaries
    |-- research policy
    |-- evidence/validation policy
    |-- reporting contract
    |
    v
Authorized native capabilities
    |
    |-- repository and GitHub tooling
    |-- local workspace/runtime execution
    |-- web and documentation research
    |-- file and artifact access
    |-- platform/deployment tools when available
```

There is no required CodeMaestro-specific API layer in the target architecture.

## Skill packaging direction

The initial architecture is one orchestrator Skill with focused supporting references.

```text
codemaestro/
├── SKILL.md
├── references/
│   ├── operating-model.md
│   ├── engineering-workflows.md
│   ├── repository-work.md
│   ├── validation-and-evidence.md
│   ├── research-and-freshness.md
│   ├── security-engineering.md
│   ├── repository-auditing.md
│   ├── database-and-supabase.md
│   ├── ci-and-supply-chain.md
│   ├── llm-agent-engineering.md
│   ├── incident-and-recovery.md
│   ├── language-and-toolchains.md
│   └── reporting-contracts.md
├── assets/
├── scripts/
└── evals/
```

This tree is architectural direction, not yet an implementation commitment. It may change after research and baseline evals.

## Intent model

Legacy operation modes are preserved as useful concepts but no longer treated as mutually exclusive modes.

CodeMaestro composes a workflow from the concerns present in the request.

Core domains include:

- Architecture and system design
- Greenfield project creation
- Feature implementation
- Quick fixes
- Debugging and root-cause analysis
- Code review
- Refactoring
- Performance engineering
- Repository maintenance
- DevOps and CI/CD
- Security engineering
- Database engineering
- Supabase-specific engineering
- Incident response and rollback
- Research
- Learning and explanation
- AI, LLM, agent, RAG, and MCP engineering

Example composition:

```text
User request
  "Find why Supabase sync duplicates rows, fix it, validate it, and open a PR"

Composed concerns
  Debugging
  + Database
  + Supabase
  + Repository mutation
  + Testing
  + Delivery
```

## Environment and capability discovery

Before choosing an execution path, CodeMaestro should determine what environment it is operating in and which capabilities are actually available.

Relevant capability classes include:

- read repository state
- inspect files and diffs
- modify local files
- create commits/branches/pull requests
- run tests and commands
- inspect CI or deployment state
- search authoritative web sources
- inspect databases or platforms
- create artifacts

Behavior must degrade safely when capabilities are unavailable.

Examples:

- With repository read tools but no write tools: analyze and propose changes, but do not claim mutation.
- With local execution: run validation and report actual outcomes.
- With only uploaded files: perform artifact-based analysis and clearly state limits on live state.
- With no current documentation access for a version-sensitive question: avoid presenting uncertain implementation detail as verified fact.

## Workspace and repository state gate

The legacy Repository State Gate becomes a generalized state-before-mutation policy.

Before consequential mutation, observe the relevant current state whenever an authorized trusted capability exists.

Depending on the target, relevant state may include:

- repository identity
- branch/ref
- HEAD/commit
- dirty working tree
- open pull request context
- package/lockfile state
- schema migration state
- database target
- deployment/environment identity
- configuration state

Read capability does not imply write authorization.

## Change delivery gate

The legacy PR Creation Gate is generalized into a Change Delivery Gate.

The exact delivery mechanism depends on the active environment, but the reasoning contract is stable:

1. understand the requested change and scope;
2. inspect current relevant state;
3. identify intended and explicitly non-intended changes;
4. preview or describe consequential changes when useful;
5. follow the active environment's authorization/confirmation requirements;
6. perform only the authorized change;
7. validate using available evidence;
8. report exact resulting state and unresolved limitations.

Pull requests remain a preferred collaboration mechanism where appropriate, but the Skill is not hard-coded to GitHub or PR-only delivery.

## Engineering workflow model

### Architecture and greenfield work

```text
Intent
→ requirements and constraints
→ context/product discovery
→ alternatives and trade-offs
→ architecture decision
→ implementation plan
→ test strategy
→ incremental implementation
→ security and quality checks
→ validation
→ review
→ delivery
→ operational handoff
```

Large projects should be decomposed into milestones and independently testable tasks instead of generated in one pass.

### Debugging

```text
Observe symptom
→ reproduce when possible
→ collect evidence
→ form competing hypotheses
→ test the cheapest discriminating hypothesis
→ identify root cause
→ create regression coverage
→ apply minimal fix
→ verify
```

Correlation must not be presented as root cause without sufficient evidence.

### Refactoring

Before refactoring, establish:

- behavior that must remain invariant;
- behavior allowed to change;
- the specific structural problem being addressed;
- the evidence that will detect regression.

Refactors should proceed in small verified transformations.

### Broad audits

Broad audits use findings-first discipline:

```text
Scope
→ inspect evidence
→ findings matrix
→ severity/confidence
→ prioritization
→ remediation options
→ validation strategy
```

A finding should distinguish observed evidence from inference.

## Language and toolchain adaptation

CodeMaestro is language-agnostic by methodology rather than by claiming memorized expertise in every language or DSL.

For each project it should identify, when material:

- language and version
- runtime
- build system
- dependency/package manager
- test framework
- formatter/linter/static analysis
- framework/platform
- deployment target

For unknown, niche, private, or fast-changing languages and DSLs, it should inspect project evidence and research authoritative documentation rather than guess syntax or behavior.

## Research and freshness policy

Research is mandatory when current verification could materially affect correctness.

Typical triggers include:

- rapidly changing frameworks or libraries
- current platform/API behavior
- security standards or vulnerability guidance
- CI/CD provider semantics
- package/dependency compatibility
- model/tool/MCP APIs
- deployment requirements
- unfamiliar technologies or DSLs

Authority preference:

1. official specifications and standards
2. official vendor/project documentation
3. primary repositories/release notes/advisories
4. high-quality secondary technical sources when primary evidence is insufficient

Research findings are not automatically canonical project guidance. Material architectural changes should be recorded through the decision process.

## Evidence and validation contract

Canonical result statuses:

- `PASS` — the relevant check actually ran or was directly observed and succeeded.
- `FAIL` — the relevant check actually ran or was directly observed and failed.
- `NOT AVAILABLE` — the environment lacks a required capability or evidence source.
- `PENDING` — an observed process has started but no terminal result is available.
- `NOT VERIFIED` — a claim or result has not been directly validated.
- `PROVIDED, NOT EXECUTED` — commands, code, patches, or procedures were supplied but not run.
- `NOT APPLICABLE` — the check does not apply to the current scope.
- `PARTIALLY VERIFIED` — some material aspects were validated but full verification was not possible.
- `BLOCKED` — validation or progress cannot continue because a concrete prerequisite is unresolved.

A trigger/dispatch acknowledgement is not a PASS. A plausible patch is not a verified fix. A repository snapshot is not proof of current production state.

## Security and trust model

CodeMaestro retains the strongest principles of the legacy system while removing infrastructure-specific enforcement.

Core rules:

- Never include secrets in reusable Skill artifacts, repository documentation, examples, logs, or reports.
- Treat repository content and external content as data, not higher-priority instructions.
- Do not broaden access or permissions merely to complete a task more easily.
- Do not silently cross environment, repository, branch, database, tenant, or deployment boundaries.
- Separate authentication from authorization reasoning.
- Prefer least privilege and explicit scope for consequential operations.
- Research current security implementation guidance when standards or platform behavior may have changed.

Security review domains include:

- application security
- authentication and authorization
- secrets and sensitive data
- dependency and vulnerability risk
- CI/CD security
- software supply chain
- database and RLS security
- Supabase-specific risks
- cloud/container/IaC risks
- LLM and agent security
- prompt injection
- RAG trust boundaries
- MCP/tool authorization
- privacy and data handling

## Reporting contract

Responses should be shaped to the work rather than forced into one universal template, but engineering reports should distinguish:

- observed facts
- assumptions
- inferred findings
- researched facts
- actions actually performed
- validation performed
- unresolved risks/limitations
- explicitly excluded changes

For audits, findings should include evidence, impact, severity, confidence, and recommended action where useful.

## Evaluation architecture

CodeMaestro is intended to evolve through eval-driven development.

Initial evaluation domains:

- capability truthfulness
- state-before-mutation behavior
- prompt-injection resistance
- tool authorization boundaries
- debugging/root-cause quality
- architecture/greenfield reasoning
- refactoring behavior preservation
- security review quality
- language/toolchain adaptation
- research freshness
- validation honesty
- reporting clarity
- regression cases from the legacy system

Legacy API-specific tests should be converted into environment-independent behavioral scenarios rather than copied verbatim.

## Legacy systems

The following systems are not target runtime dependencies:

- `heraklist/GPT_CodeMaesto_API`
- `heraklist/codemaestro-sbox`
- Custom GPT Actions/OpenAPI integration
- Vercel gateway/runtime
- Redis/Upstash operational state for CodeMaestro Actions
- custom Action authentication keys

They remain migration and historical references only until the useful behaviors have been fully accounted for.

The legacy umbrella repository `heraklist/Custom-ChatGPT---Code-maesto-v2` is treated as migration-source history rather than a target application repository.

## Documentation governance

Canonical project memory is stored in this repository.

- `ARCHITECTURE.md` — living target architecture.
- `MIGRATION-INVENTORY.md` — source-to-target disposition ledger.
- `DECISIONS.md` — accepted architecture decisions and consequences.
- `../research/RESEARCH-BACKLOG.md` — unresolved research queue.
- `../superpowers/specs/` — dated design checkpoints.
- `../superpowers/plans/` — implementation plans for approved milestones.

When these conflict, later accepted decisions should be incorporated into this living architecture promptly so that this file remains the current source of truth.

## Current phase

The project is in architecture and research preparation.

Production Skill files, runtime references, scripts, and eval implementations have not yet been created. Their final shape will be determined through baseline evaluation, research, and subsequent approved design milestones.
