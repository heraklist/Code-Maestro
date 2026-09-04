# Routing evaluation results

This directory stores immutable result and manifest artifacts for frozen routing corpora.

## Repeated-run contract

A qualifying runtime/model configuration requires at least three complete independent runs over the same frozen corpus, skeleton, and grader identity. Each run has a `RunManifest` recording `run_id`, runtime surface, provider, exposed model identifier/version, configuration, corpus SHA-256, skeleton SHA-256, grader version, start timestamp, and result path.

Unavailable model/version metadata is recorded literally as `NOT AVAILABLE`; required manifest fields are never omitted or left empty.

Aggregation is valid only when corpus SHA-256, skeleton SHA-256, and grader version match across the repeated runs. Statistics report min/max/mean/population-standard-deviation for primary, exact supporting-set, and clarification accuracy. Descriptive statistics never override the gate: fewer than three runs cannot be GREEN, and every complete run must independently satisfy `is_green()`; therefore the worst complete run governs readiness.

Do not edit frozen expectations, skeleton configuration, or grader semantics between repeated runs. Any such change starts a new configuration/evidence series.
