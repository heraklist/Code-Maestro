# Routing Pilot — Skeleton v0

## Evidence identity

- Corpus: `evals/routing/pilot-real-derived.json`
- Skeleton: `evals/routing/skeleton-v0.json`
- Result: `evals/routing/results/pilot-skeleton-v0.json`
- Grader: `tools/routing_eval.py`
- Pilot size: 10 cases / 10 ambiguity clusters
- Provenance: 10/10 real-derived; 0 synthetic

## Diagnostic metrics

The full 100-case GREEN gate does **not** apply to this pilot.

| Metric | Result |
|---|---:|
| Primary | 7 / 10 |
| Supporting exact set | 1 / 10 |
| Clarification | 10 / 10 |
| Unknown capability IDs | 0 |
| Malformed results | 0 |
| High-risk primary + clarification | 2 / 3 |

## Primary failures

### `testing-review-001`

- Expected primary: `review-audit-compliance`
- Skeleton primary: `testing-assurance`
- Classification: **SKELETON SIGNAL GAP**
- Reason: the prompt is explicitly an audit of assurance quality. A defensible primary owner exists (`review-audit-compliance`), but repeated `test`/`assurance` lexical signals outweigh the single `audit` signal in the deliberately primitive skeleton.
- Taxonomy implication: none yet. The case supports a boundary rule that task intent (`audit`) can dominate subject matter (`tests`).

### `performance-reliability-001`

- Expected primary: `performance-capacity`
- Skeleton primary: `reliability-observability-sre-incident`
- Classification: **SKELETON SIGNAL GAP**
- Reason: sustained-load latency is a defensible Performance/Capacity primary problem, with timeouts/observability as reliability support. The skeleton overweights multiple reliability words instead of the causal load/latency objective.
- Taxonomy implication: boundary needs explicit causal/goal semantics in the future contract/eval set, but both families remain defensible and composable.

### `ai-interface-security-001`

- Expected primary: `ai-llm-agent-mcp`
- Skeleton primary: `security-trust`
- Classification: **SKELETON SIGNAL GAP**
- Reason: the object being reviewed is an LLM/tool-calling system, so AI/LLM/Agent/MCP owns the primary domain review while Security, Privacy, and Interface are supporting concerns. The lexical skeleton counts the numerous security terms and loses the subject-domain signal.
- Taxonomy implication: future routing must distinguish primary domain ownership from cross-cutting risk modifiers.

## Supporting-set failures

Nine of ten exact supporting sets differ. This is expected to be highly sensitive to the minimal skeleton's raw keyword scoring. The failures are retained as evidence for later contract/composition design; expected sets are not edited to improve the score.

The only exact supporting-set match is `product-frontend-001`.

## Clarification behavior

All ten pilot expectations currently specify `clarification_required=false`, and the skeleton returns false for all ten. This pilot therefore does **not** yet challenge clarification discrimination. The 100-case corpus must include genuine clarification-required cases as required by the approved plan.

## Early taxonomy-stop rule

Observed cases classified `TAXONOMY BOUNDARY AMBIGUOUS`: **0 / 10**.

Distinct clusters with no defensible primary owner after architecture/provenance review: **0**.

Therefore neither early-stop condition is met:

```text
>=3 taxonomy-boundary-ambiguous cases: NO
>=2 clusters with no defensible primary owner: NO
```

## Decision

**CONTINUE**

The pilot does not validate the 17-family taxonomy. It provides an initial falsification attempt that produced three primary-routing failures, all attributable at this stage to the intentionally minimal signal model rather than inability to assign a defensible primary capability. Expand to the provenance-balanced 100-case corpus and use the observed Review-vs-Testing, Performance-vs-Reliability, and AI-domain-vs-Security boundaries as stress targets.
