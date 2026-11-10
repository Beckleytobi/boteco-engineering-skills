# Requirements model and validation

## Requirement record

Use stable IDs and keep each requirement atomic enough to validate independently.

| Field | Meaning |
|---|---|
| ID | `FR-`, `NFR-`, `EXC-`, or `INV-` identifier |
| Statement | Required observable outcome or constraint |
| Rationale | Why it is needed |
| Source | Evidence reference, not a vague attribution |
| Status | Proposed, confirmed, changed, rejected, or open |
| Priority | Use the project's vocabulary; do not invent urgency |
| Dependencies | Other requirements, decisions, services, or constraints |
| Acceptance criteria | `AC-` identifiers that demonstrate satisfaction |
| Assumptions | Explicit assumptions on which the requirement depends |

## Functional requirements

Describe what an actor or system must be able to do, including inputs, outputs, permissions, business rules, state transitions, side effects, and failure behaviour. Prefer observable behaviour over implementation choices. A requirement such as “use Redis” is usually a design decision unless a confirmed constraint specifically requires Redis.

## Non-functional requirements

Include only qualities relevant to the change. Convert them into measurable constraints or explicit decision gaps.

- Performance: response time, throughput, batch duration, or resource bound under stated conditions.
- Reliability and availability: allowed failure, retry, durability, or continuity expectation.
- Capacity and scale: supported users, records, payload, concurrency, or growth horizon.
- Security and privacy: access, isolation, retention, minimization, audit, or threat-related constraints; route specialist judgment to security review.
- Accessibility and usability: applicable standard, interaction, assistive-technology, or completion expectation.
- Compatibility: supported clients, versions, schemas, migration windows, or coexistence rules.
- Recoverability: acceptable data loss, recovery time, rollback, or restoration expectation when justified.
- Maintainability and operability: only requirements with a concrete product or delivery consequence.
- Compliance: record the confirmed obligation and source; never invent a legal requirement.

Do not create fake precision. If a threshold matters but is not yet known, record a decision item with an owner and validation method.

## Exception scenarios

For each important journey or state mutation, ask what must happen when the normal path does not complete. Consider invalid or missing input, unauthorized access, duplicate submission, timeout, dependency failure, partial completion, cancellation, retry, concurrency, stale data, incompatible version, and recovery after interruption.

An exception scenario states:

1. initiating condition;
2. expected system response;
3. state and side effects that may or may not remain;
4. user-visible result;
5. recovery or escalation path;
6. evidence needed to validate it.

## Measurable acceptance criteria

Each material criterion should answer:

- Given which starting conditions and actor?
- When what action or event occurs?
- Then what observable result follows?
- How will the result be measured or inspected?
- What threshold, boundary, or exact outcome constitutes success?
- In which environment and with which representative data?

Not every criterion needs numeric output. “A user without the billing-admin role receives HTTP 403 and no invoice record is created” is measurable because the expected response and state are unambiguous.

## Validation pass

Check:

- Necessity: each requirement supports an approved outcome or constraint.
- Clarity: different readers are unlikely to infer incompatible meanings.
- Completeness: important actors, states, exceptions, data, and quality constraints are covered.
- Consistency: requirements and criteria do not contradict one another.
- Feasibility: no known platform, budget, time, legal, or operational constraint makes the requirement impossible; unresolved feasibility becomes an open decision.
- Testability: evidence can distinguish success from failure.
- Traceability: every requirement has a source and every material criterion maps back to a requirement.
- Boundary integrity: design choices are not disguised as requirements.
- Approval readiness: high-impact assumptions and conflicts are resolved or plainly presented for decision.

Validation may use review, prototype, calculation, model, test design, existing evidence, or stakeholder confirmation. Record which method was used. Do not mark a requirement validated merely because it is well written.

## Explicit completeness registers (FR4)

The baseline JSON requires business_rules, assumptions and open_decisions. Each is an object with items (a list); an empty list requires none_reason explaining why none were identified. Business rules reference their canonical requirement_ids rather than duplicating functional-rule wording. Each item has a unique id, requirement_ids, owner, validation_method and disposition. Business-rule status is PROPOSED, CONFIRMED or REJECTED.

Assumptions additionally have statement, material (boolean), and status OPEN, VALIDATED or REJECTED. Decisions additionally have statement, material, and status OPEN, RESOLVED or DEFERRED. VALIDATED assumptions and RESOLVED decisions require evidence_reference. OPEN/DEFERRED records remain visible; their disposition states the next action or bounded consequence. Review material unresolved items before approval; a structural pass cannot resolve them.

validation_state must be VALIDATED, VALIDATED WITH OPEN ITEMS, NEEDS DECISION or BLOCKED. Requirement/acceptance-criterion links must agree in both directions. Every functional/non-functional/exception/invariant category is assessed for relevance during validation; do not invent irrelevant records to fill categories.

These registers are part of immutable baseline content. Adding them to an old baseline changes its hash: preserve the old artifact, issue a reviewed revision and obtain approval where required. Never auto-fill historical approval evidence. The hash algorithm is unchanged.

### Baseline JSON shape

Use top-level baseline_id, version, change_id, content_hash, validation_state, approval, requirements, acceptance_criteria, business_rules, assumptions, open_decisions and downstream_artifacts. The baseline identity is not nested inside a `baseline` envelope here; that envelope is for downstream handoffs.

requirements is a list of {id, kind, statement, sources, acceptance_criterion_ids}. kind is functional, non_functional, exception or invariant; sources and acceptance_criterion_ids are nonempty string lists. acceptance_criteria is a list of {id, requirement_ids, condition, observable_result, evidence_method, success_threshold}. The four text fields must be explicit; genuinely unknown thresholds stay visibly pending and require NEEDS DECISION or another appropriate non-final validation result, never invented precision. Invariants belong in requirements with kind invariant so they participate in the same traceability.

For a draft, approval is {"state":"APPROVAL REQUIRED"} and downstream_artifacts may be []. Compute content_hash using the existing canonical hash contract only after the payload exists. An illustrative NOT COMPUTED hash is a drafting placeholder, not validator-ready evidence. Business-rule items point to canonical requirement_ids; assumptions and decisions follow the register schema above. Run the baseline validator before claiming structural completeness.
