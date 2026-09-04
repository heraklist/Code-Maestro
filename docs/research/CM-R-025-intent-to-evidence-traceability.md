# CM-R-025 — Intent-to-Evidence Traceability & Drift Propagation

**Priority:** P0
**Status:** IN RESEARCH
**Accepted:** 2026-09-04

## Research question

How should CodeMaestro preserve bidirectional traceability from user intent through requirements, decisions, specifications, implementation plans, code, tests, evals, and observed evidence, while detecting drift and invalidating stale approvals without creating heavyweight process for trivial work?

## Accepted direction

CodeMaestro will treat traceability as a cross-cutting mechanism rather than as documentation bookkeeping.

Conceptual chain:

```text
USER INTENT
   ↕
REQUIREMENTS
   ↕
DECISIONS / SPECIFICATION
   ↕
IMPLEMENTATION PLAN
   ↕
CODE
   ↕
TESTS / EVALS
   ↕
OBSERVED RESULT / OPERATIONAL EVIDENCE
```

Traceability must work in both directions:

- forward: intended behavior → design → implementation → verification;
- backward: actual code/test/runtime reality → affected plans/specifications/requirements.

## Research scope

Study and define:

- stable identifiers for material requirements, decisions, findings, tests, and evidence when justified;
- adjacency links and end-to-end traceability;
- orphan detection;
- stale-approval invalidation;
- code-to-spec and evidence-to-requirement back-propagation;
- traceability across repository revisions;
- relationship to provenance under CM-R-020;
- relationship to repository/architecture drift under CM-R-022;
- minimal vs rigorous traceability profiles;
- eval scenarios for broken, stale, orphaned, contradictory, and over-specified artifact chains.

## Candidate orphan classes

- requirement with no implementation;
- requirement with no verification;
- implementation behavior with no current authority where explicit authority is required;
- test that verifies behavior no longer required;
- specification that contradicts accepted code reality;
- plan that targets superseded architecture;
- accepted finding whose underlying evidence no longer matches the current repository state.

## Design constraints

1. Do not turn every small task into requirements bureaucracy.
2. Stable IDs are used where maintenance value exceeds ceremony cost.
3. Code reality may invalidate documentation, but code does not silently become normative authority.
4. Artifact invalidation must be explicit and evidence-backed.
5. Traceability claims must bind to repository/version provenance where material.
6. The mechanism must survive context resets and multi-agent handoffs.

## Representative reference systems

- `tomzx/agents` — SDLC back-propagation, assumptions/questions/decisions, approval regression.
- Cusp / Cusp Steward — normative authority and evidence separation.
- Trail of Bits spec-to-code compliance — requirement-by-requirement implementation evidence.
- GitNexus — repository/source impact and provenance concepts.

## Expected output

- traceability data/relationship model;
- proportional-rigor rules;
- artifact invalidation semantics;
- orphan taxonomy;
- drift propagation workflow;
- integration with Research Lab, Repository Intelligence, Evidence, testing, and migration workflows;
- baseline eval design.

## Non-decision

This research item does not require a standalone Traceability Skill. Physical packaging remains eval-driven.
