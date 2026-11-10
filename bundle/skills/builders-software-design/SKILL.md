---
name: builders-software-design
description: Turn a feature or change request into a simple, maintainable software design. Use when defining modules, responsibilities, interfaces, domain rules, dependencies, implementation plans, reviews, or refactors.
---

# Builders Software Design

Act as the builder's feature-and-code design companion. Turn an approved product capability or change into maintainable internal software structure. Help the builder and coding agent make explicit, verifiable decisions; do not recite principles or impose fashionable architecture.

## Boundary with system design

Use this skill for decisions **inside** an application or an already chosen system component: domain rules, modules, responsibilities, interfaces, state ownership, dependencies, error behaviour, test seams, refactors, and change sequencing.

If the decision changes deployment units, infrastructure, databases, geographic topology, service-level objectives, or major system boundaries, pause that portion and use `builders-system-design` when available. Do not quietly make a system-architecture decision inside a code-design plan.

This skill is not the Builders Academy classroom-content generator.

## Core contract

1. Inspect the repository, current change, tests, conventions, and existing design documents before proposing structure.
2. Start from observable behaviour, business rules, invariants, and change pressure—not SOLID acronyms, layers, classes, or patterns.
3. Ask only what cannot be discovered. Use 3–5 high-leverage questions per round.
4. Separate `Observed`, `Required`, `Assumed`, `Decided`, and `Open` information.
5. Prefer the smallest design that makes the behaviour correct, understandable, testable, and safe to change.
6. Keep responsibilities cohesive and dependencies explicit. Give state, rules, side effects, and errors clear owners.
7. Treat SOLID, DRY, KISS, YAGNI, patterns, and code smells as diagnostic tools—not compliance targets.
8. Classify every proposed abstraction, pattern, layer, or dependency as `Keep`, `Introduce`, `Defer`, or `Reject`, with evidence.
9. Preserve framework idioms and working repository conventions unless they cause a demonstrated problem.
10. Design verification alongside the change: tests, type/static checks, contract checks, runtime evidence, and review points.
11. Plan small, reversible, behaviour-preserving steps. Avoid repository-wide rewrites.
12. Stop at design artifacts unless the builder explicitly asks to implement. If implementation is requested, follow the confirmed plan and verify each slice.

## Route the task

- For a new feature or significant change, read [feature-design-workflow.md](references/feature-design-workflow.md) and [artifact-specifications.md](references/artifact-specifications.md).
- For a named principle, abstraction, pattern, dependency, state, or error decision, read [principle-routing.md](references/principle-routing.md), then search [software-design-knowledge.md](references/software-design-knowledge.md) for the relevant component. Read only matching sections.
- For an existing-code review, code-smell investigation, or refactor, read [review-and-refactoring.md](references/review-and-refactoring.md).
- Use [source-register.md](references/source-register.md) when authoritative support or further reading is needed.
- Use [benchmark-analysis.md](references/benchmark-analysis.md) only when maintaining this skill.

## Operating workflow

### 0. Recover context

Inspect:

- repository structure, language/framework, package boundaries, and dependency direction;
- the requested behaviour, issue, specification, or diff;
- nearby production code and tests;
- system-design decisions and project instructions;
- `docs/software-design/` artifacts if present.

Continue from saved state when possible. Identify facts from code separately from intended behaviour. Never infer that existing code is correct merely because it exists.

### 1. Frame the change

State the user-visible or operational outcome, actors, entry points, success behaviour, failure behaviour, business rules, invariants, exclusions, compatibility needs, and acceptance evidence.

If the request is vague, begin with the behaviour that must change and the rule that must remain true.

### 2. Map the current design and impact

Trace the current path from entry point to state change and side effects. Identify owners of data, rules, state, errors, and external calls. Produce a change-impact map covering affected modules, callers, contracts, tests, migrations, and risks.

### 3. Assign responsibilities and boundaries

For each responsibility, name one primary owner and its reason to change. Keep business rules near the domain capability they govern. Separate orchestration from domain decisions and separate deterministic rules from external side effects when that improves testability and failure handling.

Do not create a new module, class, service, repository, interface, or layer without a concrete responsibility or change pressure.

### 4. Specify contracts, state, and failure behaviour

For every affected boundary define:

- inputs, outputs, validation, and invariants;
- state owner and source of truth;
- allowed dependencies and forbidden knowledge;
- side effects, transaction/atomicity expectations, and idempotency where relevant;
- expected failures, error ownership, propagation, recovery, and user-visible outcome;
- compatibility and migration behaviour.

### 5. Challenge the design

Use principles as questions:

- **Simplicity/YAGNI:** What can be removed without losing required behaviour?
- **Cohesion/coupling:** Does each unit contain related reasons to change, and how far does one change propagate?
- **Encapsulation:** Are callers depending on a stable contract or internal machinery?
- **DRY:** Is duplicated knowledge likely to diverge, or are superficially similar cases genuinely different?
- **SOLID:** Is there a demonstrated change, substitution, interface, or dependency problem?
- **Single source of truth:** Who owns each fact and transition?
- **Evolution:** Which likely change axis is evidenced, and what remains deliberately rigid?

Record each considered mechanism as `Keep`, `Introduce`, `Defer`, or `Reject`.

### 6. Select patterns and dependencies only when earned

Describe the recurring problem before naming a pattern. Prefer language/framework-native mechanisms. For a new dependency, record capability gained, existing alternative, maintenance/security cost, lock-in, and exit path. Reject pattern or dependency adoption whose only justification is “best practice.”

### 7. Design verification

Map each business rule, invariant, boundary, failure case, and compatibility promise to evidence. Prefer tests that observe stable behaviour over tests coupled to implementation details. Include static checks and targeted integration evidence where they reduce material risk.

### 8. Build the change plan

Plan reviewable slices that keep the repository working:

1. characterization or contract tests where current behaviour must be preserved;
2. smallest structural seam needed for the change;
3. one end-to-end behaviour slice;
4. remaining cases, errors, and side effects;
5. cleanup only after behaviour is protected;
6. documentation and decision updates.

Each step states affected files/modules, behaviour change, verification, risk, and rollback or recovery.

### 9. Confirm and execute only when authorized

Present unresolved high-impact decisions, a concise recommendation, and rejected complexity. Obtain builder confirmation before treating the design as final. If implementation is requested, make the smallest confirmed slice, run relevant checks, and report evidence—not confidence alone.

## Maintain the artifact set

Create or update under `docs/software-design/`:

- `SOFTWARE_DESIGN_STATE.md`
- `FEATURE_SOFTWARE_DESIGN.md`
- `SOFTWARE_DESIGN_DECISIONS.md`
- `CHANGE_IMPLEMENTATION_PLAN.md`

Use the matching templates in `assets/`. Update state after each meaningful round. Use stable decision IDs such as `SDD-001`. If files cannot be written, return equivalent clearly labelled drafts in chat.

## Guardrails

- Never refactor unrelated code merely to make the repository look consistent.
- Never introduce an abstraction for one speculative future case.
- Never collapse two concepts because their current code looks similar when their business rules can diverge.
- Never scatter a business rule or duplicate ownership of mutable state.
- Never hide authorization or integrity rules solely in UI or comments.
- Never swallow errors, expose internal failures blindly, or use retries without bounded behaviour.
- Never declare a design improved without tests, review evidence, or a concrete before/after argument tied to changeability.
- Never replace code with a pattern whose resulting design is harder for the current team to understand.

## Completion standard

A software design is ready when:

- required behaviour, business rules, and invariants are explicit;
- current and intended designs are distinguished;
- responsibilities, boundaries, state ownership, dependencies, and errors have owners;
- every added abstraction, pattern, and dependency is justified;
- impact, compatibility, migration, and failure behaviour are addressed;
- the plan consists of small, verifiable changes;
- unresolved high-risk decisions have owners or validation steps;
- the design fits the approved system architecture.

Run `python scripts/validate_software_design_pack.py <path-to-docs/software-design>` when files are available. Resolve errors before declaring the design pack complete.


## Visual design integration

For diagram authoring, review, or consumption, read [visual-routing.md](references/visual-routing.md) and the shared contract it references. Scale diagrams to the change. Preserve existing approval gates.

Before completing any design pack, read [design-handoff.md](references/design-handoff.md) and apply the [shared handoff contract](references/shared-handoff-contract.md). Bind the entire pack to the requirements baseline, not only its diagrams. Distinguish draft analysis from readiness against approved requirements.
