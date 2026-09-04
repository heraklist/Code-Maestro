# CM-R-027 — Interface, Protocol & Contract Engineering

**Priority:** P1
**Status:** IN RESEARCH
**Started:** 2026-09-04

## Question

How should CodeMaestro design, review, evolve, migrate, and verify consumer-facing and system-to-system contracts across APIs, RPC, events, streams, webhooks, schemas, and protocol boundaries?

## Why this is distinct

Interfaces are durable behavioral agreements, not merely route lists or serialized schemas. Correctness depends on semantics, ownership, compatibility, delivery behavior, consumer assumptions, failure modes, and deployed-boundary evidence.

General architecture guidance does not by itself provide enough precision for interface evolution. Migration methodology handles cutover mechanics but does not own contract semantics. Security review covers threats but does not own consumer-visible behavior.

## Research scope

Study a portable methodology for:

- consumer jobs and domain meaning;
- authoritative data/schema ownership;
- null vs absent semantics, defaults, identifiers, units, ordering, filtering, and pagination;
- authorization expectations and preconditions;
- mutation semantics, idempotency scope/equivalence, retries, deadlines, concurrency, partial outcomes, and errors;
- synchronous and asynchronous delivery contracts;
- duplicate, gap, reorder, reconnect, checkpoint, and replay semantics;
- resource limits, quotas, and abuse boundaries;
- consumer-aware compatibility assessment;
- deprecation and evolution policy;
- contract migration and rollback integration with CM-R-026;
- misuse-resistance / pit-of-success analysis;
- multi-boundary verification.

## Multi-boundary verification model

Research should preserve at least these distinct evidence boundaries:

1. **Contract** — syntax/schema validation, references, examples, negative examples, documented semantics.
2. **Provider** — implementation conformance for success, failure, authorization, limits, concurrency, and side effects.
3. **Consumer** — actual client/consumer expectations, generated-client behavior, strict/tolerant decoding, fixtures.
4. **Compatibility** — consumer-relative behavioral and schema change assessment.
5. **Deployed** — end-to-end validation against the intended environment with telemetry and rollback evidence where applicable.

A schema linter, generated document, mock, or provider test must not be presented as stronger evidence than the boundary it actually verifies.

## Core hypotheses to test

1. Compatibility is consumer-relative; additive changes are not automatically safe.
2. Interface contracts need explicit failure, retry, concurrency, idempotency, and delivery semantics to be reviewable.
3. Deployed-boundary verification catches failures invisible at contract/provider/mock layers.
4. Misuse resistance should be evaluated as part of secure interface quality.
5. A shared contract methodology can cover REST, GraphQL, RPC, events, streams, webhooks, and data contracts without one Skill per interface family.

## Relationship to existing tracks

- **CM-R-002 / CM-R-003** — secure and misuse-resistant interface design.
- **CM-R-006** — contract and conformance testing within the Assurance Ladder.
- **CM-R-014** — distributed delivery/ordering/consistency invariants.
- **CM-R-020** — evidence provenance, coverage, and target fidelity.
- **CM-R-024** — spec-to-code compliance and finding verification.
- **CM-R-025** — traceability from intent/spec to interface implementation and deployed evidence.
- **CM-R-026** — compatibility migration, deprecation, cutover, rollback.

## Expected output

- semantic contract model and template;
- provider/consumer ownership model;
- interface selection and trade-off criteria;
- sync/async delivery semantics;
- error/idempotency/retry/concurrency contract model;
- consumer-aware compatibility assessment;
- deprecation/evolution methodology;
- multi-boundary verification strategy;
- misuse-resistance review integration;
- baseline eval scenarios.

## Preferred authorities

Prefer current primary sources:

1. protocol and API standards/specifications;
2. official OpenAPI, AsyncAPI, GraphQL, gRPC/Protocol Buffers and relevant ecosystem specifications/documentation;
3. official platform/provider guidance for target-specific behavior;
4. mature contract-testing/evolution projects where primary specifications do not answer the engineering question;
5. high-quality secondary material only when necessary.

Exact current behavior remains subject to CodeMaestro's research/freshness and target-fidelity rules.

## Physical Skill boundary

This research item does **not** authorize a standalone interface Skill or one Skill per protocol. Physical packaging remains eval-driven.
