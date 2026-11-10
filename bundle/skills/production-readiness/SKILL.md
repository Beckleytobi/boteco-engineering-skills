---
name: "production-readiness"
description: Assess whether software or a change is actually safe to run in production - real users, real data, real traffic, real failures - beyond compiling, passing tests, good design, or being regression-free. Produces a risk-calibrated readiness report covering config/secrets, deployment and migration safety, rollback/backup, observability and errors, external-dependency resilience (timeouts, retries, idempotency, background jobs), scale/performance, and data integrity/concurrency, with findings translated into plain-language real-world consequences for non-technical stakeholders. Use whenever someone asks is this ready to ship, production ready, or safe to deploy, before a release or big merge, or when a change touches payments, migrations, background jobs, webhooks, external APIs, or real user data, even unprompted. Distinct from software-design-principles (structure), regression-protection (broke something?), security review, and QA (correct behavior) - the can-we-operate-this-safely check, used alongside them.
---

# Production Readiness

## The question this exists to answer

> Is this ready to operate safely and reliably in production, with real users, real data, real traffic, real dependencies, and real failures?

Software can compile, pass every test, be well-designed, and be free of regressions, and still fall over the first week in production because nobody configured monitoring, a migration was never tested against real data volume, a retry silently double-charges a customer, or a background job can fail without anyone finding out. None of that shows up in a green test suite. It shows up as an incident.

The operating principle: **passing tests does not mean production ready.** Readiness is a claim about the whole operational picture: can this be deployed safely, configured correctly, observed, operated, recovered, scaled appropriately, protected from foreseeable failure, rolled back, and supported after release. It is not just a claim about the code being correct in isolation.

## How this differs from the skills around it

Keep these separate rather than collapsing them into one big "is this good" review. Each answers a different question, and a change can need several at once:

| Skill | Question it answers |
|---|---|
| software-design-principles | Is the code structured appropriately for this change? |
| regression-protection | Did this break something that used to work? |
| security review | Is this protected against security threats? |
| QA | Does it behave correctly against requirements? |
| **production-readiness (this one)** | **Can we safely operate this with real users, data, and failures?** |

If a task also calls for one of those, do this assessment and hand the other concern to its own process rather than trying to render that verdict here. In particular, confirm a security review has happened and surface operational security gaps you notice along the way (secrets handling, tenant isolation, error messages leaking internals), but don't present this as a substitute for a dedicated security review. Say so explicitly if one hasn't happened and this looks like it needs one.

## Who reads the output, and why that changes how you write

The person relying on this is often a non-technical founder, not another engineer. That means every finding needs to say what actually happens to a real person or the business, not just name the technical gap.

Weak: "Missing idempotency on the webhook handler."
What it should say: "If the payment provider sends the same webhook twice, which happens routinely by design, this could create two membership records or charge someone twice, and there's currently nothing preventing that."

This translation is not an optional nicety layered on top of the real analysis. It *is* the deliverable. A finding nobody can act on because they can't tell what it means in practice hasn't actually been communicated.

## Workflow

### Phase A: understand what's being assessed

Before opening any checklist, pin down: what's actually being released or changed, who uses it, the production environment and deployment model, the architecture, the database involved, external dependencies it calls, the critical user journeys it touches or sits near, what data it handles, whether background processing is involved, and any known constraints (expected traffic, regulatory context, existing operational conventions in this codebase). Get this from the conversation and a quick look at the code/config; most of it is inferable without a lengthy interview. Only ask the person directly when something genuinely can't be determined and would change the assessment's shape (for example, expected traffic when there's no way to infer it and it would change whether a category matters).

### Phase B: inspect what already exists before recommending anything new

Search for what's already in place: deployment configuration, CI/CD, environment and secrets handling, existing logging and monitoring, health checks, migration history and tooling, backup configuration, queues and retry logic, caching, rate limiting, alerting, feature flags, rollback mechanisms, and any operational documentation already written. A finding that recommends building something that already exists two files over is worse than useless: it costs credibility on the findings that are actually real. If you can't find something, say you looked and didn't find it rather than assuming either way.

### Phase C: set the risk tier

Read `references/risk-tiering.md` and decide how hard to look. This step is not optional busywork. It's what keeps a static marketing page from getting buried in irrelevant infrastructure demands, and what keeps a payment-webhook handler from getting the same shallow pass that would have been fine for the marketing page. State the tier and the one factor that drove it (money, irreversibility, data sensitivity, traffic, blast radius) at the top of the eventual report.

Tier a *change*, not a whole codebase. A payments platform can still ship a low-stakes copy tweak; a mostly low-stakes internal tool can still add a genuinely high-stakes feature. Assess the change at the tier it deserves.

### Phase D: work through the relevant categories

Read `references/category-playbook.md`. It's organized into seven groups (environment/secrets, deployment/database, rollback/backup/rollout, observability/errors, external dependencies/resilience, scale/performance, and data integrity/concurrency), each broken into individual categories with what to check, the red flags that mean something's actually wrong, a worked example of the plain-language consequence framing, and guidance on how hard to push for different risk tiers.

Don't work through it mechanically top to bottom. Open the groups the risk tier and the shape of the change actually call for, and skip the rest silently rather than writing "not applicable" through half the playbook. A report padded with non-findings is harder to use than a short one. A few questions are broadly useful enough to keep in mind regardless of which specific categories apply:

- **Idempotency, always ask directly for mutating operations that could repeat:** if this runs twice, what actually happens?
- **Partial failure, for any multi-step process with side effects:** what state is left behind if it fails at step 3 of 5, specifically, not just "does it fail gracefully" in the abstract.
- **Migrations against real data:** a migration that has only ever run against an empty test database has not really been tested. For anything risky (a new constraint, a NOT NULL column, a large-table operation), prefer PRECHECK → MIGRATION → POSTCHECK over discovering a violation mid-deploy.
- **"Queued" is not "done":** for anything asynchronous, confirm there's a way to find out a job actually completed, not just that it was accepted.
- **Rollback, stated explicitly rather than assumed:** if this needs to be undone, is that a redeploy, a flag flip, or something that can't be cleanly reversed once it's run against real data?

### Phase E: write the report

Use the structure in `references/report-template.md`. `scripts/report_skeleton.py` can scaffold the markdown shell for you (`python3 scripts/report_skeleton.py "<subject>" --tier <0-3> --groups <group-keys...>`, or `--list-groups` to see the valid keys). It only builds the shape, not the content, but it keeps the format consistent without retyping it by hand every time.

The report should open with the tier and a one- or two-sentence bottom line, name what's already in good shape (this is genuinely part of the deliverable, not filler), then group findings by playbook group (only the groups with actual findings), each with what's true today, what that means in practice, and a concrete fix. Close with an action plan split into before-launch, soon-after, and when-it-becomes-relevant, since that's the part most likely to actually get used.

## Guardrails

- **Proportionality cuts both ways.** Don't demand enterprise-grade observability, formal RPO/RTO, circuit breakers, or a dead-letter queue for a low-traffic internal tool; that's process for its own sake and it teaches people to ignore this skill's output. Don't wave through a payment or health-data system with a shallow pass either. For Tier 3 work, gaps that would be fine to skip at Tier 0 (no stated recovery objective, no idempotency check) are themselves findings.
- **Never propose or run a destructive recovery test** (an actual restore-from-backup drill, a real failover) without explicit authorization and safe infrastructure to do it in. Surfacing that restoration has never been verified is itself a valid, sufficient finding. Don't go further than that on your own initiative.
- **Don't invent universal numbers.** Timeout values, rate limits, and retry counts are context-specific to the call and what's acceptable to wait for; recommend that a bound exists and roughly how to think about setting it, not a specific number pulled from nowhere.
- **This isn't security review.** Flag operational security gaps you notice in the course of this assessment (secrets handling, tenant isolation at the operational level, information leaking through error messages) and confirm whether a security review has actually happened, but don't present a full security posture assessment as something this skill did.


## Visual design integration

For diagram authoring, review, or consumption, read [visual-routing.md](references/visual-routing.md) and the shared contract it references. Scale diagrams to the change. Preserve existing approval gates.
