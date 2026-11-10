# Evidence and Verdicts

## Evidence strength

- `STRONG`: observed automated test against an appropriate implementation, boundary, data shape, and environment.
- `MODERATE`: reproducible bounded manual verification or an automated proxy with documented limitations.
- `WEAK`: static reasoning, review, build/lint/type success, or a heavily mocked check that does not exercise the material boundary.
- `ABSENT`: no observed verification.

Expected behaviour is not observed evidence. "CI is configured to run tests" is expected; "run 123 executed 142 tests, all passed" is observed. A successful build, review, deployment, or health check proves only its own state.

## Human-readable report contract

For meaningful verification work, report:

### Verification scope

Requested behaviour, artifact/version, explicit non-goals, and environment.

### Acceptance criteria

Stable ID, criterion, source (`CONFIRMED` or `INFERRED`), materiality, and any ambiguity.

### Risk

Project taxonomy or `LOW`/`MEDIUM`/`HIGH`/`CRITICAL`, with dominant drivers.

### Test strategy

Selected levels/techniques and the risk each addresses. Mention important omissions where their absence could otherwise be mistaken for oversight.

### Tests created or identified

Location/name, purpose, criterion IDs, and notable real or mocked boundaries.

### Execution

Command/steps, environment, artifact identity, run ID/time, exit code, counts for each result state, and evidence reference. Keep separate runs separate when environment or artifact differs.

### Acceptance traceability

| Criterion | Test/evidence | Level | Observed result | Strength | Limitations |
|---|---|---|---|---|---|

No material criterion may disappear. Use `NOT RUN` or `BLOCKED` explicitly.

### Coverage and quality

Available structural coverage, meaningful branch/condition gaps, assertion quality, mutation evidence if used, mock limitations, and existing thresholds. Never invent unavailable metrics or infer correctness from a percentage.

### Limitations and gaps

Untested behaviour, unavailable dependencies, nonrepresentative environments/data, skips, flakes, manual checks, mocks, and unresolved ambiguity.

### Handoffs

Actionable evidence for Regression Protection, Security, Production Readiness, CI/CD, and human/UAT review where applicable.

### Final verification verdict

Exactly one of `PASS`, `FAIL`, `BLOCKED`, `INSUFFICIENT EVIDENCE`, `NOT APPLICABLE`, followed by a brief evidence-based reason.

## PASS decision rule

`PASS` requires all of the following:

- every material confirmed acceptance criterion has relevant observed evidence;
- required executions completed and passed;
- no material result is failed, blocked, not run, flaky, or an infrastructure failure;
- negative, boundary, state, side-effect, integration, and environment depth is proportionate to risk;
- mocks do not hide the material behaviour;
- limitations do not undermine a material claim.

Coverage percentage, clean review, build success, some passing tests, or absence of a known defect cannot substitute for these conditions.

Use `FAIL` when evidence disproves a criterion. Use `BLOCKED` when a required check cannot be attempted safely or technically. Use `INSUFFICIENT EVIDENCE` when checks ran or reasoning exists but their relevance, scope, assertions, representativeness, flakiness, or omissions do not justify pass/fail. Use `NOT APPLICABLE` only when no executable behaviour needs verification.

## Machine-readable evidence

The included validator accepts this compact JSON form:

```json
{
  "subject": "Password reset token reuse",
  "artifact": "commit-or-build-id",
  "risk": {"level": "HIGH", "drivers": ["authentication", "state transition"]},
  "criteria": [
    {
      "id": "AC-01",
      "statement": "A used token cannot be reused",
      "material": true,
      "source": "CONFIRMED",
      "result": "PASS",
      "evidence": ["run-123:test_reused_token"],
      "strength": "STRONG"
    }
  ],
  "runs": [
    {
      "id": "run-123",
      "command": "project test command",
      "environment": "CI",
      "exit_code": 0,
      "counts": {"passed": 1, "failed": 0, "skipped": 0, "flaky": 0, "not_run": 0, "infrastructure_failure": 0}
    }
  ],
  "limitations": [],
  "handoffs": {"regression": [], "security": [], "production_readiness": [], "ci_cd": [], "human_uat": []},
  "verdict": "PASS",
  "reason": "AC-01 passed in CI against the real token store."
}
```

Run `python scripts/validate_evidence.py evidence.json`. The validator checks structure and rejects mechanically inconsistent `PASS` claims; it does not decide whether tests are semantically adequate.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
