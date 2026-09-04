# Code Maestro

CodeMaestro is being rebuilt as a next-generation, portable software-engineering Skill.

The project preserves the useful engineering methodology, safety boundaries, validation discipline, and domain playbooks from the legacy Custom GPT while removing the old custom Actions/API infrastructure.

## Current phase

Architecture and research preparation.

Production Skill files, runtime references, scripts, and eval implementations have **not** been created yet. The repository currently establishes the canonical architecture, migration ledger, decisions, research backlog, and implementation planning foundation.

## Canonical project documents

- [Living architecture](docs/architecture/ARCHITECTURE.md)
- [Legacy migration inventory](docs/architecture/MIGRATION-INVENTORY.md)
- [Architecture decision log](docs/architecture/DECISIONS.md)
- [Research backlog](docs/research/RESEARCH-BACKLOG.md)
- [CodeMaestro v3 architecture design checkpoint](docs/superpowers/specs/2026-09-04-codemaestro-v3-architecture-design.md)
- [Architecture documentation foundation plan](docs/superpowers/plans/2026-09-04-architecture-documentation-foundation.md)

## Architectural direction

The target is a Skill-first system with:

- tool-independent engineering methodology;
- native-tool execution where authorized capabilities exist;
- evidence-before-assertion;
- state-before-mutation;
- validation-before-success claims;
- dynamic authoritative research for version-sensitive guidance;
- progressive disclosure through focused references;
- eval-driven development and regression protection;
- zero CodeMaestro-specific runtime infrastructure by default.

The migration goal is **behavioral parity and improvement**, not recreation of the legacy API surface.

## Legacy systems

The following repositories are migration/reference sources only and are not target runtime dependencies:

- `heraklist/GPT_CodeMaesto_API`
- `heraklist/codemaestro-sbox`
- `heraklist/Custom-ChatGPT---Code-maesto-v2`

## Public repository security rule

Do not commit secrets, credentials, tokens, private `.env` values, production configuration, or secret-bearing artifacts from the legacy system to this repository.
