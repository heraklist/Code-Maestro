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

## Milestone 0 logging sub-question

**Status:** RESOLVED FOR MILESTONE 0 — broader CM-R-032 remains `IN RESEARCH`.

The narrow repository work-session logging retention/deletion/public-sanitization prerequisite is defined in:

`../project-governance/LOGGING-PRIVACY-RETENTION-POLICY.md`

The decision establishes:

- public repository records are sanitized/public-safe only;
- raw private/local transcripts are optional, purpose-specific, authorized, and revocable;
- retention is purpose-limited rather than an invented universal duration;
- legitimate privacy/security/confidentiality/legal deletion may override ordinary semantic append-only behavior;
- authorized purge may include history rewrite when necessary to remove the payload;
- purge evidence remains non-sensitive and does not preserve the removed payload;
- policy re-review is triggered by material changes in data class, storage/replication, repository visibility, authority, Self-Evolution activation, or applicable requirements.

This resolves only the Milestone-0 logging lifecycle question. The broader Privacy & Data Lifecycle Engineering expected outputs above remain open research.

## Primary authorities

- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST data-processing glossary: https://csrc.nist.gov/glossary/term/data_processing
- NIST minimization glossary: https://csrc.nist.gov/glossary/term/minimization
- NIST Privacy Engineering: https://www.nist.gov/privacy-engineering
- NIST About Privacy Engineering: https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/about
- NISTIR 8062: https://www.nist.gov/publications/introduction-privacy-engineering-and-risk-management-federal-information-systems
- NIST systems privacy engineering glossary: https://csrc.nist.gov/glossary/term/systems_privacy_engineering
- NIST SP 800-53 Rev. 5: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf

**Last verified:** 2026-09-04

## Evidence limitations

Privacy requirements depend on data type, system purpose, jurisdiction, deployment context, current regulation, and contractual obligations. The Milestone-0 policy is a project-specific privacy-engineering decision for repository development logs; it is not legal advice and does not complete the full CM-R-032 methodology.
