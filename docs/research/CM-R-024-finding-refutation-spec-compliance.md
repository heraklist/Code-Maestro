# CM-R-024 — Finding Verification, Refutation & Spec-to-Code Compliance

**Priority:** P0
**Status:** IN RESEARCH

## Question

How should CodeMaestro verify candidate findings, actively search for counter-evidence, distinguish false positives from real defects, and compare implementation behavior against authoritative specifications or requirements?

## Accepted direction

A candidate finding is not a confirmed finding. Material findings should pass a verification/refutation process proportional to their impact and uncertainty.

## Candidate finding lifecycle

```text
CANDIDATE CLAIM
→ RESTATE EXACT CLAIM
→ ROOT CAUSE / TRIGGER / IMPACT MODEL
→ SUPPORTING EVIDENCE
→ COUNTER-EVIDENCE SEARCH
→ REFUTATION ATTEMPT
→ REPRODUCTION / EXECUTION WHEN POSSIBLE
→ VERIFIED / REJECTED / PARTIAL / UNDECIDABLE
→ REPORT
```

Pattern resemblance, dangerous-looking code, or similarity to a known bug does not establish a defect in the current target.

## Spec-to-code dimension

Where a meaningful authoritative requirement/specification exists, compare each requirement against implementation behavior explicitly.

Candidate verdicts:

- `IMPLEMENTED`
- `PARTIAL`
- `CONTRADICTED`
- `STRONGER_THAN_SPEC`
- `ABSENT`
- `UNDECIDABLE`
- `NOT_CHECKED`

The reverse direction must also be considered: implementation constraints or behavior may exist without corresponding documentation or normative authority.

## Research targets

- false-positive resistance;
- threat/execution-model reconstruction;
- complete source-to-sink or state-transition tracing where relevant;
- fresh-context or independent refutation;
- exploitability vs code smell distinction;
- severity confidence;
- requirement extraction from specifications;
- requirement-to-code search evidence;
- specification ambiguity as a first-class finding;
- unverified/unchecked coverage reporting;
- variant analysis after a verified defect;
- application beyond security: correctness, migrations, concurrency, protocols, language conformance.

## Primary stress cases

- Cusp normative specification vs compiler implementation;
- security findings from broad audits;
- database/RLS policy claims;
- migration compatibility claims;
- protocol/API conformance;
- concurrency/idempotency findings.

## Preferred references

- Trail of Bits `fp-check`
- Trail of Bits `spec-to-code-compliance`
- Trail of Bits `variant-analysis`
- current formal verification and testing methods where suitable
- Cusp authority and conformance model
- CodeMaestro evidence/provenance research under CM-R-020

## Non-decision

Not every low-risk review comment requires an independent verifier. Refutation rigor is proportional to impact, uncertainty, and verification cost; exact routing thresholds remain research items.
