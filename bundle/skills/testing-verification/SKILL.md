---
name: testing-verification
description: Prove that newly implemented, changed, or fixed software behaviour satisfies its requirements and acceptance criteria using risk-proportionate test design, execution, traceability, and evidence. Use when building or changing executable behaviour, fixing bugs, designing or running tests, investigating test failures, assessing test quality, or conducting a standalone verification audit. Do not use for purely informational or documentation-only work with no executable behaviour change.
---

# Testing & Verification

## Mission

Answer one question: **Does the requested behaviour work correctly according to its requirements and acceptance criteria?**

Own prospective correctness: derive what must be true, select proportionate tests, create tests when authorized, execute them, interpret results, identify gaps, and issue an evidence-backed verdict. Never turn `UNKNOWN`, `NOT RUN`, `UNAVAILABLE`, or `NOT VERIFIED` into `PASS`.

## Boundaries

- Consume requirements and design context, but derive expected behaviour independently of the implementation.
- Verify new or changed behaviour. Hand the broader question "what previously worked and might have broken?" to `regression-protection`.
- Exercise functional authentication and authorization behaviour, but hand adversarial analysis and security posture judgments to the appropriate security skill.
- Execute performance, resilience, migration, or recovery checks when they are needed to prove a requirement; hand operational interpretation to `production-readiness`.
- Produce evidence and suggested gates. `ci-cd-delivery-governance` decides pipeline orchestration, required checks, and merge or deployment authority.
- Define adequate smoke checks. CI/CD decides when they run and enforces their results.
- Prepare UAT scenarios and record human results; never fabricate human acceptance.

Read [boundaries-and-handoffs.md](references/boundaries-and-handoffs.md) when another governance capability is implicated.

## Workflow

### 1. Establish the verification contract

Before inspecting implementation details, determine:

- requested behaviour and explicit non-goals;
- acceptance criteria and their source;
- valid inputs, outputs, boundaries, failure behaviour, permissions, state transitions, and side effects;
- external dependencies and representative environments;
- ambiguities or contradictions that prevent a reliable expected result.

Assign stable criterion IDs such as `AC-01`. Mark inferred criteria as inferred; do not silently promote them to confirmed requirements. Every material criterion must map to evidence or an explicit gap.

For a bug, establish the reported failure and intended result first. Prefer `reproduce -> failing test for the right reason -> fix -> pass -> regression handoff`.

### 2. Discover the repository before choosing tools

Read repository instructions, inspect its structure, technology, existing tests, fixtures, helpers, coverage configuration, CI commands, required services, and environment assumptions. Prefer canonical project commands and the existing test stack. Do not introduce a second framework merely because it is familiar. If an essential capability is missing, report the gap before materially changing tooling.

### 3. Classify risk and testable behaviours

Use the project's existing risk taxonomy when available. Otherwise make a concise `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` classification based on consequence and verification difficulty: money, sensitive data, auth or tenant isolation, irreversible mutation, shared contracts, concurrency, asynchronous work, external systems, blast radius, reversibility, and regulatory or safety impact.

Translate each criterion into observable behaviours, including the important happy path, negative and error paths, boundaries, state changes, permissions, side effects, and integration seams. Read [risk-and-strategy.md](references/risk-and-strategy.md) to select the cheapest reliable evidence at suitable depth.

### 4. Design an explicit strategy

For each behaviour, choose the test level and design technique that can actually prove it. Record a short rationale for material choices and important omissions: why unit, integration, API, component, contract, system, E2E, manual, exploratory, performance, or resilience evidence is or is not needed.

Avoid mechanically applying every test type. Read [test-design-and-domains.md](references/test-design-and-domains.md) for boundaries, state machines, decision tables, databases, APIs, frontends, accessibility, asynchronous flows, time, concurrency, and specialized assurance.

Before writing tests, check that they will fail when the required behaviour is absent or wrong. Do not mirror implementation logic, mock away the subject, or assert only that code ran.

### 5. Implement and execute safely

Create or modify tests only when the task authorizes implementation. Follow repository conventions and produce readable, deterministic, behaviour-focused tests with diagnostic failures.

Before any execution with payments, messages, third-party APIs, production data, destructive migrations, or other external mutation, establish a safe test environment and authorization. Prefer synthetic fixtures, disposable records, and provider sandboxes. If safe execution cannot be established, stop that check and classify the outcome honestly.

Run focused, cheap checks before broader or expensive checks when this preserves the required evidence; let risk override the order. Parallelize only independent tests with isolated state and attributable results. Read [execution-and-diagnosis.md](references/execution-and-diagnosis.md) for execution records, test isolation, flaky results, failure diagnosis, and safe test mutation.

### 6. Interpret results without green-at-all-costs behavior

Classify results as `PASS`, `FAIL`, `SKIPPED`, `FLAKY`, `BLOCKED`, `NOT RUN`, `NOT APPLICABLE`, or `INFRASTRUCTURE FAILURE`. When a test fails, distinguish product defect, test defect, requirement mismatch, test-data problem, configuration or environment failure, external dependency failure, flake, infrastructure failure, and unknown before editing either code or test.

Never delete, skip, loosen, overwrite snapshots, change expected output, add broad mocks, or retry indefinitely merely to obtain green status. A test changed with the implementation needs a reason: additive/legitimate, suspicious weakening, or unresolved ambiguity. A fail-then-pass retry remains flaky evidence, not a clean pass.

Keep these states distinct: lint clean, type-check clean, build successful, tests passing, deployment successful, application healthy, and user journey verified. Review findings and coverage percentages are supporting signals, not execution proof.

### 7. Assess completeness and issue a verdict

Build the traceability chain:

`requirement -> acceptance criterion -> test -> execution -> observed result -> evidence`

Assess whether material criteria, negative paths, boundaries, integrations, state and side effects were actually exercised at a depth proportionate to risk. Report mocks, skipped or unrun checks, environment limits, flaky tests, unavailable dependencies, manual checks, and weak assertions. Coverage shows execution, not correctness.

Use exactly one final verdict:

- `PASS`: sufficient observed evidence demonstrates all material acceptance criteria at risk-appropriate depth, with no unresolved material failure or gap.
- `FAIL`: observed evidence contradicts a material criterion or a required test fails because of the product.
- `BLOCKED`: required evidence cannot currently be obtained because safe execution, tooling, permissions, environment, or dependencies are unavailable.
- `INSUFFICIENT EVIDENCE`: available evidence does not justify pass or fail, including material untested, skipped, flaky, weakly asserted, or over-mocked behaviour.
- `NOT APPLICABLE`: no executable behaviour requires verification; explain why.

When both failure and missing evidence exist, use `FAIL` if the observed failure already disproves correctness; otherwise select the verdict that most accurately describes the limiting condition. Do not average criteria into a score.

Read [evidence-and-verdicts.md](references/evidence-and-verdicts.md) and use its report contract for meaningful work. For machine-readable evidence, use its JSON shape and optionally run `python scripts/validate_evidence.py <evidence.json>`.

## Completion test

Before claiming completion, be able to answer: what behaviour was proved; which criteria define success; what could go wrong; why the selected levels were appropriate; which negative and boundary cases ran; exactly what passed, failed, skipped, or did not run; where it ran; whether mocks hide an important boundary; whether coverage is meaningful; which material behaviour remains unverified; what evidence supports the verdict; and what must be handed to Regression Protection, Security, Production Readiness, CI/CD, or a human.

If any material answer is only assumed, it cannot support `PASS`.


## Visual design integration

For diagram authoring, review, or consumption, read [visual-routing.md](references/visual-routing.md) and the shared contract it references. Scale diagrams to the change. Preserve existing approval gates.
