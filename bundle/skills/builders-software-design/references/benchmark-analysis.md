# Benchmark Analysis and Differentiation

Maintainer reference for the Builders Software Design skill, researched 1 September 2026.

## Compared approaches

| Existing approach | Useful pattern | Gap for Builders Academy |
|---|---|---|
| [DeerHide software-architecture skill](https://github.com/DeerHide/agent_skills/blob/main/skills/software-architecture/SKILL.md) | Broad coverage of SOLID, DRY, KISS, YAGNI, DDD, Clean Architecture, and refactoring | Principle/architecture catalogue can encourage compliance and over-design rather than evidence-led feature decisions |
| [jordanbyron philosophy-of-software-design](https://github.com/jordanbyron/agent-skills/blob/main/design/philosophy-of-software-design/SKILL.md) | Strong module-depth, interface, boundary, and complexity questions; good trigger coverage | Expert design lens rather than a novice-owned, persistent product-feature workflow |
| [luckys/agent-skills](https://github.com/luckys/agent-skills) | Rich specialist skills for clean code, DDD, TDD, hexagonal architecture, OOP, and functional design | Fragmented catalogue requires the user/agent to select the right doctrine before clarifying the problem |
| [solidifier](https://github.com/FernandoJRR/solidifier) | Treats over-engineering as a defect and applies SOLID with restraint | Primarily SOLID/pattern-focused and especially oriented to OO maintainability |
| Typical Clean Architecture/SOLID skills | Repeatable layer, dependency, and testability conventions | Often prescribe repositories, services, dependency injection, and interfaces before evidence exists |

## Distinct role

Builders Software Design is not a style guide, pattern catalogue, linter, code generator, or universal Clean Architecture mandate. It is a persistent reasoning workflow between an approved product capability and implementation.

Distinct mechanisms:

1. **Behaviour before structure:** begins with actor, outcome, rules, invariants, and failures.
2. **Repository evidence:** discovers current paths and conventions before asking or proposing.
3. **Builder ownership:** separates observed code, requirements, assumptions, decisions, and questions.
4. **Responsibility ownership:** rules, state, side effects, and errors receive explicit owners.
5. **Mechanism admission:** every abstraction, interface, layer, pattern, and dependency is kept, introduced, deferred, or rejected.
6. **Principles as diagnostics:** SOLID/DRY/KISS/YAGNI answer concrete questions rather than become targets.
7. **Small-change planning:** creates reversible slices instead of architecture rewrites.
8. **Verification as design:** maps rules and boundaries to observable evidence.
9. **System-design boundary:** does not silently redesign deployment/infrastructure while changing code.
10. **Resumability:** preserves feature design decisions across sessions and agents.

## Forward-test scenarios

1. Add cancellation rules to a small monolith without creating unnecessary layers.
2. Extend a multi-tenant permission path while preserving server-side authorization.
3. Refactor a giant function with weak tests using characterization-first steps.
4. Evaluate duplicated code where two cases look similar but business rules can diverge.
5. Add a second payment provider and determine whether an adapter/strategy is now earned.
6. Review an AI-generated repository containing repositories, factories, services, and interfaces with only one implementation.
7. Add a stateful workflow with expected failures, retries, and external side effects.
8. Handle a feature request that actually requires a new database/service, correctly routing the macro decision to system design.

Score behavioural correctness, unsupported assumptions, responsibility clarity, abstraction restraint, repository fit, change size, verification quality, builder comprehension, and cross-artifact consistency.

## Evidence caveat

Recent empirical work such as [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401) reports that many software-engineering skills produce little measurable pass-rate improvement. Treat packaging as insufficient: forward-test this skill against real repositories and improve only from observed failures.

