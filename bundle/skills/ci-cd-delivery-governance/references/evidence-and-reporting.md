# Evidence, statuses, traceability, and founder reporting

Use this reference for a merge/release decision or handoff.

## Evidence quality

Rank evidence roughly from strongest to weakest:

1. enforced platform state or independently observable run/result tied to the exact commit/artifact;
2. independent reviewer output tied to the diff;
3. reproducible local command output tied to the workspace state;
4. repository documentation or configuration not verified in the platform;
5. agent or human assertion without supporting record.

Use weaker evidence when it is all that is proportionate and available, but label it. Never promote an assertion into a verified fact.

## Evidence ledger

For each required gate record:

- gate name and why required;
- status;
- evidence source/link/run ID;
- exact commit or artifact where applicable;
- actor/provider and independence;
- time or freshness when relevant;
- unresolved condition and owner;
- next safe action.

Also retain requirement/issue → branch/PR → commit → CI/review → artifact → environment/deployment → health/monitoring → completion/rollback traceability.

## Status resolution

- A required `FAIL`, `UNKNOWN`, or `NOT RUN` prevents `PASS` for the parent decision.
- `PASS WITH CONDITIONS` is allowed only when conditions are explicit, owned, time-bounded where useful, and do not hide a failed required gate.
- `APPROVAL REQUIRED` is not `PASS`; it means evidence may be ready but authority is outstanding.
- `NOT APPLICABLE` needs a risk-based reason.
- Conflicting evidence stays `BLOCKED` or `UNKNOWN` until resolved.

Run `python scripts/evaluate_delivery.py <evidence.json>` to check structured records for contradictions. The script does not inspect external systems or grant authority.

## Founder-facing release example

```text
DELIVERY STATUS

Change: Add profile caching
Risk: MEDIUM — changes API behavior and stale-data handling
Decision: APPROVAL REQUIRED

Independent review: PASS — PR #214, no unresolved serious findings
Automated checks: PASS — CI run 8912 on commit a13f…
Regression checks: PASS — profile update, permissions, and cache invalidation
Security: PASS — no new privileged access or exposed credentials
Build/artifact: PASS — image digest sha256:… from run 8912
Staging: PASS — critical profile journeys checked
Production readiness: PASS WITH CONDITIONS — monitor stale-read rate for 30 minutes
Production authority: APPROVAL REQUIRED — product owner
Recovery: PASS — disable cache flag and redeploy known-good image
Post-deploy health: NOT RUN — deployment has not occurred

Next safe action: Product owner approves the production release; then deploy the verified image and run the listed health checks.
```

Keep raw logs accessible for investigation, but do not make a non-technical founder interpret them to understand the decision.

## Evidence-based completion

Do not say “done,” “released,” “protected,” or “healthy” unless the corresponding outcome was observed. If the requested work ends before production, state the actual terminal condition, such as “PR ready but approval required,” “artifact verified; deployment not authorized,” or “deployment completed; health verification failed and rollback is required.”
