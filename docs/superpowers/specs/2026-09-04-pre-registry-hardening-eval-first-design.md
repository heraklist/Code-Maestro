# CodeMaestro v3 — Pre-Registry Hardening & Eval-First Amendment

## Status

**Status:** WRITTEN SPEC — PENDING USER REVIEW

**Date:** 2026-09-04

**Scope:** Post-foundation amendment before Capability Registry implementation.

**Base authority:**

- `docs/superpowers/specs/2026-09-04-codemaestro-v3-consolidated-design-v2.md`
- `docs/architecture/ARCHITECTURE.md`
- `docs/architecture/DECISIONS.md`
- `docs/project-governance/SESSION-LOGGING-PROTOCOL.md`
- merged foundation boundary `6bb21fff2279584979ba8bee7ab61d57edcb5425`

This amendment does not replace the consolidated architecture. It changes the **implementation ordering, validation burden, and preconditions** for the Capability Registry/contract slice after external review exposed places where the current architecture is not yet sufficiently falsifiable or mechanically guarded.

---

# 1. Problem statement

The merged foundation deliberately established architecture, research provenance, repository governance, a current Living Architecture, and Milestone 0 before product/runtime implementation.

That foundation is now stable enough to expose the next risk:

> If CodeMaestro writes the 17 capability contracts before adversarial routing evidence and context-size constraints exist, the contracts can become internally consistent but empirically untested taxonomy prose.

The same review also exposed remaining tooling/governance weaknesses in `tools/doc_consistency.py`, CI run semantics, durable ledger closure, and secret-handling enforcement.

Therefore the next implementation stage is amended from:

```text
Capability Registry
-> 17 capability contracts
-> RED evals later
```

to:

```text
Pre-Registry hardening
-> disclosure/context budget contract
-> routing RED corpus
-> provisional freeze challenge
-> registry skeleton
-> capability contracts driven by failed routing cases
-> routing/composition GREEN
```

---

# 2. Goals

This amendment must achieve five outcomes before the first full capability contract is authored.

1. **Close repository-governance drift.** Durable logs must agree with already-observed verification state.
2. **Harden machine-checkable project truth.** Confirmed checker/CI weaknesses must be fixed with RED→GREEN evidence.
3. **Make progressive disclosure operational.** Level 1 / capability / deep-reference material receives enforceable size budgets before content expansion.
4. **Make the 17-family taxonomy falsifiable.** Routing ambiguity is tested before contracts are written to defend the taxonomy.
5. **Preserve architectural restraint.** No new capability family is added merely because an eval is difficult; new breadth requires evidence that existing families cannot express the responsibility cleanly.

---

# 3. Non-goals

This amendment does **not**:

- create production `SKILL.md`;
- implement the production router/orchestrator;
- implement the final capability registry runtime loader;
- write all 17 capability contracts;
- implement the Self-Evolution Controller;
- publish/package CodeMaestro;
- reopen the full architecture from first principles;
- add LICENSE/CODEOWNERS/SECURITY.md merely as checklist hygiene while the repository is intended to become private.

---

# 4. Repository privacy assumption

The repository is expected to become **private**.

This changes distribution/hygiene priority, but not repository-security semantics:

- a private Git secret is still a durable secret exposure;
- public-distribution licensing is not a pre-registry blocker;
- CODEOWNERS provides little value for a single-owner private repository today;
- SECURITY.md is optional until there is an external reporting surface or contributor model;
- secret scanning remains required because privacy of the repository does not make credentials safe to persist.

If the repository later becomes public or multi-contributor, licensing, contributor/security reporting, CODEOWNERS, and public disclosure policy must be reconsidered explicitly.

---

# 5. Governance closure before new architecture work

Two historical events remain `PENDING` despite later verification evidence:

- `CM-EVENT-20260904T133229+0300-state-sync-001`
- `CM-EVENT-20260904T144900+0300-log-correction-001`

They must **not** be rewritten.

Append new resolution events that:

- reference the original event IDs;
- cite the exact subsequent successful CI evidence;
- record the merged foundation SHA;
- distinguish `verified before merge` from `verified after merge on main`;
- close their pending state through append-only supersession/resolution semantics.

A new checkpoint then establishes:

```text
main = 6bb21fff2279584979ba8bee7ab61d57edcb5425
foundation merged
post-merge documentation consistency = PASS
append-only guard = operational
next authorized stage = Pre-Registry Hardening
```

---

# 6. Checker hardening

## 6.1 Research-reference negation is per occurrence

Current behavior collects negated CM-R IDs per file. This can create a false negative when a file contains both:

```text
No CM-R-033 is opened here.
```

and later:

```text
CM-R-033 defines the next research stage.
```

Required behavior:

- evaluate negation at the specific reference occurrence or its bounded sentence/context;
- a negative occurrence suppresses only itself;
- a positive occurrence to an unindexed CM-R still fails.

## 6.2 Status parsing uses explicit canonical semantics

Substring classification such as:

```text
"SUPERSEDED" in status.upper()
```

is not sufficient.

Required behavior:

- parse an explicit status/authority vocabulary;
- distinguish canonical active states from `ABSORBED`, `SUPERSEDED`, `HISTORICAL`, `NON-CANONICAL` authority markers;
- strings such as `NOT SUPERSEDED` must not accidentally match a non-active state by substring.

The long-term preferred direction is machine-readable metadata for status/authority, but this amendment may first harden the current Markdown representation without rewriting the whole documentation corpus.

## 6.3 Project-event fields are line-anchored

Every required event field must be recognized only as a field line, not as an incidental token inside prose.

Required pattern conceptually:

```text
^FIELD NAME:\s*...
```

for all required fields.

A sentence such as:

```text
ACTION: Verified that EVIDENCE: was discussed elsewhere.
```

must not satisfy the required `EVIDENCE:` field.

## 6.4 Markdown anchor validation

Internal Markdown validation must distinguish:

```text
path/to/file.md
path/to/file.md#section-anchor
#local-section-anchor
```

Required behavior:

- file existence remains checked;
- local and cross-file fragment identifiers are validated against headings/explicit anchors using a deterministic normalization rule;
- fenced code examples remain excluded from link validation.

## 6.5 ADR definition authority is location-aware

Do not solve ADR consistency by treating all Markdown equally.

Definitions and references are separate concepts.

Required model:

- canonical/active ADR definitions are permitted only in designated architecture decision artifacts;
- historical/absorbed checkpoints may repeat ADR identifiers only with explicit non-active authority markers;
- README/logs/specs may reference ADR IDs but do not become canonical definitions merely by mentioning them;
- the checker should eventually reject active ADR definitions in unauthorized locations.

This preserves the invariant that logs are evidence, not authority.

---

# 7. CI semantics

## 7.1 Authoritative run policy

The current workflow can run on both `push` and `pull_request`, producing duplicate evidence for one branch state.

The new CI contract must define one authoritative interpretation:

- PR validation: the PR-triggered run is authoritative for pre-merge review;
- main validation: the `push` run on the merge commit is authoritative post-merge evidence.

Add `concurrency` so stale runs for the same branch/PR are cancelled rather than accumulating contradictory-looking run IDs.

Example policy shape:

```yaml
concurrency:
  group: documentation-consistency-${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
```

The final exact expression may be adapted to valid GitHub Actions syntax.

## 7.2 Append-only guard remains mandatory

`tools/check_append_only_logs.py` is now part of the foundation and remains required.

The amendment must not weaken it.

Existing project ledgers at the comparison base must remain exact byte-prefixes of their corresponding HEAD versions. New ledgers are allowed. Truncation, rewrite, or deletion fails unless an explicitly authorized privacy/security purge workflow is invoked under the logging policy.

A future purge exception must be explicit rather than silently disabling append-only enforcement.

---

# 8. Secret scanning

Repository privacy does not remove secret risk.

Before capability-registry expansion, CI must include a deterministic secret-scanning gate suitable for repository use.

Preferred direction:

- Gitleaks or an equivalent mature scanner;
- scan the repository/worktree and, where practical, relevant commit range;
- fail on detected credential/token/private-key patterns;
- allow explicit reviewed baselines/allowlists only with documented justification;
- never use a real secret as a test fixture.

If GitHub-native secret scanning/push protection is available for the private repository/account tier, enable it as an additional control rather than a substitute for repository CI scanning.

A minimal `.gitignore` should also be created before generated/runtime artifacts expand, covering common local/editor/cache/secret-environment artifacts without hiding source files that belong under version control.

---

# 9. Progressive-disclosure budgets

Progressive disclosure is already constitutional. This amendment makes it measurable.

The budgets are **engineering limits**, not claims about a universal host token limit.

## 9.1 Budget classes

Define three content budgets before capability contracts are authored:

### Level 1 — Compact core orchestrator

Contains only cross-cutting behavior needed on most consequential tasks:

- mission/public contract;
- constitutional invariants;
- routing/composition core;
- authority/trust gates;
- evidence/completion rules;
- Project Quality Contract;
- capability/freshness discovery;
- cross-runtime contract;
- Self-Evolution command gate only, not its full methodology.

**Initial design target:** <= 4,000 words and <= 24,000 characters of normative prose, excluding metadata/comments.

**Hard review trigger:** exceeding either limit requires evidence that the content cannot be moved to Level 2/3 without harming routing/safety/correctness.

### Level 2 — Individual capability contract

A capability contract is routing/behavioral interface, not a textbook.

**Initial design target per capability:** <= 900 words and <= 6,000 characters.

It must prioritize:

- when to activate;
- when not to activate;
- nearest-neighbor boundaries;
- evidence obligations;
- escalation/de-escalation;
- risk modifiers.

Deep techniques belong at Level 3.

### Level 3 — Deep reference

No single universal word limit is imposed because domains differ, but references must be independently loadable and narrow in purpose.

**Initial review trigger:** > 2,500 words should prompt decomposition unless cohesion or external-format constraints justify the size.

## 9.2 Budget semantics

These numbers are **provisional engineering budgets** intended to prevent unconstrained growth before host/package constraints are finalized.

They must be revalidated against current Agent Skills/OpenAI packaging and runtime behavior before production packaging.

Failing a provisional budget does not automatically mean content must be deleted; it requires architectural justification or decomposition.

Machine-checkable budget metrics should be based on deterministic characters/words/file role, not estimated model tokens that vary by tokenizer/model.

---

# 10. Provisional Capability Freeze

Rename the current first-generation freeze operationally to:

> **Provisional First-Generation Capability Freeze**

Meaning:

- the current hypothesis is exactly 17 canonical engineering capability families;
- no new top-level family is added merely because a domain label exists;
- the taxonomy is intentionally challenged by routing/composition evals;
- a new family is justified only if repeated representative tasks expose a responsibility that cannot be cleanly owned/composed by the existing 17 without persistent ambiguity, duplicated methodology, or evidence loss.

The freeze becomes stronger after the first representative routing/composition eval corpus passes.

The wording does not revoke the Pass-5 research record; it clarifies the epistemic maturity of the implementation taxonomy before empirical routing validation exists.

---

# 11. Eval-first routing corpus

## 11.1 Purpose

The first eval corpus must test **discrimination**, not merely enumeration.

A registry entry having the correct `id` proves structural integrity. It does not prove the router can distinguish adjacent responsibilities.

## 11.2 Minimum corpus before full contracts

Create representative task cases covering at least these ambiguity clusters:

1. Build / Toolchain / Environment vs CI/CD / Platform / Delivery vs Debugging
2. Software Implementation vs Debugging / Diagnostics
3. Testing / Assurance vs Review / Audit / Compliance
4. Security / Trust vs Privacy / Data Lifecycle
5. Database / Data vs Interface / Protocol / Contract
6. Migration / Compatibility vs ordinary Implementation
7. Performance / Capacity vs Reliability / Observability / Incident
8. Product / UX / UI vs frontend Implementation
9. Research / Experimental / Language vs Shared Intelligence Language/Freshness
10. AI / LLM / Agent / MCP vs generic Interface/Security/Implementation composition

Each cluster must include:

- positive primary-owner examples;
- negative examples that should **not** primarily route there;
- ambiguous multi-capability examples;
- at least one case where clarification should be unnecessary because evidence resolves the route;
- at least one case where clarification is appropriate because different routes materially alter scope/risk/outcome.

## 11.3 Real-task style

Cases should resemble actual engineering requests, for example:

```text
"The app builds locally but CI fails immediately after a dependency bump."
```

The expected result is not a single magical label. It may be:

```text
primary: Build / Toolchain / Environment
supporting: CI/CD / Platform / Delivery, Debugging / Diagnostics
reason: failure discriminates environment/toolchain parity before pipeline orchestration
```

## 11.4 RED requirement

Run the corpus against the current pre-contract routing representation/skeleton.

The expected first state is **RED or materially incomplete**.

Do not write contracts first and then invent examples they already satisfy.

The failed/ambiguous cases become direct inputs to contract wording and nearest-neighbor boundaries.

---

# 12. Registry/contracts after RED evidence

Only after budget rules and the initial routing RED corpus exist may the Capability Registry/contract slice proceed.

Registry structural invariants remain useful and mandatory:

- exactly 17 provisional canonical IDs;
- unique IDs;
- required fields;
- valid contract paths;
- known nearest-neighbor IDs;
- registry/contract identity parity.

But structural tests are explicitly **necessary, not sufficient**.

Each capability entry/contract must also include routing evidence derived from the eval corpus.

At minimum each capability contract should contain or reference:

- positive routing cases;
- at least two negative/not-primary cases;
- nearest-neighbor boundary examples;
- supporting-capability composition cases where relevant.

The eval corpus remains the authority for behavior; examples embedded in contracts are explanatory projections and must not diverge from it.

---

# 13. Self-Evolution roadmap gate

Self-Evolution remains part of the long-term architecture and protected governance model.

This amendment does **not** remove it.

However, production implementation timing is no longer assumed to be pre-1.0.

Before implementing the Self-Evolution Controller, create an explicit roadmap decision evaluating:

- legacy behavioral-parity necessity;
- risk surface;
- eval maturity;
- rollback/audit readiness;
- value compared with finishing core routing/capability/cross-runtime behavior.

A valid decision may place the controller in a post-1.0 or experimental milestone while retaining the architecture/spec contract.

---

# 14. Research WIP discipline

The backlog may retain all research tracks and provenance.

Operationally, introduce a WIP rule:

- only tracks materially needed by the current milestone are actively advanced;
- other `IN RESEARCH` records may remain architecturally open but are not all treated as simultaneous execution priorities;
- no research track is marked complete merely to reduce visible WIP.

This is scheduling discipline, not epistemic status rewriting.

---

# 15. Revised implementation order

The post-foundation sequence becomes:

```text
A. durable governance closure
B. checker hardening
C. CI authoritative-run/concurrency hardening
D. secret scanning + minimal .gitignore
E. main protection/ruleset configuration where available
F. progressive-disclosure budget contract
G. provisional-freeze wording integration
H. initial routing RED corpus
I. Capability Registry skeleton + structural validator
J. capability contracts driven by RED failures
K. routing/composition GREEN + regression corpus
L. physical Skill packaging
M. compact orchestrator + progressive modules/references
N. cross-runtime validation
O. stabilization
P. explicit Self-Evolution implementation-timing gate
```

The architecture/capability-registry implementation plan must be amended or superseded before Tasks 2–7 continue.

---

# 16. Completion gate for this amendment

The Pre-Registry Hardening stage is complete only when:

```text
pending durable events have explicit resolution events
AND
current project checkpoint matches actual branch/SHA/evidence
AND
confirmed doc checker bugs have RED→GREEN regression coverage
AND
append-only guard remains GREEN
AND
CI concurrency/authoritative-run semantics are documented and implemented
AND
secret-scanning CI exists and is GREEN
AND
minimal .gitignore exists
AND
main protection/ruleset state is explicitly resolved or documented as unavailable
AND
Level 1/2/3 provisional budgets are canonical
AND
Capability Freeze is explicitly provisional/eval-challengeable
AND
initial routing ambiguity corpus exists
AND
its pre-contract RED/incomplete baseline is recorded
```

Only then may the full Capability Registry and 17 capability contracts resume.

---

# 17. Expected authority after approval

If approved, authority order for this stage is:

1. current user/system authority;
2. consolidated v2 constitutional architecture;
3. canonical ADRs;
4. this amendment for **pre-registry ordering, budgets, hardening, and eval-first requirements**;
5. existing architecture-capability-registry implementation plan only where it does not conflict with this amendment;
6. later implementation plan derived from this amendment.

This amendment changes implementation sequencing and validation maturity. It does not silently rewrite the original design intent or claim that the 17-family architecture has already been empirically validated.
