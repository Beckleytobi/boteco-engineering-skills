# Deriving the regression surface

Read this when the change touches a shared utility, a contract (API, interface, schema, event), a database or migration, or an external integration - the cases where "what could this affect" isn't obvious from the diff alone.

## Direct vs. indirect impact

**Direct impact** is the behavior the change explicitly targets - changing password-reset validation directly affects password reset. This is usually easy to see and easy to test.

**Indirect impact** is everything that depends on what changed. This is where regressions actually hide, because nobody was looking at it. Changing shared token-validation logic can indirectly reach login, password reset, email verification, API authentication, and session refresh - none of which appear in a diff that only touches the token-validation file. Always ask both questions; a review that only covers direct impact isn't a regression review, it's a feature review.

## Dependency-aware tracing

Don't stop at "which files changed" - a changed shared utility can affect dozens of behaviors without any of their files appearing in the diff. For each changed symbol or module, work outward:

- Who imports this? Who calls it?
- What does it call, in turn?
- What contracts does it implement, and what contracts consume it?
- What data does it read or write?
- What events does it publish or consume; what queues or jobs depend on it?
- What APIs expose it, directly or indirectly?
- What user journeys pass through it?

Use whatever repository tools and static analysis are actually available (search for callers, follow imports, check test files that exercise the symbol) rather than reasoning from the name alone. Where dynamic behavior (reflection, dependency injection, string-based dispatch) makes the true call graph uncertain, say so rather than presenting a traced graph as complete when it isn't.

## Critical user journeys

Signup, login, password reset, authentication, onboarding, payment, subscription, checkout, booking, creating or updating core records, file upload, notifications, search, permissions, admin workflows, data export, and cancellation are common examples - but the actual list has to come from the project, not from this list. If the repository documents its critical journeys explicitly, use that. If a test-planning pass already produced a prospective regression checklist for this feature before it was built, treat that as a strong candidate list too - cross-check it against what you derive independently rather than either ignoring it or trusting it blindly, since a mismatch between what was planned to matter and what the actual diff touches is itself worth reporting. If neither exists, infer cautiously from product requirements, existing tests, routes, and domain entities, and be upfront that it's an inference rather than a confirmed list. If you genuinely can't tell which journeys matter here, say that plainly (a governance gap worth surfacing) rather than picking journeys that sound plausible and presenting them as known.

For each journey that intersects the regression surface, that's a strong candidate for Level 4 (critical journey) evidence in the test-selection hierarchy - see `risk-and-test-strategy.md`.

### Registering critical journeys

Where a project doesn't already have one, it's worth proposing a lightweight registry rather than re-deriving the journey list from scratch on every change. A simple numbered format works well because it lets other reports and other agents reference a journey by ID instead of re-describing it:

```
CRITICAL JOURNEYS
CJ-001  Existing user login
CJ-002  New user signup
CJ-003  Password reset
CJ-004  Checkout
CJ-005  Payment confirmation
CJ-006  Subscription cancellation
CJ-007  Tenant isolation
CJ-008  Admin approval
```

If a registry like this already exists for the project, consume it as-is rather than inventing a competing format. When reporting which journeys a change touches, reference them by ID (CJ-003, CJ-005) so the regression surface report stays terse and cross-referenceable.

## Baseline confidence

Regression protection requires knowing, to some degree, what the previous working state actually was. Look for a previous commit or target branch, an approved implementation baseline, a currently-passing test suite, contract snapshots, or CI results from a known-good state.

Keep a specific distinction in mind: "this existing test currently passes" is not the same claim as "this existing behavior is known to have worked before this change." The first is something you can verify directly. The second requires a trustworthy baseline to compare against. If no trustworthy baseline exists - no prior green build, no known-good commit, nothing to diff against - say so explicitly:

```
BASELINE CONFIDENCE: LIMITED
```

and be specific about what that limits: you can confirm the new code doesn't crash and the tests that exist pass, but you cannot confirm that behavior which isn't covered by any test actually matches what it did before. Don't manufacture a baseline (e.g., by assuming undocumented behavior was "probably fine") just to produce a cleaner-looking report.

## Contract regression

Contracts are the places other things depend on a fixed shape: API request/response shapes, function signatures, interfaces, event schemas, database schemas, serialization formats, webhook payloads, message schemas, configuration contracts, public SDK behavior, error semantics, and authentication/authorization expectations.

For every contract the change touches, work through:

1. Was this change to the contract intentional, or incidental to something else?
2. Is it backward compatible?
3. Who actually consumes this contract (trace it, don't assume)?
4. Have those consumers been updated to match?
5. Does this need compatibility testing before it ships?
6. Does this need versioning rather than an in-place change?

An incidental, unintentional contract change is one of the higher-value things this analysis can catch, because it's exactly the kind of thing that passes every test the author thought to run.

### Backward compatibility

Contract regression has a time dimension whenever old and new versions of something can coexist, which is more often than it first appears: a mobile app with users who haven't updated, API consumers who deploy on their own schedule, a rolling deployment where old and new instances of the same service run side by side, worker processes at different versions, a migration that hasn't finished applying everywhere, webhooks, and external integrations that don't upgrade in lockstep with you.

For each of these, ask directly: can the old consumer still work with the new producer? Can a new consumer work with data or messages the old producer already produced? Does deployment order matter, and if it does, is that ordering actually guaranteed? If compatibility can't be guaranteed across one of these boundaries, that's not a detail to bury in the fine print - surface it explicitly, since it's exactly the kind of gap that only shows up in production during the rollout window and nowhere in a normal test run.

## Database and migration regression

Give database changes their own pass. Inspect migrations, columns, constraints, indexes, defaults, nullability, foreign keys, unique constraints, triggers, functions, row-level-security policies, data transformations, enum changes, and anything destructive.

Then reason about consequences, not just syntax: is existing data compatible with the new shape? Does migration ordering matter here? What happens on rollback? Will an old application version still work against the new schema during a rolling deploy, and will the new version work against data written by the old one? Is there data-loss risk? Could query behavior change in a way nothing currently tests?

"The migration executed successfully" is not the same claim as "there is no regression risk here" - a migration can run cleanly and still silently corrupt or drop data that nothing in the test suite happens to check.

This is especially true for migrations and background processing, where a handful of data-integrity properties are worth checking directly rather than assuming they held: no unintended record deletion, no duplicate records, foreign-key relationships still consistent, unique constraints still respected, tenant ownership still correctly scoped, timestamps behaving as expected, status transitions staying within their valid set, and historical records still readable after the shape underneath them changed.

## Integration regression

For changes touching external services, consider request format, response handling, authentication, timeouts, retries, idempotency, rate limits, error handling, webhook processing, fallback behavior, and provider-specific assumptions that might be baked into the code without being obvious.

Where live testing against the real external service would be unsafe, costly, or simply unavailable, use mocks, contract tests, sandbox environments, or recorded fixtures - and say plainly where you had to rely on those instead of the real thing, since that's a real limit on confidence, not a detail to gloss over. Never perform uncontrolled production side effects (real charges, real emails, real webhooks to real endpoints) purely to gather regression evidence.
