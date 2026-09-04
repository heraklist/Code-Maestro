# CM-R-028 — Performance, Benchmarking & Capacity Engineering

**Priority:** P1 by default; P0 for performance-critical or resource-critical systems
**Status:** IN RESEARCH
**Started:** 2026-09-04

## Question

How should CodeMaestro measure, diagnose, optimize, benchmark, and capacity-plan software systems without relying on premature optimization, misleading microbenchmarks, or stale platform-specific thresholds?

## Why this is distinct

Frontend performance and SRE cover only parts of the problem. CodeMaestro also needs a general method that works across languages, runtimes, compilers, databases, services, data pipelines, distributed systems, and infrastructure.

The governing principle is:

```text
performance requirement / workload model
→ representative baseline
→ measurement / profiling / tracing
→ bottleneck or saturation evidence
→ competing hypotheses
→ targeted optimization or capacity decision
→ same-condition comparison
→ regression gate
→ production observation where relevant
```

## Research scope

Study a portable methodology for:

- workload definition and representativeness;
- baseline capture;
- latency distributions and tail latency;
- throughput;
- CPU, memory, allocation, GC, storage, I/O, and network;
- queueing, saturation, contention, locks, pools, and backpressure;
- cold-start and warm-state behavior;
- load, stress, spike, endurance/soak, and recovery testing;
- benchmark reproducibility and variance;
- profiler/tracer/tool selection;
- bottleneck hypothesis discrimination;
- capacity/headroom planning;
- elasticity/autoscaling lag and stability;
- retry amplification and overload behavior;
- cost-performance trade-offs;
- performance regressions and budgets;
- current platform/runtime threshold research.

## Core hypotheses to test

1. Performance decisions should be grounded in a representative workload and baseline rather than generic optimization checklists.
2. A valid optimization claim requires comparable before/after conditions and evidence that the intended bottleneck or user-facing metric improved.
3. System performance often depends on saturation, queues, pools, retries, cold starts, and elasticity rather than local code speed alone.
4. Static vendor/platform thresholds should remain dynamic research unless stable standards justify local encoding.
5. Performance testing should integrate with release/readiness evidence when regressions materially affect users, cost, or reliability.

## Evidence contract

Performance evidence should capture, when relevant:

- target identity and version;
- workload/scenario definition;
- input/data shape;
- environment and resource configuration;
- warm-up policy;
- sample/repetition count;
- measurement tool/version;
- raw distribution or summary statistics;
- baseline/candidate comparability;
- variance and known confounders;
- resource/cost footprint;
- pass/fail/regression threshold and its authority;
- limitations and unmeasured surfaces.

A faster microbenchmark must not be presented as proof of a faster end-to-end system unless the relationship is demonstrated.

## Relationship to existing tracks

- **CM-R-006** — performance regression tests within the Assurance Ladder.
- **CM-R-007** — database-specific performance research.
- **CM-R-009** — runtime observability, user-facing SLOs, saturation, production evidence.
- **CM-R-010** — frontend accessibility/performance specialization.
- **CM-R-014** — distributed-system queueing, retries, contention, partial failure.
- **CM-R-015** — performance readiness/release gates.
- **CM-R-016** — language/runtime/toolchain-specific profiler discovery.
- **CM-R-020** — benchmark provenance, coverage, reproducibility, target fidelity.
- **CM-R-026** — performance comparison during migration/cutover where material.

## Expected output

- general performance investigation workflow;
- workload and baseline contract;
- profiler/tool-selection model;
- benchmark reproducibility and statistics guidance;
- load/stress/spike/soak methodology;
- capacity/headroom/elasticity reasoning;
- cost-performance decision framework;
- performance regression gate model;
- dynamic-source policy for fast-changing platform guidance;
- baseline eval scenarios.

## Preferred authorities

Prefer current primary sources:

1. language/runtime/compiler profiler and performance documentation;
2. database/platform/cloud primary performance and capacity guidance;
3. primary benchmarking and observability tooling documentation;
4. established systems/performance engineering literature;
5. workload-specific standards/specifications where applicable.

Community optimization recipes are discovery material, not canonical evidence.

## Physical Skill boundary

This research item does **not** authorize a standalone performance Skill. Physical packaging remains eval-driven.
