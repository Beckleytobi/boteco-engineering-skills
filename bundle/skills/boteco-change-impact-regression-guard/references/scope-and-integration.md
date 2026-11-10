# Scope boundaries and multi-agent integration

## What this skill does not own

Stating these explicitly matters, because the overlap is real and it's easy to drift into doing someone else's job less well than they'd do it:

- **Software design principles** owns whether the change is architecturally sound and maintainable. This skill consumes that output where it exists (changed modules, blast radius, architectural boundaries already identified) but doesn't substitute for it - a well-designed change can still regress something, and a badly-designed one can still be regression-safe.
- **Security review** owns specialized security assessment. Where a change touches authentication, authorization, tenant isolation, secrets, or validation, this skill's job is to identify those as part of the regression surface and flag the affected behavior - not to render the security verdict itself. Example: a change to authentication middleware might leave login working correctly while quietly weakening tenant isolation. This skill's job is to notice "authentication/authorization behavior affected" and route it to security review, not to decide on its own whether the weakening is acceptable.
- **QA** owns broader product-quality validation beyond the specific question of whether existing behavior still works.
- **Production readiness** owns whether the overall system or change is operationally ready for real-world release - deployment checklists, monitoring, rollback plans, whether configuration is valid for the actual production environment.
- **Requirements validation** owns whether the requested feature is actually the right thing to have built in the first place.

What's left, and what this skill actually owns: evidence that relevant, previously-working behavior remains intact after a change.

## Where this fits in a pipeline

A reasonable multi-agent flow places this after implementation and design review, and before security and QA sign off:

```
REQUIREMENT -> ARCHITECT -> SOFTWARE DESIGN PRINCIPLES -> PLAN -> HUMAN APPROVAL
  -> BUILDER -> DIFF -> DESIGN REVIEW -> REGRESSION PROTECTION -> SECURITY -> QA
  -> PRODUCTION READINESS -> RELEASE APPROVAL
```

But it doesn't have to wait until a diff exists to be useful. During planning, this skill can look at a proposed change and flag what it will put at risk before a single line is written - "this proposed change touches shared authentication infrastructure and will require login, password-reset, and session-refresh regression verification" is exactly the kind of thing that's cheap to act on during planning and expensive to discover after the fact.

## Front-loading guardrails for a builder

Used before implementation, this skill can hand the builder an explicit list of what must survive the change, derived from the same impact analysis it would otherwise do after the fact:

```
PROTECTED BEHAVIOUR

While implementing this change, preserve:
- existing email notifications
- SMS notifications
- notification preferences
- retry behaviour
- password-reset notification flow
```

This turns regression protection from a check that happens to a builder into a constraint the builder can design against from the start, which is generally cheaper than discovering the same list after the diff already exists.

## Independent verification

Don't rely solely on the implementing agent's own claim that its change is regression-safe - that's exactly the self-verification bias this skill exists to correct for. Where the surrounding system supports it, have this analysis run as a genuinely separate pass: inspect the diff independently, derive the regression surface independently, run or inspect the relevant tests independently, and compare the result against whatever the builder itself reported. Discrepancies between the two are worth surfacing on their own, since a builder that reports "all good" while an independent pass finds gaps is itself useful signal about how much to trust that builder's self-reports going forward.

## Inputs already produced by sibling skills

Where a pipeline includes other skills covering design, test planning, or failure-mode design, don't re-derive from scratch what they've already produced - consume it, cross-check it against what your own analysis finds, and only fill the gap between the two. Re-deriving it silently wastes effort and risks a diff between your surface and theirs that nobody notices.

**A design-review skill's change boundary** (commonly expressed as three lists: what's expected to change, what may need to change because it depends on the changed area, and what's protected and should stay untouched) maps directly onto Phase C here: the first two lists are a head start on direct and indirect impact, and its drift-check findings (files touched outside the boundary, unplanned refactoring) are exactly the kind of signal Phase B is looking for. If that skill already reports status as PASS / PASS WITH CONCERNS / ESCALATE / FAIL, use that same vocabulary rather than introducing a competing one - this skill's own status line only adds BLOCKED, for when required verification can't run at all, which isn't something a design review would ever need to express.

**A test-planning skill's prospective regression checklist** (built from a PRD or acceptance criteria before any code exists, listing what must still work after the change ships) is a genuinely useful cross-check for critical-journey identification in Phase C - treat it as a candidate list to verify against, not a substitute for deriving the surface from the actual diff. The plan and the diff can disagree, and when they do, that disagreement is worth reporting on its own.

**A failure-mode or edge-case design skill's idempotency contracts and retry-strategy tables** (per-operation idempotency keys, what happens on a duplicate, retry/backoff rules) are the specification that the concurrency and async-workflow checklists in `domain-specific-regression.md` exist to verify against. If that contract already exists for the operation being changed, check the diff against it directly rather than inventing fresh idempotency expectations - the contract is the spec, this skill's job is confirming the implementation still honors it.

If none of these exist for a given project, fall back to deriving everything from scratch as the rest of this skill describes - their absence is a gap worth naming, not a blocker.
