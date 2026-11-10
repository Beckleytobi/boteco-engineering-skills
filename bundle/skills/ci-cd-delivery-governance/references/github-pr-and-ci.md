# GitHub, pull requests, and CI governance

Use this reference for Git/GitHub delivery, GitHub Actions, branch protection, independent review, or CI diagnosis. Adapt concepts to other providers.

## Discover before editing

Inspect repository instructions; current branch strategy; default branch; `.github/workflows/**`; action versions; permissions; triggers; reusable workflows; path filters; matrices; caches; artifacts; environments; concurrency; timeouts; required checks/rulesets when verifiable; dependency manifests; documented build/test commands; deployment integrations; and recent run evidence when available.

Do not assume a ruleset exists because documentation recommends it. Report `UNKNOWN` when platform state cannot be inspected.

## Pull request as control point

Use the PR to join four distinct evidence sources:

1. actual diff and risk analysis;
2. independent code review, including CodeRabbit when configured;
3. deterministic CI results;
4. approval from the authorized owner where required.

CodeRabbit or another reviewer reasons about the diff; CI executes defined checks. Neither replaces security review, QA, Regression Protection, or production authority when those are relevant. An unresolved serious finding blocks even if all automated checks are green.

## GitHub Actions baseline

Prefer the smallest adequate workflow. Common concerns:

- pre-merge `pull_request` checks for protected targets;
- trusted post-merge or release triggers for deployment;
- explicit least-privilege `permissions`;
- pinned/maintained actions and controlled third-party actions;
- deterministic dependency installation and lockfiles;
- fail-fast ordering for cheap checks before expensive checks;
- job dependencies that prevent deploy on failed prerequisites;
- environment-scoped secrets and approvals;
- `concurrency` for stateful deployments;
- timeouts and bounded retries;
- artifact identity and retention appropriate to traceability;
- reusable workflows only when duplication and governance justify them.

Do not pass secrets to untrusted fork code. Treat `pull_request_target`, privileged tokens, artifact consumption across trust boundaries, self-hosted runners, and executable PR-controlled scripts as elevated risk.

## Pipeline self-protection

Changes to workflows, deploy config, action permissions, test thresholds, security scanners, migration automation, branch rules, or environment protections are high-sensitivity changes.

Compare before/after controls. Ask whether the same PR benefits from the weakened control. Require separate review/authority for legitimate reductions. Never respond to a failing gate by silently deleting tests, skipping checks, lowering thresholds, suppressing findings, or removing a required status check.

Prefer enforceable mechanisms when practical:

- protected branches/rulesets;
- required status checks;
- required independent approvals or code owners;
- resolved-conversation requirements;
- protected environments and deployment approvals;
- restricted force-push/deletion;
- least-privilege workflow permissions.

## Failure classification

| Evidence | Classification | Safe response |
|---|---|---|
| deterministic test/lint/type/build failure | application/change failure | find root cause, fix, rerun affected pipeline |
| intermittent failure with no cause | suspected flake | keep blocked, preserve failed run, reproduce/classify, repair or explicitly quarantine with owner/expiry |
| runner outage, provider incident, quota/network infrastructure failure | CI infrastructure failure | do not label app pass/fail; verify provider evidence and retry safely when restored |
| workflow syntax/permission/config failure | pipeline failure | treat pipeline change as security-sensitive; repair and independently verify |
| missing run or cancelled required job | `NOT RUN`/insufficient evidence | rerun or block |

Retries may establish a later pass, but they must not erase the original failure or conceal flakiness. Avoid repeated destructive or paid actions while diagnosing.

## Branch and merge governance

Use the repository's valid strategy. Normally avoid direct changes to protected production branches. Before merge, verify the head commit matches the reviewed/tested commit, all required checks apply to it, serious findings are resolved or explicitly authorized, conversations/approvals meet policy, and merge authority exists.

After merge, retain PR, commit SHA, check-run links, reviewer/approval evidence, and artifact/run identifiers needed for traceability.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
