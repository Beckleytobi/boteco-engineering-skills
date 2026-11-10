# Risk classification and test strategy

Read this to calibrate how much regression work a given change actually warrants, and for the detailed patterns behind bug fixes, refactors, and legacy code.

## Change classification

A change can fall into more than one of these categories - classify by what it actually touches, not by how the task was described:

UI-only, business logic, shared utility, API, authentication, authorization, database/schema, migration, external integration, background job, queue/event, caching, infrastructure/configuration, dependency or library upgrade, refactor, bug fix, performance optimization, security change.

The classification isn't bookkeeping - it should change what you do next. A CSS-only change and an authentication-token change warrant genuinely different regression strategies; running the same checklist on both either wastes effort on the first or leaves the second dangerously under-verified.

## Risk-based depth

Don't run every possible test on every change unless the project's own policy requires that. Weigh:

- how critical the affected behavior is
- size of the diff
- how architecturally central the changed code is (how many things depend on it)
- number of dependents traced in the surface analysis
- whether any contract changed
- whether data or schema changed
- security, payment, or auth relevance
- whether a migration is involved, and whether it's reversible
- external side effects
- how good existing test coverage already is
- baseline confidence (from `regression-surface.md`)
- how novel or unusual the implementation approach is

If you use LOW / MEDIUM / HIGH / CRITICAL or similar labels, define what each one actually requires in terms of evidence gathered - a label with no operational meaning behind it is worse than no label, because it looks like rigor without providing any. Avoid manufacturing false precision (a numeric risk score to two decimal places is not more honest than a well-justified HIGH).

## Test inventory before test invention

Before writing anything new, find out what protection already exists: unit, integration, contract, end-to-end, smoke, snapshot, migration, API, security-adjacent, browser, mobile, and critical-journey tests. Map what you find onto the regression surface from Phase C of the main workflow. The goal is to know what's already covered so effort goes toward the actual gaps, not toward re-proving things that are already proven. Don't run tests just because they exist and are nearby - run the ones the surface analysis says matter.

## Selection hierarchy

Work outward through these levels, going as deep as the risk classification warrants:

1. **Direct tests** - cover the behavior intentionally changed.
2. **Dependency tests** - cover consumers and dependents of what changed.
3. **Contract tests** - protect the boundaries the change touches.
4. **Critical journey tests** - end-to-end or integration coverage of workflows the change intersects.
5. **Broader regression suite** - reserved for changes where blast radius or risk genuinely justifies the cost.

## Test pyramid awareness

Solve each regression concern at the lowest testing level that reliably protects it, rather than reaching for an expensive end-to-end test by default. Many focused unit tests, fewer integration or contract tests, and a small number of high-value end-to-end tests for genuinely critical journeys is a reasonable shape for most systems - but don't enforce a rigid numerical ratio, since different architectures legitimately call for different distributions. The point isn't the ratio; it's not paying end-to-end cost for something a unit test would have caught just as reliably.

## Avoid test explosion

An AI agent asked to add regression coverage can easily generate hundreds of tests that don't actually add confidence - duplicated assertions restated across many tests, tests that just mirror the source code back at itself, brittle tests pinned to internal structure that will break on the next unrelated refactor, or trivial implementation-detail tests that a real bug would never trip. Prioritize meaningful behavior, critical boundaries, business rules, contracts, previous defects, and high-risk or negative paths instead. Regression protection is about confidence, not a test count - a handful of well-aimed tests beats a large pile of shallow ones every time, and the pile also costs everyone who has to maintain it going forward.

## Test independence and fixtures

Regression tests that only pass in a specific order, or that quietly depend on shared mutable state, a database record left over from an earlier test, a stale cache, or a mock that didn't get reset, provide weaker protection than they appear to - a failure in one can mask or fake a failure in another, and the suite becomes harder to trust the more this happens. Where you're adding new tests, keep them independent and prefer fixtures simple enough that someone can look at a failure and immediately see the starting state, the action taken, the expected result, and the resulting state. Complex fixtures make failures hard to interpret, which quietly undermines the whole point of having the test.

## Missing coverage

This is one of the more valuable things this analysis produces, so don't let it get lost. If the regression surface includes behavior that matters and has no meaningful test protecting it, "all existing tests passed" is not an adequate report - because there was nothing there to fail. Say both things plainly and separately:

```
EXISTING TESTS: PASS
REGRESSION CONFIDENCE: LIMITED
MISSING PROTECTION:
Password reset depends on the modified token-validation function but currently
has no regression test.
```

Where it's proportionate to the risk, propose or write the minimum test that actually closes the specific gap identified - not a batch of tests chosen to move a coverage percentage. A single well-aimed test on the actual gap is worth more than ten tests that don't touch it.

## Characterization tests for under-tested legacy code

When a change needs to modify behavior that's poorly covered by tests, consider locking down current behavior before touching it: capture what the code currently does, write tests that describe that behavior, make the change, then check whether anything unintended moved. This gives you a real before/after comparison even where no test suite existed to provide one.

Don't let this become an excuse to preserve a bug. If the current behavior looks wrong or conflicts with what the change is actually supposed to do, that's a genuine ambiguity - escalate it rather than quietly locking in behavior everyone would agree is a defect if they looked closely.

## Bug-fix rule

The useful shape for a confirmed bug fix is: reproduce the bug, write a test that fails because of it, fix it, confirm the test now passes, then run the relevant regression checks around the fix. Where practical, the new test should specifically demonstrate that this exact bug can't come back silently - that's more valuable than a generic assertion that "the fix works." Where automated testing genuinely isn't practical for a given bug, it's fine to skip this - just say why, rather than silently omitting the test and letting it look like an oversight.

## Refactoring rule

A refactor is supposed to change structure without changing externally observable behavior - that's the whole premise, and the regression check for a refactor is really just verifying that premise held. Establish the behavioral baseline, run the relevant tests before touching anything, do the refactor, run the same tests again, and specifically inspect for contract changes. A refactor that unintentionally changed behavior isn't a successful refactor just because the resulting code is cleaner - cleaner code that does something different is a different feature, not a refactor, and should be treated with the scrutiny that implies.
