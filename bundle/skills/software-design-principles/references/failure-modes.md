# Failure modes: overengineering, underengineering, and AI-specific patterns

## Contents

1. AI-coding-agent failure patterns
2. Overengineering: the check before adding anything
3. Underengineering: when "simple" is actually just broken

---

## 1. AI-coding-agent failure patterns

These aren't hypothetical. They're the specific, recurring ways an agent optimizing for "make the tests pass" or "satisfy the request" quietly degrades a codebase. Recognize them in your own output, not just in someone else's.

**Rewriting a whole file instead of extending it.** It's often mechanically easier to regenerate a file from scratch than to make a surgical edit, especially when the file wasn't written by you. But a full rewrite discards conventions, comments, and edge-case handling that existed for reasons the rewrite doesn't know about. Default to editing in place; only rewrite wholesale when the file's structure is itself the problem, and say so.

**Replacing a working implementation instead of extending it.** Close cousin of the above, at the design level rather than the file level: reaching for "let me redo how notifications work" when "let me add a provider" was available. This is exactly what Open/Closed is warning against.

**Inventing an abstraction that doesn't match the repository.** Every codebase has its own vocabulary and shape for things — how it names services, where it puts validation, how it structures errors. An abstraction that's individually reasonable but stylistically foreign makes the codebase incoherent even when each part, judged alone, looks fine.

**Duplicating a utility because you didn't search first.** The single most avoidable failure on this list. Phase B in the main skill (inspect before inventing) exists specifically to prevent this. If you write a `formatCurrency` helper and one already exists two files away, that's not a design disagreement, it's a process failure.

**Changing unrelated code "for consistency" or "while I'm in here."** Reformatting a neighboring function, renaming a variable you noticed, fixing an unrelated lint warning — each individually reasonable, collectively turning a five-line diff into a hundred-line one that's much harder to review and much more likely to introduce an unrelated regression. This is opportunistic refactoring (see the main skill) sneaking in uninvited.

**Adding a dependency without checking what's already available.** Reaching for a new library to solve a problem the codebase's existing dependencies already solve, because the existing solution wasn't obvious from where you were looking. Costs the project a new transitive dependency, a new thing to keep updated, and often a second way of doing the same thing sitting next to the first.

**Silently changing a contract.** An error path that used to throw now returns `null`; a field that used to be required becomes optional; a function that used to be synchronous is now async. Any of these can be the right call — but silently, as a side effect of an unrelated change, is how downstream callers break in ways nobody connects back to this diff.

**Broad refactoring folded into feature work.** See "Classify any refactoring you're tempted to do" in the main skill. The tell is a diff where the feature-relevant lines are a small fraction of the total change.

**Generating excessive boilerplate.** Scaffolding a full CRUD layer — controller, service, repository, DTO, mapper — for something that needed a single function. This usually comes from pattern-matching to "how a professional codebase looks" rather than to what this specific requirement needs.

**Creating patterns inconsistent with the project's own conventions.** Introducing a new state-management approach, a new error-handling style, or a new way of structuring tests when the codebase already has an established one, even a suboptimal one. Consistency with what's there almost always beats individual technical elegance — see Least Surprise.

**Removing unusual-looking code without understanding why it exists.** That odd-looking special case, that seemingly redundant null check, that comment-free workaround — it's usually there because of a bug it was fixing, not because whoever wrote it didn't know better. Before deleting something that looks wrong, understand what it's protecting against, or leave it and flag the question instead.

**Fixing unrelated lint or test failures inside a bounded task.** Feels responsible in the moment; expands the diff and the review burden past what the task actually asked for. Flag it separately instead.

**Claiming design compliance without inspecting the actual diff.** The "SRP: PASS" written from memory of the plan rather than from looking at what actually got written. See Principle theatre in `review-checklist.md`.

---

## 2. Overengineering: the check before adding anything

Before introducing a new abstraction, interface, service, microservice, event, queue, cache, repository layer, design pattern, dependency, or configuration system, answer all five:

1. What current, stated requirement makes this necessary?
2. What concrete problem does it solve — not a class of problems in the abstract, the actual one in front of you?
3. Does the repository already have a simpler mechanism that does this?
4. Would a direct implementation be easier for the next person (or agent) to understand and maintain?
5. Are you solving a real requirement, or a plausible-sounding future one nobody has actually asked for?

If the honest answers are weak, build the simpler thing. A single extra `if` statement is almost always cheaper than a new abstraction layer, and it's much easier to introduce the abstraction later — once you actually have the second case that justifies it — than to unwind one that was built on a guess.

Overengineering rarely announces itself as excess. It shows up dressed as good practice: "this should be configurable" (for a value that has one caller and no stated reason to vary), "let's make this a plugin architecture" (for a feature with one implementation and no second one in sight), "we should abstract the database layer" (in an app with one database and no migration planned). Each of these might be right in a different context — the question is always whether *this* context actually has the requirement, not whether the pattern is generally good practice.

## 3. Underengineering: when "simple" is actually just broken

KISS and YAGNI are correct principles that get abused as cover for cutting a corner that shouldn't be cut. A simple implementation is not automatically a *good* one. Watch for a "simple" shortcut that actually produces:

- **Duplicated business rules** that will now drift out of sync the first time one copy gets updated and the other doesn't.
- **A security gap** — an auth check skipped "for now," input trusted without validation, a secret handled in plaintext because encrypting it felt like overhead for a small feature.
- **Fragile coupling dressed up as simplicity** — two modules reaching directly into each other's internals because building a proper interface felt like unnecessary ceremony.
- **Untestable code** — logic wired so tightly to a framework, a database, or a global that it can't be exercised without standing up the whole system.
- **Uncontrolled side effects** — a function that quietly mutates shared state or fires a network call as a side effect of something that looks like a pure computation.
- **Data-integrity risk** — skipping a transaction boundary or a validation step because handling it "properly" seemed like more code than the feature warranted.
- **A large future change cost hiding behind a small present one** — a hardcoded value or copy-pasted block that's cheap today and expensive to unwind once it's spread to ten call sites.
- **Unclear ownership** — logic placed wherever was convenient to write rather than where it logically belongs, so the next person doesn't know where to look for it.
- **Inappropriate cross-layer access** — a UI component querying the database directly because wiring it through the existing service layer felt like extra steps.

The test isn't "how little code did this take." It's "appropriate simplicity" — the least complexity that doesn't create one of the problems above. When KISS and safety point in different directions, safety wins; see the conflict-priority order in the main skill.
