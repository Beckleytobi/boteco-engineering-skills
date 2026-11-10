# Protected behaviors, invariants, and the security boundary

## Protected behaviors

Projects often have a small set of things that must never break, regardless of what else is going on in a given change. Common examples: existing users must always be able to log in, a payment must never be charged twice, one tenant's data must never become visible to another tenant, an approved record must not be silently deleted, notifications must not duplicate, a completed transaction must stay immutable.

Where a project documents these explicitly - in a governance doc, a critical-journey registry, or comments in code - treat that list as a standing checklist consulted on every change that plausibly touches it, not just the changes that happen to mention it by name. Where nothing is documented, it's still worth naming the protected behaviors that seem to apply to this specific change based on what the product evidently does, while being clear that this is an inference rather than a confirmed list - that distinction matters if it's ever relied on later.

## Invariants

Related but slightly different: invariants are properties of the system that must remain true at all times, not just specific user-facing behaviors. Examples: an account balance can't become internally inconsistent, an order can't be fulfilled twice, an approved application can't silently revert to draft without an authorized transition, a successful idempotency key can't produce a duplicate transaction.

Where invariants like this exist for the system being changed, regression testing should specifically try to confirm they still hold after the change - these are exactly the kind of thing that can break quietly, through a state machine gaining an unexpected transition or a uniqueness check losing its enforcement, without any single test obviously failing.

## The security boundary

This skill is not a substitute for a dedicated security review, and shouldn't try to make security-specific judgment calls on its own. But if a change touches authentication, authorization, tenant boundaries, secrets, permissions, security middleware, or input validation, that's still squarely inside the regression surface - identify those existing behaviors as part of the analysis, note what could plausibly regress, and hand the security-specific evaluation to whatever security process the project has, rather than either skipping the area entirely or trying to render a security verdict that isn't this skill's job to render.
