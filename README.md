# Code Maestro

CodeMaestro is being rebuilt as a next-generation, portable software-engineering operating system implemented as one public `@codemaestro` Skill.

The project preserves useful engineering methodology, safety boundaries, validation discipline, research/evidence practices, and domain workflows from the legacy Custom GPT while removing the old custom Actions/API infrastructure as a required runtime dependency.

## Current phase

**Written specification approved; Milestone 0 — Repository Work-Session Logging Foundation is executing inline under the Superpowers implementation plan.**

The documentation-consistency gate, narrow logging privacy/retention decision, canonical logging schemas, and repository work-session protocol are being established before the actual logging filesystem is declared operational. Production Skill files, runtime capability modules, full executable Skill eval suites, and the Self-Evolution Controller have **not** been created yet.

## Start here — current authority

- [Architecture gateway](docs/architecture/ARCHITECTURE.md)
- [CodeMaestro v3 consolidated design v2 — approved canonical written specification](docs/superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md)
- [Architecture decision log](docs/architecture/DECISIONS.md)
- [Research backlog / canonical research execution-status index](docs/research/RESEARCH-BACKLOG.md)
- [Legacy migration inventory](docs/architecture/MIGRATION-INVENTORY.md)

The consolidated v2 Status section defines the authority relationship among earlier focused specs and historical amendments/checkpoints.

## Repository work-session governance

Every Chat / Work / Codex session that develops or maintains this repository must follow the repository work-session protocol once the Milestone-0 filesystem is operational. These instructions govern **development of CodeMaestro itself** and are not generic portable behavior of the future Skill.

- [Repository work-session logging protocol](docs/project-governance/SESSION-LOGGING-PROTOCOL.md)
- [Canonical logging schemas](docs/project-governance/LOGGING-SCHEMAS.md)
- [Logging privacy & retention policy](docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md)
- [Milestone 0 implementation plan](docs/superpowers/plans/2026-09-04-repository-work-session-logging-foundation.md)

The protocol requires a Session Admission Gate, real-time/event-time logging, progressive history loading, privacy/redaction checks, explicit `LOG WRITE FAILED` behavior, and checkpoint/handoff records.

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

## Architecture foundation plan

- [Architecture Documentation Foundation plan](docs/superpowers/plans/2026-09-04-architecture-documentation-foundation.md) — completed for its original five-file foundation scope; it does not claim to have planned the later architecture/research expansion.

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

CM-R-021 through CM-R-032 remain `IN RESEARCH` with accepted architectural direction. For CM-R-032, the narrow Milestone-0 repository logging lifecycle sub-question is resolved by the logging privacy policy, while the broader Privacy & Data Lifecycle Engineering track remains open.

## Logging ownership

Repository-development logging and portable Skill behavior are deliberately separate:

- `logs/conversations/` — real-time session history for the user's Chat / Work / Codex sessions developing this repository once the filesystem is bootstrapped;
- `logs/logs/project/` — real-time project mutation/state history maintained by those project-working sessions;
- `logs/logs/self-evolution/` — reserved dedicated audit stream owned by the CodeMaestro Self-Evolution protocol when that controller is implemented.

The nested `logs/logs/` name is intentional under the project owner's chosen root/subfolder structure, not an accidental typo.

Because this repository is public, committed session history must be public-safe. Secrets and non-public sensitive/confidential payloads are never persisted for transcript completeness.

## Milestone 0 ordering

Milestone 0 executes in this order:

1. documentation-consistency checker and CI gate;
2. narrow CM-R-032 privacy/retention/public-sanitization decision;
3. canonical logging schemas;
4. canonical real-time project-working-session protocol;
5. actual `logs/` filesystem and first live sanitized records;
6. append/correction/redaction/resume/handoff end-to-end validation.

Milestone 0 is not operational until the complete verification gate passes.

## Legacy systems

The following repositories are migration/reference sources only and are not target runtime dependencies:

- `heraklist/GPT_CodeMaesto_API`
- `heraklist/codemaestro-sbox`
- `heraklist/Custom-ChatGPT---Code-maesto-v2`

## Public repository security rule

Do not commit secrets, credentials, tokens, private `.env` values, production configuration, private keys, or other secret-bearing artifacts from the legacy system or project sessions to this repository.
