# Risk and Test Strategy

Use this reference after acceptance criteria are known and before selecting tests.

## Risk model

Prefer the repository's established severity model. If none exists, use a lightweight classification:

- `LOW`: narrow, reversible, low-consequence behaviour with few dependencies.
- `MEDIUM`: meaningful user or business impact, persistent state, or a nontrivial integration, but bounded blast radius.
- `HIGH`: money, sensitive data, authentication/authorization, shared contracts, significant mutation, concurrency, broad impact, or difficult recovery.
- `CRITICAL`: safety/regulatory consequence, tenant isolation, irreversible or catastrophic loss, or failure that could materially harm many users.

The label is less important than the reasons. Record the dominant risk drivers, likelihood-relevant conditions, reversibility, and evidence difficulty. Do not inflate low-risk work merely because it occurs in a high-risk product.

## Select the cheapest reliable evidence

Choose levels by what they can prove, not by habit:

| Level | Best evidence for | Common limitation |
|---|---|---|
| Unit | calculations, validation, decisions, transformations, state transitions | cannot prove real integrations |
| Component/module | coherent UI, service, or domain component behaviour | may still replace important boundaries |
| Integration | service-database, API-persistence, queue-worker, provider adapters | can be slower and environment-dependent |
| API | validation, status, schema, auth behaviour, errors, pagination, idempotency | may not prove the full user journey |
| Contract | consumer/provider schemas and compatibility | does not prove provider implementation health |
| System | integrated application requirements | diagnosis may be less precise |
| E2E | a selective critical journey through real boundaries | expensive, slower, and prone to broad failures |
| Manual | bounded visual, hardware, assistive-tech, or human judgment | must be reproducible and recorded |
| Exploratory | discovery around uncertainty and interacting risks | complements rather than replaces scripted evidence |

Use a portfolio, not a ritualized pyramid. Prefer many cheap tests for isolated rules, fewer boundary tests, and selective E2E journeys. Do not duplicate the same assertion across layers unless each layer proves a distinct risk.

## Context-sensitive baseline

A normal feature commonly needs direct acceptance-criterion evidence, a happy path, important negative/error behaviour, relevant boundaries, the material integration seam, and at least one maintainable automated check. This is a starting point, not a universal checklist.

Increase depth when consequence or uncertainty increases:

- money or irreversible writes: transaction, duplicate, idempotency, failure, and concurrency evidence;
- auth or tenant boundaries: functional allow/deny tests plus Security handoff;
- database migrations: empty and representative existing-data paths, constraints, rollback or recovery considerations;
- async work: production, queueing, consumption, retry/duplicate handling, side effect, and final state;
- shared external contracts: integration and contract evidence, malformed/error responses, compatibility;
- critical journeys: a selective E2E check in addition to lower-level diagnosis.

For a static text change, rendered-content confirmation may be enough. Do not require load, chaos, MC/DC, a full browser matrix, or database testing without a relevant risk.

## Prioritization under constraint

If not everything can run, prioritize:

1. material changed behaviour and acceptance criteria;
2. critical business and permission rules;
3. high-risk boundaries and integrations;
4. important negative and error paths;
5. critical journeys;
6. lower-risk supplementary evidence.

List every material omission. Time pressure changes the verdict or limitation; it does not turn missing evidence into success.

## Strategy decision record

For meaningful changes, state:

- selected levels and what risk each proves;
- important levels deliberately omitted and why;
- environment and data needed;
- automation versus bounded manual evidence;
- stopping condition for expensive or unsafe verification.

Do not invent performance targets, browser matrices, devices, or coverage thresholds. Discover requirements, baselines, analytics, and supported platforms first.
