---
name: regression-protection
description: Verify that a code change hasn't broken behavior that used to work, before anyone calls it done. Use right after implementing, fixing, or refactoring code, and before declaring a task complete, saying something is "ready to merge", or reporting a bug fixed - especially when the change touches a shared utility, API contract, database schema, authentication, concurrency, or feature flags. A passing build or a passing test for the new feature is not evidence that nothing else broke; this is what checks for that. Trigger on "is this safe to ship", "did I break anything", "regression test this", "what could this change affect", "review this diff for regressions", or whenever an agent finishes a change and needs to confirm existing behavior still holds. Also usable earlier, during planning, to tell a builder what must stay intact. Distinct from design review, security review, QA, and production-readiness - this is specifically about whether previously-working behavior still works.
---

# Regression Protection

## The question this skill exists to answer

After a change, what evidence do we have that behavior which worked before still works now?

AI coding agents are very good at making the thing they were asked to build work, and this creates a specific blind spot: an agent grading its own work checks the thing it just touched, not the things it didn't mean to touch. A request to "improve the signup flow" can produce a signup flow that works perfectly while quietly breaking login, because both share a token-validation function the agent rewrote along the way. The implementation succeeded by its own test. The product broke.

The rule this skill operationalizes: never verify only that the new behavior works. Verify that the existing behavior around it still works too. Treat these as separate questions requiring separate evidence, because a change can pass the first and fail the second.

Do not let "regression safe" get claimed on the basis of: the code compiles, the new feature's tests pass, the changed file's own tests pass, linting is clean, or the implementation reads correctly. Every one of these is consistent with a regression existing somewhere else. And the inverse matters just as much: **absence of a detected failure is not evidence of regression safety.** If a relevant behavior was never verified, the honest statement is "no regression was detected within the verified scope, coverage remains incomplete for X" - not "no regressions." Regression safety needs evidence about the *rest* of the system, sized to how much of the system the change could plausibly reach, and every claim in the final report should trace back to something actually gathered, never to the mere absence of a complaint.

## What this skill owns, and what it hands off

This skill owns exactly one thing: evidence that relevant previously-working behavior remains intact after a change. It does not decide whether the change was well-designed (design review), whether it's secure (security review), whether the product is ready for real-world release (production readiness), or whether the requested feature was the right thing to build (requirements validation). Where those checks overlap this one - a change that touches auth is both a regression concern and a security concern - do the regression analysis and then hand the specialized judgment to the process built for it, rather than trying to render that verdict here. `references/scope-and-integration.md` covers this in full, including where this skill sits in a multi-agent pipeline and how it can front-load guardrails for a builder before implementation even starts, plus why a self-report from the agent that made the change shouldn't be the only verification anyone relies on.

## Workflow

Work through these phases. Skip nothing, but the *depth* within each phase should track the risk classification established in Phase C - a CSS tweak and a shared-auth-utility change both go through every phase, but the second gets far more scrutiny at each step.

### Phase A: Understand what was supposed to change

Before looking at any code, pin down the intended behavior change, the acceptance criteria, what was explicitly in scope, what critical journeys are known to exist in this product, and what architectural context already exists (design docs, prior review output). This is the baseline for spotting scope creep in Phase B.

### Phase B: Inspect what actually changed

Analyze the real diff, not the plan. Look at changed files, changed functions and classes, new dependencies, removed or renamed behavior, modified contracts, schema or migration changes, configuration changes, and changed side effects or environment assumptions.

Compare the actual change against the plan from Phase A. A discrepancy - the agent touched three extra files, or refactored a helper "while it was in there" - is not automatically wrong, but it is a signal to raise scrutiny, because unplanned changes are exactly the ones nobody was watching for regressions in.

### Phase C: Map the regression surface

The regression surface is every existing behavior, component, contract, integration, data path, and user journey that could reasonably be affected by the change - not just the files that changed. A shared utility can be touched in one file and break a dozen behaviors that never appear in the diff.

Do this in order:

1. **Classify the change** (UI-only, business logic, shared utility, API, auth, schema/migration, external integration, background job/queue, caching, config, feature flag, dependency upgrade, refactor, bug fix, performance, concurrency-sensitive, security-adjacent - a change can be more than one). The classification drives how much of the rest of this workflow is worth doing in depth, and which domain checklists in `references/domain-specific-regression.md` apply (concurrency and race conditions, asynchronous workflows, feature flags, dependency upgrades, configuration, API, UI, error handling, and observability each have their own).
2. **Trace direct impact**: the behavior the change explicitly targets.
3. **Trace indirect impact**: who imports, calls, or depends on what changed. A shared token-validation function touched for one reason can indirectly reach login, password reset, email verification, API auth, and session refresh - trace outward from the changed symbol, not just from the changed file.
4. **Identify which critical user journeys intersect the surface.** Pull from a project's own critical-journey registry where one exists, infer cautiously where it doesn't, and say so explicitly if you can't determine this with confidence rather than inventing certainty.
5. **Establish baseline confidence.** "An existing test currently passes" and "this behavior is known to have worked before this change" are different claims - don't collapse them. If there's no trustworthy baseline, say `BASELINE CONFIDENCE: LIMITED` and be explicit about what that limits you from proving. Never manufacture a baseline that isn't there.

Full guidance on deriving the surface - dependency tracing, contract and backward-compatibility regression, database and data-integrity regression, external integration regression, and the critical-journey registry format - is in `references/regression-surface.md`. Read it whenever the change touches a shared utility, a contract, a database or migration, or an external integration.

Once the surface is mapped, write it down as a **Regression Surface Report** before moving on - the template is in `references/reporting-and-status.md`. This is what lets Phase D target evidence at the actual surface instead of guessing.

### Phase D: Plan, then gather evidence proportional to the risk

Before running anything, turn the surface into a short **Regression Protection Plan**: what new behavior needs verifying, what existing behavior needs verifying, which contracts and critical journeys are in scope, and what evidence will be used for each (template in `references/reporting-and-status.md`). A plan derived from the actual impact analysis catches gaps that a generic checklist won't.

Don't run every possible test on every change - that's wasted effort on trivial changes and false confidence on nothing. Don't run only the tests for the file that changed either - that's the exact gap this skill exists to close. Calibrate using the risk factors in `references/risk-and-test-strategy.md`, and work outward through the standard levels of evidence there (direct, dependency, contract, critical-journey, broader suite) only as far as the risk warrants. That file also covers test-pyramid awareness, avoiding test explosion, test independence, and deterministic fixtures - all ways this phase can go wrong even when the intent is right.

As evidence comes in, report what actually ran, not a vibe. "Tests passed" is not evidence; "18 passed, 0 failed, 0 skipped" is. If something wasn't executed, say so plainly rather than letting silence imply it was. `references/reporting-and-status.md` covers the evidence hierarchy (different kinds of evidence carry different weight - a pure calculation is well protected by focused unit tests, a multi-service payment workflow usually isn't) and the exact format for reporting execution results without fabrication.

Special cases worth handling deliberately - bug fixes, refactors, and changes to poorly-tested legacy code - are covered with full patterns in `references/risk-and-test-strategy.md`.

For everything about *how* to run and interpret evidence well once you're executing the plan - telling a pre-existing failure from a new one, handling flaky tests honestly, writing a bounded manual-verification plan when automation isn't available, and checking negative paths, state/side-effects, and performance with the right proportion of care - see `references/verification-techniques.md`.

### Phase E: Handle failures without shortcuts

When something in the plan fails, work through it rather than around it: confirm whether the failure is new or pre-existing, reproduce it, identify what's actually affected, fix it where that's the right call, rerun the failed check, and rerun what surrounds it. Don't modify the test to make the failure go away, don't suppress it, and don't proceed as if it were resolved when it wasn't.

If the fix for a regression turns out to require unexpectedly broad changes, stop and reassess rather than pushing through - a broad repair can open a new regression surface of its own, which means recalculating the surface and the plan rather than assuming the original ones still apply. In a multi-agent setup, this phase may hand a failure back to the implementing agent for repair and then rerun; that loop needs a bounded retry budget rather than running indefinitely, and there are defined conditions under which this skill should simply stop and escalate to a human rather than continuing to iterate on its own. All of this - the repair loop, retry budgets, stop conditions, and how an escaped regression should feed back into future protection - is in `references/failure-handling-and-repair.md`.

This phase is also where test-mutation scrutiny matters most: if tests changed alongside the implementation, classify why (legitimate, additive, suspicious, or ambiguous) rather than assuming a passing suite after the edit means the edit was fine. `references/ai-failure-modes.md` has the full classification and the broader catalogue of AI-specific ways a change can look safe without being safe - worth a read on any change above the lowest risk tier, since these are the failure modes this skill exists specifically to catch.

## Protected behaviors and invariants

Some things must never break regardless of what else is going on: existing users can always log in, payments never double-charge, one tenant never sees another's data, an approved record doesn't get silently deleted, a completed transaction stays immutable. Where a project has documented these, treat them as a standing checklist consulted on every relevant change. Where it hasn't, name the ones that seem to apply and flag that they're inferred rather than confirmed. Full detail is in `references/protected-behaviors.md`, including where this hands off to a dedicated security process.

## Reporting the result

Every report ends with a status and a confidence level, defined operationally rather than vibed:

- **PASS** - the relevant regression surface has sufficient evidence and no regression was detected.
- **PASS WITH CONCERNS** - available verification passed, but a meaningful coverage gap or uncertainty remains.
- **FAIL** - a regression attributable to this change was detected.
- **ESCALATE** - regression safety can't reasonably be determined without a human decision, broader changes, an unavailable environment, or more evidence than is currently available.
- **BLOCKED** - required verification can't currently run because of an environment or tooling dependency.

Confidence (HIGH / MEDIUM / LOW) is derived from the quality of the baseline, how complete the impact analysis was, how relevant the tests actually were, and how much critical-journey and contract coverage exists - not from intuition, and never as a fabricated percentage.

Never collapse a report into "all tests passed, looks good" when the surface analysis surfaced gaps - a clean test run and a clean bill of health are different claims. The full report structure (the compact evidence artifact downstream agents can consume, and the human-facing version for a founder deciding whether to ship) is in `references/reporting-and-status.md`. When the audience is non-technical, follow the structured report with plain language about what it means in practice - what's verified, what isn't, why, the potential consequence of shipping anyway, and the options available - rather than only the technical finding.
