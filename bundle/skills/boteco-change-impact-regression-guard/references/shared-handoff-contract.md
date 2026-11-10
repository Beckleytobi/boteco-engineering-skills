# Shared handoff contract

Every impact or regression artifact declares:

```text
artifact_id
artifact_type
artifact_version
change_id
created_at

baseline:
  baseline_id
  version
  content_hash
  approval_state
  approval_evidence

dependencies:
  source_ids
  functional_requirement_ids
  non_functional_requirement_ids
  exception_ids
  acceptance_criterion_ids
  critical_journey_ids
  invariant_ids
  decision_ids
  risk_ids

change_boundary:
  expected
  may_change
  protected

direct_impact
indirect_impact
contracts
data
integrations
protected_behaviours
regression_risk
planned_evidence
executed_evidence
missing_coverage
limitations
technical_status
confidence

approval:
  state
  authority
  evidence_reference
  decided_at
  conditions

invalidation:
  state
  superseded_by
  changed_dependencies
  affected_artifacts
  reason
  required_action
```

Stable prefixes are `CHG-`, `SRC-`, `FR-`, `NFR-`, `EXC-`, `AC-`, `CJ-`, `INV-`, `DEC-`, `RSK-`, and `EVD-`.

Technical status uses the preserved Regression Protection vocabulary: `PASS`, `PASS WITH CONCERNS`, `FAIL`, `ESCALATE`, or `BLOCKED`. Approval state and invalidation state are separate. Never map `STALE` or `INVALIDATED` to technical `PASS`.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
