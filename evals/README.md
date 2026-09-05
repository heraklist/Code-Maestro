# CodeMaestro Eval Surfaces

CodeMaestro keeps **generation** and **grading** separate.

## Deterministic CI checks

CI may run deterministic, credential-free checks only: schemas, parsers, graders, corpus integrity, harness conformance, reproducibility fixtures, and other checks whose result does not require model inference.

- No model inference in CI.
- No model-graded CI.
- No LLM-as-judge grader.
- Deterministic routing-skeleton execution is a **harness/grader conformance regression**, not a qualifying model baseline and never contributes to the B7 verdict.

## Model-based interactive evals

Model-produced eval results are generated only inside an authorized interactive target surface using capabilities already available through the active ChatGPT / Codex / Work subscription. Their committed evidence may include structured per-case outputs, manifests, hashes, deterministic grader reports, instability vote patterns, and explicit limitations.

Every interactive model suite must declare an invocation budget before execution. Quota pressure may distribute work across windows or days, but it must not reduce the frozen corpus, required run count, or acceptance thresholds. Model identity is recorded for every qualifying run; if the exposed model identity changes inside a configuration, that configuration is invalidated and restarted from the beginning.

Cross-runtime conformance is evaluated separately per target surface. Results from different surfaces or model configurations are never averaged into one verdict.

See `docs/architecture/DECISIONS.md` CM-ADR-031 and `docs/evals/ROUTING-EVAL-PROTOCOL.md`.
