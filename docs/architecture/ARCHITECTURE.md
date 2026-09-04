# CodeMaestro Architecture

## Status

**CANONICAL GATEWAY — detailed canonicalization pending written-spec approval**

The previous body of this living architecture file became stale during the 2026-09-04 architecture/research expansion and is intentionally no longer presented as current architecture text.

Until the written-spec gate is approved and full canonicalization is performed, the current architecture authority is:

1. `../superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md` — current consolidated written-spec review candidate;
2. `DECISIONS.md` — canonical accepted ADR wording;
3. `../research/RESEARCH-BACKLOG.md` and its referenced research records — canonical research queue/index;
4. dated acceptance checkpoints in this directory, including Pass 4 and Pass 5.

Historical versions of this file remain available in Git history. They must not be used as current authority where they conflict with the sources above.

## Current architecture summary

CodeMaestro is designed as one public `@codemaestro` Skill with internally composed engineering capabilities, Shared Intelligence, execution/governance, and optional independent roles.

Core current constraints include:

- `CAPABILITY != SKILL != ROLE != TOOL`;
- tool-independent methodology, tool-aware execution;
- evidence before assertion;
- state before mutation;
- validation before success claims;
- availability is not authorization;
- routing cannot create authority;
- one public Skill, with internal modularity and progressive disclosure;
- capability-first behavior across Chat, Work, Codex, and future surfaces;
- protected Project Quality Contract;
- accepted Pass-5 Capability Freeze, reopenable by real eval/task evidence;
- Command-Gated Self-Evolution that cannot self-expand authority;
- repository development logs and portable Skill Self-Evolution logging have distinct ownership boundaries.

The canonical capability-family definitions, Shared Intelligence model, routing/composition contract, cross-runtime contract, Self-Evolution protocol, evaluation model, logging ownership boundary, and post-review milestone ordering are defined in the consolidated v2 design linked above.

## Documentation governance

This file will be expanded back into a full living architecture **after** the current written-spec candidate passes review. That canonicalization is intentionally scheduled after Milestone 0 repository work-session logging, per the approved ordering in the consolidated v2 design.

No production `SKILL.md`, runtime modules, scripts, or eval implementation are authorized by this gateway file.
