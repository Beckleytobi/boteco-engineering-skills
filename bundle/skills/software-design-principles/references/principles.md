# Design principles, in depth

Each principle below follows the same shape: what it actually asks of you, why it matters for a codebase that will outlive this one change, and — just as important — the way it gets over-applied until it stops helping. Read a section when the one-liner in SKILL.md isn't enough to resolve a real decision in front of you. You don't need to reread all of this for every task.

## Contents

1. Modularity
2. Single Responsibility Principle
3. Open/Closed Principle
4. Separation of Concerns
5. KISS
6. DRY
7. YAGNI
8. Loose Coupling and High Cohesion
9. Dependency Inversion
10. Composition Over Inheritance
11. Encapsulation
12. Explicit Interfaces and Contracts
13. Law of Demeter
14. Principle of Least Surprise
15. Bounded Change
16. Resolving conflicts between these

---

## 1. Modularity

Build the system as cohesive units with an explicit responsibility and a boundary, so that a change to one behavior tends to stay inside the module that owns it. This is the property that makes the rest of this document possible — SRP, coupling/cohesion, and bounded change are all really facets of "does this system have real modules or not."

**Over-applied**, modularity becomes fragmentation: a codebase where following one piece of logic means opening fifteen files because every intermediate step got its own module. If understanding a single feature requires a map, the modules are too fine-grained for what the system actually needs right now.

## 2. Single Responsibility Principle

A unit — function, class, component, service — should have one reason to change. This is about *reasons to change*, not about line count or "does one thing" in some literal, mechanical sense. A function that validates and formats a phone number has one responsibility (representing phone numbers) even though it does two things; a function that also happens to log analytics and update a cache has three reasons to change bundled into one place, and that's the smell SRP is naming.

**Over-applied**, SRP turns into dozens of one-method classes created purely to say each one "does one thing," with the actual behavior now scattered across so many indirections that nobody can hold the whole responsibility in their head at once. If splitting something up makes it *harder* to see what it does, you've inverted the principle's purpose.

## 3. Open/Closed Principle

Prefer extending behavior through the extension points the system already has — an interface, a plugin slot, a strategy object — over repeatedly cutting open and modifying code that already works. If `NotificationProvider` already has `EmailProvider` and `SMSProvider`, a new `WhatsAppProvider` should implement the same contract, not trigger edits inside `EmailProvider`.

This doesn't mean stable code is untouchable forever — it means the default move, when an extension point already exists and fits, is to use it rather than reopen working code.

**Over-applied**, Open/Closed becomes an excuse to build extension points nobody asked for: a plugin architecture for a feature that will only ever have one implementation, an abstract base class with a single concrete subclass "in case we need another one." That's YAGNI's territory colliding with this one — see the conflict-resolution section below.

## 4. Separation of Concerns

Keep presentation, application logic, domain/business logic, persistence, infrastructure, external integrations, auth, configuration, and observability in the places the codebase already keeps them. The exact layer names and boundaries vary by architecture and by how big the system actually is — a ten-file internal tool does not need the same layering as a multi-team platform.

**Over-applied**, this becomes cargo-cult layering: a repository interface, a service layer, and a DTO for a CRUD screen that will only ever have one backend. If you're adding layers a small system doesn't need, ask what problem the layer solves today, not hypothetically.

## 5. KISS (Keep It Simple)

Build the simplest thing that actually satisfies the requirement — no framework, service, pattern, or indirection that isn't earning its complexity against something real. Complexity should be traceable to a requirement or a constraint, not to "this is how it's usually done" or "this might be more elegant."

**Over-applied** (or rather, mis-applied), KISS becomes an excuse for a shortcut that's actually unsafe: skipping input validation, hardcoding something that needed to be configurable, or duplicating a security check instead of centralizing it. Simple and safe are both required; simplicity doesn't outrank correctness or security.

## 6. DRY (Don't Repeat Yourself)

Avoid duplicating a *business rule* or meaningful behavior — not avoiding duplicated *text*. If two pieces of code compute a discount the same way, and that rule will change together in the future, that's the duplication DRY cares about. If two pieces of code happen to look structurally similar today but represent unrelated concepts that could reasonably diverge tomorrow, that's coincidental similarity, not duplication.

**Over-applied**, DRY produces a shared abstraction built from two examples that don't actually share a *reason* to change together — and the first time one of them needs to diverge, the abstraction has to be pulled apart under pressure, usually badly. A little short-term duplication is frequently cheaper than a premature abstraction built on insufficient evidence about what varies and what doesn't. Three real instances of the same rule is a much safer trigger for abstracting than two superficially similar snippets.

## 7. YAGNI (You Aren't Gonna Need It)

Don't build functionality, extension points, configuration knobs, or scalability mechanisms because they *might* be needed someday. Build for the requirement in front of you, in a way that doesn't paint the system into a corner — that second clause matters; YAGNI is not license to make choices that would be expensive to walk back later, only license to not build the speculative thing itself.

**Over-applied**, or rather misused, YAGNI becomes the excuse in section 6/underengineering — "we'll add auth checks when we need them" said about something that obviously needs them now. The test is whether the need is speculative, not whether building it is inconvenient right now.

## 8. Loose Coupling and High Cohesion

Keep strongly related behavior together (cohesion) and minimize unnecessary dependencies between unrelated parts (coupling). A change in one area of the system shouldn't have to ripple through unrelated areas to keep working.

**Over-applied**, this becomes a refusal to share any code at all, because sharing implies a dependency — leading right back to DRY-violating duplication of things that genuinely should be shared. Coupling to something stable and well-owned (a shared type, a well-tested utility) is not the problem; coupling to something volatile or badly-owned is.

## 9. Dependency Inversion

Core business/domain logic shouldn't be tightly bound to a volatile implementation detail or a specific third-party provider it doesn't need to know about. Depend on an abstraction where there's real value in being able to swap, test against, or reason about the implementation independently — for instance, keeping pricing rules free of Stripe-specific types so they can be unit tested without hitting the network and swapped to a different processor without touching business logic.

**Over-applied**, this produces an interface with exactly one implementation, added purely for "testability" or "flexibility" that nobody has asked for and no test actually exercises differently. An interface that exists solely to satisfy this principle in the abstract, with no real second implementation on the horizon and no actual testing benefit realized, is theoretical purity, not architecture.

## 10. Composition Over Inheritance

Prefer assembling behavior from small, focused components over building deep or fragile inheritance hierarchies, especially when the "is-a" relationship is shaky or when subclasses exist mainly to override one or two methods.

**Over-applied**, this becomes avoiding inheritance even in the cases where a genuine is-a relationship with shared, unchanging behavior makes it the clearest fit — replacing three lines of inheritance with a much more elaborate composition wiring. Apply this where the hierarchy would actually be fragile, not reflexively everywhere.

## 11. Encapsulation

Hide a module's implementation details behind a contract, and don't reach into another module's internals to get something its public interface doesn't offer. If you find yourself importing a private helper, reading another module's internal state directly, or relying on an implementation detail that isn't part of its documented behavior, that's the module boundary being violated, and it will break the next time that module is refactored — correctly, by someone who had no way to know you depended on its insides.

**Over-applied**, encapsulation turns into a getter/setter for every field with no actual behavior hidden behind them — form without the substance the principle is for.

## 12. Explicit Interfaces and Contracts

Interactions between important components should have a contract someone can understand without reading the implementation: function signatures, API shapes, schemas, event payloads, expected inputs and outputs, and error semantics. Preserve these unless the task specifically requires changing them, and if it does, that change is exactly the kind of thing worth calling out explicitly rather than letting slip inside a larger diff.

There isn't really a meaningful "over-applied" failure mode here beyond documenting genuinely trivial internals — the risk with this one runs almost entirely in the underengineering direction: silently changing a contract's behavior (an error that used to throw now returns null, a field that used to be required is now optional) without treating that as the significant, callout-worthy event it is.

## 13. Principle of Least Knowledge (Law of Demeter)

Avoid reaching through multiple layers of another object or module to get something — `order.getCustomer().getAddress().getCity()` chains that mean your code now depends on the entire internal shape of `Customer` and `Address`, not just on `Order`. Ask the object you actually have a relationship with to do the thing, rather than borrowing its internals to do it yourself.

**Over-applied**, this produces a wrapper method on every class purely to avoid one level of chaining, multiplying the surface area of the codebase without actually reducing coupling — it just moves the chain one level up. Apply it where the chain crosses a real ownership boundary, not reflexively at every dot.

## 14. Principle of Least Surprise

Code should look, structurally and behaviorally, like the rest of the codebase already looks, so the next person's (or agent's) intuition about how things work here is usually right. This is a strong argument for following existing conventions even ones you'd personally have chosen differently.

The tension worth naming: this can conflict with fixing an actually bad existing convention. Following a broken pattern because "that's what's here" isn't least-surprise, it's just perpetuating a known problem — see "Existing architecture comes first" in the main SKILL.md for how to hold that line.

## 15. Bounded Change

Especially for an AI agent, explicitly separating what should change, what may need to change, and what must not change is often the single highest-leverage thing you can do before writing code — most of the failure modes in `failure-modes.md` are really bounded-change violations wearing different costumes. This isn't a "principle" in the classic SOLID sense so much as the discipline that makes all the others enforceable in practice: none of SRP, DRY, or Open/Closed protect you from scope creep on their own.

---

## 16. Resolving conflicts between these

These principles are not simultaneously maximizable — several of them actively pull in opposite directions by design, and treating any one as an absolute will eventually make the codebase worse, not better. The recurring tensions:

- **DRY vs. YAGNI / premature abstraction.** DRY wants you to unify; YAGNI (and the over-application warning under DRY above) wants you to wait for real evidence of repetition before you do. Prefer waiting for a third instance over abstracting from two.
- **Open/Closed vs. KISS/YAGNI.** Open/Closed wants an extension point ready; KISS and YAGNI want you not to build one until something needs it. Build the extension point when you're implementing the *second* real variant, not preemptively for a first one.
- **Dependency Inversion vs. simplicity in a small system.** An abstraction layer that would matter in a large system can be pure overhead in a small one with one real implementation and no near-term second one.
- **Modularity vs. fragmentation.** More boundaries are not automatically better; a boundary is only worth its cost if it's protecting something that actually varies independently.

When a specific decision has a genuine conflict like this and you're not sure which way to go, fall back to the priority order in the main SKILL.md: correctness and explicit requirements, then safety/security, then existing architectural constraints, then long-run maintainability, then simplicity, then extensibility that a real requirement justifies. That order exists precisely because these principles disagree with each other often enough that you need a tiebreaker, not because any one of them is universally more important.
