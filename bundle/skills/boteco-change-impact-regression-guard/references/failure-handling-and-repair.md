# Failure handling, repair, and stop conditions

Read this once evidence-gathering (Phase D) has actually turned something up - a failing test, an unexpected diff, a suspicious test change - and the question becomes what to do about it.

## Handling a failure

When a regression check fails, work through it in order rather than jumping to a fix: determine whether the failure is new or was already there before this change, reproduce it, identify whether the current change is actually the cause, identify exactly what behavior is affected, correct the implementation where that's the appropriate response, rerun the specific check that failed, and then rerun the checks around it that could plausibly have been affected by the fix itself.

Three things not to do, because they're the shortcuts that quietly turn this skill into theater: don't modify the test to make the failure disappear, don't suppress the failure, and don't proceed toward release as though the regression were resolved when it hasn't actually been re-verified.

## Bounded repair

A repair for a detected regression is itself a change, and can introduce a new regression surface of its own - so treat it as one rather than assuming the original plan still covers it. If fixing a regression turns out to require unexpectedly broad changes, stop and reassess before continuing, rather than pushing through under the assumption that "it's still the same fix."

The loop looks like this:

```
CHANGE
  -> REGRESSION DETECTED
  -> BOUNDED REPAIR
  -> NEW DIFF
  -> RECALCULATE REGRESSION SURFACE
  -> RETEST
```

The "recalculate" step matters - a repair that touched more than expected needs its own Phase C pass, not a rubber-stamped extension of the original one.

## Rework loops in multi-agent setups

Where a builder agent and this skill operate as separate steps, a failure naturally produces a loop: the builder receives the evidence, attempts a repair, and this skill reruns and reports PASS, FAIL, or ESCALATE again. That loop needs a bound. An unlimited autonomous repair cycle is a way for a genuinely hard problem to consume unbounded effort while looking, at every individual step, like normal progress.

The actual retry or rework budget (how many cycles are allowed before this stops being autonomous) should come from the project's own governance rather than being hardcoded here, since it depends on how much autonomy that project has decided to grant. What this skill should do is track that the budget exists and escalate once it's exhausted, rather than continuing to iterate past it.

## Learning from escaped defects

When a regression makes it past this process and reaches staging or production anyway, that failure is itself useful information and shouldn't be treated as a closed incident once it's fixed. Where the surrounding governance infrastructure supports it, feed it back:

```
ESCAPED REGRESSION
  -> ROOT CAUSE
  -> MISSING PROTECTION IDENTIFIED
  -> REGRESSION TEST ADDED
  -> CRITICAL JOURNEY / INVARIANT REGISTRY UPDATED IF NECESSARY
```

This is a handoff, not a mandate to build incident-management tooling inside this skill - the point is just that an escaped regression should leave the protection stronger than it found it, rather than the same gap quietly waiting to be rediscovered the same way next time.

## Stop conditions

Some situations call for stopping rather than continuing to push toward a release, even though it would be technically possible to keep going: a confirmed regression that hasn't been resolved, a critical test failure, a contract change nobody can explain, an unexpectedly destructive migration, a test suite that was modified in a way that reads as suspicious rather than legitimate, a critical journey with no available verification at all, an unavailable baseline for a change that's otherwise high-risk, a blast radius that turned out to be far wider than expected, a required external environment that simply isn't reachable, or a repair that's exceeded its approved scope.

None of these are reasons to give up on the change - they're reasons to escalate rather than to keep iterating autonomously. The ability to keep working is not the same thing as it being the right call to keep working.
