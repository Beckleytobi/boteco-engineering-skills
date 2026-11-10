# Risk tiering

The single most common way this skill goes wrong is applying the same depth of scrutiny to everything. A contact-form page and a payment-retry handler are not the same job, and treating them the same produces two bad outcomes at once: the contact form gets buried in irrelevant infrastructure demands nobody will act on, and the payment handler gets the same shallow pass that would have been fine for the contact form.

Before touching the category playbook, decide how hard to look. This isn't a formality: it determines which categories you open at all, and how deep you go inside the ones you do open.

## The factors that actually move the needle

Weigh these together rather than mechanically scoring them. No single factor decides the tier by itself.

- **Reversibility.** Can a bad outcome be undone cheaply (redeploy, feature flag off) or is it permanent (money sent, data deleted, a destructive migration already ran against real rows)? Irreversibility is the single strongest signal to go deeper.
- **What's touched.** Real user data, payment instruments, health information, or anything regulated raises the tier immediately, regardless of how small the code change looks.
- **Blast radius.** Does this affect one user's session, or every tenant on a shared resource (a cache key, a rate limiter, a queue)?
- **Traffic and scale.** A feature serving 50 known users behaves very differently under load than one serving an open signup funnel.
- **Novelty vs. well-trodden ground.** A tenth CRUD endpoint on an existing, already-hardened service needs far less scrutiny than the first integration with a new payment provider or the first background job the codebase has ever had.
- **Failure visibility.** If this breaks, will anyone notice before a customer complains? Silent failure modes (a queue quietly backing up, a webhook silently failing signature checks) deserve more attention than loud ones (a page 500s immediately).

## Working tiers

Treat these as a starting orientation, not a rigid classification form. State which tier you're using and why in one sentence at the top of the report. That sentence is often more useful to a non-technical founder than the whole rest of the assessment, because it tells them how much weight to put on what follows.

### Tier 0: low stakes, easily reversible
Examples: a static marketing page, a copy change, an internal admin tool used by three trusted employees, a UI-only tweak with no new data path, a feature behind a flag that's off by default and easy to flip back.

Depth: a fast pass. Check environment/secrets handling if any new config or credential is involved, check basic error handling, and stop. Most of the category playbook simply doesn't apply; say so in one line rather than working through categories that clearly don't fit, and don't manufacture findings to look thorough.

### Tier 1: standard feature, real users, no money or sensitive data
Examples: a new dashboard view, a search filter, a notification preference, most day-to-day SaaS feature work.

Depth: cover environment/config, error handling, logging, and basic observability. Check external dependencies and timeouts if the feature calls one. Check database changes for anything destructive. Skip deep dives into rate limiting, caching, multi-tenancy, and formal RPO/RTO unless something about this specific feature makes one of them relevant.

### Tier 2: money, sensitive data, or costly-to-reverse changes
Examples: a schema migration touching a live table with real rows, a feature that emails or messages users at scale, anything handling personal or health data, a change to an authentication or authorization path, a new background job or queue.

Depth: this is where most of the category playbook earns its keep. Go through migration safety and preflight checks in real detail for schema changes. Check idempotency and retry behavior for anything that mutates state and might be repeated. Check background-job recovery and observability. Confirm rollback is actually possible, not just assumed.

### Tier 3: payments, health, regulated data, high traffic, or hard-to-undo actions
Examples: payment processing or webhook handling, healthcare data, financial records, anything with real regulatory exposure, a system already carrying meaningful production traffic where an outage has real cost.

Depth: full rigor. Idempotency is not optional to check; ask explicitly "if this runs twice, what happens?" for every mutating operation. Partial-failure sequencing matters (what happens if step 3 of 5 fails). Circuit breaking and graceful degradation for external dependencies deserve real attention. Kill switches for anything capable of causing repeated harm or cost at machine speed. Recovery objectives (RPO/RTO) should be stated explicitly, and their absence is itself a finding worth flagging, not something to wave through the way you would on Tier 0 or 1.

## A system can contain multiple tiers at once

Don't tier the whole project. Tier the change. A Tier 3 payments platform can still ship a Tier 0 copy tweak to its marketing page; don't drag that tweak through a full assessment because it lives in the same repository as Stripe integration code. Conversely, a mostly low-stakes internal tool that just added its first feature touching real payment data has a Tier 3 change sitting inside a Tier 0 product. Assess that change at the tier it deserves, not the tier of everything around it.

If you're genuinely unsure which tier a change sits at, say so and default one tier higher rather than guessing low. The cost of a slightly-too-thorough pass is wasted time; the cost of a slightly-too-shallow pass on something that turns out to matter is a production incident.
