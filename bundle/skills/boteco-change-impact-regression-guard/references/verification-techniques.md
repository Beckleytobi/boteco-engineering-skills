# Verification techniques

Read this for how to run and interpret evidence honestly, once you know (from the main workflow and `risk-and-test-strategy.md`) what evidence to gather.

## Before-and-after comparison

For refactors, dependency upgrades, architecture changes, shared-utility changes, and migrations, compare the relevant tests before and after the change where that's practical - not just after.

If the baseline itself already had failing tests, keep these two things distinct:

- **Pre-existing failure**: was already broken before this change touched anything.
- **New failure introduced by this change**: started failing because of this change.

Don't let a genuinely pre-existing, already-documented failure get pinned on the current change. Just as importantly, don't excuse a new failure by pointing at unrelated pre-existing ones ("the suite was already red, so one more failure doesn't matter") - a new failure is still a new failure regardless of what else was already broken.

## Flaky and non-deterministic tests

A test failure doesn't automatically mean a regression, and a test passing on retry doesn't automatically mean there wasn't one. When a test looks flaky: retry in a way that's actually informative (not just "run it until it's green and stop looking"), check whether it has a history of flakiness if that's available, and try to tell infrastructure failure (timeouts, ordering, shared state) apart from a genuine application-level problem. Where you can't resolve the ambiguity, record the uncertainty explicitly rather than picking whichever outcome is more convenient to report.

## Manual verification

Where automation genuinely isn't available for something that matters, a bounded manual verification plan is a legitimate substitute - but it should be the exception, not the default answer to missing automated coverage. Write it as concrete numbered steps with an expected result at each step, for example:

```
MANUAL REGRESSION CHECK
1. Log in as an existing user.
2. Request a password reset.
3. Follow the reset link.
4. Set a new password.
5. Confirm the old password no longer works.
6. Confirm the new password works.
7. Confirm the existing session behaves as expected afterward.
```

If a gap could reasonably be covered by an automated test instead, say so - a manual checklist is a fallback, not a preference.

## Negative paths

Happy-path verification alone misses a large share of real regressions. For anything in the regression surface, consider what happens with invalid input, an expired token, a duplicate request, a permission that should be denied, a provider failure, a timeout, an unavailable dependency, a malformed response, a partial failure, a retry, or a cancellation mid-flow. Apply this proportionally - a low-risk UI tweak doesn't need a full negative-path sweep, but anything touching auth, payments, or shared infrastructure usually does.

## State and side-effect regression

Changes that touch state or produce side effects deserve extra scrutiny on: database writes, file storage, email, SMS, push notifications, payments, webhooks, queues, background jobs, external API calls, analytics events, and audit logs. When testing these, avoid triggering real, uncontrolled side effects (an actual charge, a real email to a real inbox, a live webhook) unless that's been explicitly authorized and safely sandboxed - prefer test doubles, sandboxes, or fixtures that let you verify the behavior without the real-world consequence.

## Performance regressions

Behavioral regression is the core focus of this skill, but a severe performance regression can make previously-working functionality effectively unusable, which is a real regression even though nothing is technically "broken." Where a change touches a performance-sensitive path, it's worth a look at latency, query count (especially N+1 patterns introduced by a seemingly innocent change), memory, CPU, network call count, and payload size. This doesn't need to become a full benchmarking exercise on every change - reserve that depth for changes where the risk classification actually justifies it.
