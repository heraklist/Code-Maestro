# CM-R-016 — Universal Language Intelligence and Experimental Language Support

**Priority:** P0  
**Status:** IN RESEARCH  
**Started:** 2026-09-04

## Research objective

Design the language-intelligence layer that lets CodeMaestro work reliably across mainstream, niche, legacy, domain-specific, and experimental languages without requiring one permanently installed Skill per language.

The target is not a static encyclopedia. The target is a disciplined mechanism for identifying a language and its actual project environment, acquiring the smallest authoritative knowledge needed, selecting the correct engineering workflow, and validating exact claims or generated code at the strongest evidence level available.

## Accepted architectural direction

CodeMaestro will separate:

1. **Autonomous engineering sub-skills** — debugging, testing, refactoring, security, architecture, performance, CI/CD, database work, and other engineering methodologies.
2. **Shared Language Intelligence** — language detection, maturity classification, version/freshness reasoning, toolchain discovery, source-of-truth routing, language profiles, and unknown-language research.
3. **Selective standalone language correction/orientation skills** — only for languages where a generic profile is insufficient because syntax, semantics, tooling, or model misconceptions change rapidly or require unusually specialized guidance.

The parent CodeMaestro orchestrator may compose these capabilities, but each engineering sub-skill must remain correct when invoked independently. The parent must not compensate for a sub-skill that lacks its own scope, evidence, failure, freshness, or output contracts.

## Why not one Skill per language

A universal language capability cannot be implemented as hundreds of permanently installed language skills without creating unnecessary discovery/context overhead and a very large maintenance surface.

A language catalog and on-demand profiles scale better because most languages need structured discovery and verification rather than a unique procedural Skill.

Standalone language skills are a promotion path, not the default representation.

## Initial research evidence

### GitHub Linguist

GitHub Linguist maintains a broad machine-readable catalog of languages known to GitHub, including language type, file extensions, filenames, aliases, interpreters, group relationships, and related metadata.

Use: seed catalog, file/language detection hints, aliases, and classification support.

Do not use: syntax/API correctness authority.

Primary source: `github-linguist/linguist` — `lib/linguist/languages.yml`.

### Modular Mojo Agent Skills

Modular publishes official Agent Skills for Mojo. Its `mojo-syntax` skill is intentionally a correction layer for rapidly changing syntax and known model misconceptions rather than a bundled copy of the full language documentation. It emphasizes concise corrective knowledge and compilation/testing of generated Mojo code.

Architectural lesson: a fast-moving language may justify a maintained correction skill, especially where pretrained knowledge is predictably stale.

Primary source: `modular/skills`, especially `mojo-syntax/SKILL.md`.

### MoonBit Agent Skills

MoonBit publishes multiple official Agent Skills, including orientation, refactoring, proof, C bindings, spec-test development, and migration workflows.

The `moonbit-orientation` skill uses a freshness gate, project/toolchain inspection, authoritative API discovery, bounded research, explicit verification, and refusal to turn plausible cross-language guesses into exact MoonBit facts.

Architectural lesson: language support can be a routed set of narrow capabilities, and exact API/tool claims should be verified from local or official sources rather than inferred from model memory.

Primary source: `moonbitlang/skills`, especially `skills/moonbit-orientation/SKILL.md`.

## Language Profile Contract — draft

A language profile should be able to describe, when applicable:

### Identity

- canonical language name
- aliases
- extensions and significant filenames
- language/domain classifications
- maturity/status
- official specification
- official documentation
- canonical repository or project source

### Toolchain

- compiler/interpreter
- runtime
- package/dependency manager
- build system
- test runner
- formatter
- linter/static analysis
- language server
- debugger
- project and dependency manifests
- common source layout

### Semantics and engineering model

- primary paradigms
- type system
- memory/ownership model
- error model
- concurrency/async model
- module/package model
- FFI/interoperability model
- supported targets/backends

### Reliability-sensitive guidance

- idiomatic conventions
- known anti-patterns
- known model misconceptions
- security-sensitive constructs
- version-sensitive areas
- narrow validation commands
- source hierarchy
- freshness policy

Profiles are references/data contracts, not automatically standalone Skills.

## Language classification dimensions — draft

### Domain classification

A language may belong to one or more domains:

- general-purpose/application
- systems/native
- managed/VM
- scripting
- shell/automation
- functional
- scientific/numerical
- data/query
- web/markup/style/template
- configuration/build/IaC
- GPU/shader/parallel
- hardware/HDL
- blockchain/smart-contract
- formal verification/proof
- specification/modeling
- parser/grammar/meta-language
- assembly/IR/bytecode
- legacy/enterprise
- educational/esoteric

### Maturity classification

- `STABLE`
- `EVOLVING`
- `FAST-MOVING`
- `EXPERIMENTAL`
- `LEGACY`
- `HISTORICAL`
- `DEPRECATED`

Maturity is independent of domain and should influence freshness and verification requirements.

## Language Reliability Levels — draft

- **L1 — Locally Verified:** relevant code/project behavior was checked against the local toolchain, build, tests, or direct execution.
- **L2 — Current Officially Verified:** exact syntax/API/tool behavior was checked against current authoritative documentation/specification but not locally executed.
- **L3 — Reference Grounded:** reliable language guidance exists, but exact current behavior has not been directly verified.
- **L4 — Research Required:** fast-moving, experimental, unfamiliar, or obscure language where exact implementation claims require current research.
- **L5 — Recognition Only:** enough evidence exists to identify/explain the language, but not enough to claim production-correct code generation.

The final answer or engineering report must not imply a stronger level than the evidence supports.

## Unknown-language protocol — draft

```text
Detect identity
→ identify project/version evidence
→ locate authoritative spec/docs/repository
→ determine maturity
→ discover compiler/runtime/toolchain
→ discover build/test/format workflow
→ learn only the syntax/semantics required for the task
→ implement narrowly
→ compile/test when possible
→ report actual evidence level
```

Unknown or rare languages are not automatically unsupported. They enter a research-and-verification path.

## Source hierarchy — draft

For exact language/toolchain claims, prefer:

1. local project files and installed toolchain behavior when they represent the actual target environment;
2. official language specification;
3. official language/toolchain documentation;
4. official repository, release notes, changelog, or maintainer guidance;
5. official package registry or API documentation;
6. high-quality community sources only when primary evidence is insufficient.

Discovery catalogs such as GitHub Linguist may identify a language but do not establish syntax or API correctness.

## Standalone language-skill promotion criteria — draft

A language should receive its own CodeMaestro language correction/orientation Skill only when the generic Language Intelligence layer is demonstrably insufficient and several of the following apply:

1. syntax or semantics change quickly enough to invalidate model knowledge;
2. models show repeatable, important misconceptions;
3. the language has a substantially different mental model;
4. the toolchain requires unusual procedural guidance;
5. CodeMaestro usage justifies the context and maintenance cost;
6. authoritative sources are available and maintainable;
7. meaningful evals can be constructed;
8. a generic profile fails to produce reliable engineering outcomes.

Promotion should be justified by eval evidence, not popularity alone.

## Autonomous engineering sub-skill contract — draft

Every future CodeMaestro engineering sub-skill should explicitly define:

- trigger conditions
- scope
- non-goals
- required context
- source hierarchy
- workflow
- tool/capability contract
- failure behavior when capabilities are absent
- freshness gate
- output contract
- verification contract
- evidence/status vocabulary
- required and optional dependencies
- standalone fallback behavior
- eval scenarios
- regression expectations

A sub-skill must not depend on hidden parent-orchestrator behavior to remain safe or correct.

## Universal code-quality contract — draft

When CodeMaestro generates or modifies code in any language, the target is:

- correct for the detected version/environment;
- idiomatic for the ecosystem where evidence permits;
- the smallest necessary change;
- no invented APIs or unverified exact calls presented as fact;
- no unexplained unsafe behavior;
- consistent with project formatting/toolchain conventions;
- tested or otherwise validated appropriately to the change when capabilities allow;
- reported with an evidence level that distinguishes plausible code from code that actually compiled or passed tests.

## Representative coverage set

The language system should be evaluated across different language families rather than only mainstream web languages. Initial representative families include:

- C, C++, Rust, Zig
- Java, Kotlin, Scala
- C#, F#
- Python, Ruby, PHP
- JavaScript, TypeScript, Luau
- Go
- Swift, Objective-C
- Dart
- Haskell, OCaml, Elm, Gleam, Roc
- Erlang, Elixir
- Lisp, Scheme, Clojure, Racket
- Julia, R, Fortran
- Bash, PowerShell, Fish
- SQL and major dialects
- GraphQL, Cypher, PromQL
- HCL, Nix, CUE, Starlark, Jsonnet
- Solidity, Vyper, Move, Cairo, Sway, Tact
- CUDA, OpenCL, GLSL, HLSL, WGSL, Metal shading languages
- Verilog, SystemVerilog, VHDL
- Lean, Rocq/Coq, Agda, Dafny, TLA+, Alloy
- LLVM IR and WebAssembly text
- COBOL, Ada, legacy Fortran
- Mojo, MoonBit, Carbon, Koka, Flix, Nickel

This is a representative test matrix, not a whitelist. Long-tail languages remain addressable through the unknown-language protocol.

## Open research questions

1. What is the minimum profile schema that still supports reliable engineering across language families?
2. Which profile fields should be generated dynamically versus stored?
3. Which catalogs should seed language detection and which should be excluded as correctness sources?
4. How should CodeMaestro detect the actual language/toolchain version from a project reliably?
5. How should profile freshness be measured and invalidated?
6. What thresholds justify promotion to a standalone language Skill?
7. How should multiple languages in one repository be composed without unnecessary context loading?
8. How should embedded DSLs, generated languages, shader languages, query languages, and private DSLs fit the same model?
9. Which representative languages best expose weaknesses in the generic protocol during evals?
10. Can official vendor-maintained Agent Skills be consumed as research/correction sources without creating hidden dependency or trust problems?

## Next research steps

- validate the Agent Skills packaging/context-cost assumptions against current primary specifications;
- inspect additional official language-agent repositories where available;
- compare language metadata sources and design a source registry;
- draft a machine-readable Language Profile schema;
- design baseline evals for stable, fast-moving, experimental, obscure, multi-language, and private-DSL scenarios;
- use those evals before creating `codemaestro-language-intelligence` or any promoted standalone language Skill.
