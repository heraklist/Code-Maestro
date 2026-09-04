# CodeMaestro v3 — Pre-Registry Hardening & Eval-First Amendment v2

## Status

**Status:** WRITTEN SPEC — PENDING USER REVIEW

**Date:** 2026-09-04

**Supersedes for this stage:** `2026-09-04-pre-registry-hardening-eval-first-design.md`

**Base authority:** consolidated v2 architecture, canonical ADRs, Living Architecture, repository logging governance, merged foundation boundary `6bb21fff2279584979ba8bee7ab61d57edcb5425`.

This v2 preserves the approved taxonomy-first → eval-first reversal and incorporates the second review before implementation planning.

---

# 1. Problem and governing principle

The foundation established architecture, research provenance, repository governance, Milestone 0, Living Architecture, tests, documentation consistency, and an append-only ledger guard before production Skill implementation.

The next risk is empirical: writing 17 capability contracts before adversarial routing evidence and size constraints could create a coherent taxonomy that has never been forced to discriminate real engineering tasks.

The next stage therefore remains:

```text
Pre-Registry hardening
-> disclosure budget
-> machine-readable routing corpus + deterministic grader
-> measured RED baseline
-> registry skeleton
-> contracts driven by failures
-> measured GREEN
```

Evidence must precede claims, and repository governance applies to the work that defines repository governance itself.

---

# 2. Goals

Before full capability contracts are authored:

1. close durable-governance drift;
2. harden mechanically checkable repository truth;
3. define one enforceable disclosure-size metric per level;
4. challenge the 17-family taxonomy with machine-readable real-task routing cases;
5. define the grader and GREEN thresholds before observing implementation performance;
6. preserve the 17-family freeze as a provisional hypothesis until representative eval evidence exists.

---

# 3. Non-goals

This stage does not create production `SKILL.md`, the production router/orchestrator, all 17 full contracts, final packaging, or the Self-Evolution Controller.

LICENSE, CODEOWNERS, and SECURITY.md are not mechanically added merely as hygiene. Repository visibility and distribution state determine whether they become requirements.

---

# 4. Repository visibility and protection decision

## 4.1 Target state

The repository target is **private**.

No paid GitHub-plan upgrade is assumed by this spec.

The repository is currently public until the visibility change is actually performed and verified. Therefore documentation must not claim the repository is already private.

## 4.2 Protection modes

The protection gate has two valid outcomes:

### Mechanically enforced mode

If the active GitHub plan supports required branch protection/rulesets for this private repository, configure `main` so required CI checks gate integration.

### Process-enforced fallback

If the active plan does not support required protection for private repositories, record explicitly:

```text
main protection mode = PROCESS-ENFORCED
reason = private repository tier does not expose required mechanical protection
required behavior = no merge without exact-head authoritative GREEN evidence
```

This is a documented degradation, not a claim that branch protection exists.

A future paid-plan upgrade is a separate user decision and may move the repository from process-enforced to mechanically enforced mode.

## 4.3 Visibility reconciliation

Because the repository is public today but intended to become private, the visibility change is a governed transition.

When it occurs, reconcile repository documentation that describes storage as `public`, `public-safe`, or `public repository`:

- `public-safe` remains a valid **content-safety standard** where intended; it must not be rewritten merely because visibility becomes private;
- statements that assert actual repository visibility must match reality;
- distribution/licensing requirements must be reevaluated at the transition;
- a visibility-change event and documentation reconciliation evidence are required.

Until the repository becomes private, the absence of a LICENSE remains a known public-distribution limitation, not an ignored fact.

---

# 5. Governance closure

Before new implementation work:

1. preserve historical events unchanged;
2. append resolution events for the previously pending `state-sync-001` and `log-correction-001` using exact successful CI evidence;
3. preserve the delayed correction event for the initially unlogged amendment commit `fdd35d76c3a6ca346023c438ca9b792c1b30d01a`;
4. append a checkpoint identifying the current branch/SHA, merged foundation SHA, verification state, and next authorized stage.

The delayed amendment event is a visible governance defect and must not be rewritten away.

---

# 6. Checker hardening

The implementation plan must include RED→GREEN regression coverage for these confirmed weaknesses.

## 6.1 Per-occurrence research negation

A negative CM-R reference suppresses only that occurrence. A positive unindexed reference elsewhere in the same file must still fail.

## 6.2 Explicit status semantics

ADR authority/status classification must not use ambiguous substring matching. Canonical active and explicit historical/non-canonical states must be parsed deterministically.

## 6.3 Line-anchored event fields

Required project-event fields count only when present as actual field lines. Tokens embedded inside another field's prose do not satisfy the schema.

## 6.4 Markdown fragment validation

Validate file existence and local/cross-file fragment targets with deterministic heading/explicit-anchor normalization. Continue excluding fenced code examples.

## 6.5 ADR definition locations

Canonical active ADR definitions are permitted only in designated architecture-decision artifacts. Logs, README, specs, and other documents may reference ADRs without becoming authority merely by mentioning an ID.

## 6.6 Reachability

Authoritative/current architecture and governance documents must be reachable from a canonical navigation root such as README or Living Architecture. Add a targeted reachability check rather than attempting general graph-theory completeness over all Markdown.

---

# 7. CI and append-only evidence semantics

## 7.1 Authoritative runs

- For an open PR, the `pull_request` workflow run at the exact PR head is authoritative pre-merge evidence.
- For `main`, the `push` workflow run at the exact merge commit is authoritative post-merge evidence.

Duplicate or stale feature-branch work should not create ambiguous evidence.

## 7.2 Concurrency

Concurrency may cancel stale feature-branch/PR work but **must never cancel an in-progress `main` run merely because a later main commit appears**.

Required semantic shape:

```yaml
concurrency:
  group: documentation-consistency-${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}
```

The implementation may adjust syntax only as needed for valid GitHub Actions behavior while preserving this invariant.

## 7.3 Workflow path coverage

Use directory-level coverage for growing validation code:

```text
tools/**
tests/**
```

Do not require a workflow edit every time a new checker/test file is added.

## 7.4 Append-only comparison range

The existing append-only checker remains mandatory but its CI comparison base must be hardened beyond `HEAD^`.

For PR/feature-branch validation, compare against the appropriate merge base with the target branch, normally:

```text
git merge-base origin/main HEAD
```

and fetch sufficient history (`fetch-depth: 0` or another proven mechanism) so the base is real.

The invariant is:

> every project ledger that existed at the comparison base must remain an exact byte-prefix of its HEAD counterpart.

This catches truncation/rewrite introduced in any commit in the branch range, not merely the final commit transition.

For `main` push evidence, the implementation must use an event-appropriate trusted pre-push/base SHA rather than assuming `HEAD^` is always sufficient for multi-commit pushes.

Privacy/security purge remains a future explicit exception workflow; it may not silently disable the guard.

---

# 8. Secret scanning, ignore rules, and tool quality gates

Before registry expansion:

- add deterministic repository secret scanning, preferably Gitleaks or equivalent;
- never use a real credential as a fixture;
- add a minimal `.gitignore` for local/editor/cache/environment artifacts;
- determine and add proportionate Python lint/type/static gates as validator code grows.

The Project Quality Contract applies to CodeMaestro's own tooling. The exact linter/type checker is an implementation-plan decision, but the plan must not omit the quality-gate decision.

---

# 9. Progressive-disclosure budgets

Use **one deterministic primary metric per level** to avoid dead duplicate limits.

These are provisional engineering budgets, not universal host-token claims.

## Level 1 — compact core orchestrator

**Primary budget:** <= 24,000 characters of normative content, excluding machine metadata/comments.

Contains only cross-cutting mission, invariants, routing/composition core, authority/trust gates, evidence/completion rules, Project Quality Contract, discovery/freshness behavior, cross-runtime contract, and the Self-Evolution command gate.

Exceeding the budget requires evidence that the content cannot move to Level 2/3 without harming routing, safety, or correctness.

## Level 2 — individual capability contract

**Primary budget:** <= 6,000 characters per capability contract.

Prioritize activation, exclusions, nearest-neighbor boundaries, evidence obligations, risk modifiers, and composition/escalation behavior. Deep techniques belong at Level 3.

## Level 3 — deep reference

**Review trigger:** > 15,000 characters prompts decomposition review unless cohesion or an external-format constraint justifies the size.

Budgets must be revalidated against current Skill packaging/runtime behavior before production packaging. Character counting is deterministic and tokenizer-independent.

---

# 10. Provisional First-Generation Capability Freeze

The current hypothesis remains exactly 17 canonical engineering capability families.

The freeze is **provisional and eval-challengeable** until representative routing/composition evidence passes.

A new family is justified only when repeated representative tasks show that existing families cannot own/compose the responsibility without persistent ambiguity, duplicated methodology, or evidence loss.

A difficult eval is not by itself evidence for a new family.

---

# 11. Eval-first routing corpus and grader

## 11.1 Corpus format

The corpus is machine-readable and version-controlled. JSON is the default format unless the implementation plan demonstrates a concrete advantage for YAML.

Each case contains at least:

```json
{
  "id": "route-build-ci-debug-001",
  "cluster": "build-ci-debug",
  "prompt": "The app builds locally but CI fails immediately after a dependency bump.",
  "expected_primary": "build-toolchain-environment",
  "expected_supporting": ["ci-cd-platform-delivery", "debugging-diagnostics"],
  "clarification_required": false,
  "acceptable_alternates": [],
  "rationale": "Environment/toolchain parity is the first discriminating responsibility; CI and debugging support diagnosis."
}
```

`expected_supporting` is compared as a set unless a case explicitly declares ordering significant.

Every case has a stable ID. Expected labels are authored **before** implementation output is observed and are changed only through reviewed corpus revisions with rationale.

## 11.2 Minimum size and coverage

Before full capability contracts, the initial corpus contains **at least 50 cases** across the 10 ambiguity clusters defined by the approved v1 amendment.

Each cluster contributes at least five cases covering:

1. clear positive primary ownership;
2. clear negative/not-primary boundary;
3. ambiguous multi-capability composition;
4. evidence-rich case where clarification is unnecessary;
5. materially ambiguous case where clarification is required.

The corpus should use realistic engineering-task language rather than taxonomy definitions.

## 11.3 Deterministic grader

A deterministic local grader consumes:

```text
expected corpus JSON
+
actual routing-result JSON
```

and emits per-case and aggregate metrics.

The grader itself does **not** ask an LLM to decide whether an answer is correct. It compares structured fields using fixed rules.

Required per-case comparisons:

- exact `expected_primary` match, unless an explicitly predeclared acceptable alternate exists;
- `expected_supporting` set comparison;
- exact `clarification_required` boolean;
- unknown capability IDs are hard failures;
- missing required output fields are hard failures.

Required aggregate metrics:

- primary accuracy;
- supporting-set exact-match rate;
- clarification accuracy;
- per-cluster primary accuracy;
- unknown-ID count;
- malformed-result count.

The grader must return a non-zero exit code when the applicable GREEN gate is not met.

## 11.4 What produces the initial actual results

The initial RED baseline must not be manufactured by declaring “no router exists.”

Before full contracts, create the **smallest evaluable routing skeleton** that expresses only the already-approved pre-contract routing representation: canonical family IDs, minimal trigger/exclusion/neighbor hints, and clarification semantics. It is an eval fixture/prototype, not the production router and not a full capability contract.

This skeleton produces structured actual results for the corpus through a deterministic harness interface.

If a task cannot be classified from that minimal representation, the result must still be explicit (for example `unresolved`) rather than omitted.

The first corpus run is expected to expose errors, but RED is informative only because the grader measures specific disagreements against precommitted expected labels.

Do not tune the corpus expected answers after seeing skeleton output merely to improve scores.

## 11.5 Pre-contract RED baseline

Record all metrics from the first evaluable skeleton run.

A valid RED baseline requires at least one failed GREEN criterion. If the minimal skeleton unexpectedly meets all GREEN thresholds, independently review the corpus for insufficient challenge before treating the taxonomy as validated.

The RED record includes:

- corpus commit/SHA or content hash;
- skeleton commit/SHA;
- grader version/SHA;
- aggregate metrics;
- per-cluster metrics;
- failing case IDs;
- unresolved/malformed/unknown-ID counts.

## 11.6 Predeclared GREEN thresholds

The initial routing/composition GREEN gate is defined **before contract implementation** as:

```text
primary accuracy >= 90%
supporting-set exact-match >= 80%
clarification accuracy >= 90%
every ambiguity cluster primary accuracy >= 80%
unknown capability IDs = 0
malformed results = 0
```

Additionally, no case designated as a high-risk authority/safety boundary may fail primary ownership or clarification expectation. Such cases must be explicitly marked in corpus metadata before evaluation.

These thresholds are provisional first-generation release gates. They may be tightened later. Lowering them requires an explicit reviewed architecture/eval decision with before/after evidence; they may not be lowered merely to make an implementation pass.

## 11.7 Reproducibility

Given identical corpus, routing-result JSON, and grader version, grading must be byte-stable apart from explicitly excluded timestamps/paths.

Cross-runtime conformance later evaluates whether Chat/Work/Codex produce equivalent structured routing outcomes for the same cases. The deterministic grader remains the scoring authority; model/runtime generation may vary, but the scoring rules do not.

---

# 12. Registry and contracts after RED evidence

Only after budgets, corpus, grader, minimal routing skeleton, and recorded RED baseline exist may full registry/contracts proceed.

Structural invariants remain necessary:

- exactly 17 provisional canonical IDs;
- unique IDs;
- required fields;
- valid contract paths;
- known neighbor IDs;
- registry/contract identity parity.

They are not sufficient.

Each full capability contract must be informed by failed/borderline eval cases and contain or reference positive routing cases, at least two negative/not-primary cases, nearest-neighbor boundary examples, and supporting composition cases where relevant.

Expected eval labels remain authoritative behavioral fixtures; contract examples are explanatory projections and may not silently diverge from them.

---

# 13. Self-Evolution roadmap gate

Self-Evolution remains in the long-term architecture but production implementation timing is not assumed pre-1.0.

Before implementing the controller, make an explicit roadmap decision based on legacy parity necessity, risk, eval maturity, rollback/audit readiness, and opportunity cost versus finishing core routing/capability/cross-runtime behavior.

Post-1.0 or experimental placement is valid without deleting the architecture contract.

---

# 14. Research WIP discipline

Keep research provenance. Do not mark tracks complete merely to reduce visible WIP.

Only tracks materially needed by the current milestone are active execution priorities; other architecturally open tracks remain backlog/context rather than simultaneous work.

---

# 15. Revised implementation order

```text
A. durable governance closure, including delayed amendment-event correction
B. checker hardening + reachability
C. CI authoritative-run/concurrency/path-filter hardening
D. append-only comparison-range hardening
E. secret scanning + .gitignore + Python quality-gate decision
F. visibility/protection-mode resolution and visibility-documentation reconciliation plan
G. single-metric progressive-disclosure budgets
H. provisional-freeze integration
I. >=50-case machine-readable routing corpus with precommitted expected labels
J. deterministic grader + predeclared GREEN thresholds
K. minimal evaluable pre-contract routing skeleton
L. recorded measured RED baseline
M. Capability Registry skeleton + structural validator
N. capability contracts driven by measured failures
O. measured routing/composition GREEN + regression corpus
P. physical Skill packaging
Q. compact orchestrator + progressive modules/references
R. cross-runtime validation
S. stabilization
T. explicit Self-Evolution implementation-timing gate
```

The previous architecture/capability-registry implementation plan is superseded for sequencing wherever it conflicts with this v2 amendment.

---

# 16. Completion gate before full Capability Registry/contracts

Pre-Registry Hardening is complete only when:

```text
historical PENDING events have append-only resolution records
AND delayed amendment logging defect has a durable correction record
AND current checkpoint matches actual branch/SHA/evidence
AND confirmed checker bugs have RED->GREEN regression coverage
AND authoritative CI/concurrency semantics are implemented
AND main runs cannot be cancelled by later main runs
AND tools/** and tests/** are covered by CI triggers
AND append-only validation covers the full relevant branch/push range
AND secret scanning is GREEN
AND minimal .gitignore exists
AND Python validator quality-gate decision is implemented or explicitly deferred with rationale
AND repository visibility/protection mode is explicitly recorded
AND visibility-dependent documentation reconciliation is defined
AND disclosure budgets use the canonical single metric
AND the 17-family freeze is provisional/eval-challengeable
AND machine-readable routing corpus has >=50 cases with required cluster coverage
AND expected labels were committed before implementation tuning
AND deterministic grader exists and is regression-tested
AND GREEN thresholds are committed before contract implementation
AND minimal evaluable routing skeleton exists
AND measured pre-contract RED baseline is recorded with reproducible evidence
```

Only then may full capability-contract implementation begin.

---

# 17. Deferred but tracked items

The implementation plan must also track, without necessarily blocking the first RED corpus:

- canonical inbound navigation/reachability for this v2 amendment;
- tag absence at the merged foundation boundary and whether a later recoverable release/boundary marker is still useful;
- LICENSE decision while the repository remains public and reconciliation if/when it becomes private;
- future mechanical branch protection if plan capability changes.

---

# 18. Authority after approval

If approved, authority for this stage is:

1. current user/system authority;
2. consolidated v2 constitutional architecture;
3. canonical ADRs;
4. this v2 amendment for pre-registry ordering, repository hardening, budgets, eval format/grading/thresholds, and provisional-freeze maturity;
5. the v1 amendment only for historical rationale not contradicted here;
6. older implementation plans only where they do not conflict with this v2;
7. the implementation plan derived from this v2.

This amendment changes sequencing and validation maturity. It does not claim the 17-family taxonomy is already empirically validated.