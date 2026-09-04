# CM-R-029 — Cross-Runtime Portability, Capability Discovery & Conformance

**Priority:** P0
**Status:** ACCEPTED
**Opened:** 2026-09-04
**Accepted by:** `../architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md`

## Question

How should CodeMaestro preserve equivalent engineering behavior across Chat, Work, Codex, and future surfaces while capability availability, permission, execution mechanics, and connected-app support differ?

## Expected output

- runtime capability-discovery contract;
- availability vs authorization model;
- execution-ceiling semantics;
- graceful degradation/recovery rules;
- cross-surface handoff/evidence contract;
- capability-first shell/filesystem/repo/app/database/deployment semantics;
- cross-runtime conformance eval design;
- current packaging/installation constraints for portable Agent Skills/OpenAI surfaces.

## Accepted direction

CodeMaestro is capability-first and surface-aware. Product surface names do not artificially cap execution depth. Equivalent available-and-authorized capabilities should produce equivalent engineering behavior; exact tool traces may differ.

## Primary authorities

- OpenAI Skill guidance: https://learn.chatgpt.com/docs/build-skills
- Agent Skills specification: https://agentskills.io/specification
- OpenAI Plugins in ChatGPT and Codex: https://help.openai.com/en/articles/20001256-plugins-in-codex/
- OpenAI Apps in ChatGPT: https://help.openai.com/en/articles/11487775

**Last verified:** 2026-09-04

## Evidence limitations

OpenAI product behavior is fast-moving. Surface-specific availability and packaging requirements must be reverified before implementation or release claims.
