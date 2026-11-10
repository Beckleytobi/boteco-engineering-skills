# Templates: design check, drift detection, escalation, and completion evidence

## Contents

1. The full design check (for non-trivial changes)
2. Drift detection checklist (run against the actual diff)
3. Principle theatre and what evidence actually looks like
4. Escalation report format
5. Regression handoff — what to give the next agent

---

## 1. The full design check

Use this for changes big enough that a one-line design check (the short form in the main SKILL.md) isn't enough to reason about — new architectural elements, anything crossing more than one existing module boundary, or anything an independent reviewer will need to evaluate without you in the room.

```
DESIGN CHECK

Requirement:
<what was actually asked for, in one or two sentences>

Owner module:
<where this behavior naturally lives>

Existing extension point (if any):
<what you're building on, or "none — new capability">

Proposed approach:
<the shape of the implementation, 2-4 sentences>

Expected files:
<from Phase C>

May need to change:
<from Phase C, with the reason each one is affected>

Protected areas:
<from Phase C — call out anything a reader might assume is in scope but isn't>

Principle assessment:
<one line per principle that's actually relevant to this change — skip the ones
that don't apply rather than padding the list. Each line needs the evidence
sentence, not just a label. See section 3 below.>

Primary architectural risk:
<the single most likely way this goes wrong, architecturally>

Regression surface:
<what existing behavior could plausibly be affected — see section 5>
```

Don't force this template onto a two-line bug fix. Use the short form from the main skill there, or just fix it — the goal is judgment proportional to the change, not paperwork proportional to your available tokens.

---

## 2. Drift detection checklist

Run this against the *actual diff*, after implementation, not against your memory of the plan. If you planned the change yourself, this is the point where you should be genuinely willing to be surprised by what you find — that willingness is the whole value of the step.

- [ ] Are all modified files inside "expected to change" or "may need to change"? List anything outside those two sets by name.
- [ ] Did any new cross-module dependency appear that wasn't in the plan? In which direction, and does it match the codebase's existing dependency direction?
- [ ] Is there duplicated logic that Phase B (inspect before inventing) should have caught?
- [ ] Did a public contract change — function signature, API shape, schema, event payload, error behavior — that the design check didn't call out as intentional?
- [ ] Did any function, class, or component pick up more than one responsibility along the way, even if it started clean?
- [ ] Was a new abstraction, dependency, or pattern introduced that the design check's overengineering check (see `failure-modes.md`) didn't justify?
- [ ] Is there unrelated refactoring mixed into this diff? If so, is it required, opportunistic, or remediation (see the main skill's classification), and was it separated out or at least flagged?
- [ ] Are there hidden side effects — something that looks like a pure read or computation but also writes, logs with side effects, or calls out to a network?
- [ ] Is there dead code or an old path left behind after something was replaced?
- [ ] Did the regression surface actually grow beyond what the design check anticipated?

If any box reveals a real issue: either fix it before calling the change done, or write down concretely why the deviation was necessary. "It seemed cleaner this way" is not a concrete reason. "The shared `UserProfile` type is imported by three other modules, so widening it here means updating their call sites too — done in files X, Y, Z" is.

---

## 3. Principle theatre and what evidence actually looks like

Principle theatre is writing an assessment that *looks* like verification without being any — a list of principle names each followed by "PASS," produced from the plan or from general confidence rather than from looking at the actual code. It's worse than skipping the assessment, because it gives a reviewer (human or agent) false confidence that something was checked.

**Theatre:**
```
SRP: PASS
DRY: PASS
KISS: PASS
Open/Closed: PASS
```

**Evidence:**
```
Open/Closed: PASS
Evidence: WhatsAppProvider implements the existing NotificationProvider
interface (send(), validateRecipient()). No changes were made to
EmailProvider.ts or SMSProvider.ts.

DRY: PASS WITH CONCERNS
Evidence: The phone-number formatting logic in WhatsAppProvider is similar
to the one in SMSProvider but not identical — WhatsApp requires the
country code inline, SMS doesn't. Left as separate implementations rather
than forcing a shared abstraction over a two-instance, already-diverging
case. Worth revisiting if a third channel needs the same formatting.
```

The second version tells a reviewer exactly what was checked and where the judgment call was made. The first tells them nothing. If you can't write the evidence sentence for a principle, either go look until you can, or report it honestly as unverified rather than as a pass.

Use these four statuses, and don't invent a fifth unless the surrounding pipeline already has its own system to defer to:

- **PASS** — verified against the actual code, no open concerns.
- **PASS WITH CONCERNS** — works, ships, but there's a trade-off worth someone knowing about (see the DRY example above).
- **ESCALATE** — see section 4; a human decision is needed before proceeding.
- **FAIL** — don't ship this as-is; say what needs to change.

---

## 4. Escalation report format

```
RECOMMENDATION:
<your actual recommendation, stated as a decision, not a list for them to
weigh unaided — this is the first thing they read>

WHAT CHANGED / WOULD CHANGE:
<the specific technical fact>

WHY:
<why the task seems to require it>

IMPACT:
<translated into consequences a non-technical reader can act on — what
becomes harder, riskier, slower, or more expensive later, not just what
technical property was affected>

OPTIONS:
<the realistic alternatives, briefly — not an exhaustive design-space tour>

RISKS:
<what could go wrong with each option, briefly>
```

Recommendation-first is deliberate: a founder who trusts the call should be able to stop after line one and say "go ahead." Everything below it exists for the times they want to check your reasoning or push back on it — it's backup, not a prerequisite to reading the answer.

Two worked examples of the translation step inside IMPACT, which is the part most often skipped:

- Technical: "Dependency inversion violation — pricing logic now imports the Stripe SDK directly." → Impact: "Pricing rules and Stripe billing code are now tangled together. Testing a pricing change means also touching Stripe's test mode, and switching payment providers later means rewriting pricing logic, not just the billing integration."
- Technical: "This requires a schema migration that adds a NOT NULL column to the orders table." → Impact: "Every existing order in production needs a value backfilled before this ships, or the migration will fail against real data. This needs a migration plan, not just a code change, and probably a maintenance window."

Keep the whole thing short. A founder who has to read past the fifth paragraph to find the reasoning behind line one will skim past the risks that mattered.

---

## 5. Regression handoff — what to give the next agent

You are not the regression or QA process, but you owe it a clear starting point rather than making it rediscover what you already know. Hand off:

- **Changed behavior** — what actually behaves differently now, described in terms of observable outcomes, not implementation.
- **Affected modules** — from your change boundary, not just the files touched.
- **Affected contracts** — any API, schema, or interface whose shape or semantics shifted.
- **Affected integrations** — anything external (another service, a third-party API, a queue) that now sees different input or timing.
- **Existing behavior that could plausibly be impacted** — the things you didn't change but that sit close enough to the change that they're worth someone double-checking, especially anything the drift check flagged as "may need to change."

This list is the difference between a QA pass that actually targets the risk you introduced and one that re-tests everything shallowly because nobody told it where to look closely.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
