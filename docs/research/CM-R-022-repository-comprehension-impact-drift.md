# CM-R-022 — Repository Comprehension, Impact & Architecture Drift

**Priority:** P0
**Status:** IN RESEARCH

## Question

How should CodeMaestro understand unfamiliar repositories, model architecture and assumptions, estimate blast radius, and detect meaningful architecture/documentation drift before judging or modifying the codebase?

## Accepted direction

Repository comprehension is a distinct phase from review, debugging, refactoring, remediation, and security hunting.

Preferred high-level sequence:

```text
UNDERSTAND
→ MODEL BOUNDARIES / FLOWS / ASSUMPTIONS
→ IDENTIFY OPEN QUESTIONS
→ ANALYZE IMPACT
→ ONLY THEN JUDGE OR CHANGE
```

## Research targets

- repository topology and entry-point mapping;
- execution-flow and dependency mapping;
- state/data ownership;
- invariants and assumptions;
- caller/callee and upstream/downstream impact;
- tests and validation ownership;
- build/CI/deployment paths;
- architecture/documentation drift;
- graph/PDG-assisted navigation vs direct-source verification;
- changed-code blast-radius analysis;
- comprehension-only output contracts;
- stale derived-index handling;
- evidence hierarchy for graph-derived claims.

## Key questions

1. When is repository comprehension mandatory before audit/debug/change work?
2. What is the smallest useful repository dossier?
3. How should impact analysis degrade when graph/index tools are unavailable?
4. How should CodeMaestro distinguish observed source facts from derived graph claims?
5. What signals justify a deeper blast-radius pass?
6. How should code↔docs↔architecture drift be measured without treating documentation as automatically authoritative?
7. What parts of this capability belong in a shared layer vs specialized review/architecture skills?

## Preferred references

- Trail of Bits `audit-context-building`
- Trail of Bits `spec-to-code-compliance`
- `abhigyanpatwari/GitNexus`
- codebase-research/onboarding skill systems with explicit comprehension-only boundaries
- existing CodeMaestro repository-state and findings methodology

## Non-decision

No repository graph engine, indexer, or MCP service is a mandatory dependency. Tool-assisted graph analysis is an optional evidence/navigation accelerator; current source and executable evidence remain authoritative.
