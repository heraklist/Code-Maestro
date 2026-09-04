# CodeMaestro Logging Ownership & Timing Amendment

## Status

Approved architectural refinement on 2026-09-04.

This amendment corrects the ownership boundary of the logging design described in the consolidated CodeMaestro v3 design. Where earlier wording can be read as making all repository logging a portable CodeMaestro Skill behavior, this document takes precedence until the next consolidated review candidate incorporates the correction directly.

---

## 1. Two different logging responsibilities

The repository contains three logical history streams, but they do **not** have the same owner.

```text
Code-Maestro/
└── logs/
    ├── conversations/          # repository work-session governance
    └── logs/
        ├── project/            # repository work-session governance
        └── self-evolution/     # CodeMaestro Skill self-evolution contract
```

### 1.1 `logs/conversations/`

Owner: **the user's Chat / Work / Codex sessions that are developing or maintaining the CodeMaestro repository**.

Purpose:

- preserve the human-visible session history;
- support continuity across chats/surfaces;
- capture timestamps, session identity, branch/SHA context, checkpoints and handoffs;
- provide durable historical evidence for repository work.

This is **not** a generic runtime feature of the portable `@codemaestro` Skill. Installing or invoking CodeMaestro in an unrelated project does not, by itself, require conversation transcripts to be created there.

### 1.2 `logs/logs/project/`

Owner: **the user's Chat / Work / Codex sessions that are developing or maintaining the CodeMaestro repository**.

Purpose:

- record what changed in the CodeMaestro project;
- preserve material repository mutations and state transitions;
- link decisions, files, commits, PRs, evals, approvals and evidence;
- support reconstruction, handoff and audit of the development process.

This is also **not** a portable runtime behavior of the CodeMaestro Skill.

### 1.3 `logs/logs/self-evolution/`

Owner: **the CodeMaestro Skill when explicitly executing the Command-Gated Self-Evolution Protocol**.

Purpose:

- record why/how CodeMaestro researched itself;
- preserve self-audit findings and hypotheses;
- record RED evals, candidate changes, regressions, review and promotion status;
- record rejected/no-change outcomes;
- preserve rollback information and the evidence supporting an upgrade claim.

This stream is part of the Skill's self-evolution behavior when the self-evolution target/repository and write capability are available and authorized.

---

## 2. Real-time repository work-session instruction

After written-spec review approval, the **first implementation milestone** is repository work-session logging infrastructure for the user's project-working chats.

Before any other implementation work, create and verify:

```text
logs/conversations/
logs/logs/project/
```

plus a canonical repository instruction that every Chat / Work / Codex session working on the CodeMaestro repository must follow.

That instruction must require **real-time / event-time maintenance**, not retrospective end-of-session reconstruction.

Canonical behavior:

```text
SESSION START
-> locate/read the repository work-session protocol
-> initialize or resume session history
-> capture repository/branch/SHA context
-> perform project work
-> append conversation/session history as work progresses
-> append material project events when they occur
-> append corrections/supersessions rather than rewriting history
-> write checkpoint/handoff state before ending or transferring work
```

Material events include, when relevant:

- design/research approval;
- file mutation;
- branch/commit/PR change;
- eval failure/pass;
- state or scope change;
- rollback/correction;
- other consequential project state transitions.

The repository work-session protocol is project-development governance. It must not be embedded as a generic requirement that the portable CodeMaestro Skill impose on unrelated user projects.

---

## 3. Self-evolution logging is implemented with Self-Evolution

The Self-Evolution audit mechanism is a separate concern and is implemented **when the Command-Gated Self-Evolution Controller is implemented**, not as part of the initial repository-chat logging bootstrap merely because the directory name has been designed.

At self-evolution implementation time, create/activate the dedicated stream:

```text
logs/logs/self-evolution/
```

and enforce this invariant:

> Every explicit self-evolution run opens or resumes its dedicated audit record before substantive self-research/evolution work and appends material evidence, hypotheses, failures, candidate mutations, eval results, reviews, promotion decisions and rollback state as they occur.

The self-evolution audit trail belongs to CodeMaestro's runtime methodology; `conversations/` and `project/` belong to the user's repository-development workflow.

---

## 4. Relationship during a self-evolution development session

When a project-working chat is also executing or developing a self-evolution run, all three streams may exist simultaneously but represent different facts:

```text
logs/conversations/
    human-visible discussion/session continuity

logs/logs/project/
    what actually changed in the repository

logs/logs/self-evolution/
    why/how CodeMaestro researched, evaluated or changed itself
```

A real repository mutation caused by self-evolution should be represented in both relevant domains:

- `self-evolution/` contains the self-evolution rationale/evidence/eval history;
- `project/` contains the actual repository mutation and references the self-evolution ID.

This is intentional cross-reference, not duplicated ownership.

---

## 5. Conversation history and Self-Evolution

Conversation transcripts are **not default input** to Self-Evolution.

Default self-evolution evidence should come from current repository/executable state, canonical specifications/ADRs, eval evidence, relevant project logs, previous self-evolution records and current authoritative external research.

Conversation transcripts may be consulted only when their expected evidentiary value justifies the context, privacy exposure and processing cost, for example to reconstruct missing rationale, resolve historical intent conflict, investigate recurring user corrections, or satisfy an explicit user request.

If consulted, the self-evolution record should state why and what scope was used.

---

## 6. Timing gate after final written-spec review

The required sequence is:

```text
WRITTEN SPEC APPROVED
        |
        v
MILESTONE 0 — REPOSITORY WORK-SESSION LOGGING
        |- create logs/conversations/
        |- create logs/logs/project/
        |- create schemas/templates
        |- create canonical real-time session instruction
        |- verify append-only/event-time workflow
        |
        v
ONLY THEN
        |- architecture/research canonicalization
        |- capability contracts
        |- RED evals
        |- Skill packaging/orchestrator/modules
        |- Self-Evolution Controller
        |    `- create/activate self-evolution audit mechanism at that time
        `- stabilization
```

Therefore the two commitments are deliberately separate:

1. **Immediately after review:** build real-time session history + project logging for the chats used to develop CodeMaestro.
2. **At the Self-Evolution implementation stage:** build and enforce CodeMaestro's own dedicated self-evolution audit logging.

---

## 7. Canonical ownership invariants

> **Repository conversation history and ordinary project-change logs are development-governance records maintained by the user's project-working Chat / Work / Codex sessions. They are not generic runtime features of the portable CodeMaestro Skill.**

> **The dedicated self-evolution audit stream is part of CodeMaestro's Command-Gated Self-Evolution Protocol and is maintained by the Skill when explicitly performing self-evolution.**

> **Repository work-session logs are established first after written-spec approval; Self-Evolution-specific logging is implemented with the Self-Evolution Controller at its proper implementation stage.**
