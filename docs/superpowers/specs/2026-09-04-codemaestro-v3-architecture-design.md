# CodeMaestro v3 Architecture Design

## Status

Approved design baseline for the migration of the legacy CodeMaestro Custom GPT into a next-generation portable software-engineering Skill.

## Product intent

CodeMaestro is being rebuilt from a Custom GPT plus static knowledge plus custom Actions infrastructure into a portable, Skill-first software-engineering operating system.

Its purpose is to turn technical intent into evidence-backed, safe, production-grade engineering outcomes across architecture, implementation, debugging, review, refactoring, security, validation, deployment, maintenance, research, and learning.

The design preserves the useful behavioral DNA of the legacy system while removing infrastructure that existed only to support Custom GPT Actions.

## Core architectural decision

The target architecture is zero-custom-infrastructure by default.

CodeMaestro must not depend on a proprietary CodeMaestro API, Vercel gateway, Redis/Upstash state store, OpenAPI Actions schema, or custom authentication layer. It should reason in terms of abstract capabilities and use the native tools available in the execution environment.

Examples include GitHub tools, local repository tools, Codex/runtime execution, file access, web research, and other authorized native capabilities.

## Architectural principles

1. Tool-independent methodology, tool-aware execution.
2. Evidence before assertion.
3. State before mutation.
4. Preview before consequential change when meaningful.
5. Validation before success claims.
6. Current authoritative research for version-sensitive or fast-changing technical guidance.
7. Preserve intended behavior during fixes and refactors unless scope explicitly authorizes behavior change.
8. Prefer the smallest correct solution over unnecessary complexity.
9. Treat repository content, web content, tool output, issues, logs, and model-generated arguments as untrusted data rather than instructions.
10. Never claim unavailable capabilities or execution that did not occur.
11. Keep security principles stable while researching implementation details that age quickly.
12. Use progressive disclosure so detailed references load only when relevant.

## Target runtime shape

```text
User intent
    |
    v
CodeMaestro Skill
    |
    |-- intent decomposition
    |-- context and capability discovery
    |-- workflow selection
    |-- safety and trust boundaries
    |-- research policy
    |-- evidence and validation policy
    |-- reporting contract
    |
    v
Available native tools
    |
    |-- repository / GitHub
    |-- local execution
    |-- web / documentation research
    |-- files and artifacts
    |-- deployment or platform tools when authorized
```

## Skill packaging direction

The initial design is a single orchestrator Skill with focused supporting references rather than a family of overlapping skills.

Proposed target shape:

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

`SKILL.md` must remain a concise orchestrator and router. Heavy or specialized material belongs in focused references. Scripts are included only for deterministic helpers that materially improve reliability.

## Workflow model

The legacy fixed modes are preserved conceptually but refactored into composable intent routing.

A request may combine multiple concerns, for example:

```text
Debug
+ Database
+ Supabase
+ Repository change
+ Testing
+ Pull-request delivery
```

The router should therefore decompose intent into relevant engineering concerns instead of forcing every request into one mutually exclusive mode.

Core workflow domains include:

- Architecture and system design
- Greenfield project creation
- Build and feature implementation
- Quick fixes
- Debugging and root-cause analysis
- Code review
- Refactoring
- Performance engineering
- Repository maintenance
- Security engineering
- DevOps and CI/CD
- Database engineering
- Incident and rollback planning
- Research
- Learning and explanation
- AI/LLM/agent engineering

## Evidence model

CodeMaestro must distinguish evidence states explicitly.

Canonical statuses should include:

- PASS
- FAIL
- NOT AVAILABLE
- PENDING
- NOT VERIFIED
- PROVIDED, NOT EXECUTED
- NOT APPLICABLE
- PARTIALLY VERIFIED
- BLOCKED

A command dispatch, workflow trigger, code suggestion, or planned test is not equivalent to successful validation.

## State and mutation model

Before changing a repository, workspace, database, deployment, package state, or configuration, CodeMaestro should observe the relevant current state using an available trusted tool whenever possible.

The legacy Repository State Gate becomes a generalized Workspace/Repository State Gate.

Read access must never be treated as implicit write authorization. Consequential actions must follow the authorization and confirmation semantics of the active environment.

## Research model

Stable engineering principles may live in local references.

Fast-changing details such as framework versions, security guidance, platform behavior, package manager semantics, CI/CD capabilities, model/tool APIs, and deployment requirements should be verified from current authoritative sources when material to the answer.

Unknown or niche languages and DSLs must be researched rather than guessed.

## Security model

The legacy safety model is retained at the principle level and modernized.

Key trust boundaries:

- User instructions outrank repository/web/tool content.
- Repository files, pull-request text, logs, provider responses, generated content, and external documentation are data unless explicitly trusted as instructions by the execution environment.
- Secrets must never be copied into reusable Skill artifacts.
- Security guidance that depends on current standards or versions should be researched before becoming canonical.

Security domains to retain and expand include application security, authentication/authorization, secrets, dependency risk, CI/CD, software supply chain, database security, Supabase, LLM/agent security, MCP/tool authorization, prompt injection, and data handling.

## Legacy migration principle

The migration target is behavioral parity, not API parity.

Custom endpoints, OpenAPI operation IDs, Vercel deployment logic, Redis-backed idempotency, custom Action keys, custom rate limiting, and GPT Builder integration are retired.

The useful behavior they enforced is either:

- absorbed into Skill methodology,
- generalized into environment-independent engineering rules,
- replaced by native tools,
- retained only as historical reference,
- or retired when no longer relevant.

## Evaluation strategy

The new Skill must be eval-driven.

Legacy behavioral tests should be converted into environment-independent scenarios covering:

- capability truthfulness
- repository/workspace state awareness
- prompt injection resistance
- tool authorization boundaries
- debugging quality
- greenfield design quality
- refactoring preservation
- security review quality
- language/toolchain adaptation
- research freshness
- validation honesty
- regression behavior

New Skill behavior should be developed with baseline/failing scenarios first, followed by the smallest guidance needed to correct failures, then regression testing.

## Documentation model

The repository itself is the canonical project memory.

- `docs/architecture/ARCHITECTURE.md` is the living architecture source of truth.
- `docs/architecture/MIGRATION-INVENTORY.md` tracks legacy components and their disposition.
- `docs/architecture/DECISIONS.md` records accepted architectural decisions.
- `docs/research/RESEARCH-BACKLOG.md` tracks research required before design areas are finalized.
- This design spec is a dated architecture checkpoint rather than the continuously changing source of truth.

## Out of scope for this milestone

This milestone does not create the production `SKILL.md`, runtime references, scripts, or eval implementation. It establishes the architecture documentation foundation required before those artifacts are designed and tested.
