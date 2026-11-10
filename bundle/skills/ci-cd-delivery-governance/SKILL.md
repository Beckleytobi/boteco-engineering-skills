---
name: ci-cd-delivery-governance
description: Govern pull requests, CI pipelines, merge gates, build artifacts, deployments, and post-release verification using risk, evidence, and explicit authority. Use for delivery-path design or review, GitHub Actions and branch controls, release decisions, deployment/rollback, and CI/CD failures; do not use for implementation design alone, test-design alone, or general production-readiness analysis without a delivery decision.
---

# CI/CD Delivery & Pipeline Governance

Own **DELIVER SAFELY**: move a completed change through integration and release only when proportionate evidence, controls, recovery, and authority support the next action.

Do not treat an implementation report as release evidence. Do not perform external mutations merely because this skill identifies them as technically possible.

## Invariants

1. Discover the repository and delivery system before modifying either.
2. Prefer independent verification over the builder's self-report when available.
3. Never weaken a test, check, threshold, review, ruleset, or security control merely to get green.
4. A successful deployment is not proof of application health.
5. `UNKNOWN` and `NOT RUN` are never `PASS`.
6. Capability does not imply authority.
7. Increase evidence and governance with actual impact and irreversibility.
8. Treat pipeline, deployment, branch-rule, and secret-handling changes as security-sensitive.
9. Require a proportionate recovery path before production changes.
10. Avoid ceremony that does not materially reduce risk.
11. Prefer enforceable repository or platform controls over instructions alone where practical.
12. Never claim a check, review, approval, protection, deployment, or recovery capability without evidence.

## Route the task

- Read [risk-and-authority.md](references/risk-and-authority.md) for risk classification, permissions, hotfixes, or proportional delivery paths.
- Read [github-pr-and-ci.md](references/github-pr-and-ci.md) when inspecting or changing Git/GitHub flow, PR gates, GitHub Actions, independent review, branch rules, or CI failures.
- Read [artifacts-deployment-and-recovery.md](references/artifacts-deployment-and-recovery.md) for builds, artifacts, environments, deployment strategies, concurrency, health verification, monitoring, and rollback.
- Read [migrations-secrets-and-security.md](references/migrations-secrets-and-security.md) for database changes, secrets, privileged workflows, or supply-chain concerns.
- Read [evidence-and-reporting.md](references/evidence-and-reporting.md) when making a gate decision, producing traceability, or reporting to a non-technical founder.
- Read [skill-handoffs.md](references/skill-handoffs.md) when another engineering skill or agent must supply evidence.

Load only the references relevant to the current change.

## Mandatory operating workflow

Follow every stage, scaling the depth rather than deleting the stage.

### 1. Discover

Inspect repository instructions, stack, package manager, repository shape, default and protected branches, workflows, deployment configuration, environments, migration tooling, secrets approach, rollback mechanism, observability, and documented commands. Preserve valid conventions. Label anything material that cannot be verified `UNKNOWN`.

### 2. Understand change

Use the requirement and actual diff or proposed change. Identify affected behavior, delivery/configuration files, data changes, dependencies, environments, user impact, and reversibility. Separate observed facts from assumptions.

### 3. Classify risk

Assign `LOW`, `MEDIUM`, or `HIGH` using impact, privilege, blast radius, data sensitivity, operational consequence, and reversibility—not filenames alone. Elevate changes to authentication, authorization, payments, sensitive data, migrations, secrets, infrastructure, CI/CD, or branch protection unless evidence justifies otherwise.

### 4. Plan delivery path

Define the branch/PR path, required checks, independent reviews, environments, approval owner, artifact strategy, deployment method, health checks, observation window, stop conditions, and recovery action. Distinguish recommendations from controls verified as enforced.

### 5. Execute checks

Run the smallest adequate set in fail-fast order. CI decides when evidence is collected and what it gates; Regression Protection determines deeper regression scope. Do not blindly run everything or skip required evidence because checks are expensive.

### 6. Collect evidence

Record commands or run identifiers, commit SHA, artifact identity, results, timestamps when useful, reviewer findings, approvals, environment, and source links. Keep unverified claims as `UNKNOWN` or `NOT RUN`.

### 7. Evaluate gates

Resolve every required gate with the status vocabulary below. A green workflow does not override an unresolved serious review, missing approval, unsafe migration, secret exposure, failed health check, or missing recovery path.

### 8. Approve or block

State the decision, evidence, missing evidence, authority owner, and next safe action. The agent may recommend; only an authorized actor or verified automation may approve or execute protected actions.

### 9. Merge

Merge only through the repository's authorized pathway with required checks and reviews satisfied. Do not infer branch protection from a documented recommendation.

### 10. Deliver

Promote the verified artifact where practical. Respect environment protections, least-privilege credentials, deployment concurrency, migration ordering, and approved strategy.

### 11. Verify

Confirm application-specific health, smoke tests, critical journeys, migrations, and dependency behavior after deployment. A provider's “deployed” status is only deployment evidence.

### 12. Monitor

Observe relevant errors, latency, saturation, business signals, queues, and user impact for a risk-proportionate period. State what was observed and what was not.

### 13. Complete or rollback

Complete only with required evidence and stable health. If stop conditions occur, halt rollout, roll back, disable via an approved feature flag, or execute the documented recovery path. Never improvise destructive recovery without authority.

## Status vocabulary

Use exactly: `PASS`, `FAIL`, `BLOCKED`, `PASS WITH CONDITIONS`, `APPROVAL REQUIRED`, `NOT APPLICABLE`, `NOT RUN`, `UNKNOWN`.

- `PASS`: required evidence directly supports the gate.
- `FAIL`: evidence shows the gate was not met.
- `BLOCKED`: progress cannot safely continue because a required gate, dependency, or authority condition is unmet.
- `PASS WITH CONDITIONS`: evidence supports progress only with explicit, owned conditions that do not conceal a failed required gate.
- `APPROVAL REQUIRED`: technical prerequisites may be satisfied, but authority is outstanding.
- `NOT APPLICABLE`: the gate was deliberately excluded with a reason.
- `NOT RUN`: the check has not executed.
- `UNKNOWN`: the state cannot be verified.

Sibling skills may use their own vocabulary. Preserve their original result in the evidence ledger, then map it explicitly: `PASS` → `PASS`; `PASS WITH CONCERNS` → `PASS WITH CONDITIONS` only when every concern has an owner and does not hide a failed required gate; `FAIL` → `FAIL`; `ESCALATE` → `BLOCKED` until the named human decision or evidence resolves it; `BLOCKED` → `BLOCKED`. A Production Readiness report with any `BLOCKING` finding maps to `BLOCKED`. Do not silently normalize a concern or escalation into `PASS`.

## Decision rules

- Any failed required gate blocks the governed next step.
- Any required `UNKNOWN` or `NOT RUN` evidence blocks; it does not become a warning-only pass.
- Unresolved serious independent-review or security findings block even when CI is green.
- Suspected flaky tests remain failed/blocked until classified with evidence; retries do not erase the original signal.
- CI-provider failure is infrastructure failure, not application failure and not application success.
- Hotfixes may compress time and scope, never erase required safety, authority, traceability, verification, or recovery.
- A change to remove or weaken a required control needs separate justification and authorization; it must not self-authorize the change it enables.
- Concurrent deployments to the same stateful environment must serialize, cancel safely, or use a verified isolation strategy.
- Keep gate outcome separate from the overall delivery decision. For example, post-deploy health can be `FAIL` while the overall delivery becomes `BLOCKED` pending rollback or verified recovery.
- A pre-deploy hotfix decision may be `PASS WITH CONDITIONS` when its remaining conditions are necessarily post-deploy verification and monitoring. It is not final completion until those conditions have evidence.

When evidence is captured in JSON, use `python scripts/evaluate_delivery.py <evidence.json>` as a deterministic consistency check. It supports the decision; it does not grant approval or execute delivery.

## Skill boundaries and handoffs

- **`software-design-principles` — BUILD WELL:** owns internal structure, boundaries, maintainability, and change design. Consume its change boundary, drift check, regression handoff, and evidence-backed status; do not restate its methodology.
- **`regression-protection` — DON'T BREAK:** owns regression-surface analysis, protected behavior, evidence planning, and confidence. Consume its Regression Evidence artifact; CI/CD schedules and gates the required evidence.
- **`production-readiness` — OPERATE SAFELY:** owns risk-tiered operational assessment for real traffic, data, dependencies, and failures. Consume its blocking findings, action plan, and unresolved access limits before significant production delivery.
- **CI/CD — DELIVER SAFELY:** owns the path, evidence ledger, gates, authority, merge, artifact promotion, release verification, and rollback decision.

If a referenced skill is unavailable, mark its required output `UNKNOWN` and either gather equivalent evidence within the user's scope or block/escalate. Never claim the skill ran.

## Output contract

For release decisions, provide a concise founder-facing summary followed by evidence links/details:

```text
DELIVERY STATUS
Change: <plain-language change>
Risk: LOW | MEDIUM | HIGH — <why>
Decision: <status>
Code/independent review: <status + evidence>
Automated checks: <status + evidence>
Security: <status + evidence>
Build/artifact: <status + identity>
Staging/production readiness: <status + evidence>
Production authority: <status + owner>
Recovery: <status + method>
Post-deploy health: <status + evidence>
Next safe action: <one explicit action>
```

Omit irrelevant rows only when their `NOT APPLICABLE` rationale remains traceable.

## Completion standard

The work is complete only when the requested delivery outcome—not merely file creation or a successful deploy command—is supported by evidence; required gates and authority are resolved; deployed source/artifact/environment are traceable; health and monitoring are assessed; and the final state is either safely complete or explicitly rolled back/blocked.


## Visual design integration

For diagram authoring, review, or consumption, read [visual-routing.md](references/visual-routing.md) and the shared contract it references. Scale diagrams to the change. Preserve existing approval gates.
