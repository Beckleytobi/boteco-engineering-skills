# Boundaries and Handoffs

## Ownership map

| Capability | Question owned | Testing & Verification interaction |
|---|---|---|
| Requirements/product | What should be built and accepted? | Consume confirmed criteria; expose ambiguity and missing criteria. |
| Software Design Principles | Is the implementation structured well? | Consume boundaries, contracts, state, dependencies, and side effects; preserve an independent expected result. |
| Testing & Verification | Does requested new/changed behaviour work? | Own strategy, tests, execution, traceability, evidence, and verdict. |
| Regression Protection | Did relevant previously-working behaviour remain intact? | Hand off new/changed behaviours, tests, commands, boundaries, limitations, and remaining risk. |
| Security | Does the system resist adversarial threats? | Run functional allow/deny tests; escalate bypasses, isolation failures, injection signals, secret exposure, and security judgment. |
| Production Readiness | Can it operate safely with real data, traffic, dependencies, and failure? | Supply performance, resilience, migration, and recovery observations; do not issue the operational verdict. |
| CI/CD | How is evidence enforced through delivery? | Supply structured results and recommended gate status; CI/CD owns orchestration and authority. |
| Human/UAT | Does the product meet human/business expectations? | Prepare scenarios and record results; never fabricate approval. |

This is a conceptual flow, not a requirement to invoke every capability for every change.

## Regression handoff

After requested behaviour is accepted, its tests become regression assets. Provide:

- changed/new behaviours and criterion IDs;
- tests added, modified, or removed and their locations;
- canonical commands and observed results tied to an artifact/environment;
- important boundaries, fixtures, mocks, and limitations;
- unverified behaviour and remaining risk.

Regression Protection determines the broader existing-behaviour surface. Avoid duplicate execution when evidence remains valid for the same artifact and environment.

## Security handoff

Testing may establish facts such as "an unauthenticated request returned 200" or "tenant A read tenant B's record." Record the exact request, environment, observed result, and affected criterion, then invoke or recommend the relevant security capability. Do not broaden the functional evidence into "the application is secure" or conduct destructive adversarial testing without authorization.

## Production Readiness handoff

Provide observed latency, throughput, error rates, retry/idempotency behaviour, queue failure, resource exhaustion, migration/data findings, dependency instability, or recovery results with workload and environment. Production Readiness decides operational acceptability, monitoring, rollout, backup/restore, and recovery requirements.

For migrations, Testing & Verification proves schema/data behaviour; Production Readiness owns safe rollout and recovery. For performance/resilience, Testing & Verification executes requirement-driven checks; Production Readiness judges production capacity and operational risk.

## CI/CD handoff

Provide at minimum:

- verdict and reason;
- required versus executed tests;
- counts for passed, failed, skipped, flaky, not-run, and infrastructure-failure states;
- verified and unverified criterion IDs;
- coverage status without invented metrics;
- limitations and evidence references;
- recommended gate status.

CI/CD decides when smoke, acceptance, or other suites run, how artifacts are traced, and whether a merge/deploy gate opens. A deployment event is not proof of health or of a working journey.

## Browser tooling

Use Playwright, Cypress, platform UI tooling, or another existing browser stack only when browser-level evidence is appropriate. Follow repository tooling and any applicable browser-testing skill. Prefer resilient semantic selectors and collect useful traces/screenshots on failure where supported. Browser tooling is an execution mechanism, not a reason to turn all acceptance criteria into E2E tests.

## Product experiments and staged validation

A/B testing compares outcomes between already functioning variants; it does not replace functional verification. Verify assignment, rendering, event tracking, and contamination controls, while product analytics owns experiment interpretation.

Alpha and beta programs may supply realistic validation evidence, but release/product governance owns entry, exit, and release decisions. Label their evidence and limitations rather than treating participation as PASS.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
