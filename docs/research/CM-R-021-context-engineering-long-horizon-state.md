# CM-R-021 — Context Engineering & Long-Horizon State

**Priority:** P0
**Status:** IN RESEARCH

## Question

How should CodeMaestro preserve task-relevant state, evidence, plans, and coordination across long-running sessions, compaction, parallel agents, tool-output growth, and interrupted/resumed work without turning the active context into an unbounded memory dump?

## Accepted direction

CodeMaestro needs an explicit Context & Long-Horizon Intelligence capability. Durable state should live in files/artifacts when it must survive compaction, handoff, resumption, replication, or audit. Active context should contain the smallest high-signal working set needed for the current decision.

## Research targets

- context degradation and poisoning;
- context compression and loss analysis;
- filesystem-backed context and durable scratchpads;
- raw evidence vs lossy summaries;
- just-in-time retrieval;
- context isolation across subagents;
- handoff payload design;
- stale-context detection;
- context budgets and stop/refresh criteria;
- long-horizon task briefs;
- state recovery after interruption;
- evals for context retention, contamination, and routing.

## Key questions

1. Which artifact types must be durable by default?
2. Which state is append-only vs replaceable?
3. When is summarization acceptable, and when must raw evidence remain retrievable?
4. How should CodeMaestro detect context rot, stale assumptions, or contradictory state?
5. What minimum context should be transferred to a fresh agent?
6. How can context quality be tested independently of model eloquence?
7. How should token/context cost enter routing and orchestration decisions?

## Preferred references

- `muratcankoylan/Agent-Skills-for-Context-Engineering`
- OpenAI/Codex skill and agent architecture
- Superpowers durable planning/handoff patterns
- Cusp research/evidence artifacts
- rigorous long-horizon agent systems with reproducible state

## Non-decision

This track does not yet decide that Context Intelligence will be a standalone physical Skill. It may remain a shared orchestration/reference capability if evals show that is cleaner.
