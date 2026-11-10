# Baseline versioning, approval evidence, and invalidation

## Immutable baseline identity

Every baseline must record:

- `baseline_id` and monotonically advancing `version`;
- `change_id` and creation timestamp;
- content hash over the normalized requirements artifact;
- source identifiers and versions;
- validation result and unresolved items;
- approval state;
- approval evidence when approved;
- previous baseline identity, when any;
- change classification and affected downstream artifacts.

An approval record contains the exact baseline ID, version, content hash, decision, approver identity or role as actually supplied, decision timestamp, evidence reference, scope, and any conditions. Missing evidence means `APPROVAL REQUIRED`, not approved.

## Material change test

A change is material when it can alter design, implementation, verification, risk, operational behaviour, user outcome, or an earlier decision. Examples include:

- adding, removing, or changing a functional requirement;
- changing a non-functional threshold, supported condition, or quality constraint;
- changing scope, actor, permission, business rule, state transition, side effect, or non-goal;
- adding or changing an exception scenario or recovery expectation;
- changing acceptance evidence, threshold, environment, or success meaning;
- changing an invariant, compatibility promise, data classification, security boundary, integration, migration, or regulatory constraint;
- resolving an assumption in a way that invalidates downstream reasoning.

Spelling, formatting, link repair, and wording clarification may be non-material only when meaning, scope, thresholds, evidence, and traceability remain unchanged. Record the reasoning; do not use “editorial” to avoid reapproval.

## Dependency-aware invalidation

Every downstream artifact should declare:

```text
artifact_id
artifact_type
based_on.baseline_id
based_on.version
based_on.content_hash
requirements_used
approval_state
approval_evidence
```

When a material baseline change occurs:

1. create a new baseline version; never mutate the approved one;
2. compute changed requirement, criterion, invariant, exception, and constraint IDs;
3. find downstream artifacts that consume those IDs or depend on the previous baseline as a whole;
4. classify each approval as `CURRENT`, `STALE`, `INVALIDATED`, or `PENDING REAPPROVAL`;
5. state the exact change, affected reasoning or evidence, and required rework;
6. preserve unaffected approvals when their dependency declaration demonstrates independence;
7. obtain and record new approval before presenting an invalidated artifact as approved.

`STALE` means the artifact has not yet been reassessed against the new baseline. `INVALIDATED` means a known dependency changed such that its prior approval no longer applies. Do not collapse either state into a warning-only pass.

## Approval boundaries

Requirements approval authorizes the baseline as the source for downstream design. It does not authorize implementation, purchasing, external communication, data mutation, deployment, or release. Downstream approvals retain their own authority owners and evidence.


## Visual artifact register

Follow the bundled Visual Design Contract; do not duplicate its rules here.

| Diagram ID/version | Purpose/level | Source | Governing baseline and decisions | Validation evidence | Approval/freshness |
|---|---|---|---|---|---|
| | | | | | |

Record omitted views and their reasons. Store machine-readable records in diagram-records/*.json beside the design pack. Each record follows the shared contract and is checked by scripts/validate_visual_pack.py. A draft without records may be reviewed but cannot claim visual completion.

## Machine-readable approval validation (revision 2)

An APPROVED baseline requires approval.baseline_id, baseline_version and content_hash to equal the baseline identity, plus approver, decided_at and evidence_reference. Identity/evidence text fields must be nonblank strings, not boolean placeholders. A CURRENT downstream artifact's artifact_id and approval_evidence must also be nonblank strings; approval_evidence is the reference to its actual approval record. Approval metadata remains outside the immutable content hash.

A CURRENT downstream artifact must contain artifact_id, approval_evidence, complete based_on {baseline_id, version, content_hash}, and a nonempty requirements_used list referencing this baseline. If based_on exactly equals the current identity, no equivalence review is needed. An older identity in the same baseline lineage requires equivalence_review with decision EQUIVALENT, exact from_baseline and to_baseline identities, requirements_reviewed matching the entire requirements_used set, reviewer, reviewed_at, evidence_reference and rationale. Otherwise mark it STALE, INVALIDATED or PENDING REAPPROVAL with a reason. A missing declaration cannot be interpreted as proof of independence.

These checks require recorded evidence and exact bindings; they do not authenticate approvers or independently prove semantic equivalence. Review the referenced evidence before relying on approval. Existing approved artifacts lacking these fields need explicit evidence reconciliation; never auto-fill approval or silently reapprove them. The revision does not change the content-hash algorithm.
