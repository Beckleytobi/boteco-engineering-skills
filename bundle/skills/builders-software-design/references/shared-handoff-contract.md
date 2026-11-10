# Shared handoff contract

Use this contract for requirements, design, implementation, testing, regression, production-readiness, and delivery artifacts. Omit inapplicable optional fields; never omit identity, provenance, baseline, approval, or invalidation state.

```text
artifact_id
artifact_type
artifact_version
change_id
created_at
created_by

baseline:
  baseline_id
  version
  content_hash
  approval_state
  approval_evidence

traceability:
  sources
  requirement_ids
  acceptance_criterion_ids
  critical_journey_ids
  invariant_ids
  decision_ids
  risk_ids
  evidence_ids

scope:
  included
  excluded
  protected

facts
assumptions
open_decisions
findings
evidence
limitations
required_handoffs

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

Stable ID prefixes:

- `CHG-` change
- `SRC-` evidence source
- `FR-` functional requirement
- `NFR-` non-functional requirement
- `EXC-` exception scenario
- `AC-` acceptance criterion
- `CJ-` critical journey
- `INV-` invariant
- `DEC-` decision
- `RSK-` risk
- `EVD-` evidence

Approval and technical verdict are separate fields. A technically acceptable artifact can still be `APPROVAL REQUIRED`; an approved older artifact can be `STALE` or `INVALIDATED` after a material baseline change.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.
