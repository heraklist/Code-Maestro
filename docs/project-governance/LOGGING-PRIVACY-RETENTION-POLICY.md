# Repository Logging Privacy & Retention Policy

**Status:** Milestone-0 narrow policy decision
**Date:** 2026-09-04
**Scope:** CodeMaestro repository work-session records only. This does not complete the broader CM-R-032 Privacy & Data Lifecycle Engineering research track.

## Scope

This policy governs repository-development records under:

```text
logs/conversations/
logs/logs/project/
```

and the public/private handling of source material used to create those records. `logs/logs/self-evolution/` is reserved for the later Skill-owned Self-Evolution audit contract and inherits the same privacy principles when implemented, but its operational policy is not activated by Milestone 0.

The repository is public. Therefore repository continuity value never overrides privacy, confidentiality, security, or legitimate deletion requirements.

## Storage classes

### Public repository record

May contain only sanitized, public-safe information needed for project continuity, audit, reconstruction, and evidence links.

Permitted examples:

- user-visible project discussion that is already safe for public disclosure;
- repository paths, branch names, public commit SHAs, public issue/PR identifiers;
- design decisions, validation results, and non-sensitive action summaries;
- explicit redaction markers in place of omitted sensitive material.

### Private/local raw transcript

Optional and not required for normal CodeMaestro repository operation.

Use only when a concrete continuity, evidentiary, or recovery need justifies retaining material that cannot safely be committed publicly. It must live in an authorized private/local storage location, not in the public repository, and its existence must not be implied unless actually created.

### Public digest/reference

When raw material must remain private, the repository may retain a sanitized summary, digest, or reference that preserves the project-relevant fact without revealing the private payload.

## Public-safe transcript rule

Before persistence to the public repository, session/project content is classified for public safety.

Do not commit:

- credentials, secrets, tokens, private keys, session cookies, private `.env` values;
- non-public personal data not necessary for the public engineering record;
- confidential client/business/internal material;
- private attachment contents or raw data whose public disclosure is not authorized;
- hidden chain-of-thought or other non-user-visible private model reasoning.

If a visible exchange contains mixed public and private content, persist only the minimum public-safe portion required for continuity and record that redaction/omission occurred.

## Retention

Retention is purpose-limited rather than indefinite-by-default.

### Public sanitized repository records

Sanitized conversation/project-event history may be retained while it continues to serve an active project purpose such as continuity, auditability, decision traceability, regression investigation, or historical reconstruction and while project authority continues to authorize retention.

Retention must be reconsidered when:

- the project ends or the record no longer serves a material engineering/audit purpose;
- the repository changes visibility or ownership;
- the data classification changes;
- a privacy/security concern is raised;
- an applicable policy/legal requirement changes.

No fixed universal duration is asserted by CodeMaestro. Duration is a project-authority decision informed by purpose, data sensitivity, and current applicable requirements.

### Private/local raw transcripts

Raw private copies are opt-in, purpose-specific, and should be retained only for as long as the concrete continuity/evidence need remains active. The person/project authority controlling that store must be able to revoke retention and delete the material.

## Deletion and purge

A legitimate privacy, security, confidentiality, or legal deletion requirement overrides ordinary semantic append-only behavior.

Authorized purge may include:

- deleting a file or selected private/local source material;
- removing a sensitive payload from current repository state;
- rewriting Git history when leaving the payload in historical commits would defeat the deletion requirement;
- removing copies/archives under project control where reasonably required by the deletion purpose.

After purge, retain only a non-sensitive purge event sufficient to show that sanitation occurred. The purge record must not reproduce, hash in a reversible/useful identifying way, quote, or otherwise preserve the removed secret/private payload.

Deletion authority belongs to the user/project/repository authority or another authority actually entitled to require the purge. CodeMaestro does not self-authorize history rewriting merely because it detects sensitive material.

## Redaction

Canonical secret marker:

```text
[REDACTED SECRET — not persisted]
```

Typed equivalents may be used for non-secret private/sensitive information, for example:

```text
[REDACTED PRIVATE DATA — not persisted]
[REDACTED CONFIDENTIAL CONTENT — not persisted]
```

A marker describes the omission without revealing the removed payload.

Redaction is applied before public persistence whenever possible. If sensitive content was already committed, use the authorized purge process rather than relying on a new marker alone.

## Access and authority

- Repository read/write availability is not authorization to publish private data.
- Public persistence requires content to be public-safe and within the repository work-session purpose.
- Creating or retaining a private/local raw transcript requires an actual authorized private storage location and a stated purpose.
- History rewrite/purge is consequential and requires project/user authority appropriate to the repository and data involved.
- Self-Evolution may not broaden these permissions or redefine retention authority.

## Review trigger

Re-review this policy when any of the following becomes material:

- repository visibility changes;
- logging begins to include a new class of personal/sensitive/confidential data;
- a new storage/backup/replication mechanism is introduced;
- Self-Evolution audit storage is activated;
- project ownership or access model changes;
- current law/regulation/contractual requirements materially affect retention/deletion;
- an incident demonstrates that current minimization/redaction controls are insufficient.

A policy review may change future retention behavior, but prior history is not silently rewritten except through an explicitly authorized deletion/sanitation process.

## Evidence basis

Authoritative sources reviewed on 2026-09-04:

1. NIST Privacy Framework — data processing spans the complete lifecycle, including collection, retention, logging, use, disclosure, and disposal.
   - https://www.nist.gov/privacy-framework
   - https://csrc.nist.gov/glossary/term/data_processing

2. NIST CSRC minimization definition — creation, collection, use, storage, maintenance, dissemination, and disclosure of PII should be limited to what is relevant/necessary for the authorized purpose and retained only as long as necessary for that purpose.
   - https://csrc.nist.gov/glossary/term/minimization

3. NIST SP 800-53 Rev. 5 — information disposal reduces security/privacy risk when information is no longer needed; disposal applies to originals, copies, archived records, and system logs that may contain PII.
   - https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf

These sources provide privacy-engineering/risk-management guidance rather than project-specific legal advice. Exact legal or contractual retention duties remain jurisdiction-, data-, and context-specific and must be researched separately when material.

## Decision

For Milestone 0, the narrow CM-R-032 prerequisite is resolved as follows:

```text
PUBLIC REPOSITORY
-> sanitized/public-safe continuity and project-event records only

PRIVATE/LOCAL RAW TRANSCRIPT
-> optional, purpose-specific, authorized, revocable retention

RETENTION
-> purpose-limited; no invented universal duration

DELETION/PURGE
-> privacy/security/legal requirement may override semantic append-only
-> authorized purge may include history rewrite where necessary
-> retain only non-sensitive purge evidence

REVIEW
-> trigger on data/storage/visibility/authority/legal-context change
```

Broader Privacy & Data Lifecycle Engineering remains `IN RESEARCH` under CM-R-032.
