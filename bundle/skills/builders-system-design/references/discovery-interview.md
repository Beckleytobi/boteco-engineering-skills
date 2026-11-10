# Adaptive Product Discovery Interview

Use this as a decision tree, not a questionnaire. Ask only 3–5 questions at a time and update the state file after each round.

## Interview behaviour

- Start with what the builder already knows. Accept plain language.
- Reflect the current understanding before asking the next round.
- Offer bounded choices with examples when the builder does not know a technical term.
- Explain why an answer matters in one sentence.
- Distinguish a launch assumption from a long-term aspiration.
- If an answer is unknown, record a range and define a cheap validation step.
- Do not make the student “approve” technology they do not understand. Describe the consequence in product language first.

## Round A — Product and value

Ask enough to complete:

- Product statement: For `[user]`, who needs `[job/problem]`, the product enables `[outcome]`.
- Primary user and any secondary actors: customer, operator, administrator, partner, service account, agent.
- One critical journey that must work for the product to have value.
- Failure consequence for that journey.
- Product stage: experiment, private pilot, launch, growth, or migration.

Useful branches:

- If multiple user types exist, ask what each can see and change.
- If the product handles money, health, identity, education records, children, employment, or legal decisions, open a trust/compliance question immediately.
- If AI is central, ask what happens when it is wrong, slow, unavailable, or unsafe.

## Round B — Usage and workload

Do not accept “many users” or “it should scale.” Ask for a launch range and a plausible 12-month range.

- Registered, daily active, and concurrently active users.
- Peak event: what causes it, how long it lasts, and what users do during it.
- Read-heavy, write-heavy, upload-heavy, compute-heavy, or mixed workload.
- Largest and most frequent operation.
- User geography and whether latency or data residency matters.
- Initial data size, monthly growth, file/media sizes, and retention.

Derive transparent estimates:

- average requests/second = daily actions / 86,400;
- peak requests/second = average × an explicit peak factor;
- storage growth = records or files × average size × retention;
- outbound bandwidth = downloads × average payload size.

Label every derived value as an estimate and retain the inputs.

## Round C — Data, identity, and permission

- Core nouns/entities and who owns each one.
- Relationships, lifecycle, deletion, retention, and source of truth.
- Whether users belong to organizations/tenants.
- Authentication methods and account recovery.
- Role and row/resource-level permissions.
- Sensitive data, secrets, audit history, export, and deletion needs.
- Operations requiring strong consistency, uniqueness, or transactions.

If permissions differ by tenant or record, require an authorization matrix and test cases. UI hiding is never authorization.

## Round D — Interactions and integrations

- Client surfaces: web, mobile, desktop, public API, internal console.
- Synchronous actions users wait for.
- Slow, retryable, scheduled, or fan-out work suitable for background execution.
- Realtime collaboration, presence, streaming, or notification needs.
- Third-party services, ownership of credentials, quotas, webhooks, and outage behaviour.
- Files, image/video processing, search, payments, email/SMS, maps, or analytics.
- AI models, retrieved knowledge, tools/actions, human approval, and evaluation needs.

For every external side effect, ask about idempotency, retries, timeouts, and reconciliation.

## Round E — Quality constraints

- What response time feels acceptable for each critical journey?
- Which failures can be retried, degraded, delayed, or never tolerated?
- How much data loss and downtime are acceptable? Use product consequences before RPO/RTO terminology.
- Budget ceiling and which costs vary with use.
- Team size, skills, operational capacity, and delivery deadline.
- Regulatory, contractual, residency, accessibility, or audit constraints.
- Required monitoring and who responds when it fails.

## Round F — Confirmation

Present:

1. confirmed facts;
2. risky assumptions;
3. unresolved decisions ranked by consequence;
4. recommended minimum architecture;
5. components deliberately deferred or excluded;
6. next validation experiments.

Ask the builder to correct the product model before finalizing architecture.

## Branching signals

| Signal in the answers | Explore next | Do not assume |
|---|---|---|
| Static public media, geographically distributed readers | CDN/object storage, cache policy, invalidation | CDN for authenticated or rapidly changing data |
| Slow/retryable or fan-out work | Queue, worker, idempotency, dead-letter/reconciliation | Async work for every request |
| Repeated expensive reads with tolerable staleness | Cache target, TTL, invalidation, stampede control | Redis by default |
| Tenant or record-specific access | Authorization model, RLS/resource checks, audit | UI filters provide isolation |
| Concurrent editing or live presence | Ordering, conflict policy, connection lifecycle | Realtime is needed for notifications alone |
| Money or external side effects | Idempotency, ledger/source of truth, webhook verification | Exactly-once delivery |
| Global audience | Latency budget, CDN, regional deployment, residency | Multi-region database writes |
| AI-generated decisions/actions | evals, grounding, permission scope, human approval, traceability | Model output is trustworthy |
| Search across meaning, not exact terms | search quality benchmark; perhaps hybrid/vector retrieval | Vector database before measuring retrieval need |

