# Routing Evals

This directory contains the pre-registry routing challenge corpus, deterministic baseline skeleton inputs/outputs, and evidence artifacts.

## Contract

- Expectations are committed before outputs are generated.
- Capability IDs are the 17 provisional first-generation IDs defined by the approved architecture.
- Supporting capability sets are compared as sorted unique sets.
- The deterministic grader is implemented in `tools/routing_eval.py`.
- Structural validity is necessary but does not prove routing quality.
- The 10-case pilot is diagnostic and does not use the full-corpus GREEN gate.
- The full corpus requires at least 100 cases, at least 10 per ambiguity cluster, and at least one third real-derived provenance.
- Model/runtime result generation is evaluated with at least three independent runs per configuration; the worst complete run controls GREEN.

## Evidence order

```text
precommitted corpus expectations
-> committed minimal skeleton/config
-> generated result artifact
-> deterministic grader report
-> failure classification / taxonomy decision
```

Never edit expected labels merely to match an observed result. Corrections require a new corpus version or an explicit correction record.
