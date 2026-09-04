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

Pilot counts:

```text
current-project-task: 5
legacy-request: 3
legacy-eval: 2
synthetic: 0
real-derived total: 10 / 10
```

## Corpus v1 — frozen challenge composition

`evals/routing/corpus-v1.json` contains exactly 100 precommitted cases: 10 cases in each of the 10 approved ambiguity clusters. No full-corpus skeleton/model/runtime output was generated before these expectations were authored.

Every cluster deliberately contains positive-primary, negative/not-primary, multi-capability, no-clarification, and clarification-required cases. The three pilot failure boundaries receive explicit adversarial coverage: Testing vs Review, Performance vs Reliability, and AI vs Interface/Security.

Corpus v1 composition:

```text
build-ci-debug: 10
implementation-debug: 10
testing-review: 10
security-privacy: 10
database-interface: 10
migration-implementation: 10
performance-reliability: 10
product-frontend: 10
research-language-freshness: 10
ai-interface-security: 10
TOTAL: 100
```

Provenance balance:

```text
real-derived: 40 / 100
synthetic adversarial: 60 / 100
real-derived floor required: >= 1/3
```

For each cluster, cases `001`–`004` are normalized variants grounded in the durable source family listed below; cases `005`–`010` are synthetic adversarial cases authored before full-corpus routing output. A real-derived variant preserves the engineering decision boundary of its cited source family but may change incidental wording or scenario details; it is not represented as a verbatim historical request.

| Cluster | Real-derived cases | Durable source family | Boundary preserved |
|---|---|---|---|
| `build-ci-debug` | `001`–`004` | pre-registry design v2 §11 | build/toolchain vs CI/delivery vs diagnosis |
| `implementation-debug` | `001`–`004` | pre-registry design v2 §6 | known implementation work vs unknown-cause debugging |
| `testing-review` | `001`–`004` | pre-registry design v2 §6 | executable assurance vs audit/review of assurance quality |
| `security-privacy` | `001`–`004` | pre-registry design v2 §8 | trust enforcement vs privacy/data lifecycle |
| `database-interface` | `001`–`004` | legacy repository audit playbook | stored/query behavior vs public interface behavior |
| `migration-implementation` | `001`–`004` | legacy dependency-maintenance playbook | compatibility transition vs ordinary implementation |
| `performance-reliability` | `001`–`004` | legacy validation rules / Performance Gate | capacity bottleneck vs resilience/incident ownership |
| `product-frontend` | `001`–`004` | consolidated CodeMaestro design / current workflow pattern | experience/design decision vs approved frontend implementation |
| `research-language-freshness` | `001`–`004` | legacy maintainer instructions | freshness/authority research vs implementation from established facts |
| `ai-interface-security` | `001`–`004` | legacy LLM review starter | AI/agent semantics vs interface contract vs security enforcement |

### Corpus-v1 freeze rule

Once the corpus-v1 validation/freeze commit is established, observed routing output must not silently change its prompts, expected primary labels, exact supporting sets, clarification labels, high-risk flags, or provenance. Any legitimate correction requires an explicit correction record or a new corpus version.

## Provenance classification

`source_ref` values identify durable artifacts from which real-derived task boundaries were derived. They do not make legacy artifacts normative architecture authority. Synthetic cases intentionally have an empty `source_ref` and state their pre-output adversarial purpose in `source_transform`.

## Redaction rule

No credentials, private identifiers, user personal data, or environment-specific secrets are copied into routing fixtures. Normalization may remove names and implementation-specific identifiers only when the engineering decision boundary remains intact.
