# CodeMaestro Conversation History

**Owner:** repository project-working Chat / Work / Codex sessions.

This directory stores sanitized, public-safe user-visible session history for development and maintenance of `heraklist/Code-Maestro`.

Canonical protocol:

`../../docs/project-governance/SESSION-LOGGING-PROTOCOL.md`

Canonical schemas:

`../../docs/project-governance/LOGGING-SCHEMAS.md`

Privacy/retention policy:

`../../docs/project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md`

## Rules

- session history is maintained event-time once operational;
- transcripts contain user-visible dialogue and bounded observable action summaries, never hidden chain-of-thought;
- public records are sanitized before persistence;
- unavailable earlier transcript content is not fabricated;
- conversation history is continuity/evidence, not canonical project authority;
- current repository state, accepted specifications/ADRs, and verified evidence outrank historical conversation text;
- corrections are appended rather than silently rewriting ordinary history, subject to the authorized privacy/security purge exception.
