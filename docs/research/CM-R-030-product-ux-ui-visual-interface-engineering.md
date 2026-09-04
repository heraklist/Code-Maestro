# CM-R-030 — Product, UX/UI & Visual Interface Engineering

**Priority:** P1 by default; P0 for user-facing/product-critical work
**Status:** IN RESEARCH
**Disposition:** DIRECTION ACCEPTED
**Opened:** 2026-09-04
**Direction accepted by:** `../architecture/2026-09-04-pass-5-acceptance-and-capability-freeze.md`

## Question

How should CodeMaestro design, audit, implement, and validate user-facing software across product framing, UX, interaction, visual design, accessibility, responsive behavior, design systems, and visual/interaction QA without fabricating user research?

## Expected output

- product/UX problem-framing workflow;
- research-integrity boundary between heuristic/expert analysis and observed user research;
- task/journey and information-architecture methodology;
- interaction/visual design guidance;
- accessibility integration;
- design-system/token/component governance;
- design-to-code and visual/interaction QA workflow;
- user-flow correctness evidence;
- eval scenarios for user-facing systems.

## Accepted direction

Product / UX / UI Engineering remains a canonical capability family. UI quality is multi-boundary:

```text
render correctness
+ interaction correctness
+ accessibility
+ visual fidelity
+ user-flow correctness
```

Heuristic/expert analysis must never be presented as observed user research, and CodeMaestro must not invent participants, observations, consent, or quotes.

## Primary authorities

- W3C WAI WCAG 2.2 / ISO update: https://www.w3.org/WAI/news/2025-10-21/wcag22-iso/
- Current platform/framework primary documentation as applicable to the target project.

**Last verified:** 2026-09-04

## Evidence limitations

Detailed product/UX methodology remains to be synthesized. Accessibility/platform guidance is version-sensitive and must be researched at execution time where material.
