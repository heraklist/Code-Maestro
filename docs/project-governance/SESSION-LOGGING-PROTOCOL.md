# CodeMaestro Repository Work-Session Logging Protocol

**Status:** Canonical Milestone-0 repository-development protocol
**Date:** 2026-09-04
**Owner:** Chat / Work / Codex sessions that develop or maintain `heraklist/Code-Maestro`

This protocol governs the user's project-working sessions for the CodeMaestro repository. It is **not** generic runtime behavior that the future portable `@codemaestro` Skill imposes on unrelated projects.

Normative companions:

- `LOGGING-SCHEMAS.md`
- `LOGGING-PRIVACY-RETENTION-POLICY.md`

## SESSION ADMISSION GATE

A project-working session with authorized repository access must establish logging continuity before material repository work.

Required sequence:

```text
1. identify the CodeMaestro repository;
2. inspect current branch and SHA/state;
3. read this protocol and the logging privacy policy;
4. locate or create the current session transcript;
5. read only recent/relevant project-event or transcript history needed for continuity;
6. append/capture session-start state using the canonical schema;
7. only then begin material project work.
```

If the session starts before the logging filesystem exists as part of Milestone 0 bootstrap, it must not fabricate prior persistence. Once the filesystem becomes operational, it creates a truthful first record whose `Coverage` field states the actual conversation/session coverage available.

If repository write capability is unavailable or unauthorized, the session states that durable repository logging is unavailable and must not claim persistence occurred.

## EVENT-TIME LOGGING

Logging is maintained as events occur, not reconstructed only at session end.

Append near the time of a material event, including when relevant:

- user/design/research approval or rejection;
- material requirements/scope decision;
- file creation/modification/deletion/move;
- branch/SHA/state change;
- commit creation;
- PR creation/update/state change;
- test/eval/validation failure or pass;
- research status/disposition change;
- correction/refutation/supersession;
- rollback/recovery;
- consequential database/deployment/external mutation;
- material blocker or capability limitation.

Use the project-event schema in `LOGGING-SCHEMAS.md`, including a stable `EVENT ID` for material events.

Do not convert a plan, dispatched command, pending workflow, or proposed action into a success event. Record the actual evidence state.

## Conversation history maintenance

`logs/conversations/` records public-safe user-visible session history and bounded observable action summaries required for continuity.

The transcript:

- may include user and assistant visible messages;
- may include material observable tool/action outcomes in summarized form;
- does not include hidden chain-of-thought;
- does not become normative authority merely because it is durable;
- uses `STATE CHANGE` entries rather than rewriting its historical header.

When exact earlier visible dialogue is unavailable to the current session, record the coverage boundary and continue from the available point. Never manufacture missing transcript history.

## PROGRESSIVE HISTORY LOADING

History follows the same progressive-disclosure principle as methodology.

At session start or resume:

```text
current canonical project state
+ current/recent project-event tail
+ latest relevant checkpoint
+ narrowly relevant transcript segments if needed
```

Do **not** ingest every historical conversation/log by default.

Read older history only when a concrete continuity/evidence question requires it, for example:

- missing rationale;
- contradictory historical intent;
- unresolved prior blocker;
- correction/supersession trace;
- user-requested historical reconstruction.

Current repository state, accepted specs/ADRs, and verified evidence outrank old conversation text.

## PRIVACY / REDACTION GATE

Before public persistence, apply `LOGGING-PRIVACY-RETENTION-POLICY.md`.

Mandatory rules:

```text
public repository -> public-safe sanitized records only
secrets/private keys/tokens -> never persist
non-public sensitive/confidential payload -> redact/omit
raw private transcript -> optional, authorized private/local storage only
```

Canonical secret marker:

```text
[REDACTED SECRET — not persisted]
```

Typed private/confidential markers may be used where appropriate. A marker must not reveal the omitted payload.

If sensitive material was already committed, do not treat a new redaction marker as sufficient remediation; follow the authorized purge/sanitation policy.

## Project-event ownership

`logs/logs/project/` answers:

> What actually changed in the CodeMaestro project, why, under what authority, and with what evidence/result?

It does **not** replace the conversation transcript and it does **not** contain the Self-Evolution reasoning ledger.

When a future Self-Evolution run causes an actual repository mutation:

- the Self-Evolution stream records why/how CodeMaestro researched/evaluated the change;
- the project stream records what actually changed;
- the two cross-reference using evolution ID, project `EVENT ID`, commit, or artifact.

## Semantic append-only rule

Under normal operation:

- append new facts/events;
- do not silently clean up prior failures or rejected decisions;
- append `CORRECTION / SUPERSEDES EVENT <event-id>` for historical errors;
- append rollback/recovery as new events;
- preserve the original event unless an authorized privacy/security purge requires actual deletion/history rewrite.

The privacy purge exception is explicit and does not convert ordinary editing into acceptable log rewriting.

## LOG WRITE FAILURE

If a required session/project log write fails, report the explicit status:

```text
LOG WRITE FAILED
```

Behavior:

### Consequential work

Pause further consequential mutation until one of the following is true:

1. the required audit/continuity write is restored; or
2. the user/project authority explicitly authorizes a safe alternative/fallback with the continuity limitation recorded.

### Low-risk analysis / research

May continue only when safe, while explicitly stating the continuity limitation and without claiming repository logging succeeded.

A logging failure is evidence about execution state, not permission to bypass the protocol.

## CHECKPOINT / HANDOFF GATE

Before session end, interruption, context transfer, or cross-surface handoff, append the canonical `CHECKPOINT` from `LOGGING-SCHEMAS.md` when write capability is available and authorized.

The checkpoint records, when material:

- current branch/SHA;
- last completed action;
- decisions/approvals;
- repository/external mutations;
- evidence/validation state;
- unresolved issues/risks;
- active Self-Evolution ID if applicable;
- next expected/authorized action.

A handoff is sufficient only if another project-working session can determine the current state and next action without relying on model memory or loading the full historical corpus.

## Session resume

On resume:

```text
read protocol
-> inspect current repo/branch/SHA
-> read latest relevant checkpoint
-> read recent project-event tail
-> read only transcript segments needed for continuity
-> compare durable state with actual repository state
-> append STATE CHANGE / correction if history is stale
-> continue
```

Do not assume a checkpoint is still current merely because it is the latest written record.

## Relationship to Self-Evolution

Repository work-session logging and CodeMaestro Self-Evolution logging are separate contracts.

`logs/logs/self-evolution/` is reserved for the future Self-Evolution Controller. Ordinary project-working chats must not write there merely because they are modifying CodeMaestro source/specs.

Only an explicit CodeMaestro `SELF` evolution/audit/research workflow activates the Skill-owned Self-Evolution audit behavior, when that controller exists and is authorized.

## Compliance evidence

Milestone 0 validates this protocol through executable tests and live drills covering at least:

- session admission/start;
- event-time append;
- stable event identifiers;
- correction/supersession;
- redaction without persisting a real secret;
- log-write failure behavior;
- checkpoint/handoff;
- progressive resume;
- ownership separation from Self-Evolution.
