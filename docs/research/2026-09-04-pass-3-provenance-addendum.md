# Comparative Research Pass 3 — Provenance Addendum

**Date:** 2026-09-04
**Applies to:** `2026-09-04-comparative-research-pass-3.md`
**Status:** PROVENANCE LIMITATION RECORDED

## Why this addendum exists

Comparative Research Pass 3 was conducted before CM-ADR-018 — provenance captured at production/retrieval time — had been fully operationalized as a repository documentation protocol.

The pass preserved source/repository identities and the mechanisms extracted from them, but exact upstream repository SHAs, access timestamps, URLs, and tool/runtime versions were not consistently persisted contemporaneously.

Those missing values must **not** be reconstructed later from model memory and presented as if they were original provenance.

## Evidence authority

Accordingly:

- Pass-3 comparative findings remain useful research evidence and historical rationale;
- repo-specific claims whose exact snapshot was not persisted are **pre-protocol / weaker-provenance evidence**;
- later canonical decisions may rely on the accepted mechanism only to the degree supported by the wider evidence corpus and subsequent verification;
- current/version-sensitive implementation claims require fresh authoritative verification;
- future research must follow CM-ADR-018 and capture source identity/version/state at retrieval/production time.

## Source identities retained by the original pass

The original record explicitly names or classifies sources including:

- `tomzx/agents`
- `trailofbits/skills`
- `facebookresearch/repoprover`
- `iannil/skills`
- `muratcankoylan/Agent-Skills-for-Context-Engineering`
- migration-specialized Skill collections
- product/document traceability systems

These names identify the comparative corpus but do not establish a precise immutable snapshot in the absence of the missing SHA/time metadata.

## Relationship to canonical decisions

The canonical wording of CM-ADR-019 through CM-ADR-022 lives in `../architecture/DECISIONS.md`.

The dated Pass-3 decision checkpoint is marked `ABSORBED INTO DECISIONS.md` and is historical/non-canonical where wording differs.

This addendum does not alter the accepted architecture. It bounds the evidentiary strength of the pre-protocol research material in accordance with CM-ADR-018 and CM-ADR-025.
