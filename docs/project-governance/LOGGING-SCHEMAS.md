# CodeMaestro Repository Work-Session Logging Schemas

**Status:** Canonical Milestone-0 schema contract
**Date:** 2026-09-04
**Applies to:** repository-development session history and project-event logging for `heraklist/Code-Maestro`.

This document defines copy-ready schemas for the repository work-session logging protocol. It does not make repository conversation/project logging a generic behavior of the portable CodeMaestro Skill.

Privacy and retention are governed by `LOGGING-PRIVACY-RETENTION-POLICY.md`.

## Timestamp convention

Prefer offset-aware timestamps:

```text
YYYY-MM-DD HH:mm:ss ±HH:MM
```

Example:

```text
2026-09-04 13:42:17 +03:00
```

UTC ISO 8601 may additionally be stored where useful for cross-runtime correlation. A log entry should use one unambiguous time representation consistently.

## Identifier convention

### Session ID

Each project-working session has a stable session identifier for the lifetime of that session. When the host exposes a usable conversation/session identifier, it may be incorporated. Otherwise use a collision-resistant local identifier derived at session start.

Representative form:

```text
CM-SESSION-20260904T134217+0300-chat-a1b2c3
```

### EVENT ID

Every material project event receives a stable `EVENT ID` so later correction, supersession, rollback, cross-reference, or audit records have an unambiguous referent.

Representative form:

```text
CM-EVENT-20260904T134518+0300-a1b2c3
```

Requirements:

- unique within the CodeMaestro repository event history;
- immutable once emitted;
- not reused after a correction, rollback, deletion, or purge;
- timestamp may contribute to the identifier but timestamp alone is not assumed globally unique.

## Conversation session header

Each new transcript begins with a historical header equivalent to:

```text
# CodeMaestro Conversation Transcript

Session ID: <session-id>
Session started: <YYYY-MM-DD HH:mm:ss ±HH:MM>
Surface: <Chat | Work | Codex | other actual surface>
Repository: heraklist/Code-Maestro
Initial branch: <branch>
Initial SHA: <sha>
Purpose: <bounded session purpose>
Transcript policy: semantic append-only / public-safe
Coverage: <what portion of the user-visible session is actually represented>
```

The initial header is historical. If branch, SHA, scope, or other current state later changes, append a `STATE CHANGE`; do not rewrite the original header to pretend the new state was present at session start.

If the full earlier conversation is unavailable to the executing session, `Coverage` must state that limitation rather than claiming a complete transcript.

## Conversation entry

A normal public-safe conversation entry may use:

```text
### <YYYY-MM-DD HH:mm:ss ±HH:MM> — USER
<sanitized user-visible message>

### <YYYY-MM-DD HH:mm:ss ±HH:MM> — ASSISTANT
<sanitized user-visible response or bounded observable-action summary>
```

Only user-visible/session-observable material is persisted. Hidden chain-of-thought is never part of the transcript schema.

## STATE CHANGE entry

Use when branch/SHA/scope/runtime-relevant state changes materially:

```text
### <YYYY-MM-DD HH:mm:ss ±HH:MM> — STATE CHANGE
Session ID: <session-id>
Previous state: <bounded prior state>
Current state: <new state>
Reason: <why state changed>
Evidence: <commit/tool/result/reference>
```

## Project event schema

A material project event uses the following canonical fields when applicable:

```text
EVENT ID: <stable-event-id>
TIMESTAMP: <YYYY-MM-DD HH:mm:ss ±HH:MM>
SESSION: <session-id>
EVENT / TYPE: <event type>
TARGET: <file/system/branch/PR/research track/etc.>
ACTION: <what occurred>
REASON: <why it occurred>
BEFORE: <bounded prior state or NOT APPLICABLE>
AFTER: <bounded resulting state or NOT APPLICABLE>
EVIDENCE: <test/run/source/commit/artifact/status>
AUTHORITY: <user/project/system authority supporting the action>
RESULT: <PASS | FAIL | BLOCKED | PARTIALLY VERIFIED | other canonical evidence state>
RELATED COMMIT / ARTIFACT: <commit SHA/path/PR/evolution-id/etc. or NOT APPLICABLE>
```

Fields may be omitted only when genuinely inapplicable and the event remains unambiguous/reconstructable. `EVENT ID`, `TIMESTAMP`, `SESSION`, `EVENT / TYPE`, `TARGET`, `ACTION`, and `RESULT` are expected for material project events unless an extraordinary recovery/purge context prevents a field from being known.

## Representative event types

Examples include:

```text
DESIGN_APPROVED
RESEARCH_DECISION
FILE_CREATED
FILE_MODIFIED
FILE_DELETED
STATE_CHANGE
COMMIT_CREATED
PR_UPDATED
EVAL_FAILED
EVAL_PASSED
VALIDATION_FAILED
VALIDATION_PASSED
ROLLBACK
RECOVERY
PRIVACY_PURGE
CHECKPOINT
```

This is not a closed enum. New event names must remain specific, stable enough for audit use, and not silently redefine existing event semantics.

## CORRECTION / SUPERSEDES record

Historical errors are corrected by append, not ordinary rewrite:

```text
EVENT ID: <new-stable-event-id>
TIMESTAMP: <YYYY-MM-DD HH:mm:ss ±HH:MM>
SESSION: <session-id>
EVENT / TYPE: CORRECTION
CORRECTION / SUPERSEDES EVENT <prior-event-id>
Previous statement: <bounded description of the earlier incorrect state>
Corrected state: <correct state>
Evidence: <source/commit/result proving correction>
Authority: <authority for correction>
Result: <verification status>
```

The original event remains in ordinary audit history. The privacy/security purge exception in the logging privacy policy is separate and may require authorized removal/history rewrite.

## Redaction record

Never persist a real secret merely to prove that redaction works.

Canonical secret marker:

```text
[REDACTED SECRET — not persisted]
```

Typed markers may include:

```text
[REDACTED PRIVATE DATA — not persisted]
[REDACTED CONFIDENTIAL CONTENT — not persisted]
```

A redaction note may use:

```text
TIMESTAMP: <YYYY-MM-DD HH:mm:ss ±HH:MM>
SESSION: <session-id>
EVENT / TYPE: REDACTION
TARGET: <conversation/project-event location>
ACTION: Sensitive payload omitted before public persistence
EVIDENCE: <classification reason without reproducing payload>
RESULT: REDACTED
```

## CHECKPOINT schema

Before session end, interruption, or cross-surface handoff, append:

```text
## CHECKPOINT
TIMESTAMP: <YYYY-MM-DD HH:mm:ss ±HH:MM>
SESSION: <session-id>
CURRENT BRANCH: <branch>
CURRENT SHA: <sha>
LAST COMPLETED ACTION: <action>
DECISIONS / APPROVALS: <material decisions or NONE>
MUTATIONS: <material repository/external mutations or NONE>
EVIDENCE / VALIDATION STATE: <actual executed evidence/status>
UNRESOLVED ISSUES / RISKS: <items or NONE>
ACTIVE SELF-EVOLUTION ID: <id or NOT APPLICABLE>
NEXT EXPECTED / AUTHORIZED ACTION: <next action>
```

A checkpoint reports actual state; it must not promote planned, dispatched, or unexecuted work to completed status.

## Cross-reference rules

When material, preserve links among:

```text
CONVERSATION
<-> DECISION / AUTHORITY
<-> PROJECT EVENT ID
<-> COMMIT / ARTIFACT / EVIDENCE
```

If a later Self-Evolution run causes a repository mutation, the future Self-Evolution audit record and project event cross-reference the evolution ID and relevant event/commit/artifact. Ordinary project sessions do not write Self-Evolution rationale into the reserved Self-Evolution stream.

## Append-only semantics

Under ordinary operation:

- existing events are not silently rewritten, reordered, or deleted;
- corrections, refutations, supersessions, and rollbacks append new records;
- current repository state may supersede historical state without erasing that history;
- legitimate privacy/security/legal purge follows the explicit deletion/sanitation exception in `LOGGING-PRIVACY-RETENTION-POLICY.md`.

Git version history is useful evidence but is not claimed to provide cryptographic immutability.
