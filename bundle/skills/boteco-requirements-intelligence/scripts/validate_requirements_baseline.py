#!/usr/bin/env python3
"""Validate the structural contract of a Requirements Intelligence baseline."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


REQUIRED_TOP = {
    "baseline_id",
    "version",
    "change_id",
    "content_hash",
    "validation_state",
    "approval",
    "requirements",
    "acceptance_criteria",
    "downstream_artifacts",
}
REQUIREMENT_KINDS = {"functional", "non_functional", "exception", "invariant"}
APPROVAL_STATES = {"APPROVAL REQUIRED", "APPROVED", "REJECTED"}
DOWNSTREAM_STATES = {"CURRENT", "STALE", "INVALIDATED", "PENDING REAPPROVAL"}


def fail(message: str) -> None:
    raise ValueError(message)


def validate(data: dict) -> list[str]:
    if not isinstance(data, dict):
        fail("baseline root must be an object")
    missing = sorted(REQUIRED_TOP - data.keys())
    if missing:
        fail(f"missing top-level fields: {missing}")

    from requirements_completeness import validate_completeness
    validate_completeness(data)

    approval = data["approval"]
    if not isinstance(approval, dict) or approval.get("state") not in APPROVAL_STATES:
        fail("approval.state is invalid")
    if approval["state"] == "APPROVED":
        for field in ("baseline_id", "approver", "decided_at", "evidence_reference", "baseline_version", "content_hash"):
            if approval.get(field) is None or not str(approval.get(field, "")).strip():
                fail(f"approved baseline requires approval.{field}")
            if field != "baseline_version" and (not isinstance(approval[field], str) or not approval[field].strip()):
                fail(f"approval.{field} must be a nonblank string")
        if approval["baseline_id"] != data["baseline_id"] or approval["baseline_version"] != data["version"] or approval["content_hash"] != data["content_hash"]:
            fail("approval evidence does not match the baseline ID, version and hash")

    requirements = data["requirements"]
    criteria = data["acceptance_criteria"]
    if not isinstance(requirements, list) or not requirements:
        fail("requirements must be a non-empty list")
    if not isinstance(criteria, list) or not criteria:
        fail("acceptance_criteria must be a non-empty list")

    requirement_ids: set[str] = set()
    for index, item in enumerate(requirements):
        if not isinstance(item, dict):
            fail(f"requirements[{index}] must be an object")
        rid = str(item.get("id", "")).strip()
        if not rid or rid in requirement_ids:
            fail(f"requirements[{index}] has a missing or duplicate id")
        requirement_ids.add(rid)
        if item.get("kind") not in REQUIREMENT_KINDS:
            fail(f"{rid}: unsupported requirement kind")
        if not str(item.get("statement", "")).strip() or not item.get("sources"):
            fail(f"{rid}: statement and sources are required")

    criterion_ids: set[str] = set()
    for index, item in enumerate(criteria):
        if not isinstance(item, dict):
            fail(f"acceptance_criteria[{index}] must be an object")
        cid = str(item.get("id", "")).strip()
        if not cid or cid in criterion_ids:
            fail(f"acceptance_criteria[{index}] has a missing or duplicate id")
        criterion_ids.add(cid)
        linked = set(item.get("requirement_ids", []))
        if not linked or not linked <= requirement_ids:
            fail(f"{cid}: requirement_ids must reference known requirements")
        for field in ("condition", "observable_result", "evidence_method", "success_threshold"):
            if not str(item.get(field, "")).strip():
                fail(f"{cid}: {field} is required")

    for item in requirements:
        linked = set(item.get("acceptance_criterion_ids", []))
        if not linked or not linked <= criterion_ids:
            fail(f"{item['id']}: acceptance criteria are missing or unknown")

    if not isinstance(data["downstream_artifacts"], list):
        fail("downstream_artifacts must be a list")
    current = {"baseline_id": data["baseline_id"], "version": data["version"], "content_hash": data["content_hash"]}
    for index, artifact in enumerate(data["downstream_artifacts"]):
        if not isinstance(artifact, dict):
            fail(f"downstream_artifacts[{index}] must be an object")
        state = artifact.get("approval_state")
        if state not in DOWNSTREAM_STATES:
            fail(f"downstream_artifacts[{index}].approval_state is invalid")
        if state in {"STALE", "INVALIDATED", "PENDING REAPPROVAL"} and not str(artifact.get("reason", "")).strip():
            fail(f"downstream_artifacts[{index}] requires an invalidation reason")
        if state == "CURRENT":
            based_on = artifact.get("based_on")
            used = artifact.get("requirements_used")
            if any(not isinstance(artifact.get(k), str) or not artifact[k].strip() for k in ("artifact_id", "approval_evidence")):
                fail(f"downstream_artifacts[{index}] CURRENT requires artifact identity and approval evidence")
            if not isinstance(based_on, dict) or any(not based_on.get(k) for k in current):
                fail(f"downstream_artifacts[{index}] CURRENT requires complete based_on identity")
            if not isinstance(used, list) or not used or any(not isinstance(x, str) for x in used) or not set(used) <= requirement_ids:
                fail(f"downstream_artifacts[{index}] CURRENT requires known requirements_used")
            if based_on != current:
                review = artifact.get("equivalence_review")
                if not isinstance(review, dict) or review.get("decision") != "EQUIVALENT":
                    fail(f"downstream_artifacts[{index}] CURRENT on another baseline requires equivalence review")
                if based_on["baseline_id"] != current["baseline_id"] or review.get("from_baseline") != based_on or review.get("to_baseline") != current:
                    fail(f"downstream_artifacts[{index}] equivalence review baseline identity mismatch")
                reviewed = review.get("requirements_reviewed")
                if not isinstance(reviewed, list) or any(not isinstance(x, str) for x in reviewed) or set(reviewed) != set(used):
                    fail(f"downstream_artifacts[{index}] equivalence review must cover the declared dependency set")
                for field in ("reviewer", "reviewed_at", "evidence_reference", "rationale"):
                    if not isinstance(review.get(field), str) or not review[field].strip():
                        fail(f"downstream_artifacts[{index}] equivalence review requires {field}")

    canonical = {k: v for k, v in data.items() if k not in {"content_hash", "approval", "downstream_artifacts"}}
    observed = hashlib.sha256(
        json.dumps(canonical, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()
    if data["content_hash"] != observed:
        fail(f"content_hash does not match canonical payload; expected {observed}")
    return []


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_requirements_baseline.py <baseline.json>")
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail("baseline root must be an object")
        warnings = validate(data)
    except (OSError, json.JSONDecodeError, ValueError, TypeError, KeyError) as exc:
        print(f"FAIL: {exc}")
        return 1
    for warning in warnings:
        print(f"WARNING: {warning}")
    print("PASS: requirements baseline structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
