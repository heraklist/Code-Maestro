# CM-R-032 — Privacy & Data Lifecycle Engineering

**Priority:** P1 by default; P0 for personal/sensitive/high-impact data
**Status:** IN RESEARCH
**Disposition:** DIRECTION ACCEPTED
**Opened:** 2026-09-04
**Direction accepted by:** `../architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md`

## Question

How should CodeMaestro reason about privacy risk and the lifecycle of personal, sensitive, or user-derived data even where access is authorized and no cybersecurity compromise exists?

## Expected output

- data inventory and flow-mapping methodology;
- purpose/use and collection-boundary analysis;
- minimization guidance;
- retention/deletion/archival workflow;
- backup/log/analytics/telemetry/cache/replica handling;
- vector-index, training, evaluation, and derived-dataset handling;
- third-party/export/cross-system propagation analysis;
- de-identification/re-identification reasoning;
- user control/selective disclosure guidance;
- privacy-by-design and disposal/decommissioning workflow;
- privacy-specific eval scenarios.

## Accepted direction

Privacy & Data Lifecycle Engineering is a canonical capability family distinct from Security & Trust Engineering.

Security asks whether access/use is authorized and protected. Privacy additionally asks whether data should exist or flow there, for what purpose, for how long, how it propagates, whether it can be deleted, and what harm can arise from authorized processing.

Exact legal obligations remain jurisdiction- and time-sensitive research rather than hardcoded global rules.

## Milestone 0 open requirement

The repository work-session logging retention/deletion/public-sanitization policy is **not yet resolved**. This track remains `IN RESEARCH`, and Milestone 0 logging must not be declared operational until that specific policy has been researched, decided, and recorded.

## Primary authorities

- NIST Privacy Engineering: https://www.nist.gov/privacy-engineering
- NIST About Privacy Engineering: https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/about
- NISTIR 8062: https://www.nist.gov/publications/introduction-privacy-engineering-and-risk-management-federal-information-systems
- NIST systems privacy engineering glossary: https://csrc.nist.gov/glossary/term/systems_privacy_engineering

**Last verified:** 2026-09-04

## Evidence limitations

Privacy requirements depend on data type, system purpose, jurisdiction, deployment context, and current regulation. This track establishes an accepted architectural direction but its full engineering methodology and the Milestone 0 retention/deletion policy remain open research.
