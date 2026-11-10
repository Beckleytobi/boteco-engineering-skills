# Software Design Principle Routing

Use principles to diagnose a concrete problem. Do not score code against a checklist of acronyms.

## Required design-mechanism record

For every abstraction, interface, layer, pattern, dependency, or significant structural change considered, record:

| Field | Required content |
|---|---|
| Status | Keep / Introduce / Defer / Reject |
| Problem | The behaviour, rule, failure, or change pressure addressed |
| Evidence | Repository observation, accepted requirement, defect, or measured cost |
| Smallest mechanism | Minimum design move that addresses it |
| Consequence | Complexity, coupling, indirection, migration, or learning cost |
| Verification | Behavioural evidence and review check |
| Revisit trigger | What future evidence could change the decision |

## Principle routing table

| Observed problem | Principle/lens | Useful move | Common misuse |
|---|---|---|---|
| Design solves speculative futures | Simplicity, KISS, YAGNI | Remove unearned layers/options | Calling incomplete behaviour “simple” |
| One unit owns unrelated reasons to change | Separation of concerns, cohesion | Split by domain responsibility | Fragmenting every function into a file |
| Change spreads through unrelated modules | Coupling, clear contracts | Narrow dependencies and knowledge | Interfaces everywhere without volatility |
| Callers depend on internals | Encapsulation, information hiding | Expose stable behaviour-oriented contract | Getter/setter wrapper that hides nothing |
| Same knowledge repeated and may diverge | DRY, single source of truth | Give knowledge one owner | Merging coincidental duplication |
| Variation creates large conditionals | Open/closed, strategy or polymorphism | Isolate evidenced variation axis | Plugin architecture for one case |
| Consumer needs tiny part of broad API | Interface segregation | Narrow consumer-facing contract | One interface per method |
| High-level rule imports volatile detail | Dependency inversion | Put boundary at volatility/side-effect seam | Dependency injection container by default |
| Names require comments to explain mechanics | Naming/readability | Use domain language and explicit flow | Extremely long names hiding poor boundaries |
| State can be changed from many places | State ownership, encapsulation | Centralize transitions and derive copies | Global mutable singleton |
| Errors are swallowed or inconsistent | Error handling, defensive design | Define expected/unexpected failures and owner | Catch-and-log everywhere |
| Change is risky because behaviour is unknown | Testing as design, small changes | Characterization tests and seams | Tests coupled to private implementation |
| Structure resists repeated real changes | Refactoring, evolutionary design | Incremental behaviour-preserving redesign | Rewrite to match an ideal architecture |
| Pattern name is proposed first | Design patterns | Restate the recurring problem; use pattern only if fit improves | Catalogue-driven design |

## SOLID with restraint

Use SOLID as five targeted questions:

- **SRP:** Does this unit have multiple unrelated reasons to change?
- **OCP:** Is an evidenced variation axis forcing risky edits to stable rules?
- **LSP:** Can a promised substitute preserve the behavioural contract, including errors and side effects?
- **ISP:** Is a consumer forced to depend on operations it does not use?
- **DIP:** Does stable policy directly depend on a volatile detail that needs isolation?

If the answer is no, do not add structure merely to demonstrate the principle.

## Pattern admission test

Introduce a named pattern only when all are true:

1. the recurring problem exists now;
2. the pattern improves a named quality or change path;
3. the team/framework can support it clearly;
4. a simpler local mechanism is insufficient;
5. tests can protect the resulting contract;
6. removal or migration consequences are understood.

## Dependency admission test

Before adding a package/framework, record capability, alternatives already present, activity/maintenance, security/license considerations, bundle/runtime/operational cost, API stability, lock-in, and replacement path. A dependency is not justified solely because it reduces initial lines of code.

