# Worked examples

Six scenarios, each showing the reasoning from the main skill applied to something concrete. Pseudocode is kept generic on purpose — the point is the reasoning, not a specific stack.

## Contents

A. Adding another notification provider
B. Adding a payment provider
C. A small UI feature
D. A 25-file diff for a small request
E. A duplicated business rule
F. The existing architecture is already poor

---

## A. Adding another notification provider

**Request:** "Users should be able to get order updates over WhatsApp, not just email and SMS."

**Phase B (inspect first):** The repo has `notifications/NotificationProvider` (an interface with `send(message, recipient)` and `validateRecipient(recipient)`), with `EmailProvider` and `SMSProvider` as existing implementations, registered in a `ProviderRegistry`.

**Design check:**
```
Owner module: notifications/
Existing extension point: NotificationProvider interface
Proposed approach: Implement WhatsAppProvider against the existing
  interface; register it in ProviderRegistry alongside the other two.
Expected files: notifications/WhatsAppProvider.ts,
  notifications/ProviderRegistry.ts (registration only)
Protected areas: EmailProvider.ts, SMSProvider.ts, the interface itself
Principle assessment:
  Open/Closed: PASS — new capability added by implementing the existing
    contract; no changes to the other two providers.
  DRY: PASS WITH CONCERNS — WhatsApp's recipient format needs a country
    code prefix that SMS doesn't; kept separate rather than forcing a
    shared formatter over a two-instance case that already diverges.
Primary architectural risk: WhatsApp's API is rate-limited more
  aggressively than email/SMS; ProviderRegistry doesn't currently model
  per-provider rate limits.
```

**This is what "extend, don't modify" looks like in practice** — the diff is additive, the two existing providers are untouched, and the one real risk (rate limiting) is surfaced rather than silently absorbed into the new provider's implementation.

---

## B. Adding a payment provider

**Request:** "Add support for a second payment processor as a fallback."

The naive version of this task pulls the new processor's SDK types straight into the order-total and refund-calculation logic, because that's where the "add payment support" work feels like it belongs. That's the failure to isolate infrastructure from business rules that dependency inversion exists to prevent: pricing and refund math should not need to know which processor is being called.

**Better shape:** a `PaymentProcessor` interface (`charge`, `refund`, `getStatus`) that both the existing and new processor implement; the business logic that decides *how much* to charge or refund depends only on that interface, never on either SDK directly. The new processor's SDK-specific detail — its request/response shapes, its error codes — lives entirely inside its own implementation of the interface.

```
Principle assessment:
  Dependency Inversion: PASS — refund calculation logic in
    RefundCalculator.ts takes a PaymentProcessor, not a specific SDK
    client; verified by grep — no SDK import outside the new
    provider file.
  Bounded Change: PASS WITH CONCERNS — PaymentProcessor interface needed
    a new optional field (idempotencyKey) that the existing processor's
    implementation now also needs to populate; that's a "may need to
    change" file, not scope creep, since both implementations of one
    interface must satisfy it.
```

This is the same shape as Example A, but worth calling out separately because payment logic is exactly the kind of area where a shortcut ("just call the new SDK directly where we need it") is tempting and expensive later — the whole point of Example B is that the *business rule* (how much to charge or refund) shouldn't need to change at all when the processor underneath it does.

---

## C. A small UI feature

**Request:** "Add a 'copy to clipboard' button next to the API key field."

**Overengineered version (what to avoid):** a `ClipboardService` interface, a `ClipboardServiceImpl` class wrapping the browser API, a dependency-injection registration for it, a `useClipboard()` hook wrapping the service, and a `CopyableField` component that takes a `clipboardService` prop for "testability." Five new files and an interface with exactly one real implementation and no plausible second one, for a feature that is, at its core, one button and one browser API call.

**Right-sized version:** a `copyToClipboard(text)` utility function (if one doesn't already exist — check first) and a button in the existing field component that calls it and shows a brief "copied" state. One function, one small change to an existing component, done.

```
Principle assessment:
  KISS: PASS — no new abstraction layer for a single call to a stable
    browser API with one caller.
  Dependency Inversion: N/A — not relevant at this scale; there is no
    second implementation this is ever likely to need, and introducing
    one here would be the interface-with-one-implementation pattern
    failure-modes.md warns about.
```

This is the clearest illustration of why the "principles at a glance" table exists: SRP, DIP, and testability are all real principles, and applying all three reflexively to a copy button produces something worse than the plain version, not better. The skill isn't "always add more structure" — it's "add the structure the requirement actually needs."

---

## D. A 25-file diff for a small request

**Request:** "Let admins rename a project after it's created."

**What happened:** the agent's diff touched the `Project` type definition, the API route, the database migration, the admin UI form — reasonable so far — and also 21 other files: every place that displayed a project name anywhere in the app, because the agent decided project names should now be validated against a new set of rules (no special characters, length limits) and propagated that validation everywhere a project name appeared, "for consistency."

**Change-budget check:** the request was "let admins rename a project." Nothing asked for new validation rules applied retroactively across the whole app. The honest answer to "why does this requirement need this much architectural surface area" is: it doesn't — the agent invented a second, unrequested requirement (new validation everywhere) and let it drive the diff size.

**Correct handling:** implement the rename (API route, migration if needed, admin UI form) inside the small, expected boundary. If the validation question is real — maybe project names genuinely do need tighter rules — raise it separately:

```
ESCALATE (surfaced separately, not folded into this diff)
RECOMMENDATION: Ship rename now; treat validation as its own task if
  you want it.
WHAT: Should project name validation be tightened (no special
  characters, length limit)?
WHY IT CAME UP: While adding rename support, noticed project names are
  currently unvalidated on creation too.
IMPACT: Doesn't block the rename feature. If you want it, it's a
  separate, larger change touching every display surface for project
  names, not just the rename form.
```

The 25-file version isn't wrong because 25 is a magic bad number — it's wrong because nobody asked for what actually drove the size, and it was implemented instead of surfaced.

---

## E. A duplicated business rule

**Discovery:** while implementing a new discount type, the agent notices that discount-percentage calculation is implemented separately in `CartTotal.ts` and `InvoiceGenerator.ts`, with slightly different rounding.

**Wrong move (premature abstraction under pressure):** build a shared `DiscountEngine` covering both use cases inside this task, guessing at a shape that satisfies both call sites, potentially introducing behavior change in whichever one didn't match the guess.

**Also wrong (ignore it):** duplicating the new discount type a third time in whichever file the current task touches, letting three slightly-different implementations of "how do we round a discount" exist side by side.

**Right move:** this is a real DRY violation — the same business rule (discount rounding), not coincidental similarity — but unifying it safely means understanding *why* the two are different first (was the rounding difference intentional, e.g. invoices need to round to the cent for tax reasons and carts don't? or is it just drift?). That's bigger than "implement the new discount type."

```
Classify: Architectural remediation, not required-for-this-task.
Handling: Implement the new discount type inside CartTotal.ts only
  (the file the request actually touches), matching its existing
  rounding behavior. Flag separately: "CartTotal and InvoiceGenerator
  compute discount rounding independently and currently disagree by
  a cent in some cases — worth a dedicated task to confirm intended
  behavior and unify."
```

Fixing real duplication is worth doing — just not as an uninvited side effect of an unrelated task, and not by guessing at the unification without first understanding whether the difference was intentional.

---

## F. The existing architecture is already poor

**Situation:** the request is to add a small feature, but the module it belongs in is a 2,000-line file mixing UI rendering, API calls, and business logic with no separation at all, and every existing feature in that file follows the same pattern.

**Wrong move (silent redesign):** use this task as an excuse to split the file into proper layers, because the opportunity presented itself and the principles in this skill clearly support it.

**Also wrong (perpetuate it uncritically):** add the new feature in the same tangled style, reasoning that "least surprise" means matching what's already there, no matter how bad it is.

**Right move:** implement the requested feature with the smallest reasonable addition to the existing pattern — matching the file's actual conventions closely enough that it doesn't look like a foreign transplant — while naming the debt explicitly rather than either fixing it uninvited or pretending it isn't a problem:

```
Note (not blocking, surfaced once): notifications/legacy_handler.ts
mixes UI, API calls, and business logic with no separation, and this
change adds to that pattern to stay consistent with the rest of the
file. This file has grown large enough that any future non-trivial
change here will be slower and riskier than it should be. Worth a
dedicated refactor task before the next major feature lands here —
happy to scope that separately if useful.
```

The distinction that matters: *this task* stays small and consistent with what's there; the debt gets named once, clearly, as its own thing — not fixed as a byproduct, and not silently accepted as permanent either.
