# Test Design and Domain Guidance

Read only the sections relevant to the change.

## Behaviour-derived design

- **Equivalence partitions:** representative values expected to behave alike.
- **Boundary values:** immediately below, at, and above meaningful thresholds.
- **Decision tables:** combinations of conditions that determine an outcome.
- **State transitions:** valid and invalid transitions, terminal states, and repeated commands.
- **Negative/error paths:** invalid, missing, unauthorized, expired, duplicate, and dependency-failure inputs.
- **Black-box:** requirements and observable behaviour; the default defense against implementation-derived expectations.
- **White-box:** use internal knowledge to expose missed branches, conditions, exceptions, or unreachable logic.
- **Grey-box:** use architecture knowledge while asserting externally meaningful results.

For every test, ask whether it would fail if the behaviour were removed, inverted, off by one, partially committed, or performed twice. If not, improve the assertion or choose a more representative boundary.

## Test doubles

Use stubs, mocks, spies, fakes, fixtures, and sandboxes to isolate irrelevant collaborators. Never replace the behaviour or boundary being proved. A mocked database cannot prove transaction semantics; a mocked authorization decision cannot prove the real policy; a provider stub proves adapter handling, not provider compatibility. Pair isolated tests with an appropriate real-boundary test when that boundary is material.

## APIs and contracts

Consider request validation, response body and schema, status codes, authentication, functional authorization, malformed inputs, pagination/filtering, idempotency, rate-limit behaviour when required, and provider failure. Use contract tests where separately deployed consumers/providers or backward compatibility justify them. Do not create contract infrastructure for a trivial local boundary.

## Databases and migrations

Verify relevant constraints, uniqueness, foreign keys, transactions, rollback, integrity, permissions/RLS, concurrency, and representative fixtures. For migrations distinguish:

- clean/empty database execution;
- upgrade from the actual supported prior schema;
- representative existing and adversarial data;
- post-migration invariants and compatibility;
- failure/rollback or forward-recovery path.

Success on an empty database is insufficient for a risky production migration. Hand operational rollout, backup, restore, and recovery judgment to Production Readiness and enforcement to CI/CD.

## Frontend and accessibility

Select relevant rendering, interaction, form validation, loading, empty, success, error, disabled, permission, responsive, slow-network, network-failure, and duplicate-submission states. Prefer component tests for local behaviour and selective browser E2E for critical journeys or real-browser boundaries.

For browser selectors, prefer user-visible semantics, roles, accessible names, or stable test contracts over incidental DOM structure. Do not distort accessibility semantics solely for a test.

Check semantic structure, labels, keyboard operation, focus, accessible names, form errors, and screen-reader-relevant state where applicable. Automated checks do not prove complete accessibility; identify required assistive-technology or human review. Use visual regression selectively for important layouts and design-system components, and hand broad existing-UI comparison to Regression Protection.

## Async, time, retries, and concurrency

For queues, workers, events, webhooks, and scheduled jobs, verify the observable chain:

`event produced -> delivered/queued -> consumed -> side effect -> final state`

Exercise delayed and failed processing, retries, duplicates, idempotency, ordering where promised, and dead-letter behaviour where implemented. "Accepted" or "queued" is not final completion.

Control clocks for expiry, trials, subscriptions, token lifetime, schedules, and deadlines. Cover meaningful before/at/after boundaries without arbitrary real waits.

Where concurrent execution is plausible, test duplicate submission, simultaneous update, lost update, double processing, oversell/double booking, or double charge according to the domain. Concurrency tests are risk-triggered, not universal.

## Performance and resilience

Only test against stated requirements or justified baselines. Select performance, load, stress, spike, soak, or scalability evidence according to the question, recording workload, data shape, environment, duration, percentiles/throughput/error rate, and resource context. Do not invent targets.

For resilience, exercise relevant timeouts, retry bounds, dependency failure, partial outage, circuit breaker behaviour, duplicate messages, and recovery. Do not inject destructive faults into production without explicit authorization and safe infrastructure. Production Readiness owns whether observed performance and recovery are operationally acceptable.

## Coverage and specialized assurance

Line, statement, function, branch, and condition coverage indicate executed structure, not correct assertions. Discover existing thresholds; do not impose arbitrary percentages. Decision-heavy critical logic may justify stronger branch/condition coverage than presentation code.

Use mutation testing selectively when valuable logic may have weak assertions. Use MC/DC only for safety-critical, regulatory, or exceptionally high-assurance decisions where each condition must independently affect the outcome. Neither is a default requirement.

## Exploratory and human testing

A structured exploratory charter records objective, scope, risks, areas to explore, timebox, observations, defects, and unanswered questions. Manual evidence records tester, environment, steps, expected result, observed result, and timestamp or run identifier where useful. "Manually checked" is not adequate evidence for critical behaviour.

Usability judgments and UAT approval remain human/product responsibilities. The agent may prepare scenarios and capture outcomes, but cannot impersonate acceptance.
