# Category playbook

This is the detailed reference for every area a production-readiness assessment might cover. Don't work through it top to bottom on every task. Use the risk tier and the shape of the change to decide which groups apply (see `risk-tiering.md`), then open only those. Skipping a category because it genuinely doesn't apply is correct behavior, not a gap.

Each category follows the same pattern:
- **Asks**: the question this category exists to answer.
- **Check for**: what to actually look at, and the red flags that mean this needs a finding.
- **Consequence framing**: how to translate a technical gap into what actually happens to a real user or the business, phrased the way you'd explain it to a founder who has never configured a server.
- **Proportionality**: when to go deep and when a one-line check is enough.

---

## Group A: Environment, Configuration & Secrets

Almost every assessment touches this group, even Tier 0 ones, because misconfiguration is the single easiest way for something that worked perfectly in testing to fail immediately in the real world.

### Environment configuration
**Asks:** Is production configuration explicit, correct, and separated from development/test/staging?
**Check for:** debug mode left on, localhost or test URLs hardcoded, missing required environment variables with no safe failure, unsafe fallback defaults (an API key that silently falls back to a sandbox value instead of erroring), assumptions baked in that only hold locally.
**Consequence framing:** "If the production environment variable for the payment provider isn't set, right now the app falls back to the test key silently, meaning real customers could be charged through the sandbox and the money would never actually arrive."
**Proportionality:** Even a Tier 0 static page deserves a check that it isn't pointing at a staging API. Full environment-parity review is a Tier 2+ concern.

### Secrets management
**Asks:** Are credentials, keys, and tokens handled so they can't leak?
**Check for:** hardcoded secrets in source, secrets committed to version control (including in migration files or seed data), secrets appearing in logs or error messages, secrets exposed to frontend/client code that don't need to be there, secrets returned in API responses.
**Consequence framing:** "The Stripe secret key is currently read from a config file that's committed to the repo. Anyone with read access to the codebase, including a future contractor or a leaked repo, could use it to move money."
**Proportionality:** Always worth a quick check when any new credential is introduced. You are not a substitute for a secret-scanning tool, but you should flag anything a quick look surfaces.

---

## Group B: Deployment & Database Safety

Central to Tier 2 and Tier 3 changes; often skippable for Tier 0/1 changes that don't touch the database or the deploy path.

### Deployment safety
**Asks:** Can this be deployed without breaking users who are mid-session or on the previous version?
**Check for:** migration ordering relative to code deploy (does new code assume a column that hasn't been added yet), in-flight requests during restart, graceful shutdown handling, whether old and new app versions can coexist for the length of a rolling deploy, worker/background-process deploy order relative to the API.
**Consequence framing:** "If the new code deploys before the migration finishes, for the few minutes in between, every request that touches this table will 500 for real users."
**Proportionality:** A single-instance app with a maintenance-window deploy model has much lower stakes here than a service with rolling deploys and live traffic. Say which situation you're in before deciding how hard to push on this.

### Database production readiness
**Asks:** Is the database itself set up to hold up under real usage: pooling, constraints, transaction boundaries, access policy?
**Check for:** unbounded connection creation instead of pooling, missing constraints that application code currently enforces alone (a uniqueness rule only checked in code, not in the schema), transactions that don't actually wrap the operations that need atomicity, overly broad access policies.
**Consequence framing:** "The uniqueness of a member's email is only checked in application code right now, not in the database. Two simultaneous signup requests could both pass the check and create two accounts with the same email."
**Proportionality:** Lean on whatever database-focused output already exists from architecture or design review rather than re-deriving schema quality from scratch. Your job is the operational angle (does it hold up live), not re-litigating the schema design.

### Migration safety
**Asks:** Will this migration run safely against real production data, not just an empty or small test database?
**Check for:** destructive operations (dropped columns, renamed columns without a compatibility window), type changes on populated columns, new NOT NULL columns with no default against existing rows, large-table operations that could lock for an extended period, missing backward compatibility with code still running the previous version during a rolling deploy.
**Consequence framing:** "This migration adds a NOT NULL column with no default. Against a table with 40,000 existing church member records, this will fail outright the moment it runs against production. You won't find out in testing because the test database is empty."
**Proportionality:** This is one of the highest-value checks in the entire playbook whenever a migration exists. A migration that only ever ran against an empty dev database has effectively never been tested. Don't downgrade this just because the rest of the change is low-risk.

### Preflight checks
**Asks:** For a risky migration, has the actual state of production data been verified before the migration runs against it?
**Check for:** a new unique or foreign-key constraint being added without first checking existing rows for violations; a backfill assumed to be clean without having queried for the exception cases.
**Consequence framing:** "Before adding a unique constraint on (church_id, member_id), it's worth running a quick count of existing duplicate pairs in production. If there are any, say from an old import that didn't dedupe, the migration will fail partway through, on production, during the deploy."
**Proportionality:** Push this hard for Tier 2/3 migrations against tables that already hold real data. Skip it entirely for a migration against a brand-new table nothing has written to yet. Recommend the PRECHECK → MIGRATION → POSTCHECK shape (query for violations first, run the migration, then verify the invariant holds afterward) rather than running the migration and finding out.

---

## Group C: Rollback, Backup & Progressive Rollout

Ask "if this goes wrong, how do we get out of it?" This is where a lot of otherwise-careful teams have nothing written down, because it only matters on the bad day.

### Rollback and recovery
**Asks:** If this release causes a problem, what's the actual path back to a working state?
**Check for:** whether the rollback mechanism is application-only (fine) or also requires reversing a migration (much harder: many migrations can't be cleanly reversed once they've run against live data), whether a feature flag exists to disable behavior without a full redeploy, whether "we'll just roll back" has actually been thought through for this specific change or is an assumption.
**Consequence framing:** "There's no flag to turn this off. If it misbehaves after launch, the only fix is a full redeploy, which takes about ten minutes, during which this feature stays broken for every user."
**Proportionality:** For Tier 0/1, a one-line confirmation that redeploying reverts the change is usually enough. For Tier 2/3, especially irreversible migrations, this deserves a real plan, not an assumption.

### Backup and recovery
**Asks:** If important data were lost or corrupted, could it actually be restored, not just "are backups turned on"?
**Check for:** whether backups exist at all, what they cover (all tables, or a subset), retention window, and, the question that actually matters, whether restoration has ever been considered or attempted, even hypothetically. "Backups are enabled" and "we could recover from this" are different claims.
**Consequence framing:** "Backups run nightly, but nobody has ever tried restoring one. If the production database were corrupted tomorrow, the honest answer right now is 'probably, but we don't actually know how long it would take or whether the restore process works.'"
**Proportionality:** Don't propose or run a destructive recovery test yourself. That requires explicit authorization and safe infrastructure, and is out of scope for this skill to execute. Surfacing that restoration has never been verified is itself the finding.

### Recovery objectives (RPO/RTO)
**Asks:** How much data loss can this product tolerate, and how long can it be down?
**Check for:** whether these have been stated anywhere, even informally.
**Consequence framing:** "Nobody has said out loud how much data loss would be acceptable if the database failed. For a church attendance tracker, losing a day might be a shrug. For giving records, it's a much bigger problem, and that difference should be a deliberate decision, not a default."
**Proportionality:** Don't force a formal RPO/RTO statement onto a Tier 0/1 project; that's process for its own sake. For Tier 3 systems, the total absence of any stated expectation is itself worth flagging as a gap, not something to silently skip.

### Feature flags and progressive rollout
**Asks:** For a risky change, should activation be separated from deployment?
**Check for:** whether a large-blast-radius change ships fully on for everyone at once versus being flagged off, enabled for a small group, and expanded after observation.
**Consequence framing:** "This changes how giving records are calculated for every church at once. A staged rollout, on for one pilot church first, would catch a calculation bug before it touches everyone's numbers instead of after."
**Proportionality:** Don't demand a flag for every change; most Tier 0/1 work doesn't need one. Push for it specifically where blast radius and reversibility both look bad together.

### Kill switches
**Asks:** For a feature capable of doing real, repeated, or costly harm quickly, can it be shut off fast without a full deploy?
**Check for:** automated or high-frequency actions (bulk messaging, AI-driven automation, repeated external charges, high-volume outbound calls to a paid API) that have no way to be paused short of a code change and redeploy.
**Consequence framing:** "If the automated giving-reminder email starts firing every minute instead of once a day because of a bug, right now the only way to stop it is to push a fix and redeploy, which could be twenty minutes of every church member getting spammed. A single config flag that pauses the sender would turn that into a thirty-second fix."
**Proportionality:** Reserve this for genuinely high-velocity or high-cost automated actions. A feature that a human triggers once per use doesn't need one.

---

## Group D: Observability & Error Handling

The difference between "we found out from a customer complaint" and "we found out from a dashboard three minutes after it started."

### Observability
**Asks:** If something goes wrong, can anyone tell, quickly, and specifically enough to know where to look?
**Check for:** whether there's any signal at all when error rates climb or latency degrades, whether that signal reaches a person, whether it's specific enough to point at a component rather than just "something, somewhere, is wrong."
**Consequence framing:** "Right now, if the webhook handler starts silently failing, the first anyone hears about it is a church admin emailing to ask why a member's payment didn't register, potentially days later."
**Proportionality:** A Tier 0 page needs essentially nothing here. A Tier 2/3 system handling money or being relied on daily needs at least basic error-rate visibility reaching a real person.

### Logging
**Asks:** Are logs useful for diagnosing a real failure, without either drowning it or leaking sensitive data?
**Check for:** no logging at all around a critical path, log volume so high the useful signal is buried, secrets or personal data (full card numbers, passwords, health information) appearing in log output, missing correlation between related log lines (a request ID that would let you trace one user's failed action through the system).
**Consequence framing:** "The webhook handler doesn't log the payment provider's event ID. If a specific transaction goes wrong, there's currently no way to search for what happened to that one event. You'd be reading through everything from that time window by hand."
**Proportionality:** Applies almost everywhere something can fail silently. Depth of correlation/tracing scales with system complexity: a single-service app needs much less than one made of several services talking to each other.

### Error handling
**Asks:** Do failures fail safely and predictably, without exposing internals or leaving things in a bad state?
**Check for:** raw stack traces, database errors, or provider error messages surfaced directly to end users; errors that are swallowed silently instead of surfaced anywhere; inconsistent handling of recoverable versus non-recoverable failures.
**Consequence framing:** "Right now, if the database times out, the user sees a raw Postgres error message on screen, including the table name and query. Beyond looking unprofessional, that's handing a stranger a hint about your schema."
**Proportionality:** Worth checking on essentially every assessment above Tier 0: it's cheap to check and the failure mode is embarrassing and sometimes a real information leak.

### Health and readiness checks
**Asks:** Does "the process responded" actually mean "this instance can serve real traffic"?
**Check for:** a health check that only confirms the web process is up, with no check on whether its required dependencies (database, critical external service) are actually reachable; conversely, a health check so heavy it creates meaningful load on those same dependencies every few seconds.
**Consequence framing:** "The health check currently just confirms the app responds to a ping. It doesn't check whether the app can actually reach the database. An instance that's lost its database connection would still show as 'healthy' and keep receiving traffic it can't serve."
**Proportionality:** Matters most for systems behind a load balancer or auto-scaler that actually acts on health check results. Largely moot for a single-instance deploy with no automated traffic routing.

---

## Group E: External Dependencies & Resilience

This is the largest group and the one where most subtle production incidents live: everything about what happens when something else (a provider, a network, a queue) doesn't behave the way the happy path assumed.

### External dependencies
**Asks:** For each significant external service this relies on, what happens when it's slow, down, wrong, or rate-limiting you?
**Check for:** an inventory of what's actually called (payment provider, email/SMS, storage, AI provider, auth provider) and, for each, whether the slow/down/malformed/expired-credential/rate-limited cases have been considered at all.
**Consequence framing:** "If the SMS provider is slow today, right now that means the entire signup flow hangs, because nothing sends the verification text and returns control to the user in the meantime."
**Proportionality:** Scale the inventory to how many external calls actually exist. A feature with zero external calls skips this entirely.

### Timeouts
**Asks:** Does every network call have a bounded wait, or can one slow provider hang the whole request?
**Check for:** any external call with no timeout configured, relying on defaults that may be far too long (or absent) for the framework/library in use.
**Consequence framing:** "There's no timeout set on the call to the AI provider. If it hangs instead of erroring, the request handling it hangs too, and depending on the server setup, that can tie up a worker that could otherwise be serving other users."
**Proportionality:** A quick, high-value check anywhere a network call exists. Don't propose specific timeout numbers as universal defaults; they're context-specific to the call and what's acceptable to wait for.

### Retries
**Asks:** Are retries applied deliberately, to failures that are actually safe to retry, with sane limits?
**Check for:** blanket retry-on-any-failure logic, no backoff or max-attempt cap (risking a retry storm that makes an outage worse), retrying operations that have side effects without checking idempotency first.
**Consequence framing:** "The payment charge call currently retries automatically on any failure, including a timeout where the charge may have actually succeeded on the provider's end before the response was lost. That retry could charge the customer twice."
**Proportionality:** Deserves real scrutiny for any mutating call (payments, order creation, messaging); read-only retries are lower stakes.

### Idempotency
**Asks:** If this operation runs twice (retry, duplicate webhook delivery, double-click), what actually happens?
**Check for:** payment creation, webhook handlers, order/booking submission, and notification sending are the classic offenders; ask directly whether there's an idempotency key, a uniqueness constraint, or a check-before-act pattern preventing duplication.
**Consequence framing:** "If Stripe sends the same webhook event twice, which it does, by design, as a normal occurrence, will this create two membership records, or one? Right now the answer is two."
**Proportionality:** This is one of the highest-leverage single questions in the whole playbook for Tier 2/3 work. Ask it explicitly for every operation that mutates state and could plausibly be repeated, rather than only where a problem happens to be obvious.

### Background jobs
**Asks:** Does a job being queued actually mean the work got done?
**Check for:** whether job failures are surfaced anywhere, retry behavior on job failure, concurrency limits, whether a crashed worker silently drops in-flight jobs, deduplication for jobs that could be enqueued more than once.
**Consequence framing:** "The nightly attendance sync is queued every night, but if the job itself throws partway through, right now nothing surfaces that. The next person to notice is whoever wonders why last Tuesday's numbers look wrong, possibly weeks later."
**Proportionality:** Applies to anything with a queue or scheduled/background execution. Skip entirely for purely synchronous request/response systems.

### Dead-letter / failed job handling
**Asks:** After a job fails repeatedly, is the failure visible and recoverable, or silently lost?
**Check for:** what happens after the retry limit is exhausted: does the job just disappear, or is there some way an operator finds out and can retry or inspect it.
**Consequence framing:** "After three failed attempts, the sync job for a church's records is currently just dropped. There's no list anywhere of 'these jobs failed and need attention'. The data gap is invisible until someone notices the numbers are wrong."
**Proportionality:** A full dead-letter queue is overkill for a low-volume internal job; a simple failure log a human can check is often enough. Match the mechanism to the actual consequence of a lost job.

### Queue backpressure
**Asks:** What happens if work arrives faster than it can be processed?
**Check for:** unbounded queue growth, worker concurrency with no ceiling, whether hitting an external provider's rate limit while draining a backlog has been considered.
**Consequence framing:** "If every church's weekly digest email enqueues at once on Sunday morning, and the email provider only allows a certain send rate, the queue could back up for hours with no visibility into how far behind it's fallen."
**Proportionality:** Only relevant where a queue or batch process exists at meaningful volume; skip for anything low-volume or synchronous.

### Graceful degradation
**Asks:** If a non-critical dependency fails, does the whole product need to fail with it?
**Check for:** a core flow (checkout, login, core data entry) that's needlessly coupled to a non-critical one (analytics, recommendations, a nice-to-have enrichment call) such that the non-critical failure takes down the critical path too.
**Consequence framing:** "Right now, if the analytics call fails, it takes the entire donation form down with it. A member trying to give money can't, because of a service that has nothing to do with processing their gift."
**Proportionality:** Look specifically for critical-path code that calls something non-critical without isolating the failure. Don't invent degradation strategies for dependencies that are actually critical; those should just be handled well, not gracefully bypassed.

### Circuit breaking and dependency isolation
**Asks:** Can a repeatedly failing dependency take the rest of the system down with it?
**Check for:** a struggling external service being hammered with retries from many requests simultaneously, with no mechanism to back off and fail fast once it's clearly down, and no isolation preventing that dependency's slowness from exhausting shared resources (connection pools, worker threads) needed by unrelated requests.
**Consequence framing:** "If the AI provider starts timing out, right now every request that touches that feature will hang for the full timeout period, one at a time, potentially exhausting the app's worker pool and making unrelated pages slow too."
**Proportionality:** Reserve for genuinely high-risk external dependencies at real scale. Not worth introducing for a low-traffic app calling one external service occasionally; the complexity isn't earned yet.

---

## Group F: Scale, Performance & Resource Bounds

Asks whether the thing that works today keeps working as usage grows, without over-building for scale that doesn't exist yet.

### Scalability
**Asks:** Will this hold up at the traffic and data volume actually expected, not some hypothetical hyperscale?
**Check for:** obvious bottlenecks relative to realistic near-term growth: a single-threaded process handling something that will clearly need concurrency soon, a data pattern that grows unbounded with no plan for it.
**Consequence framing:** "This works fine with the current 40 churches. At the growth rate discussed, it'll cross the point where this query noticeably slows down within roughly a year. Worth knowing now, not the week it happens."
**Proportionality:** Anchor to actual or realistically expected numbers, not hypothetical hyperscale. A product with 100 users doesn't need to defend against a million.

### Performance
**Asks:** Are there specific, findable inefficiencies (not vibes) worth fixing before this carries real load?
**Check for:** N+1 query patterns, unnecessarily large payloads, repeated computation of something cacheable, blocking operations on a request path that should be fast.
**Consequence framing:** "Loading a church's member list currently makes one query per member instead of one query total: fine at 20 members, but at 2,000 it'll be a visibly slow page load."
**Proportionality:** Prefer pointing at something measured or clearly identifiable in the code over speculative optimization. Don't propose changes based only on general suspicion.

### Database indexes
**Asks:** Do the query patterns that actually matter have the indexes they need?
**Check for:** a new or changed query path (especially one introduced by this change) running against a column with no index, particularly one already known to be filtered/sorted/joined on frequently.
**Consequence framing:** "This new search filters by church and date range, but neither column is indexed. It'll feel instant on a test database with 50 rows and noticeably slow once a church has a few years of records."
**Proportionality:** Check the query paths this specific change introduces or touches; don't audit the entire schema's indexing unless that's actually the task.

### Caching
**Asks:** Where caching exists, does it actually solve a real load or latency problem, and is it safe?
**Check for:** cache key design that could leak one tenant's data into another's cache hit, TTL and invalidation strategy, what happens on a cache failure (does the app degrade to the source of truth, or break), whether caching was added because "production systems need it" rather than to fix an observed problem.
**Consequence framing:** "The cache key for a church's dashboard doesn't include the church ID. Under load, one church could briefly see another church's cached numbers."
**Proportionality:** If nothing is cached, this is a non-issue, not a gap; don't recommend adding caching speculatively.

### Rate limiting and abuse resistance
**Asks:** Is anything protected against being hit far more than a legitimate user ever would?
**Check for:** authentication and password-reset endpoints, public-facing forms, expensive search or AI-backed endpoints, and anything that triggers an outbound SMS/email: check whether these have any limit at all, and whether that limit is tight enough to matter without being so tight it blocks real usage.
**Consequence framing:** "The password reset endpoint has no rate limit. Someone could script ten thousand reset emails to one address in a minute, and right now nothing would stop them or even notice."
**Proportionality:** Focus on genuinely abuse-prone surfaces (auth, anything that costs money per call, anything that emails/texts someone else). Don't propose rate limits on low-risk internal reads.

### Resource limits
**Asks:** Is anything a user controls (file size, request size, page size, batch size) actually bounded?
**Check for:** unbounded file upload size, unbounded pagination, unbounded export size, unbounded batch operations, unmetered AI token usage per request.
**Consequence framing:** "There's no size cap on the CSV a church admin can upload to bulk-import members. A malformed 2GB file would currently be accepted and likely crash or badly stall the import process."
**Proportionality:** Check any surface where a user supplies a size or quantity. Skip where inputs are inherently small and fixed.

---

## Group G: Data Integrity & Concurrency

The category that catches the failures nobody notices until the numbers don't add up.

### Data integrity
**Asks:** Can a failure partway through leave related data inconsistent with itself?
**Check for:** operations that update more than one system or table where success in one and failure in the other leaves a mismatch: payment succeeded but the order record didn't get created, a file uploaded but the database row referencing it failed.
**Consequence framing:** "If the payment succeeds but the membership record fails to save right after, the church has taken someone's money with no record of what it was for, and nothing today would catch or flag that mismatch."
**Proportionality:** Look specifically for multi-step operations spanning more than one system or table. A single atomic database write doesn't need this treatment.

### Partial failure
**Asks:** For a multi-step process, what happens if it fails at each individual step, not just at the end?
**Check for:** walk the actual steps (e.g., create record → charge payment → send confirmation → update reporting) and ask, for each one, what state things are left in if everything before it succeeded and this step failed.
**Consequence framing:** "If step 3 of this signup flow (sending the welcome email) fails, right now the account is already fully created and the payment already charged. The person just never finds out their account exists. Worth deciding: is that acceptable, or does something need to retry the email specifically?"
**Proportionality:** Worth doing explicitly, step by step, for any process with three or more sequential side-effecting steps. Not needed for a single-step operation.

### Concurrency
**Asks:** If two requests or workers touch the same data at the same time, what happens?
**Check for:** race conditions on a read-then-write pattern with no lock or optimistic concurrency check, duplicate processing from two workers picking up the same job, lost updates where the second write silently overwrites the first without either party knowing.
**Consequence framing:** "If two admins edit the same church's settings at the same moment, right now whichever save happens last silently wins. The first admin's changes just disappear with no warning to either of them."
**Proportionality:** Relevant wherever the same record can plausibly be touched by more than one actor or process at once. Not worth raising for data that's structurally always single-writer.

### Multi-tenancy
**Asks:** For a system serving more than one customer/organization on shared infrastructure, is operational isolation actually maintained?
**Check for:** data queries missing a tenant filter, shared cache keys without a tenant component, background jobs or logs that don't clearly attribute work to the right tenant, rate limits or resource pools that let one noisy tenant degrade service for everyone else.
**Consequence framing:** "If one large church runs a bulk export at the same time smaller churches are using the app, right now there's nothing stopping that one export from consuming enough of the shared resources to slow the app down for everyone else."
**Proportionality:** Only relevant for genuinely multi-tenant systems. Note explicitly that deep tenant-isolation security verification (can Tenant A ever see Tenant B's data through a flaw) belongs to security review. Your job here is the operational fairness and stability angle, not the access-control audit.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
