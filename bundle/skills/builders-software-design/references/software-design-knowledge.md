# Pillar 2 — Software Engineering & Software Design Principles

Status: Canonical component specification v1.0  
Research provenance: recovered Builders Academy pillar research; authoritative source register refreshed 31 August 2026.  
Component count: 30

Each entry is retrieval-ready and may be used to generate study notes, slides, coach notes, labs, assignments, co-tutor prompts, assessments, project applications and governance assets. The “Recovered research synthesis” preserves the non-generic source context; the structured fields make it operational.

## P2-C01 — Simplicity

**Classification:** Must Know

**Core Principle:** This should probably be our first principle.

**Why It Matters:** Students need KISS and YAGNI , but practically rather than academically. AI coding agents can over-engineer remarkably quickly.

**Production Problem Solved:** Prevents AI-generated code from turning simplicity into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- This should probably be our first principle.
- Students need KISS and YAGNI , but practically rather than academically.
- AI coding agents can over-engineer remarkably quickly.

**Practical Mental Model:** Build the simplest solution that correctly solves today's known problem while leaving reasonable room for change.

**Student Decision Questions:**

- What user or production requirement makes simplicity necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add simplicity” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Simplicity decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Simplicity to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a simplicity decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

This should probably be our first principle.

Students need **KISS** and **YAGNI**, but practically rather than academically.

AI coding agents can over-engineer remarkably quickly. Google specifically cautions reviewers against unnecessary complexity and implementing speculative future requirements. UK Government engineering guidance similarly recommends avoiding premature optimisation and keeping code understandable. 

Our rule:

> **Build the simplest solution that correctly solves today's known problem while leaving reasonable room for change.**

The student should be able to challenge an agent:

**Why do we need this abstraction/service/library right now?**

</details>

---

## P2-C02 — Separation of Concerns

**Classification:** Must Know

**Core Principle:** Authentication should not be mixed with payment processing.

**Why It Matters:** UI rendering should not contain database logic. Email sending should not be scattered across unrelated components.

**Production Problem Solved:** Prevents AI-generated code from turning separation of concerns into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Authentication should not be mixed with payment processing.
- UI rendering should not contain database logic.
- Email sending should not be scattered across unrelated components.

**Practical Mental Model:** Treat Separation of Concerns as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes separation of concerns necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add separation of concerns” without requirements, constraints, acceptance evidence or review triggers.
- Authentication should not be mixed with payment processing.
- UI rendering should not contain database logic.

**AI-Building Implications:** Make the Separation of Concerns decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Separation of Concerns to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a separation of concerns decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C22 Deployments and Change Safety; P5-C07 Pagination, Filtering, Sorting & Search

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [API-05](source-register.md#api-05)

<details><summary>Recovered research synthesis</summary>

Authentication should not be mixed with payment processing. UI rendering should not contain database logic. Email sending should not be scattered across unrelated components.

ACM identifies separation of concerns as a core software-design principle. 

Students need to recognise:

**"This component is doing too many unrelated things."**

</details>

---

## P2-C03 — Modularity

**Classification:** Must Know

**Core Principle:** Break the application into understandable units with clear responsibilities and boundaries.

**Why It Matters:** Think: Users | Payments | Orders | Notifications | Search rather than: 500 files with unclear relationships. Maintainable modular code makes systems easier to understand, modify and reuse.

**Production Problem Solved:** Prevents AI-generated code from turning modularity into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Break the application into understandable units with clear responsibilities and boundaries.
- Think: Users | Payments | Orders | Notifications | Search rather than: 500 files with unclear relationships.
- Maintainable modular code makes systems easier to understand, modify and reuse.

**Practical Mental Model:** Treat Modularity as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes modularity necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add modularity” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Modularity decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Modularity to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a modularity decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Break the application into understandable units with clear responsibilities and boundaries.

Think:

**Users | Payments | Orders | Notifications | Search**

rather than:

**500 files with unclear relationships.**

Maintainable modular code makes systems easier to understand, modify and reuse. 

This becomes extremely important when an AI agent needs to modify only one part of a large application.

</details>

---

## P2-C04 — High Cohesion, Low Coupling

**Classification:** Must Know

**Core Principle:** This may sound technical, but we can teach it very simply.

**Why It Matters:** Cohesion: Things that belong together should live together. Coupling: Things that don't need to know about each other shouldn't depend heavily on each other.

**Production Problem Solved:** Prevents AI-generated code from turning high cohesion, low coupling into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- This may sound technical, but we can teach it very simply.
- Cohesion: Things that belong together should live together.
- Coupling: Things that don't need to know about each other shouldn't depend heavily on each other.

**Practical Mental Model:** If I change Feature A, how many unrelated things break?

**Student Decision Questions:**

- What user or production requirement makes high cohesion, low coupling necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add high cohesion, low coupling” without requirements, constraints, acceptance evidence or review triggers.
- Coupling: Things that don't need to know about each other shouldn't depend heavily on each other.

**AI-Building Implications:** Make the High Cohesion, Low Coupling decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply High Cohesion, Low Coupling to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a high cohesion, low coupling decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C03 High-Level Architecture; P1-C09 Scalability; P1-C15 Overload Protection; P1-C17 API Security

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

This may sound technical, but we can teach it very simply.

**Cohesion:** Things that belong together should live together.

**Coupling:** Things that don't need to know about each other shouldn't depend heavily on each other.

ACM explicitly identifies coupling and cohesion as fundamental design principles. 

The practical test:

> **If I change Feature A, how many unrelated things break?**

</details>

---

## P2-C05 — Encapsulation & Information Hiding

**Classification:** Must Know

**Core Principle:** A component should expose what other components need while hiding unnecessary implementation details.

**Why It Matters:** The student doesn't need computer-science lectures on encapsulation. They need to understand: "Other parts of my application should depend on the contract, not all the internal machinery." This makes future replacement and refactoring much easier.

**Production Problem Solved:** Prevents AI-generated code from turning encapsulation & information hiding into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- A component should expose what other components need while hiding unnecessary implementation details.
- The student doesn't need computer-science lectures on encapsulation.
- They need to understand: "Other parts of my application should depend on the contract, not all the internal machinery." This makes future replacement and refactoring much easier.

**Practical Mental Model:** Treat Encapsulation & Information Hiding as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes encapsulation & information hiding necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add encapsulation & information hiding” without requirements, constraints, acceptance evidence or review triggers.
- They need to understand: "Other parts of my application should depend on the contract, not all the internal machinery." This makes future replacement and refactoring much easier.

**AI-Building Implications:** Make the Encapsulation & Information Hiding decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Encapsulation & Information Hiding to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a encapsulation & information hiding decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P3-C03 Information Architecture; P1-C12 Concurrency, Consistency and Data Integrity; P1-C15 Overload Protection; P1-C16 Security Architecture

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

A component should expose what other components need while hiding unnecessary implementation details.

The student doesn't need computer-science lectures on encapsulation.

They need to understand:

**"Other parts of my application should depend on the contract, not all the internal machinery."**

This makes future replacement and refactoring much easier.

</details>

---

## P2-C06 — Abstraction

**Classification:** Must Know

**Core Principle:** Students need to understand when abstraction helps and when it becomes unnecessary complexity.

**Why It Matters:** Bad AI-assisted development often creates either: no abstraction , resulting in duplication, or too much abstraction , resulting in code nobody understands. The principle becomes: Abstract repeated concepts when doing so genuinely makes the system easier to change.

**Production Problem Solved:** Prevents AI-generated code from turning abstraction into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Students need to understand when abstraction helps and when it becomes unnecessary complexity.
- Bad AI-assisted development often creates either: no abstraction , resulting in duplication, or too much abstraction , resulting in code nobody understands.
- The principle becomes: Abstract repeated concepts when doing so genuinely makes the system easier to change.

**Practical Mental Model:** Abstract repeated concepts when doing so genuinely makes the system easier to change.

**Student Decision Questions:**

- What user or production requirement makes abstraction necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Consistency and reuse versus abstraction overhead and the risk of generalising before patterns are stable.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add abstraction” without requirements, constraints, acceptance evidence or review triggers.
- Not because abstraction sounds sophisticated.

**AI-Building Implications:** Make the Abstraction decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Abstraction to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a abstraction decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Students need to understand when abstraction helps and when it becomes unnecessary complexity.

Bad AI-assisted development often creates either:

**no abstraction**, resulting in duplication,

or

**too much abstraction**, resulting in code nobody understands.

The principle becomes:

> **Abstract repeated concepts when doing so genuinely makes the system easier to change.**

Not because abstraction sounds sophisticated.

</details>

---

## P2-C07 — DRY, But Not Blindly

**Classification:** Must Know

**Core Principle:** But students should not instruct an agent to remove every repeated line.

**Why It Matters:** Sometimes duplication is clearer than forcing unrelated things into one abstraction. The deeper principle is: Avoid duplicating important knowledge and business rules.

**Production Problem Solved:** Prevents AI-generated code from turning dry, but not blindly into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- But students should not instruct an agent to remove every repeated line.
- Sometimes duplication is clearer than forcing unrelated things into one abstraction.
- The deeper principle is: Avoid duplicating important knowledge and business rules.

**Practical Mental Model:** Treat DRY, But Not Blindly as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes dry, but not blindly necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Consistency and reuse versus abstraction overhead and the risk of generalising before patterns are stable.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add dry, but not blindly” without requirements, constraints, acceptance evidence or review triggers.
- But students should not instruct an agent to remove every repeated line.

**AI-Building Implications:** Make the DRY, But Not Blindly decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply DRY, But Not Blindly to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a dry, but not blindly decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C09 Scalability; P1-C19 Observability; P3-C28 Screen Reader Semantics; P3-C46 Aesthetic Quality

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

**Don't Repeat Yourself.**

But students should not instruct an agent to remove every repeated line.

Sometimes duplication is clearer than forcing unrelated things into one abstraction.

The deeper principle is:

**Avoid duplicating important knowledge and business rules.**

If the VAT calculation exists in six locations, eventually one will behave differently.

</details>

---

## P2-C08 — SOLID

**Classification:** Should Know

**Core Principle:** I would not teach Builders Academy as a SOLID memorisation exercise .

**Why It Matters:** Students should understand the ideas behind it: Single responsibility. Extensibility without constantly rewriting stable code.

**Production Problem Solved:** Prevents AI-generated code from turning solid into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- I would not teach Builders Academy as a SOLID memorisation exercise .
- Students should understand the ideas behind it: Single responsibility.
- Extensibility without constantly rewriting stable code.

**Practical Mental Model:** Treat SOLID as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes solid necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Consistency and reuse versus abstraction overhead and the risk of generalising before patterns are stable.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add solid” without requirements, constraints, acceptance evidence or review triggers.
- I would not teach Builders Academy as a SOLID memorisation exercise .

**AI-Building Implications:** Make the SOLID decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply SOLID to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a solid decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

I would **not teach Builders Academy as a SOLID memorisation exercise**.

Students should understand the ideas behind it:

Single responsibility.

Extensibility without constantly rewriting stable code.

Safe substitutability.

Small purposeful interfaces.

Depending on contracts rather than unnecessary implementation details.

But always through product examples.

</details>

---

## P2-C09 — Clear Interfaces & Contracts

**Classification:** Must Know

**Core Principle:** Modules need predictable ways of communicating.

**Why It Matters:** That includes function signatures, APIs, events, schemas, expected inputs/outputs and error behaviour. Microsoft's current architecture guidance similarly recommends well-defined APIs, encapsulation and loose coupling to allow components to evolve independently.

**Production Problem Solved:** Prevents AI-generated code from turning clear interfaces & contracts into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Modules need predictable ways of communicating.
- That includes function signatures, APIs, events, schemas, expected inputs/outputs and error behaviour.
- Microsoft's current architecture guidance similarly recommends well-defined APIs, encapsulation and loose coupling to allow components to evolve independently.

**Practical Mental Model:** Treat Clear Interfaces & Contracts as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes clear interfaces & contracts necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add clear interfaces & contracts” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Clear Interfaces & Contracts decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Clear Interfaces & Contracts to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a clear interfaces & contracts decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C05 API Contracts; P5-C36 Integration Contracts & Schema Validation; P1-C03 High-Level Architecture; P1-C06 API and Communication Design

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Modules need predictable ways of communicating.

That includes function signatures, APIs, events, schemas, expected inputs/outputs and error behaviour.

Microsoft's current architecture guidance similarly recommends well-defined APIs, encapsulation and loose coupling to allow components to evolve independently.

</details>

---

## P2-C10 — Naming & Readability

**Classification:** Must Know

**Core Principle:** AI can generate code extremely quickly, which makes readability even more important.

**Why It Matters:** Names should communicate intent. Google explicitly treats naming, readability, comments, complexity and overall design as code-review concerns.

**Production Problem Solved:** Prevents AI-generated code from turning naming & readability into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- AI can generate code extremely quickly, which makes readability even more important.
- Names should communicate intent.
- Google explicitly treats naming, readability, comments, complexity and overall design as code-review concerns.

**Practical Mental Model:** Treat Naming & Readability as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes naming & readability necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add naming & readability” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Naming & Readability decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Naming & Readability to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a naming & readability decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P3-C07 Typography; P4-C04 Persistent Project Instructions; P4-C31 Repository as Agent Context

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

AI can generate code extremely quickly, which makes readability even more important.

Names should communicate intent.

Google explicitly treats naming, readability, comments, complexity and overall design as code-review concerns. 

Compare:

`processData()`

with:

`calculateMonthlySubscriptionRevenue()`

A future agent also benefits from descriptive code because **the codebase itself becomes context for the agent**.

</details>

---

## P2-C11 — Code Organisation

**Classification:** Must Know

**Core Principle:** Students need conventions for: folders, modules, components, services, utilities, types, tests, configuration, database code, API code, and shared code.

**Why It Matters:** More importantly: The project needs a predictable structure that the AI agent understands and consistently follows.

**Production Problem Solved:** Prevents AI-generated code from turning code organisation into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Students need conventions for: folders, modules, components, services, utilities, types, tests, configuration, database code, API code, and shared code.
- More importantly: The project needs a predictable structure that the AI agent understands and consistently follows.

**Practical Mental Model:** The project needs a predictable structure that the AI agent understands and consistently follows.

**Student Decision Questions:**

- What user or production requirement makes code organisation necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add code organisation” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Code Organisation decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Code Organisation to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a code organisation decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C24 Code Review; P2-C28 Refactoring Patterns & Code Smells; P1-C02 Capacity Estimation and Workload Understanding; P1-C06 API and Communication Design

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Students need conventions for:

folders,

modules,

components,

services,

utilities,

types,

tests,

configuration,

database code,

API code,

and shared code.

More importantly:

> **The project needs a predictable structure that the AI agent understands and consistently follows.**

</details>

---

## P2-C12 — Single Source of Truth

**Classification:** Must Know

**Core Principle:** One concept should not have five competing definitions.

**Why It Matters:** If subscription plans are defined in five places, AI can easily update four and forget one. Students should constantly ask: Where is the authoritative definition of this information?

**Production Problem Solved:** Prevents AI-generated code from turning single source of truth into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- One concept should not have five competing definitions.
- If subscription plans are defined in five places, AI can easily update four and forget one.
- Students should constantly ask: Where is the authoritative definition of this information?

**Practical Mental Model:** Treat Single Source of Truth as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes single source of truth necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add single source of truth” without requirements, constraints, acceptance evidence or review triggers.
- One concept should not have five competing definitions.

**AI-Building Implications:** Make the Single Source of Truth decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Single Source of Truth to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a single source of truth decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C04 Data Architecture; P1-C13 Availability; P1-C17 API Security; P1-C26 Multi-tenancy

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

One concept should not have five competing definitions.

If subscription plans are defined in five places, AI can easily update four and forget one.

Students should constantly ask:

**Where is the authoritative definition of this information?**

</details>

---

## P2-C13 — State Management

**Classification:** Must Know

**Core Principle:** Students need a conceptual understanding of: local state, shared application state, server state, persistent state, session state, and cached state.

**Why It Matters:** The key question is: Who owns this state, and where is its source of truth?

**Production Problem Solved:** Prevents AI-generated code from turning state management into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Students need a conceptual understanding of: local state, shared application state, server state, persistent state, session state, and cached state.
- The key question is: Who owns this state, and where is its source of truth?

**Practical Mental Model:** Who owns this state, and where is its source of truth?

**Student Decision Questions:**

- What user or production requirement makes state management necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add state management” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the State Management decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply State Management to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a state management decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C10 Load Balancing and Traffic Management; P2-C17 Dependency Management; P4-C25 Context Window Management; P4-C34 Cost Management

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Students need a conceptual understanding of:

local state,

shared application state,

server state,

persistent state,

session state,

and cached state.

The key question is:

> **Who owns this state, and where is its source of truth?**

</details>

---

## P2-C14 — Error Handling

**Classification:** Must Know

**Core Principle:** AI-generated applications frequently optimise for the happy path.

**Why It Matters:** Students need predictable approaches for validation errors, network failures, database failures, external API failures, permission failures and unexpected failures. Errors should be: detected → classified → logged → communicated → recovered from where possible.

**Production Problem Solved:** Prevents AI-generated code from turning error handling into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- AI-generated applications frequently optimise for the happy path.
- Students need predictable approaches for validation errors, network failures, database failures, external API failures, permission failures and unexpected failures.
- Errors should be: detected → classified → logged → communicated → recovered from where possible.

**Practical Mental Model:** Treat Error Handling as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes error handling necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add error handling” without requirements, constraints, acceptance evidence or review triggers.
- Students need predictable approaches for validation errors, network failures, database failures, external API failures, permission failures and unexpected failures.

**AI-Building Implications:** Make the Error Handling decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Error Handling to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a error handling decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P3-C16 Error States; P3-C17 Error Prevention; P3-C45 Error Copy; P3-C37 Trust Design

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

AI-generated applications frequently optimise for the happy path.

Students need predictable approaches for validation errors, network failures, database failures, external API failures, permission failures and unexpected failures.

Errors should be:

**detected → classified → logged → communicated → recovered from where possible.**

</details>

---

## P2-C15 — Defensive Programming

**Classification:** Must Know

**Core Principle:** Never assume: the API responds, the user provides valid data, the database record exists, the network remains connected, the uploaded file is safe, or the third-party response has exactly the expected structure.

**Why It Matters:** This connects directly with our System Design reliability work.

**Production Problem Solved:** Prevents AI-generated code from turning defensive programming into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Never assume: the API responds, the user provides valid data, the database record exists, the network remains connected, the uploaded file is safe, or the third-party response has exactly the expected structure.
- This connects directly with our System Design reliability work.

**Practical Mental Model:** Treat Defensive Programming as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes defensive programming necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add defensive programming” without requirements, constraints, acceptance evidence or review triggers.
- Never assume: the API responds, the user provides valid data, the database record exists, the network remains connected, the uploaded file is safe, or the third-party response has exactly the expected structure.

**AI-Building Implications:** Make the Defensive Programming decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Defensive Programming to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a defensive programming decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SYS-03](source-register.md#sys-03), [SYS-04](source-register.md#sys-04)

<details><summary>Recovered research synthesis</summary>

Never assume:

the API responds,

the user provides valid data,

the database record exists,

the network remains connected,

the uploaded file is safe,

or the third-party response has exactly the expected structure.

This connects directly with our System Design reliability work.

</details>

---

## P2-C16 — Configuration & Secrets

**Classification:** Must Know

**Core Principle:** Configuration should not be buried throughout source code.

**Why It Matters:** Students need: environment variables, configuration separation, development/staging/production configuration, secret handling, and feature configuration. The Twelve-Factor App specifically recommends explicit dependency declaration, environment-based configuration, separation of build/release/run and treating backing services as attached resources.

**Production Problem Solved:** Prevents AI-generated code from turning configuration & secrets into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Configuration should not be buried throughout source code.
- Students need: environment variables, configuration separation, development/staging/production configuration, secret handling, and feature configuration.
- The Twelve-Factor App specifically recommends explicit dependency declaration, environment-based configuration, separation of build/release/run and treating backing services as attached resources.

**Practical Mental Model:** Treat Configuration & Secrets as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes configuration & secrets necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add configuration & secrets” without requirements, constraints, acceptance evidence or review triggers.
- Configuration should not be buried throughout source code.

**AI-Building Implications:** Make the Configuration & Secrets decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Configuration & Secrets to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a configuration & secrets decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C27 Secrets Security; P1-C16 Security Architecture; P1-C22 Deployments and Change Safety; P1-C26 Multi-tenancy

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SEC-01](source-register.md#sec-01), [SEC-02](source-register.md#sec-02)

<details><summary>Recovered research synthesis</summary>

Configuration should not be buried throughout source code.

Students need:

environment variables,

configuration separation,

development/staging/production configuration,

secret handling,

and feature configuration.

The Twelve-Factor App specifically recommends explicit dependency declaration, environment-based configuration, separation of build/release/run and treating backing services as attached resources.

</details>

---

## P2-C17 — Dependency Management

**Classification:** Must Know

**Core Principle:** Every package creates a dependency.

**Why It Matters:** Students need to ask: Do we actually need this library? What happens if it changes?

**Production Problem Solved:** Prevents AI-generated code from turning dependency management into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Every package creates a dependency.
- Students need to ask: Do we actually need this library?
- What happens if it changes?

**Practical Mental Model:** Treat Dependency Management as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- Do we actually need this library?
- Is it maintained?
- What happens if it changes?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add dependency management” without requirements, constraints, acceptance evidence or review triggers.
- AI agents should not casually install packages merely to solve tiny problems.

**AI-Building Implications:** Make the Dependency Management decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Dependency Management to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a dependency management decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C31 Dependency Security; P1-C10 Load Balancing and Traffic Management; P2-C13 State Management; P4-C25 Context Window Management

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SEC-01](source-register.md#sec-01), [SEC-02](source-register.md#sec-02)

<details><summary>Recovered research synthesis</summary>

Every package creates a dependency.

Students need to ask:

**Do we actually need this library?**

**Is it maintained?**

**What happens if it changes?**

**Are we locking versions?**

**Does it introduce security risk?**

AI agents should not casually install packages merely to solve tiny problems.

</details>

---

## P2-C18 — Secure-by-Design Software

**Classification:** Must Know

**Core Principle:** Security cannot exist only in our security module.

**Why It Matters:** OWASP's Secure-by-Design framework explicitly recommends integrating security into architecture and design before implementation, including least privilege, defence in depth, secure defaults, explicit trust boundaries and safe failure. This should influence how students structure software from the beginning.

**Production Problem Solved:** Prevents AI-generated code from turning secure-by-design software into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Security cannot exist only in our security module.
- OWASP's Secure-by-Design framework explicitly recommends integrating security into architecture and design before implementation, including least privilege, defence in depth, secure defaults, explicit trust boundaries and safe failure.
- This should influence how students structure software from the beginning.

**Practical Mental Model:** Treat Secure-by-Design Software as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes secure-by-design software necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add secure-by-design software” without requirements, constraints, acceptance evidence or review triggers.
- Security cannot exist only in our security module.
- OWASP's Secure-by-Design framework explicitly recommends integrating security into architecture and design before implementation, including least privilege, defence in depth, secure defaults, explicit trust boundaries and safe failure.

**AI-Building Implications:** Make the Secure-by-Design Software decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Secure-by-Design Software to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a secure-by-design software decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P6-C19 Secure-by-Design

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SEC-01](source-register.md#sec-01), [SEC-02](source-register.md#sec-02)

<details><summary>Recovered research synthesis</summary>

Security cannot exist only in our security module.

OWASP's Secure-by-Design framework explicitly recommends integrating security into architecture and design before implementation, including least privilege, defence in depth, secure defaults, explicit trust boundaries and safe failure. 

This should influence how students structure software from the beginning.

</details>

---

## P2-C19 — Testing as a Design Practice

**Classification:** Must Know

**Core Principle:** Testing isn't merely: "We finished.

**Why It Matters:** Run the tests." Well-designed software is easier to test because components have clear responsibilities and boundaries. Google's engineering guidance expects appropriate unit, integration or end-to-end tests alongside production changes.

**Production Problem Solved:** Prevents AI-generated code from turning testing as a design practice into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Testing isn't merely: "We finished.
- Run the tests." Well-designed software is easier to test because components have clear responsibilities and boundaries.
- Google's engineering guidance expects appropriate unit, integration or end-to-end tests alongside production changes.

**Practical Mental Model:** Specify expected behaviour, create evidence, run the check, inspect failures, then prevent regression.

**Student Decision Questions:**

- What user or production requirement makes testing as a design practice necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** More confidence and safer change versus maintenance cost, execution time and brittle test design.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add testing as a design practice” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Testing as a Design Practice decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Testing as a Design Practice to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a testing as a design practice decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C23 Testing the Architecture; P6-C01 Testing Mindset; P6-C06 Unit Testing; P6-C08 End-to-End Testing

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Testing isn't merely:

**"We finished. Run the tests."**

Well-designed software is easier to test because components have clear responsibilities and boundaries.

Google's engineering guidance expects appropriate unit, integration or end-to-end tests alongside production changes. 

This means **testability itself becomes a software-quality signal**.

</details>

---

## P2-C20 — Refactoring

**Classification:** Must Know

**Core Principle:** This is particularly important for vibe coders.

**Why It Matters:** AI will frequently produce something that works but isn't the structure we want long-term. Refactoring means improving the internal structure without intentionally changing external behaviour .

**Production Problem Solved:** Prevents AI-generated code from turning refactoring into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- This is particularly important for vibe coders.
- AI will frequently produce something that works but isn't the structure we want long-term.
- Refactoring means improving the internal structure without intentionally changing external behaviour .

**Practical Mental Model:** Treat Refactoring as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes refactoring necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add refactoring” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Refactoring decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Refactoring to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a refactoring decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C28 Refactoring Patterns & Code Smells

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

This is particularly important for vibe coders.

AI will frequently produce something that works but isn't the structure we want long-term.

Refactoring means improving the internal structure **without intentionally changing external behaviour**.

Fowler describes regular refactoring as essential to preventing codebase deterioration and sustaining development productivity. 

Students should learn:

**Make it work → verify it → improve the structure → verify again.**

</details>

---

## P2-C21 — Technical Debt

**Classification:** Must Know

**Core Principle:** Not every imperfect decision must be fixed immediately.

**Why It Matters:** Students need to distinguish: intentional shortcut from uncontrolled mess . Fowler's technical-debt metaphor is useful because poor internal structure effectively charges "interest" by making future features harder and slower to implement.

**Production Problem Solved:** Prevents AI-generated code from turning technical debt into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Not every imperfect decision must be fixed immediately.
- Students need to distinguish: intentional shortcut from uncontrolled mess .
- Fowler's technical-debt metaphor is useful because poor internal structure effectively charges "interest" by making future features harder and slower to implement.

**Practical Mental Model:** Treat Technical Debt as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes technical debt necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add technical debt” without requirements, constraints, acceptance evidence or review triggers.
- Not every imperfect decision must be fixed immediately.

**AI-Building Implications:** Make the Technical Debt decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Technical Debt to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a technical debt decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C25 Architecture Evolution and Maintainability; P1-C01 Requirements and System Boundaries; P1-C24 Cost Architecture; P3-C35 Perceived Performance

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [API-01](source-register.md#api-01), [API-02](source-register.md#api-02)

<details><summary>Recovered research synthesis</summary>

Not every imperfect decision must be fixed immediately.

Students need to distinguish:

**intentional shortcut**

from

**uncontrolled mess**.

Fowler's technical-debt metaphor is useful because poor internal structure effectively charges "interest" by making future features harder and slower to implement. 

Builders Academy students should maintain a simple **Technical Debt Register**.

</details>

---

## P2-C22 — Version Control & Git

**Classification:** Must Know

**Core Principle:** This deserves serious attention for AI builders.

**Why It Matters:** Students need: commits, branches, pull requests, diffs, merge conflicts, reverting, tags/releases, and understanding exactly what changed. The most important behaviour is: Never allow an AI agent to make huge uncontrolled changes without creating recoverable checkpoints.

**Production Problem Solved:** Prevents AI-generated code from turning version control & git into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- This deserves serious attention for AI builders.
- Students need: commits, branches, pull requests, diffs, merge conflicts, reverting, tags/releases, and understanding exactly what changed.
- The most important behaviour is: Never allow an AI agent to make huge uncontrolled changes without creating recoverable checkpoints.

**Practical Mental Model:** Never allow an AI agent to make huge uncontrolled changes without creating recoverable checkpoints.

**Student Decision Questions:**

- What user or production requirement makes version control & git necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add version control & git” without requirements, constraints, acceptance evidence or review triggers.
- The most important behaviour is: Never allow an AI agent to make huge uncontrolled changes without creating recoverable checkpoints.

**AI-Building Implications:** Make the Version Control & Git decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Version Control & Git to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a version control & git decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P3-C18 User Control & Freedom; P4-C12 Tool Calling; P4-C17 Permissions; P1-C05 Storage Architecture

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SE-02](source-register.md#se-02)

<details><summary>Recovered research synthesis</summary>

This deserves serious attention for AI builders.

Students need:

commits,

branches,

pull requests,

diffs,

merge conflicts,

reverting,

tags/releases,

and understanding exactly what changed.

The most important behaviour is:

> **Never allow an AI agent to make huge uncontrolled changes without creating recoverable checkpoints.**

</details>

---

## P2-C23 — Small Changes

**Classification:** Must Know

**Core Principle:** This is one of the strongest findings for AI-assisted development.

**Why It Matters:** Google recommends small, self-contained changes because they are easier to understand, review, test, merge and roll back, and less likely to introduce bugs. For Builders Academy: Plan → small task → AI implements → inspect diff → test → commit → next task.

**Production Problem Solved:** Prevents AI-generated code from turning small changes into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- This is one of the strongest findings for AI-assisted development.
- Google recommends small, self-contained changes because they are easier to understand, review, test, merge and roll back, and less likely to introduce bugs.
- For Builders Academy: Plan → small task → AI implements → inspect diff → test → commit → next task.

**Practical Mental Model:** Treat Small Changes as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes small changes necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add small changes” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Small Changes decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Small Changes to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a small changes decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P4-C06 Task Decomposition; P4-C35 Model Selection; P1-C18 Third-Party Dependencies; P3-C43 UX Writing

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

This is one of the strongest findings for AI-assisted development.

Google recommends small, self-contained changes because they are easier to understand, review, test, merge and roll back, and less likely to introduce bugs. 

For Builders Academy:

**Plan → small task → AI implements → inspect diff → test → commit → next task.**

Not:

**"Claude, build my entire marketplace."**

This could become a fundamental Builders Academy workflow.

</details>

---

## P2-C24 — Code Review

**Classification:** Must Know

**Core Principle:** Even if the "developer" is an AI agent, someone must review the work.

**Why It Matters:** Google's review guidance asks reviewers to examine design, functionality, complexity, tests, naming, comments and whether the change improves or degrades overall code health. For our students: AI-generated code is a proposal until it has been reviewed and verified.

**Production Problem Solved:** Prevents AI-generated code from turning code review into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Even if the "developer" is an AI agent, someone must review the work.
- Google's review guidance asks reviewers to examine design, functionality, complexity, tests, naming, comments and whether the change improves or degrades overall code health.
- For our students: AI-generated code is a proposal until it has been reviewed and verified.

**Practical Mental Model:** AI-generated code is a proposal until it has been reviewed and verified.

**Student Decision Questions:**

- What user or production requirement makes code review necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add code review” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Code Review decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Code Review to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a code review decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C11 Code Organisation; P2-C28 Refactoring Patterns & Code Smells; P4-C10 Sub-agents; P4-C35 Model Selection

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Even if the "developer" is an AI agent, someone must review the work.

Google's review guidance asks reviewers to examine design, functionality, complexity, tests, naming, comments and whether the change improves or degrades overall code health. 

For our students:

> **AI-generated code is a proposal until it has been reviewed and verified.**

That is an important mindset.

</details>

---

## P2-C25 — Documentation

**Classification:** Must Know

**Core Principle:** There are several layers: README, setup instructions, architecture documentation, API contracts, database documentation, business rules, agent instructions, and Architecture Decision Records.

**Why It Matters:** Comments should explain why , particularly where intent isn't obvious.

**Production Problem Solved:** Prevents AI-generated code from turning documentation into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- There are several layers: README, setup instructions, architecture documentation, API contracts, database documentation, business rules, agent instructions, and Architecture Decision Records.
- Comments should explain why , particularly where intent isn't obvious.

**Practical Mental Model:** Treat Documentation as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes documentation necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add documentation” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Documentation decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Documentation to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a documentation decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C06 API Documentation; P1-C30 Architecture Documentation and Decision Records; P4-C05 Planning Before Coding; P4-C08 Building Skills

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [API-04](source-register.md#api-04)

<details><summary>Recovered research synthesis</summary>

There are several layers:

README,

setup instructions,

architecture documentation,

API contracts,

database documentation,

business rules,

agent instructions,

and Architecture Decision Records.

Comments should explain **why**, particularly where intent isn't obvious.

</details>

---

## P2-C26 — Architecture Decision Records

**Classification:** Should Know

**Core Principle:** For important decisions: Decision: Supabase Postgres.

**Why It Matters:** Reason: relational transactional data + managed authentication + RLS. Alternatives considered: Firebase/MongoDB.

**Production Problem Solved:** Prevents AI-generated code from turning architecture decision records into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- For important decisions: Decision: Supabase Postgres.
- Reason: relational transactional data + managed authentication + RLS.
- Alternatives considered: Firebase/MongoDB.

**Practical Mental Model:** Treat Architecture Decision Records as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes architecture decision records necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add architecture decision records” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Architecture Decision Records decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Architecture Decision Records to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a architecture decision records decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P1-C30 Architecture Documentation and Decision Records; P3-C02 User Journeys & Task Flows; P3-C23 Smart Defaults & Autocomplete; P3-C38 Cognitive Load

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [API-05](source-register.md#api-05)

<details><summary>Recovered research synthesis</summary>

For important decisions:

**Decision:** Supabase Postgres.

**Reason:** relational transactional data + managed authentication + RLS.

**Alternatives considered:** Firebase/MongoDB.

**Trade-off:** stronger relational model but tighter platform dependency.

**Review trigger:** database requirements exceed current platform constraints.

This works beautifully with our System Design framework.

</details>

---

## P2-C27 — Design Patterns

**Classification:** Should Know

**Core Principle:** But I strongly recommend: Do not teach a catalogue of patterns.

**Why It Matters:** Teach patterns when students encounter the problem that created the pattern.

**Production Problem Solved:** Prevents AI-generated code from turning design patterns into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- But I strongly recommend: Do not teach a catalogue of patterns.
- Teach patterns when students encounter the problem that created the pattern.

**Practical Mental Model:** Treat Design Patterns as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes design patterns necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Consistency and reuse versus abstraction overhead and the risk of generalising before patterns are stable.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add design patterns” without requirements, constraints, acceptance evidence or review triggers.
- But I strongly recommend: Do not teach a catalogue of patterns.

**AI-Building Implications:** Make the Design Patterns decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Design Patterns to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a design patterns decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C28 Refactoring Patterns & Code Smells; P1-C04 Data Architecture; P3-C11 Design Systems; P4-C11 Agent Orchestration

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SEC-01](source-register.md#sec-01), [SEC-02](source-register.md#sec-02)

<details><summary>Recovered research synthesis</summary>

Repository.

Factory.

Adapter.

Strategy.

Observer.

Dependency injection.

MVC.

etc.

But I strongly recommend:

**Do not teach a catalogue of patterns.**

Teach patterns when students encounter the problem that created the pattern.

</details>

---

## P2-C28 — Refactoring Patterns & Code Smells

**Classification:** Should Know

**Core Principle:** Students should recognise warning signs: giant files, giant functions, duplicated business rules, too many parameters, deep nesting, magic numbers, unused code, unclear names, circular dependencies, god components, and excessive dependencies.

**Why It Matters:** These are especially valuable when auditing AI-generated applications.

**Production Problem Solved:** Prevents AI-generated code from turning refactoring patterns & code smells into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Students should recognise warning signs: giant files, giant functions, duplicated business rules, too many parameters, deep nesting, magic numbers, unused code, unclear names, circular dependencies, god components, and excessive dependen…
- These are especially valuable when auditing AI-generated applications.

**Practical Mental Model:** Treat Refactoring Patterns & Code Smells as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes refactoring patterns & code smells necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** Consistency and reuse versus abstraction overhead and the risk of generalising before patterns are stable.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add refactoring patterns & code smells” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Refactoring Patterns & Code Smells decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Refactoring Patterns & Code Smells to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can recognise, explain and apply with guidance a refactoring patterns & code smells decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P2-C11 Code Organisation; P2-C20 Refactoring; P2-C24 Code Review; P2-C27 Design Patterns

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

Students should recognise warning signs:

giant files,

giant functions,

duplicated business rules,

too many parameters,

deep nesting,

magic numbers,

unused code,

unclear names,

circular dependencies,

god components,

and excessive dependencies.

These are especially valuable when auditing AI-generated applications.

</details>

---

## P2-C29 — Continuous Integration

**Classification:** Must Know

**Core Principle:** Every change should be automatically checked where practical.

**Why It Matters:** Fowler connects CI, automated testing and refactoring directly with maintaining a healthy, evolvable codebase.

**Production Problem Solved:** Prevents AI-generated code from turning continuous integration into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- Every change should be automatically checked where practical.
- Fowler connects CI, automated testing and refactoring directly with maintaining a healthy, evolvable codebase.

**Practical Mental Model:** Treat Continuous Integration as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes continuous integration necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add continuous integration” without requirements, constraints, acceptance evidence or review triggers.
- Every change should be automatically checked where practical.

**AI-Building Implications:** Make the Continuous Integration decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Continuous Integration to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a continuous integration decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** P5-C28 Integration Failure; P5-C36 Integration Contracts & Schema Validation; P5-C39 Integration Testing; P6-C07 Integration Testing

**Authoritative Research Sources:** [SE-01](source-register.md#se-01), [SE-03](source-register.md#se-03), [SEC-01](source-register.md#sec-01), [SEC-02](source-register.md#sec-02)

<details><summary>Recovered research synthesis</summary>

Every change should be automatically checked where practical.

Build.

Lint.

Type check.

Tests.

Security checks.

Fowler connects CI, automated testing and refactoring directly with maintaining a healthy, evolvable codebase.

</details>

---

## P2-C30 — Evolutionary Design

**Classification:** Must Know

**Core Principle:** The application will change.

**Why It Matters:** Microsoft's guidance explicitly recommends designing for evolution through loose coupling, encapsulation, asynchronous communication where appropriate and versioned interfaces. So students should avoid architectures that assume today's requirements will remain forever.

**Production Problem Solved:** Prevents AI-generated code from turning evolutionary design into duplicated, tightly coupled or unsafe implementation that becomes hard to change.

**Concepts to Master:**

- The application will change.
- Microsoft's guidance explicitly recommends designing for evolution through loose coupling, encapsulation, asynchronous communication where appropriate and versioned interfaces.
- So students should avoid architectures that assume today's requirements will remain forever.

**Practical Mental Model:** Treat Evolutionary Design as a decision record: requirement → choice → consequence → evidence → review trigger.

**Student Decision Questions:**

- What user or production requirement makes evolutionary design necessary here?
- What measurable evidence would show that the chosen approach is working?
- At what threshold, failure mode or risk level must the decision be revisited?

**Trade-offs:** The benefit must justify added complexity, cost, maintenance burden and constraints on future change.

**Common Vibe-Coding Failure Patterns:**

- Asking an AI tool to “add evolutionary design” without requirements, constraints, acceptance evidence or review triggers.

**AI-Building Implications:** Make the Evolutionary Design decision explicit in the agent task specification. Require the agent to inspect the current system, preserve existing constraints, produce a small change and return verifiable evidence.

**Practical Application:** Apply Evolutionary Design to one critical user journey. Record the requirement, current state, chosen design, rejected alternative, acceptance check and trigger for revisiting the choice.

**Evidence/Verification:** Evidence must be reproducible: tests, review evidence and a small before/after code-quality comparison. “It worked once” or an AI-generated explanation is not verification.

**Expected Competency:** The student can make, justify and verify a evolutionary design decision for a real product, including assumptions, trade-offs, failure modes and review criteria.

**Relationships to Other Components:** See the pillar index and adjacent production lifecycle components.

**Authoritative Research Sources:** [SE-01](source-register.md#se-01)

<details><summary>Recovered research synthesis</summary>

The application will change.

Microsoft's guidance explicitly recommends designing for evolution through loose coupling, encapsulation, asynchronous communication where appropriate and versioned interfaces. 

So students should avoid architectures that assume today's requirements will remain forever.

</details>

---


