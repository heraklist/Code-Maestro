# CodeMaestro Self-Evolution Audit — Reserved Namespace

**Reserved owner:** future CodeMaestro Self-Evolution Controller.

Milestone 0 reserves this directory only. It does **not** implement Self-Evolution behavior and ordinary repository project-working sessions must not use this stream as a substitute for project-event logging.

When the Self-Evolution Controller is implemented, explicit CodeMaestro `SELF` research/audit/upgrade runs will maintain dedicated records here according to the canonical Self-Evolution contract.

Repository mutations caused by a future Self-Evolution run will be represented in both domains:

- this stream: why/how CodeMaestro researched, evaluated, promoted, rejected, or rolled back the candidate;
- `../project/`: what actually changed in the repository.

The records cross-reference by evolution ID, project `EVENT ID`, commit, and/or artifact.

Conversation transcripts are not default Self-Evolution input and remain evidence rather than authority.
