# Reporting and status

This is where every artifact this skill produces gets its exact shape, and where the underlying philosophy for status and confidence lives. Read it whenever you're about to write a Regression Surface Report, a Regression Protection Plan, an execution result, or the final verdict.

## No evidence, no claim

This is the governing rule for everything below: absence of a detected failure is not evidence of regression safety. If a relevant behavior was never verified, automated or otherwise, that is a gap in the report, not a clean bill of health for that behavior.

Concretely: don't write "no regressions" when what actually happened is that some tests passed and other relevant behavior simply wasn't checked. Write "no regression was detected within the verified scope; coverage remains incomplete for X." This distinction is what keeps an autonomous or semi-autonomous process honest, because the difference between those two sentences is often the entire difference between a safe release and a surprise one.

## Evidence hierarchy

Different kinds of evidence carry different weight, and the right evidence depends on what's being protected, not on always reaching for the strongest-sounding option. Roughly, from weaker to stronger in most contexts: code inspection, static analysis, compilation or type checking, unit tests, integration tests, contract tests, end-to-end tests, realistic fixture or sandbox verification, controlled production-like validation.

Don't treat this as a strict ladder where end-to-end is always better - a pure calculation is often more reliably protected by a handful of focused unit tests than by an end-to-end test that exercises it incidentally, while a multi-service payment workflow usually needs integration or end-to-end evidence because no unit test can see the whole path. Match the evidence to the risk and the shape of the thing being verified.

## Status semantics

Use these exactly, and don't invent competing terminology if a project already has its own governance vocabulary - integrate with what exists rather than adding a second system. If a design-review skill in the same pipeline already reports PASS / PASS WITH CONCERNS / ESCALATE / FAIL, that's the vocabulary to match; this skill's one addition is BLOCKED, for a case a design review wouldn't need - verification that can't run at all, rather than a judgment about the change itself.

- **PASS** - the relevant regression surface has sufficient evidence, and no regression was detected.
- **PASS WITH CONCERNS** - everything that was checked passed, but a meaningful coverage gap or unresolved uncertainty remains. This is not a passing grade with an asterisk quietly attached; the concern should be stated plainly enough that someone skimming the status line alone still gets the caveat.
- **FAIL** - a regression attributable to this specific change was detected.
- **ESCALATE** - regression safety genuinely can't be determined with the evidence and access available - the change is too broad, the environment isn't available, or the decision requires a human call rather than more automated checking.
- **BLOCKED** - required verification can't run right now because of an environment or tooling dependency, independent of whether the change itself is risky.

## Confidence semantics

Report confidence as HIGH / MEDIUM / LOW (or whatever categories a project's existing governance already uses), derived from actual inputs: baseline quality, how complete the impact analysis was, how relevant the tests that ran actually are to the surface, how much critical-journey and contract coverage exists, how realistic the test environment was, and what uncertainty is left unresolved. Never compute or state a numeric confidence percentage ("94% confident") unless there's a real evidence-based method producing that number - a fabricated precision is worse than an honest category, because it invites people to stop asking what the number is actually based on.

## Regression Surface Report

Produced at the end of Phase C. Keep it proportional - a two-line version is correct for a small, contained change, and an unnecessarily long report for a trivial change is itself a small failure of judgment.

```
REGRESSION SURFACE

Requested change:
Add WhatsApp notification provider.

Directly changed:
- WhatsApp provider
- provider registration
- notification configuration

Indirectly affected:
- notification dispatcher
- notification preferences
- provider fallback
- retry handling

Critical journeys potentially affected:
CJ-002 (signup verification), CJ-003 (password reset notification), order confirmation

Contracts affected:
NotificationProvider

Data affected:
Notification preferences

External integrations affected:
WhatsApp provider

Protected existing behaviour:
- Email notifications continue working
- SMS notifications continue working
- User notification preferences remain respected
- Failed provider does not duplicate messages

Regression risk: MEDIUM
Reason: Existing provider dispatch logic is shared across all notification channels.
```

## Regression Protection Plan

Produced at the start of Phase D, before running anything, derived from the surface report above rather than from a generic checklist:

```
REGRESSION PROTECTION PLAN

Change: Add WhatsAppProvider.

Verify new behaviour:
1. WhatsApp provider sends correctly.
2. Provider failure is handled correctly.

Verify existing behaviour:
3. Email provider still sends.
4. SMS provider still sends.
5. Existing notification preferences still work.
6. Provider fallback still behaves correctly.

Contract verification:
7. Existing NotificationProvider contract remains unchanged.

Critical journey verification:
8. Password-reset notification still works (CJ-003).
9. Signup verification still works (CJ-002).

Evidence: unit tests, provider contract tests, integration tests, critical journey tests.
```

## Test execution evidence

Report what actually ran, with actual numbers - never a fabricated count, and never a bare "tests passed":

```
REGRESSION TEST RESULT

Notification unit tests:        18 passed, 0 failed, 0 skipped
Notification integration tests:  7 passed, 0 failed
Authentication critical journey: 4 passed, 0 failed
```

If something in the plan wasn't executed - no environment, no time, out of scope for this pass - say that explicitly in the same place, rather than letting it silently disappear between the plan and the result.

## Evidence artifact

A compact summary another agent (or a human) can consume without re-deriving everything above. Include the fields that are actually relevant; don't force a value into a field that doesn't apply to this change:

```
REGRESSION EVIDENCE

Change ID: ...
Baseline: ...
Changed modules: ...
Regression surface: ...
Critical journeys affected: ...
Contracts affected: ...
Tests executed: ...
Passed / Failed / Skipped: ...
Missing coverage: ...
Manual checks: ...
Unresolved uncertainty: ...
Regression status: PASS | PASS WITH CONCERNS | FAIL | ESCALATE | BLOCKED
Confidence: HIGH | MEDIUM | LOW
```

If a project's governance system already defines a machine-readable schema for this (field names like `change_id`, `regression_surface`, `critical_journeys`, `tests_run`, `missing_coverage`, `status`, `confidence`, `evidence`), populate that instead of inventing a new one - the goal is other agents being able to parse the result reliably, not a specific field naming convention.

## Escalating to a human

When status is anything other than a clean PASS, translate the finding into what it actually means for the product before handing it off - don't stop at the internal mechanics:

> Weak: "Shared auth utility has high fan-out."
> Better: "The change modifies authentication code used by login, password reset, and session refresh. Login tests pass, but password reset currently has no automated protection. Releasing now would mean accepting uncertainty around that journey."

For an ESCALATE (or any status where the decision genuinely belongs to a person), lay out all five of these rather than just the technical finding, so the decision stays with the human rather than getting made implicitly by whichever way the report happened to lean:

```
WHAT IS VERIFIED
WHAT IS NOT VERIFIED
WHY
POTENTIAL CONSEQUENCE
AVAILABLE OPTIONS (gather more evidence, repair, defer, accept the risk, change scope)
```

This skill's job stops at presenting that clearly. Which option to take is the founder's or the governance process's call, not this skill's.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
