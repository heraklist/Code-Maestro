# CodeMaestro Routing Evaluation Protocol

## Status

**Status:** ACTIVE PRE-REGISTRY EVAL PROTOCOL

## Purpose

Challenge the provisional 17-family capability taxonomy before full capability contracts or production routing are authored.

## Evidence ordering

Expected routing labels and provenance are committed before any candidate routing output is generated. Candidate outputs never retroactively define the expected answer.

## Deterministic grading

`tools/routing_eval.py` parses cases/results and computes exact metrics. Given the same case JSON, result JSON, and grader version, grading is deterministic. Supporting capability order is normalized before exact-set comparison.

## Stochastic generation

A model/runtime may produce different result JSON across runs. Full candidate evaluation therefore requires at least three independent runs per runtime/model configuration. Each run records the runtime surface, provider/model identifier exposed by the environment, configuration/version when available, corpus identity, candidate/skeleton identity, grader version, run identity, timestamp, and artifact path. Unavailable metadata is recorded as `NOT AVAILABLE`, never invented.

The aggregate decision uses the worst complete run. Means and dispersion are descriptive only and cannot rescue a failing worst run.

## Full-corpus GREEN gate

Each qualifying run must satisfy all of:

- primary accuracy >= 90%;
- supporting exact-set accuracy >= 80%;
- clarification accuracy >= 90%;
- unknown capability IDs = 0;
- malformed results = 0;
- high-risk fail-closed cases = 100%;
- every ambiguity cluster has at least 10 cases and at least 9/10 primary decisions correct; when a cluster has more than 10 cases, at most one primary failure is permitted unless the approved spec is amended before execution.

## Pilot semantics

The first 10 real-derived cases are diagnostic. Full-corpus GREEN thresholds do not apply. Pilot failures are classified by boundary cause before any taxonomy decision. If at least three cases reveal taxonomy-boundary ambiguity, or at least two clusters have no defensible primary owner after provenance/architecture review, the taxonomy is reopened before corpus expansion, registry work, or capability contracts.

## Corpus-quality safeguard

If the minimal pre-contract skeleton unexpectedly passes every full GREEN threshold on a sufficiently sized challenge corpus, treat that as a corpus-quality warning. Review provenance, difficulty, leakage, and expected-label construction before accepting the result.
