# Domain-specific regression checklists

Each section below is a checklist for one kind of change. Read the ones that match the classification from Phase C and skip the rest - a UI-only change doesn't need the concurrency checklist, and a config-only change doesn't need the UI one. None of these require exhaustive testing of every possibility; each says where to focus.

## Concurrency and race conditions

Relevant whenever the changed area involves concurrent requests, background jobs, queues, inventory, payments, booking, counters, distributed processing, or any other shared resource touched from more than one place at once.

Think through what happens when two things happen at the same time that the change didn't anticipate: two workers picking up the same job, two payment requests both trying to charge the same order, two users reserving the same seat or unit, a retry that fires a duplicate notification because the original request didn't actually fail, it just timed out. Where relevant, check idempotency, locking, transaction boundaries, optimistic concurrency, deduplication, and ordering guarantees. Don't require concurrency testing for changes that don't touch shared, concurrently-accessed state - it's wasted effort there.

If the operation already has a documented idempotency contract (an idempotency key, a defined response for a duplicate call) from an earlier design pass, verify the diff against that contract directly rather than inventing fresh expectations - the contract is the spec here, and the check is whether the implementation still honors it.

## Asynchronous workflows

Relevant for anything involving queues, jobs, events, or async processing. The core trap here is stopping the analysis too early: a test proving a message was successfully added to a queue proves nothing about whether the workflow it kicks off actually completes correctly.

Think through the whole chain - API, queue, worker, database, notification, whatever the actual pipeline is - not just the first hop. Where relevant, verify producer behavior, the message or event contract, consumer behavior, retry behavior, failure handling, duplicate-processing protection, and the final state the workflow is supposed to leave things in. Where a retry or backoff strategy was already specified for this operation in an earlier design pass, check the implementation against that specification rather than assuming any retry behavior that happens to exist is the intended one.

## Feature flags

Relevant wherever the change is gated behind a flag, or wherever a flag already exists in the area being changed. Check both states - feature off and feature on - and confirm the new work doesn't leak into users who are supposed to remain on the old behavior. Also worth a look: what the default flag state actually is, what happens if the flag's configuration is simply missing, whether the flag is stale (already fully rolled out but still being checked), what a partial rollout percentage does to the affected population, and what the fallback behavior is if flag evaluation itself fails. Prioritize the flag combinations the change actually affects rather than trying to exhaustively test every combination that exists in the system.

## Dependency upgrades

A dependency upgrade can introduce a regression even when the application's own code barely changed, because the regression is inside the dependency's changed behavior, not in the diff you're looking at. For a dependency change: check what actually changed between the old and new version, look for documented breaking changes, identify what in this codebase actually uses the affected functionality, run the relevant tests, and think about whether any behavioral assumptions the codebase makes about the dependency still hold. Also check whether any configuration needs to change alongside the upgrade, and whether the upgrade pulled in transitive dependency changes that could have their own effects. "The package manager installed it successfully" is not regression evidence - it only means the version constraints resolved, not that the new version behaves the same way.

## Configuration

Configuration is part of the software's actual behavior, not a separate concern from it - a codebase can pass every test and still fail in production because a configuration assumption changed underneath it. This covers environment variables, feature flags, timeouts, URLs, credentials, runtime settings, build configuration, and deployment configuration. When any of these change, identify what new configuration is now required and what defaults changed, since a changed default is a regression for anyone who was implicitly relying on the old one. Whether the new configuration is actually valid in a real production environment is a Production Readiness concern, not this skill's - the job here is making sure the configuration surface itself is part of the regression analysis, not skipped because it "isn't code."

## API regression

For API changes, look past whether the endpoint returns a 200. Check route availability, HTTP methods, status codes, request validation, response schemas, error schemas, pagination behavior, authentication, authorization, idempotency, and backward compatibility for existing consumers. The contract is the thing being protected here, not just the happy-path response.

## UI regression

Not every UI change needs the same depth. A pure visual polish change (spacing, color, border radius) doesn't need to pull in the backend regression suite unless it touches something structurally shared. But UI behavior with actual logic behind it - forms, navigation, validation, loading states, error states, disabled states, permission-gated elements - can regress just like backend code, and deserves component tests, interaction tests, or critical-journey tests as appropriate. Visual regression tooling, accessibility checks, and full browser test infrastructure are valuable but shouldn't be treated as a hard requirement for every project; use them where they already exist or where the change specifically warrants introducing them.

## Error handling

Changes should preserve the error behavior that was there before, not just the happy path. Verify that previously-handled failure cases are still handled, that internal errors aren't newly exposed to users or callers who shouldn't see them, that retries still occur where they used to, that user-facing error states are still reachable, that a failure doesn't leave data in a corrupted intermediate state, and that fallback behavior still works. This matters most when an AI agent has refactored error-handling infrastructure directly, since that's exactly the kind of change where "it still compiles" gives no signal about whether the right errors still get caught in the right places.

## Observability

Where a change touches logging, metrics, tracing, audit events, or other operational signals, check whether something that used to be observable silently stopped being emitted. This skill isn't responsible for whether observability is *sufficient* for release - that's a Production Readiness question - but it is responsible for noticing when existing, previously-relied-upon observability quietly disappeared as a side effect of the change.
