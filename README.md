# Code Maestro

CodeMaestro is being rebuilt as a next-generation, portable software-engineering operating system implemented as one public `@codemaestro` Skill.

The project preserves useful engineering methodology, safety boundaries, validation discipline, research/evidence practices, and domain workflows from the legacy Custom GPT while removing the old custom Actions/API infrastructure as a required runtime dependency.

## Current phase

**Written-spec review and architecture documentation repair.**

Production Skill files, runtime capability modules, scripts, and eval implementations have **not** been created yet.

The current branch contains the architecture/research foundation, comparative research through Pass 5, accepted architecture checkpoints, the consolidated v3 written-spec candidate, Self-Evolution governance, and repository logging-governance design.

## Start here — current authority

- [Architecture gateway](docs/architecture/ARCHITECTURE.md)
- [CodeMaestro v3 consolidated design v2 — current written-spec review candidate](docs/superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md)
- [Architecture decision log](docs/architecture/DECISIONS.md)
- [Research backlog / canonical research index](docs/research/RESEARCH-BACKLOG.md)
- [Legacy migration inventory](docs/architecture/MIGRATION-INVENTORY.md)

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
- [Logging ownership & timing amendment](docs/superpowers/specs/2026-09-04-logging-ownership-and-timing-amendment.md)
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

## Logging ownership

Repository-development logging and portable Skill behavior are deliberately separate:

- `logs/conversations/` — future real-time session history for the user's Chat / Work / Codex sessions developing this repository;
- `logs/logs/project/` — future real-time project mutation/state history maintained by those project-working sessions;
- `logs/logs/self-evolution/` — future dedicated audit stream owned by the CodeMaestro Self-Evolution protocol when that controller is implemented.

The nested `logs/logs/` name is intentional under the project owner's chosen root/subfolder structure, not an accidental typo.

Because this repository is public, any future committed session history must follow public-safe privacy/secret handling. The current consolidated design requires retention/deletion/sanitization policy to be resolved under CM-R-032 before Milestone 0 logging is declared operational.

## Next gate

After the current written-spec review is explicitly approved, Superpowers `writing-plans` is invoked. The resulting implementation plan must make **Milestone 0 — Repository Work-Session Logging Foundation** the first implementation milestone before other implementation work.

## Legacy systems

The following repositories are migration/reference sources only and are not target runtime dependencies:

- `heraklist/GPT_CodeMaesto_API`
- `heraklist/codemaestro-sbox`
- `heraklist/Custom-ChatGPT---Code-maesto-v2`

## Public repository security rule

Do not commit secrets, credentials, tokens, private `.env` values, production configuration, private keys, or other secret-bearing artifacts from the legacy system or project sessions to this repository.
