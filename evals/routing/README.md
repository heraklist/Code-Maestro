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

## Minimal skeleton v0

`skeleton-v0.json` is intentionally not a production router and does not contain full capability contracts. For each capability, `tools/routing_skeleton.py` counts normalized configured trigger phrases found in the prompt and subtracts configured exclusion-phrase matches, floored at zero. Capabilities are ranked by descending score and then by the stable `capability_order` in the config.

If every capability scores zero, the skeleton returns `requirements-architecture-systems` and requests clarification. If multiple capabilities tie for the highest non-zero score, the stable first capability becomes the mechanical primary and `clarification_required=true`. Every other positively scoring capability is returned as supporting in stable rank order. The same prompt/config therefore produces the same decision.

The skeleton is frozen before pilot output generation. Pilot expected labels are not encoded as unit-test answers.

## Evidence order

```text
precommitted corpus expectations
-> committed minimal skeleton/config
-> generated result artifact
-> deterministic grader report
-> failure classification / taxonomy decision
```

Never edit expected labels merely to match an observed result. Corrections require a new corpus version or an explicit correction record.
