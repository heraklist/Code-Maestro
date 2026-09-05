# CM-ADR-031 Scope Correction — Subscription-only scope (Part 1)

**Status:** Accepted correction — 2026-09-05

**Authority:** User-approved clarification of CM-ADR-031. This artifact narrows and clarifies the existing ADR without changing the frozen routing corpus, expectations, skeleton, or deterministic grader. Until `DECISIONS.md` is mechanically consolidated, this correction is authoritative wherever the earlier CM-ADR-031 wording conflicts with it.

## Decision

### Part 1 development and evals

CodeMaestro Part 1 is developed and evaluated without OpenAI API execution, API keys, or API billing initiated by the project. Development and model-based eval generation use Chat / Work / Codex capabilities available through the project's existing ChatGPT subscription and ChatGPT sign-in. Deterministic checks remain eligible for CI; model inference remains interactive.

### Part 1 runtime

CodeMaestro does **not require** API access and never initiates its own API calls as a Skill requirement. The authentication mechanism used by the host surface is outside the Skill's authority and does not change CodeMaestro behavior. A user whose Codex host is authenticated with an API key is not rejected or artificially degraded merely because of that host-level authentication choice.

This preserves the distinction between:

- project development/eval governance, which is subscription-only for Part 1; and
- host authentication/runtime capability, which belongs to the user and host surface rather than the Skill.

### Part 2 portability

Portability to non-OpenAI LLM providers is deferred until CodeMaestro v1 / Part 1 is complete. Part 2 will use a separate repository/workstream derived from the completed Part 1 repository. It is not a gate, requirement, or validation target for Part 1.

Deferral of non-OpenAI validation does **not** authorize provider-specific assumptions in the methodology core. The existing tool-independent methodology, runtime capability declaration, and cross-runtime contract remain architectural constraints. Their validation against non-OpenAI providers is deferred; their abstraction is not removed.

## Repository lineage and canonical authority

The current `heraklist/Code-Maestro` repository remains the canonical architecture record for CodeMaestro Part 1 and for provider-neutral methodology decisions established before the Part 2 split.

When Part 2 is created:

1. it records the exact source repository and source commit from which it was derived;
2. Part 1 remains canonical for shared methodology unless a later explicit architecture decision transfers ownership;
3. portability-specific adaptations belong to the Part 2 repository and do not silently redefine Part 1;
4. a correction that applies to shared methodology must be proposed against the canonical Part 1 record first, then propagated to Part 2 with source decision/commit traceability;
5. a Part 2 discovery that reveals a defect in shared methodology is evidence for an upstream Part 1 architecture correction, not an implicit fork-only override.

This prevents the two repositories from becoming independent competing architecture authorities and preserves bidirectional traceability consistent with CM-ADR-019.

## Eval consequences

B7 and the Capability Freeze are explicitly coverage-bounded:

> **Scope: OpenAI Chat / Work / Codex surfaces only. This evidence is not an indication of behavior on other LLM providers.**

A B7 result may support or challenge the provisional capability taxonomy for the assessed OpenAI Part 1 surfaces only. It must not be generalized to non-OpenAI providers.

The earlier deterministic skeleton result remains narrower still: it establishes only that the frozen corpus is not trivially keyword-separable by `skeleton-v0`; it is not evidence of model difficulty.

## Relationship to original CM-ADR-031

The following earlier interpretation is superseded for Part 1 development/evals: that project development may itself use optional authorized API access when present. Part 1 project development/evals do not do so.

The no-artificial-degradation principle remains intact at runtime because host authentication is outside the Skill's authority and optional host capabilities may still be discovered and used through the host surface when authorized.
