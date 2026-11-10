# Execution and Diagnosis

## Preflight

Before running tests, discover repository instructions, canonical commands, framework and versions, test locations and naming, fixtures, setup/teardown, coverage configuration, environment variables, services, network needs, permissions, and side effects. Inspect CI configuration to understand established commands, but do not treat configured or previously run checks as evidence for the current artifact.

Prefer the repository's existing stack. If a required framework or service is unavailable, distinguish a tooling gap from a product failure. Do not install or introduce material tooling without authorization.

## Safe and attributable execution

Record for each run:

- exact command or reproducible manual steps;
- artifact identity such as commit SHA when available;
- environment (`LOCAL`, `ISOLATED TEST`, `CONTAINER`, `CI`, `PREVIEW`, `STAGING`, or explicitly production-safe verification);
- relevant configuration/data assumptions without exposing secrets;
- start time or run identifier and exit code;
- tests executed, passed, failed, skipped, flaky, not run, and infrastructure failures;
- durable evidence paths or URLs where available.

Use synthetic data, fixtures, isolated accounts, disposable records, or authorized sanitized data. Avoid real customer mutation, production secrets, and uncontrolled external actions. Payments, email, SMS, push, external APIs, production databases, and destructive migrations require verified sandboxing or explicit safe authorization. When safety is unclear, do not execute.

Parallelize only independent tests whose fixtures and mutable state cannot collide, whose rate limits permit it, and whose output remains attributable. Otherwise use serial execution.

## Ordering

When appropriate, fail fast through static prerequisite checks, targeted unit/component checks, integrations, API/contracts, broader suites, E2E, and specialized checks. This is an optimization, not evidence substitution: static analysis or a build can expose blockers but cannot prove behaviour.

## Determinism and isolation

Avoid dependence on execution order, developer data, shared mutable state, real-time waiting, external network availability, and unrelated tests. Control time, randomness, identifiers, data, responses, and environment configuration where doing so does not mock away a material integration. Document unavoidable dependencies.

Prefer condition-based waits over arbitrary sleeps. Tests should make the failed behaviour, expected result, observed result, and relevant context visible.

## Failure classification

Before editing anything, classify the best-supported cause:

1. product defect;
2. test defect;
3. requirement mismatch or ambiguity;
4. test-data problem;
5. environment failure;
6. external dependency failure;
7. configuration failure;
8. flaky/nondeterministic test;
9. infrastructure failure;
10. unknown.

Reproduce and isolate enough to distinguish them. Do not assume either code or test is wrong merely because changing one is convenient.

## Safe test mutation review

When a failing test is modified, inspect the semantic difference:

- **Additive/legitimate:** adds a criterion, corrects a demonstrably wrong expectation, adapts to an explicitly changed requirement, or improves diagnostics without reducing what is proved.
- **Suspicious weakening:** removes assertions, broadens accepted values, changes exact outcomes to existence checks, adds broad mocks, skips the case, auto-accepts a snapshot, or rewrites expected output to match current implementation.
- **Ambiguous:** requirement source or prior intent is unclear. Escalate or mark insufficient evidence rather than guessing.

When feasible, demonstrate that the test detects the defect: run it against the known-bad state, a focused mutation, or a logically controlled failing fixture. Do not destructively rewrite user work just to perform this check.

## Flakes and retries

A fail-then-pass test is `FLAKY` and unresolved unless the cause is fixed and stability is demonstrated according to the project's policy. Record initial result, bounded retries, history where available, suspected cause, and remediation. Never use unlimited retries or report only the final green run.

## Bug-fix evidence

Strong evidence shows:

1. the reported bug is reproduced;
2. a focused test fails for the expected reason on the faulty behaviour;
3. the fix changes that result to pass;
4. adjacent acceptance behaviour remains correct;
5. the new test and change context are handed to Regression Protection.

If the original defect cannot be reproduced, say so and do not claim the fix is verified solely because new code exists.
