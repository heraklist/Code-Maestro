# Code Maestro

CodeMaestro is being rebuilt as a next-generation, portable software-engineering operating system implemented as one public `@codemaestro` Skill.

The project preserves useful engineering methodology, safety boundaries, validation discipline, research/evidence practices, and domain workflows from the legacy Custom GPT while removing the old custom Actions/API infrastructure as a required runtime dependency.

## Current phase

**Written specification approved; Milestone 0 — Repository Work-Session Logging Foundation is operational.**

The repository now has a status-aware documentation consistency/CI gate, a narrow CM-R-032 logging privacy/retention decision, canonical logging schemas, a mandatory real-time repository work-session protocol, the actual logging filesystem, live public-safe session/project records, and verified correction/redaction/resume/handoff behavior.

Production Skill files, runtime capability modules, full executable Skill eval suites, and the Self-Evolution Controller have **not** been created yet.

## Start here — current authority

- [Architecture gateway](docs/architecture/ARCHITECTURE.md)
- [CodeMaestro v3 consolidated design v2 — approved canonical written specification](docs/superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md)
- [Architecture decision log](docs/architecture/DECISIONS.md)
- [Research backlog / canonical research execution-status index](docs/research/RESEARCH-BACKLOG.md)
- [Legacy migration inventory](docs/architecture/MIGRATION-INVENTORY.md)

The consolidated v2 Status section defines the authority relationship among earlier focused specs and historical amendments/checkpoints.

## Repository work-session governance

Every Chat / Work / Codex session that develops or maintains this repository must follow the repository work-session protocol. These instructions govern **development of CodeMaestro itself** and are not generic portable behavior of the future Skill.

- [Repository work-session logging protocol](docs/project-governance/SESSION-LOGGING-PROTOCOL.md)
- [Canonical logging schemas](docs/project-governance/LOGGING-SCHEMAS.md)
- [Logging privacy & retention policy](docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md)
- [Milestone 0 implementation plan](docs/superpowers/plans/2026-09-04-repository-work-session-logging-foundation.md)

The protocol requires a Session Admission Gate, real-time/event-time logging, progressive history loading, privacy/redaction checks, explicit `LOG WRITE FAILED` behavior, and checkpoint/handoff records.

## Live logging layout

```text
logs/
├── conversations/          # repository project-working session history
└── logs/
    ├── project/            # repository mutation/state-event history
    └── self-evolution/     # reserved for future Skill Self-Evolution audit behavior
```

Ownership remains deliberately separate:

- `logs/conversations/` — user-visible, public-safe continuity history for the user's project-working Chat / Work / Codex sessions;
- `logs/logs/project/` — what actually changed in the CodeMaestro repository/project;
- `logs/logs/self-evolution/` — reserved namespace owned by the future CodeMaestro Self-Evolution Controller, not ordinary project sessions.

The nested `logs/logs/` path is intentional.

## Milestone 0 verification

Milestone 0 established and validated:

1. status-aware ADR uniqueness with historical/absorbed handling;
2. CM-R backlog/record existence and status parity;
3. internal Markdown link resolution;
4. public-repository logging privacy/retention/public-sanitization policy;
5. canonical transcript/project-event/correction/redaction/checkpoint schemas with stable `EVENT ID`;
6. mandatory real-time project-working-session protocol;
7. actual logging roots and first live sanitized session/project records;
8. RED→GREEN correction/supersession and redaction drills;
9. progressive resume/handoff using durable state rather than full conversation replay;
10. ownership separation with no fabricated Self-Evolution run.

The documentation consistency workflow runs unit tests and the repository checker on the exact GitHub branch/PR checkout.

## Research and acceptance checkpoints

- [Comparative Research Pass 3](docs/research/2026-09-04-comparative-research-pass-3.md)
- [Pass 3 provenance addendum](docs/research/2026-09-04-pass-3-provenance-addendum.md)
- [Pass 3 historical decision checkpoint](docs/architecture/DECISIONS-2026-09-04-PASS3.md)
- [Comparative Research Pass 4](docs/research/2026-09-04-comparative-research-pass-4.md)
- [Pass 4 acceptance and canonicalization](docs/architecture/2026-09-04-pass-4-acceptance-and-canonicalization.md)
- [Comparative Research Pass 5](docs/research/2026-09-04-comparative-research-pass-5.md)
- [Pass 5 acceptance and Capability Freeze](docs/architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md)
- [Comparative reference registry](docs/research/COMPARATIVE-REFERENCE-REGISTRY.md)

## Focused design checkpoints

- [Initial v3 architecture design](docs/superpowers/specs/2026-09-04-codemaestro-v3-architecture-design.md)
- [Research & Experimental Engineering design](docs/superpowers/specs/2026-09-04-research-experimental-engineering-design.md)
- [Context, Repository & Evidence hardening design](docs/superpowers/specs/2026-09-04-context-repository-evidence-hardening-design.md)
- [Logging ownership & timing amendment — absorbed into v2](docs/superpowers/specs/2026-09-04-logging-ownership-and-timing-amendment.md)
- [Initial consolidated design — superseded pointer](docs/superpowers/specs/2026-09-04-codemaestro-v3-capability-runtime-consolidated-design.md)

## Architectural direction

The current target includes:

- one public `@codemaestro` entrypoint;
- `CAPABILITY != SKILL != ROLE != TOOL`;
- internal capability composition with progressive disclosure;
- tool-independent methodology and capability-aware native execution;
- evidence-before-assertion;
- state-before-mutation;
- validation-before-success claims;
- availability != authorization and routing cannot create authority;
- capability-first behavior across Chat, Work, Codex, and future surfaces;
- dynamic authoritative research for version-sensitive guidance;
- Project Quality Contract protection;
- eval-driven development and regression protection;
- accepted Pass-5 Capability Freeze, reopenable by real task/eval evidence;
- Command-Gated Self-Evolution that cannot self-expand authority;
- explicit separation between repository-development session logging and portable Skill Self-Evolution behavior;
- zero CodeMaestro-specific runtime infrastructure by default.

The migration goal is **behavioral parity and improvement**, not recreation of the legacy API surface.

## Research status model

Research execution status is distinct from architectural disposition.

A direction may be accepted while its track remains `IN RESEARCH`. `ACCEPTED` is reserved for research whose expected outputs have been sufficiently completed, reviewed, and incorporated for the stated scope.

CM-R-021 through CM-R-032 remain `IN RESEARCH` with accepted architectural direction. For CM-R-032, the narrow repository logging lifecycle prerequisite is resolved by the logging privacy policy, while the broader Privacy & Data Lifecycle Engineering track remains open.

## Next implementation stage

With Milestone 0 operational, subsequent CodeMaestro implementation may proceed in the canonical order from the approved v2:

```text
canonical architecture/documentation integration
-> capability contracts + Capability Registry
-> RED eval implementation
-> final physical Skill packaging
-> compact orchestrator
-> progressive capability/intelligence modules
-> Self-Evolution Controller + dedicated Self-Evolution audit behavior
-> cross-runtime validation
-> stabilization
```

Each subsequent implementation slice requires its own executable plan/checkpoints under the selected inline Superpowers workflow.

## Legacy systems

The following repositories are migration/reference sources only and are not target runtime dependencies:

- `heraklist/GPT_CodeMaesto_API`
- `heraklist/codemaestro-sbox`
- `heraklist/Custom-ChatGPT---Code-maesto-v2`

## Public repository security rule

Do not commit secrets, credentials, tokens, private `.env` values, production configuration, private keys, or other secret-bearing artifacts from the legacy system or project sessions to this repository.
