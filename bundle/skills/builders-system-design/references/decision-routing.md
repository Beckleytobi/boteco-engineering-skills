# Component Decision Routing

Use this guide to decide whether a component has earned a place in the design. Search `system-design-knowledge.md` for the named component before making a high-impact recommendation.

## Required decision record

For every component considered, record:

| Field | Required content |
|---|---|
| Status | Required now / Deferred / Conditional / Excluded |
| Product need | The user journey or constraint it supports |
| Evidence | Known fact, measured result, or visible assumption |
| Smallest form | Minimum useful implementation at the current stage |
| Trade-off | Complexity, latency, consistency, cost, lock-in, or operations |
| Failure behaviour | What users and operators experience when it fails |
| Verification | Test, metric, load result, restore drill, or review |
| Trigger | Measurable condition that changes the decision |

## Default architecture posture

Prefer a modular monolith, one transactional source of truth, managed infrastructure, and a single deployment region when those satisfy the product constraints. This is a starting hypothesis, not a universal rule.

Split services only for a demonstrated reason such as independent scaling, isolation, ownership, deployment cadence, compliance boundary, or incompatible runtime. Record the new distributed-systems costs.

## Routing table

| Component | Evidence that may justify it | Keep it out when | Minimum design questions |
|---|---|---|---|
| Relational database | Related business entities, transactions, constraints, reporting | Data is ephemeral or naturally key/object/document only | Ownership, keys, constraints, indexes, transactions, backup/restore |
| Document/NoSQL store | Flexible aggregates, massive known access pattern, partitionable workload | Chosen only to avoid schema design | Access patterns, partition key, consistency, hot keys, secondary indexes |
| Object storage | User files, media, exports, large immutable blobs | Small structured records belong in the database | Access control, signed access, lifecycle, scanning, metadata, deletion |
| CDN | Cacheable content consumed across locations or bandwidth-heavy delivery | Content is private, personalized, or too volatile without a safe policy | Cache key, TTL, invalidation, origin protection, signed access |
| Cache | Measured expensive/repeated reads; bounded staleness is acceptable | Database is not measured as a bottleneck | Target, hit ratio, TTL, invalidation, stampede, fallback |
| Queue/worker | Work is slow, retryable, bursty, scheduled, or fan-out | User must know the result before continuing | Job identity, idempotency, retry/backoff, poison messages, status, reconciliation |
| Search engine | Relevance, full text, facets, typo tolerance, or independent search scaling | Database search meets measured needs | Corpus sync, freshness, ranking benchmark, authorization filtering |
| Realtime channel | Presence, collaborative state, live operational updates | Polling or push notifications satisfy the experience | Ordering, reconnect, missed events, conflict policy, fan-out |
| API gateway | Multiple independently operated services/clients need centralized policy | A single application boundary is enough | Authentication, rate limits, routing, versioning, observability |
| Load balancer/autoscaling | Multiple stateless instances or variable traffic | One managed runtime already supplies it or load is small | Health checks, session state, scaling signal, drain behaviour |
| Multi-region runtime | Latency/availability/residency requirement cannot be met otherwise | “Global users” is the only reason | traffic routing, state placement, failover, data sovereignty, testing |
| Replicas/sharding | Measured read/write/storage limits and known partitioning | Forecast alone does not threaten current limits | lag, routing, consistency, shard key, rebalancing, cross-shard operations |
| Event bus/stream | Multiple consumers need durable event history or decoupled reactions | A direct call or job queue is simpler | schema, ordering, retention, replay, consumer idempotency |
| AI model service | Product outcome requires probabilistic language/vision/reasoning | Deterministic rules solve the task more safely | quality target, latency, cost, fallback, evals, data handling |
| RAG/vector retrieval | Answers must use a changing/private corpus and retrieval benchmark shows value | Model knowledge, database lookup, or full-text search suffices | chunking, metadata, permissions, retrieval eval, citations, freshness |
| Agent/tool execution | Multi-step dynamic action choice creates value | A deterministic workflow is clearer and safer | allowed tools, scoped credentials, approvals, budgets, traces, rollback |
| Observability | Always required in proportion to risk | Never fully excluded | user-visible SLI, logs/metrics/traces, alerts, ownership, retention |

## Scaling trigger examples

Triggers must be measurable and product-specific. Examples:

- add a cache when the target query exceeds its latency budget at expected peak and repeated reads dominate;
- add a queue when synchronous execution exceeds the interaction budget or burst absorption is required;
- add a read replica when measured read load cannot meet the SLO after query/index work;
- add a CDN for a content class when origin bandwidth/latency measurements justify it and caching is safe;
- split a service when an identified boundary requires independent scaling or deployment and the added failure modes are accepted;
- add regional infrastructure when real-user monitoring shows geography breaches the latency target or residency requires it.

“When we scale” and “when there are many users” are invalid triggers.

## Alternative discipline

For expensive-to-reverse choices, compare at least two viable options using the actual constraints. Include simplicity, delivery time, operational burden, data integrity, security, cost shape, portability, and migration path. Recommend one, state confidence, and identify what evidence could reverse the recommendation.

