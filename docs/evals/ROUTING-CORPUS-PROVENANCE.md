# Routing Corpus Provenance

## Pilot v0 — precommitted before skeleton output

The pilot contains exactly one case per approved ambiguity cluster. Expectations were authored before `skeleton-v0` exists. No observed router output was used to choose labels.

| Case | Source | Why representative | Transform |
|---|---|---|---|
| `build-ci-debug-001` | Current project review, v2 §11 | Real ambiguity explicitly raised during review: local build succeeds, CI fails after dependency bump. | Repository-neutral wording. |
| `implementation-debug-001` | Current project review, v2 §6 | Confirmed checker false negative required diagnosis before implementation. | Removed CM-R-specific wording from prompt while retaining failure semantics. |
| `testing-review-001` | Current project review, v2 §6 | Review challenged whether exact-string documentation tests provide meaningful assurance. | Framed as audit-only request to separate Review from Testing implementation. |
| `security-privacy-001` | Current project review, v2 §8 | Real gap between secret/privacy policy and executable enforcement. | Generalized repository names; retained security/privacy composition. |
| `database-interface-001` | Legacy repository audit playbook | Legacy audit scenario explicitly identifies missing tenant filtering as a data/security defect visible through an API. | Removed framework names; retained database/API boundary. |
| `migration-implementation-001` | Legacy dependency-maintenance playbook | Package-manager migration is a concrete legacy workflow with compatibility and validation obligations. | Generalized package managers. |
| `performance-reliability-001` | Legacy validation rules | Legacy Performance Gate requires bottleneck classification before optimization. | Added sustained-load/timeouts to expose Performance vs Reliability boundary. |
| `product-frontend-001` | Current CodeMaestro consolidated design / real project workflow pattern | Product experience direction must precede component implementation when the problem is interaction hierarchy rather than broken code. | Product-specific UI names removed. |
| `research-language-freshness-001` | Legacy maintainer instructions | Legacy contract explicitly forbids inventing unfamiliar/version-sensitive APIs, versions, packages, and CLI flags. | Converted rule into a niche-language implementation request. |
| `ai-interface-security-001` | Legacy conversation starter #7 | Legacy user-facing starter explicitly asks to review an LLM feature for prompt injection, tool use, secrets, PII, and output handling. | Added retrieval/provider wording to expose interface composition without changing the primary AI-review intent. |

## Provenance classification

Pilot counts:

```text
current-project-task: 5
legacy-request: 3
legacy-eval: 2
synthetic: 0
real-derived total: 10 / 10
```

`source_ref` values identify the durable repository artifact from which each task boundary was derived. They do not make the legacy artifact normative architecture authority.

## Redaction rule

No credentials, private identifiers, user personal data, or environment-specific secrets are copied into routing fixtures. Normalization may remove names and implementation-specific identifiers only when the engineering decision boundary remains intact.
