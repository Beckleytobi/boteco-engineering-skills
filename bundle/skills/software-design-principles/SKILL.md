---
name: software-design-principles
description: Use whenever you are about to plan, implement, extend, refactor, or review a change to an existing codebase, or acting as an architect, builder, code-reviewer, or QA agent in a development pipeline. Also trigger before adding any new abstraction, service, dependency, or design pattern, when a diff is touching more files than the request seems to justify, and when a non-technical founder asks you to "just add" or "just change" something in running software. Covers SOLID, KISS, DRY, YAGNI, coupling and cohesion, bounded-change and blast-radius reasoning, and detecting both AI-agent overengineering and shortcut-driven underengineering. Do not wait for the user to say "architecture" or "best practices" — trigger this on the coding task itself.
---

# Software Design Principles

AI coding agents are good at making code work and bad at noticing when "it works" was purchased by quietly damaging the system around it: business logic leaking into a UI component, a stable module rewritten instead of extended, a small feature that touches twenty-five files, an abstraction built for a future that was never asked for. None of that shows up in a passing test run. It shows up three months later as a codebase nobody wants to touch.

This skill exists to make you ask, before and after every change:

> What is the smallest, cleanest, safest change that satisfies the requirement while preserving the system's existing boundaries and behavior?

Not just: does the new feature work. Both questions matter, and correctness always wins when they conflict — a beautifully bounded change that doesn't meet the requirement is not a success.

## Whose hat you're wearing

This skill reads the same regardless of role, but what you *do* with it differs:

- **Architect / planner** — use Phases A–C to define the change boundary and produce the design check *before* anyone writes code.
- **Builder** — use the change boundary as a constraint while implementing (see Implementation behavior), and don't skip the drift check just because you wrote the plan yourself.
- **Reviewer** — run the drift check independently against the actual diff. Never accept a builder's self-reported "SRP: PASS" without evidence — see Principle theatre below.
- **QA / regression agent** — you mostly consume the output of this skill (the regression surface and affected contracts) rather than run the whole workflow.

If you're doing all four roles in one pass because there's no multi-agent pipeline around you, still do them in order and don't let the "reviewer" step collapse into "I already checked this while building it." A rewrite of your own diff two minutes later, with fresh eyes on the *actual* changed files rather than your intention, catches real things.

## Existing architecture comes first

Before applying any principle below, look at what's already there: the module boundaries, naming and folder conventions, existing abstractions and extension points, dependency direction, tests, and any architecture docs, ADRs, or repo-level agent instructions (CONTRIBUTING.md, CLAUDE.md, similar). Sound design principles describe good architecture in general; they don't license you to redesign a specific codebase's choices you happen to disagree with.

Hold two things apart:

- **Preserving architecture** — working within the grain of decisions that are merely different from what you'd have chosen. Default to this.
- **Perpetuating a defect** — working around a boundary that is actively causing the bug or making the requested feature unreasonably hard. Don't silently redesign around this either. Name the conflict and let the human or the architect step decide, unless the task explicitly authorized architectural change.

## Phase A — Understand the change

Before writing anything, pin down: the requested behavior and acceptance criteria, which user journeys it touches, which module most naturally owns it, how that area is implemented today, what architectural boundaries and existing extension points are in play, what depends on it, which tests already cover it, and any constraints the user stated explicitly. If any of this is genuinely unclear and guessing wrong would send you down the wrong architectural path, ask — but a clear, ordinary feature request doesn't need an interview.

## Phase B — Inspect before inventing

Search the repository before creating a new utility, service, interface, component, helper, repository, adapter, or schema. Most "I need a new X" moments are actually "I didn't look for the existing X." If something close already exists, extend or reuse it rather than standing up a parallel concept that now competes with it for future maintainers' attention. If nothing suitable exists, that's fine — build it — but you should be able to say what you looked for and didn't find.

## Phase C — Establish the change boundary

Before implementing, write down three lists:

- **Expected to change** — the files/modules that own the requested behavior.
- **May need to change** — adjacent components with a legitimate dependency on the thing you're changing (a caller whose interface shifted, a type definition consumers import).
- **Protected** — everything else, which stays untouched unless implementation surfaces a real reason it can't.

This is the contract you'll check your own diff against in the drift check later. Skipping this step is the single biggest reason agents end up making a scoped request into a sprawling one without noticing.

## Change budget: is the blast radius proportional?

Don't enforce a file-count limit — that just teaches padding tricks. Instead, when the diff is larger than the request seems to warrant, ask directly: *why does this requirement need this much architectural surface area?* Sometimes there's a real answer (a shared type genuinely needs a new field, and twelve call sites destructure it). Sometimes there isn't, and that's a sign the approach — not just the size — is wrong. If you can't articulate the "why" in a sentence, stop and reconsider the design before continuing.

## Principles at a glance

Full explanations, the trade-offs between them, and worked examples of over-applying each one are in `references/principles.md` — read it the first time any of these feels ambiguous, and always before writing the "principle assessment" part of a design check. The one-line versions:

| Principle | Ask yourself | Don't let it become |
|---|---|---|
| Modularity | Does this stay inside the module that owns the behavior? | Fragmentation — everything split until nothing coheres |
| Single Responsibility | Does this unit have one reason to change? | A dozen one-line classes created to "comply" |
| Open/Closed | Can I extend rather than modify the stable, working parts? | Speculative extension points nobody asked for |
| Separation of Concerns | Is UI, business logic, and persistence where they belong? | Layering imposed on a ten-file script |
| KISS | Is this the simplest thing that actually meets the requirement? | An excuse to skip a genuinely needed layer |
| DRY | Am I duplicating a *business rule*, not just similar-looking code? | Abstracting two things that happen to look alike today |
| YAGNI | Does a stated requirement need this, or might it someday? | A justification for known-bad shortcuts |
| Coupling & Cohesion | Do related things live together, unrelated things stay apart? | An excuse to avoid any shared code at all |
| Dependency Inversion | Does core logic depend on a volatile detail it shouldn't? | Interfaces added for theoretical purity, one implementation each |
| Composition > Inheritance | Am I building a fragile hierarchy where composing would do? | Avoiding inheritance even where it's the clean fit |
| Encapsulation | Am I reaching into another module's internals? | Getters/setters for everything, hiding nothing meaningful |
| Explicit contracts | Would a caller be surprised by this input/output/error behavior? | Documenting trivia nobody will read |
| Law of Demeter | Am I chaining through objects I don't own? | Wrapper methods that just forward one call |
| Least Surprise | Does this match how the rest of the codebase already does things? | Copying a bad convention because it's already there |
| Bounded Change | Am I inside the boundary from Phase C? | Treating "I could improve this too" as license |

### When principles conflict

They will — DRY pulls toward abstraction, YAGNI pulls away from it; Open/Closed pulls toward an extension point, KISS pulls toward not building one yet. When they genuinely trade off, resolve in this order: correctness and explicit requirements first, then safety/security, then respecting existing architectural constraints, then long-run maintainability, then simplicity, and only then extensibility that isn't yet required by anything concrete. Never trade correctness or security away to satisfy a design principle — that's a sign you picked the wrong principle to prioritize, not a genuine dilemma.

## Design check before implementation

For anything beyond a trivial change, do a short, honest design check before writing code — a few lines, not a essay:

```
Requirement: <one line>
Owner module: <path or component>
Existing extension point (if any): <what you're building on>
Proposed approach: <one or two sentences>
Expected files: <from Phase C>
Protected areas: <from Phase C>
Primary architectural risk: <the one thing most likely to go wrong>
```

Skip the ceremony for genuinely trivial changes — a copy fix, a one-line bug fix inside a single function, a config value. Use judgment: if you're not sure whether something counts as trivial, it probably doesn't, and the check takes thirty seconds anyway. The full template with principle-by-principle evidence (used for larger changes and for independent review) is in `references/review-checklist.md`.

## Implementation behavior

While building: stay inside the change boundary unless you hit a concrete reason not to (and if you do, say so rather than quietly expanding scope); preserve existing contracts unless the task requires changing them; reuse what Phase B found instead of duplicating it; keep responsibilities cohesive rather than scattering one behavior across many files "for organization"; keep the dependency direction the codebase already has; isolate new third-party/external integrations behind the same kind of seam the codebase already uses for that purpose; avoid hidden side effects and unexplained global state; keep configuration out of business logic where the codebase already does that; and keep the change testable — if you can't see how you'd test what you just wrote, that's worth noticing before you move on.

## After the diff: check for drift

Once the change exists, look at the actual diff — not your memory of the plan. Compare it against the Phase C boundary. Look specifically for: files touched that weren't expected or "may need to change"; new cross-module dependencies; duplicated logic that Phase B should have caught; a public contract changed without that being the point of the task; functions or components that grew multiple responsibilities along the way; abstractions or dependencies added that the design check didn't call for; unrelated refactoring that snuck in; dead code or an old path left behind after a replacement. If you find drift, either fix it or explain concretely why the deviation was necessary — "it seemed cleaner" is not a reason, "the shared type is used by three other callers who would otherwise break" is. Full checklist in `references/review-checklist.md`.

## Classify any refactoring you're tempted to do

- **Required** — the requested behavior genuinely cannot be built safely without it. Do it, and say so in the design check.
- **Opportunistic** — you noticed something you *could* improve while you were in there, but the task doesn't need it. Mention it to the user separately; don't fold it into this diff.
- **Architectural remediation** — a structural problem bigger than this task. Name it as its own future task rather than either fixing it unasked or silently working around it forever.

Mixing these into one diff is one of the most common ways a small, reviewable change turns into a large, unreviewable one.

## Before adding anything new

Before introducing a new abstraction, interface, service, microservice, event, queue, cache, repository layer, design pattern, dependency, or framework, answer: what concrete current requirement makes this necessary; what specific problem it solves; whether the repo already has a simpler mechanism for this; whether a direct implementation would be easier to understand; and whether you're solving something real or something hypothetical. Weak answers mean pick the simpler option.

The opposite failure is just as real: KISS and YAGNI are not an excuse for a shortcut that duplicates a business rule, creates a security gap, produces fragile coupling, or makes something untestable. "Simple" means appropriately simple for the requirement, not minimal-code-at-any-cost. `references/failure-modes.md` has both the overengineering and underengineering warning signs in more depth, plus a list of AI-coding-agent failure patterns worth recognizing in your own output: rewriting a whole file instead of extending it, inventing an abstraction that doesn't match repo conventions, duplicating a utility because you didn't search first, changing unrelated code "for consistency," adding a dependency without checking what's already available, and fixing unrelated lint or test failures inside an otherwise bounded task.

## When to stop and escalate

Don't silently push through: a major existing architectural boundary would need to be violated; the blast radius came out much larger than the request suggested; a public contract or database schema needs to change in a way with broad consequences; the existing architecture materially conflicts with what's being asked; new infrastructure would be required; the dependency direction would reverse; a security boundary would shift; or you're about to exceed the change boundary you set in Phase C without a concrete reason.

When you do escalate — especially to a non-technical founder — lead with the recommendation, not the buildup. They should get the answer in the first line and be able to stop reading there if they trust it; the reasoning stays available for anyone who wants to check it:

```
RECOMMENDATION:
WHAT CHANGED / WOULD CHANGE:
WHY:
IMPACT (in plain terms — what becomes harder, riskier, or slower later):
OPTIONS:
RISKS:
```

"Payment calculation now directly depends on Stripe-specific code" is true but not useful to a founder on its own. "This means switching payment providers later, or testing pricing rules without hitting Stripe, gets harder" is the sentence that lets them make the call. Template and more examples in `references/review-checklist.md`.

## Evidence-based completion, not principle theatre

Never write "SRP: PASS" or "DRY: PASS" as a bare label — that's principle theatre, and it's worse than saying nothing because it looks like verification without being any. Every assessment needs the evidence behind it: *"Open/Closed: PASS — the new provider implements the existing NotificationProvider interface; EmailProvider and SMSProvider were not modified."* If you can't write the evidence sentence, you haven't actually checked, and the honest status is "unverified," not "pass."

Use these statuses where useful: **PASS** (verified, no concerns), **PASS WITH CONCERNS** (works, but note the trade-off you accepted and why), **ESCALATE** (see above), **FAIL** (don't ship it as-is). Don't invent a different status system on top of whatever the surrounding pipeline already uses.

## This isn't a substitute for testing

Good bounded design reduces regression *surface*; it doesn't verify correctness. Hand off what a testing or QA process needs from you: what behavior changed, which modules and contracts were affected, what existing behavior could plausibly be impacted. That's a foundation for testing, not a replacement for it.

## Stay technology-agnostic

Everything above should hold whether the codebase is TypeScript, Python, Go, Java, C#, a mobile app, a monolith, or a pile of Lambda functions. If a stack-specific example would help, put it in `references/examples.md` rather than baking a framework assumption into the core reasoning above.

## Reference files

- `references/principles.md` — each principle explained with its rationale and its over-application failure mode, plus how to resolve the common conflicts between them.
- `references/failure-modes.md` — AI-coding-agent failure patterns, the overengineering checklist, and the underengineering warning signs, each with what to do instead.
- `references/review-checklist.md` — the full design-check template, the drift-detection checklist, the escalation report format, and the evidence-based completion statuses with more worked examples.
- `references/examples.md` — six worked scenarios (new notification provider, new payment provider, a small UI feature, a 25-file diff for a small ask, a duplicated business rule, and an existing codebase that's already poorly architected) showing this reasoning applied end to end.


## Visual design integration

For diagram authoring, review, or consumption, read [visual-routing.md](references/visual-routing.md) and the shared contract it references. Scale diagrams to the change. Preserve existing approval gates.
