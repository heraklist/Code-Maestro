# Pre-Registry Eval Readiness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` task-by-task.

**Goal:** Challenge the provisional 17-family capability taxonomy with precommitted real-derived routing tasks, deterministic grading, and repeated target-surface model runs before any full capability contract is authored.

**Architecture:** Eval Readiness is independent of Repository Hardening and is the only pre-registry gate that authorizes capability-contract authoring. Deterministic CI checks establish corpus/harness/grader integrity. Qualifying model evidence is generated only in an authorized interactive target surface under CM-ADR-031 and its accepted Part 1 scope correction.

**Coverage boundary:** **OpenAI Chat / Work / Codex surfaces only. B7 evidence is not an indication of behavior on other LLM providers.** Non-OpenAI portability validation is deferred to Part 2; the provider-neutral methodology and runtime-capability abstractions remain in Part 1.

**Tech Stack:** Python 3.12 standard library, JSON, `unittest`, Markdown provenance records, authorized Chat/Work/Codex subscription surfaces.

**Spec:** `docs/superpowers/specs/2026-09-04-pre-registry-hardening-eval-first-design-v2.md`

## Global Constraints

- The 17 capability families remain a **Provisional First-Generation Capability Freeze**, not an empirically proven taxonomy. The freeze is coverage-bounded to the assessed OpenAI Part 1 surfaces and makes no claim about non-OpenAI providers.
- No production `SKILL.md` or full capability contract may be authored before the Eval Readiness gate passes.
- Corpus expectations are committed before routing outputs are generated; `corpus-v1.json`, its expectations, `skeleton-v0.json`, and the deterministic grader remain frozen during B7.
- Full corpus: >=100 cases, >=10 per ambiguity cluster, >=1/3 real-derived provenance.
- Qualifying model evaluation uses **n >= 3 independent runs per runtime/model configuration**.
- Every invocation is a fresh single-turn session: no resume, no carryover, no `n=3` multi-generation shortcut.
- Record runtime surface, provider, non-alias model ID, model version/build when exposed, reasoning effort, adapter mechanics, timestamp, corpus SHA, skeleton SHA, grader version, run ID, result path, and the explicit coverage boundary. Unavailable metadata is literal `NOT AVAILABLE`; never invent it.
- **Model pinning rule:** pin the most specific non-alias model ID exposed by the target surface (for example `gpt-5.6-sol`, never a floating family alias such as `gpt-5.6`). A dated snapshot is not required when that generation does not expose one. Reproducibility evidence is the non-alias ID plus explicit reasoning effort/configuration, timestamps, and per-run model identity. If a surface exposes a build identifier, record it.
- GREEN is judged on the **worst complete run**, never the best run or average alone.
- Per-run full-corpus thresholds remain: primary >=90%; supporting exact-set >=80%; clarification >=90%; unknown capability IDs = 0; malformed results = 0; frozen-corpus high-risk fail-closed = 100%; each cluster >=9/10 primary correct (or at most one primary failure when a cluster contains >10 cases).
- Record min/max/mean/pstdev, but aggregate dispersion is descriptive only. Preserve **per-case, per-run outcomes and vote patterns** because instability is a primary B8 input.
- `UNSTABLE` is not a post-hoc judgment. A case is unstable when its primary/supporting/clarification outcome changes across qualifying runs. Store the observed vote pattern. For cases whose **frozen corpus label** has `high_risk: true`, primary or clarification instability fails closed.
- Deterministic skeleton execution is a **routing harness/grader conformance regression** only. It does not qualify as a B7 model run, does not contribute to B7 dispersion, and never contributes to the B7 verdict.
- No LLM-as-judge. The acceptance grader remains deterministic.
- Model inference is never required in CI. Model-based evals run only in an authorized interactive target surface.
- **Part 1 development/eval governance:** the project does not initiate OpenAI API execution, use API keys, or incur API billing. Model-based eval generation uses Chat / Work / Codex through ChatGPT sign-in. Host authentication used by a future Skill user is outside Skill authority and does not cause refusal or artificial degradation.
- Quota is a first-class budget beside context. Every model-based suite declares an invocation budget. Quota pressure may distribute runs across windows/days but may not reduce corpus size, n, or thresholds.
- If model identity changes inside a configuration while work is distributed across quota windows, invalidate that configuration and restart it from the beginning.
- Cross-runtime/model configurations receive separate verdicts and are never averaged together.
- Eval Readiness may progress while Repository Hardening is incomplete unless a hardening failure compromises eval evidence integrity.

## Eval Surface Structure

`evals/README.md` is authoritative for the permanent split:

```text
Deterministic CI
  schemas / parsers / grader / corpus integrity / harness conformance

Interactive model evals
  target-surface model generation / per-case outputs / manifests / deterministic grading / instability analysis
```

## Completed Evidence — B1 through B6

The detailed historical implementation steps remain recoverable from repository history before this plan revision. Their current accepted outputs are:

- **B1 PASS:** machine-readable routing case/result contract and deterministic grader.
- **B2 PASS:** 10-case precommitted real-derived pilot.
- **B3 PASS:** deterministic minimal `skeleton-v0`.
- **B4 CONTINUE:** pilot found skeleton signal gaps but did not meet taxonomy-reopen criteria.
- **B5 PASS:** frozen 100-case corpus, 10 cases per cluster, 40 real-derived / 60 synthetic, expectations committed before full-corpus output.
- **B6 PASS:** repeated-run manifest/aggregation semantics with n>=3, identity consistency, worst-run gating, and population statistics.

The deterministic 3x100 skeleton execution performed before this revision is retained only as conformance evidence. Its 32/100 primary result supports the narrow conclusion that the frozen corpus is **not trivially keyword-separable**; it is not evidence of model difficulty and is not a qualifying B7 baseline.

---

### Task B7: Execute the pre-contract interactive model baseline

**Files:**
- Create: `evals/routing/interactive/<configuration>/run-01.json`
- Create: `evals/routing/interactive/<configuration>/run-01.manifest.json`
- Create: corresponding run 02 and 03 artifacts
- Create: `evals/routing/interactive/<configuration>/instability.json`
- Create: `evals/routing/reports/pre-contract-baseline.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

**Interfaces:**
- Consumes frozen `corpus-v1.json`, frozen skeleton identity, unchanged deterministic grader.
- Produces at least three complete model-generated runs for each configuration actually evaluated, per-case vote patterns, dispersion, worst-run verdict, quota evidence, and explicit coverage scope.

- [ ] **Step 1: Freeze the qualifying configuration before generation**

Primary configuration:

```text
runtime_surface: Codex CLI (ChatGPT sign-in)
provider: OpenAI
model_id: gpt-5.6-sol
model_version: NOT AVAILABLE unless the surface exposes a build identifier
reasoning_effort: explicit actual Codex surface default for this model
configuration: tools disabled; read-only; single-turn; fresh/ephemeral session; strict JSON output schema
coverage_scope: OpenAI Chat / Work / Codex surfaces only; not evidence for other LLM providers
corpus_sha256: <frozen>
skeleton_sha256: <frozen>
grader_version: <unchanged>
started_at: <offset-aware>
```

Evaluate a second configuration `gpt-6-astra` if the user's current Codex subscription exposes it. It receives its own manifests, three runs, instability analysis, and verdict; never average it with Sol. If Astra is not exposed, record the exact availability limitation in the Sol evidence so future reviewers can distinguish deliberate omission from unavailable capability.

Use the target surface's actual default reasoning effort for each model and record it explicitly. Do not infer a value from another model or provider.

- [ ] **Step 2: Verify Codex CLI adapter mechanics before writing/running the loop**

Use current `codex exec --help` plus authoritative non-interactive documentation/source. The harness must preserve identical case text and result schema and must establish:

```text
new non-interactive session per invocation
no resume/fork/carryover
no persisted session state when the surface supports ephemeral execution
read-only sandbox
no project/user configuration that could inject behavior when a supported isolation flag exists
no model-generated tool trajectory contributing to the routing decision
strict JSON output schema
final structured response captured without exposing credentials
```

Current verified CLI source exposes `codex exec`, `--model/-m`, `--sandbox/-s`, `--ephemeral`, `--ignore-user-config`, `--ignore-rules`, `--output-schema`, `--json`, and `--output-last-message`. Before execution, verify the installed CLI's actual `--help`; repository source evidence does not substitute for the installed binary.

If the installed CLI cannot actually prevent tool trajectory strongly enough for a single-turn routing measurement, stop and record a surface limitation rather than silently measuring an agent trajectory.

- [ ] **Step 3: Run a 10-case quota pilot before the full corpus**

For each configuration that is actually exposed, run exactly 10 representative frozen cases using the final harness mechanics. Record:

```text
invocations consumed
observable allowance/quota signal exposed by the surface
elapsed time
model identity
reasoning effort
any throttling/retry behavior
coverage scope
```

Use this evidence to schedule the required full run budget. The full B7 budget is **300 invocations per configuration** (100 cases x 3 independent runs). Do not shrink corpus or n to fit a quota window.

- [ ] **Step 4: Execute three independent full-corpus runs per configuration**

For every case and every run, start a new session/invocation. Do not edit corpus expectations, skeleton, or grader between runs. If quota requires multiple windows/days, record timestamps and model identity continuously. Any model-identity change inside a configuration invalidates that configuration and requires restart from run 01/case 001.

- [ ] **Step 5: Grade each run independently with the unchanged deterministic grader**

Produce one `RunMetrics` record/report per run. No model judges the outputs.

- [ ] **Step 6: Compute instability vote patterns and fail-closed high-risk behavior**

For every case, preserve the three observed outcomes for:

```text
primary
supporting exact set
clarification_required
```

Record vote patterns (for example 3/3 same, 2/3 vs 1/3 split, or three-way split), not only a boolean unstable flag. `high_risk` is read exclusively from the frozen corpus label. If a frozen high-risk case changes primary or clarification outcome across runs, the configuration fails closed regardless of aggregate score.

- [ ] **Step 7: Aggregate qualifying runs separately per configuration**

Produce min/max/mean/pstdev and identify the worst complete run. GREEN is false if any qualifying run fails any threshold or the high-risk instability rule.

- [ ] **Step 8: Apply the inverse-safeguard to the qualifying model producer**

If a qualifying model configuration passes every threshold on every run with implausibly perfect or near-perfect separation, set:

```text
RESULT = CORPUS CHALLENGE REVIEW REQUIRED
```

Review provenance, ambiguous boundaries, leakage risk, and adversarial difficulty before accepting the result. The deterministic skeleton is not a qualifying producer and cannot trigger or satisfy this B7 safeguard.

- [ ] **Step 9: Record expected baseline state**

A legitimate outcome is RED. Classify failures by cluster/reason and preserve instability evidence. Do not weaken thresholds, corpus size, n, labels, high-risk rules, or coverage boundary after observing scores.

- [ ] **Step 10: Commit interactive baseline evidence**

```bash
git add evals/routing/interactive evals/routing/reports/pre-contract-baseline.md logs/logs/project/2026/2026-09-04-pre-registry.log
git commit -m "test: record interactive pre-contract routing baseline"
```

---

### Task B8: Decide whether the 17-family taxonomy survives the baseline

**Files:**
- Create: `docs/evals/ROUTING-TAXONOMY-DECISION.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

- [ ] Review every persistent failure and every unstable case. A persistent failure appears in at least two of the three required runs for the same case/configuration. Preserve 2-of-3 versus 1-of-3 vote structure rather than collapsing it to one flag.
- [ ] Classify evidence as `ROUTER LIMITATION | CONTRACT BOUNDARY NEEDS CLARIFICATION | EXPECTED LABEL DEFECT | CASE DEFECT | TAXONOMY DEFECT | RUNTIME VARIANCE`.
- [ ] Reopen taxonomy if evidence shows a responsibility cannot be cleanly owned/composed by the existing 17 without persistent ambiguity, duplicated methodology, or evidence loss. Cite exact case IDs and repeated-run evidence.
- [ ] If taxonomy survives, produce the contract-driving failure table: `case id | cluster | observed failure | primary contract to clarify | neighboring contract(s) | required boundary statement`.
- [ ] Commit the decision. Corpus corrections, if any, require a versioned correction with rationale; never silently mutate corpus v1.

If result is `REOPEN TAXONOMY`, stop before B9 and open an architecture amendment.

---

### Task B9: Establish Eval Readiness gate

**Files:**
- Create: `docs/superpowers/plans/2026-09-04-pre-registry-eval-readiness-execution.md`
- Modify: `logs/logs/project/2026/2026-09-04-pre-registry.log`

Acceptance requires:

```text
B1-B6 accepted evidence remains intact
model-based evidence generated only interactively
primary target configuration has n>=3 complete full-corpus runs
any additional configuration has a separate verdict
runtime/model/reasoning/config metadata recorded or NOT AVAILABLE explicitly
coverage scope recorded as OpenAI Chat / Work / Codex only
quota budget recorded without weakening corpus or n
per-case vote patterns recorded
frozen high-risk instability rule applied
variance statistics recorded
worst-run rule applied
inverse-safeguard applied to qualifying model producer when applicable
taxonomy decision = TAXONOMY SURVIVES
contract-driving failure table exists
```

Result vocabulary:

```text
PASS — capability registry/contracts may begin for the coverage-bounded Part 1 target
BLOCKED — missing evidence/infrastructure/quota window
REOPEN TAXONOMY — architecture review required
```

Before claiming PASS, run fresh repository validation applicable at current head, including unit tests and `tools/doc_consistency.py`, plus any Repository Hardening gates already present. Repository Hardening remains a parallel gate and does not alter the empirical taxonomy verdict.

## Post-Plan Handoff

Only after B9 `PASS`:

```text
Eval Readiness PASS
-> amend/supersede old Capability Registry plan
-> create registry skeleton + structural validator
-> write contracts against the contract-driving failure table
-> rerun the same frozen corpus at n>=3 after contract-informed routing changes
-> require worst-run GREEN before claiming routing/composition readiness
```

The first post-contract GREEN never authorizes changing corpus expectations to fit implementation or generalizing Part 1 evidence to unassessed providers.
