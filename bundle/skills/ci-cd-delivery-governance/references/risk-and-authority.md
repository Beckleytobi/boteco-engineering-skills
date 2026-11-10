# Risk, authority, and delivery paths

Use this reference when classifying a change, selecting controls, or deciding whether the agent may take the next action.

## Classify actual consequence

Start with impact and reversibility, then use file paths as evidence—not as the decision.

| Risk | Typical consequence | Typical examples | Minimum posture |
|---|---|---|---|
| `LOW` | Localized, readily reversible, no sensitive state | docs, copy, isolated styling | targeted checks, review proportional to repository policy, traceable merge |
| `MEDIUM` | User-visible behavior or service interaction can regress | business logic, API, integration, cache, worker, performance change | independent CI, relevant regression evidence, review, deploy verification, known recovery |
| `HIGH` | Security, money, sensitive data, broad outage, governance, or irreversible state is exposed | auth, payments, destructive migrations, RLS, secrets, infrastructure, production config, CI/CD, branch rules | enhanced checks and independent review, explicit authority, staging/preflight where meaningful, verified recovery, controlled rollout and monitoring |

Increase risk for broad blast radius, hidden coupling, poor observability, large or generated diffs, privileged execution, novel tooling, irreversible operations, or weak recovery. A small diff can be high risk. A large documentation-only diff can remain low risk.

## Capability is not authority

Ordinary agent capability may include inspection, branch work, local checks, commits, authorized pushes, PR updates, and failure investigation. It does not itself authorize:

- bypassing required checks or approvals;
- approving its own exception;
- reducing coverage or disabling tests/security checks to pass;
- modifying branch rules, protected environments, or production secrets;
- merging or deploying where the user/repository requires another actor;
- destructive migration or recovery;
- granting itself broader credentials.

Before any protected action, identify the authority source: explicit user instruction, repository policy, verified platform rule, or approved automation. If missing, use `APPROVAL REQUIRED` or `BLOCKED`.

## Proportionate paths

These are defaults, not universal ceremonies.

### Low

Branch/PR (if repository uses them) → targeted CI → proportionate review → merge → automated or simple deploy → smoke/health confirmation.

### Medium

Branch → PR → independent CI and review → regression evidence → build/artifact → preview or staging when useful → authority gate → deploy → health and critical-journey verification → monitoring.

### High

Branch → PR → enhanced CI → independent code/security/operational review → migration/preflight evidence → verified artifact → staging/controlled rollout → explicit approval → serialized deploy → enhanced verification and monitoring → complete or recover.

Do not invent staging, canaries, or committees for a tiny low-risk project when targeted evidence is adequate. Do not use project immaturity to waive controls for high-consequence changes.

## Hotfixes

A hotfix may shorten the path but must retain:

- incident/change identity and bounded scope;
- independent evidence feasible under the circumstances;
- explicit emergency authority;
- known recovery or containment action;
- post-deploy health verification and monitoring;
- retrospective restoration of any temporarily deferred non-blocking evidence.

Never call “urgent” an authorization to bypass security, conceal a failed gate, or perform an unreviewed destructive operation.

## Multi-agent authority

An agent can produce evidence only for work it actually performed or observed. A builder's report is not independent review. A reviewer can recommend but cannot impersonate the approval owner. Handoffs must carry change identity, commit/artifact identity, risk, completed evidence, unresolved findings, required authority, and next safe action.
