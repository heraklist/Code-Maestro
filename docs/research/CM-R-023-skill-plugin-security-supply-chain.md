# CM-R-023 — Skill/Plugin Security & Capability Supply Chain

**Priority:** P0
**Status:** IN RESEARCH

## Question

How should CodeMaestro safely discover, inspect, evaluate, adapt, and optionally adopt external Skills, plugins, prompts, scripts, tools, and agent repositories without importing prompt injection, dangerous code, excessive permissions, supply-chain risk, licensing conflicts, or hidden behavioral dependencies?

## Accepted direction

Third-party agent artifacts are untrusted inputs until reviewed. The preferred adoption path is mechanism extraction and independent redesign rather than copy-paste assembly.

## Candidate review pipeline

```text
DISCOVER
→ PROVENANCE / LICENSE CHECK
→ QUARANTINE / STRUCTURE INSPECTION
→ PROMPT-INJECTION REVIEW
→ EXECUTABLE / SCRIPT REVIEW
→ DEPENDENCY / PACKAGE REVIEW
→ FILESYSTEM / NETWORK / CREDENTIAL REVIEW
→ TOOL / PERMISSION SCOPE REVIEW
→ BEHAVIORAL / EVAL REVIEW
→ ADOPT / ADAPT / REJECT / RESEARCH FURTHER
```

## Research targets

- prompt injection embedded in skills and references;
- scripts, hooks, binaries, symlinks, installers, and hidden files;
- package/dependency typosquatting and provenance;
- network egress and credential access;
- tool authorization and declared `allowed-tools`-style contracts;
- unsafe post-install hooks or background behavior;
- transitive plugin dependencies;
- license compatibility and attribution/share-alike constraints;
- static vs dynamic analysis boundaries;
- skill marketplace trust signals;
- pre-install vs post-install validation;
- behavior/eval evidence for imported mechanisms.

## Key questions

1. What minimum review is required before merely reading an external Skill?
2. What additional review is required before executing bundled scripts?
3. How should CodeMaestro handle skill repositories with unknown or incompatible licenses?
4. Can a reusable risk taxonomy cover prompt, code, dependency, permission, and provenance risk coherently?
5. What constitutes sufficient evidence to promote a third-party mechanism into canonical CodeMaestro guidance?
6. How should installed plugin/tool permissions be represented in the capability model?
7. Which checks can be deterministic and which require manual/behavioral review?

## Preferred references

- Trail of Bits skill/security ecosystems
- `borghei/Claude-Skills` skill-security-auditor patterns
- OpenAI/Codex plugin and Skill packaging guidance
- Agent Skills specification
- current software supply-chain standards under CM-R-005
- MCP/tool authorization work under CM-R-008

## Non-decision

This track does not authorize automatic installation, execution, or import of third-party skills or plugins. Discovery and analysis remain separate from adoption and execution authority.
