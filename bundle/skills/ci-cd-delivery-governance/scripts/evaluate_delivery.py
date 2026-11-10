#!/usr/bin/env python3
"""Evaluate a structured delivery evidence record without granting authority."""

from __future__ import annotations

import json
import sys
from pathlib import Path


VALID_STATUSES = {
    "PASS",
    "FAIL",
    "BLOCKED",
    "PASS WITH CONDITIONS",
    "APPROVAL REQUIRED",
    "NOT APPLICABLE",
    "NOT RUN",
    "UNKNOWN",
    "PASS WITH CONCERNS",
    "ESCALATE",
}

ACTIVE_TASK_KINDS = {
    "delivery",
    "pipeline",
    "pull_request",
    "merge",
    "release",
    "deployment",
    "ci_failure",
    "hotfix",
}

HIGH_RISK_CLASSES = {
    "authentication",
    "authorization",
    "payments",
    "sensitive_data",
    "destructive_migration",
    "secrets",
    "infrastructure",
    "ci_config",
    "branch_protection",
    "production_config",
    "security_control",
}


def _add(blockers: list[dict[str, str]], code: str, message: str) -> None:
    if not any(item["code"] == code for item in blockers):
        blockers.append({"code": code, "message": message})


def _risk(record: dict) -> str:
    supplied = str(record.get("risk", "UNKNOWN")).upper()
    classes = set(record.get("change_classes", []))
    if classes & HIGH_RISK_CLASSES:
        return "HIGH"
    deployment = record.get("deployment", {})
    if record.get("environment") == "production" and deployment.get("concurrency_conflict"):
        return "HIGH"
    if record.get("environment") == "production" and deployment.get("health_status") == "FAIL" and record.get("critical_health_check"):
        return "HIGH"
    return supplied if supplied in {"LOW", "MEDIUM", "HIGH"} else "UNKNOWN"


def evaluate(record: dict) -> dict:
    task_kind = record.get("task_kind", "delivery")
    if task_kind not in ACTIVE_TASK_KINDS:
        return {
            "activate": False,
            "risk": _risk(record),
            "status": "NOT APPLICABLE",
            "classifications": [],
            "blockers": [],
            "next_action": "Route to the skill that owns the requested work.",
        }

    blockers: list[dict[str, str]] = []
    classifications: list[str] = []
    conditions: list[str] = list(record.get("conditions", []))
    risk = _risk(record)

    if not record.get("discovery_complete", False):
        _add(blockers, "DISCOVERY_REQUIRED", "Repository and delivery discovery is incomplete.")

    for gate in record.get("gates", []):
        name = gate.get("name", "unnamed gate")
        status = str(gate.get("status", "UNKNOWN")).upper()
        required = gate.get("required", True)
        if status not in VALID_STATUSES:
            _add(blockers, "INVALID_STATUS", f"{name} uses invalid status {status!r}.")
            continue
        if required and status in {"FAIL", "BLOCKED", "UNKNOWN", "NOT RUN", "APPROVAL REQUIRED", "ESCALATE"}:
            _add(blockers, f"GATE_{status.replace(' ', '_')}", f"Required gate {name} is {status}.")
        if required and status in {"PASS", "PASS WITH CONDITIONS", "PASS WITH CONCERNS"} and not gate.get("evidence"):
            _add(blockers, "MISSING_GATE_EVIDENCE", f"Required gate {name} has no evidence reference.")
        if status in {"PASS WITH CONDITIONS", "PASS WITH CONCERNS"}:
            gate_conditions = gate.get("conditions", [])
            if not gate_conditions:
                _add(blockers, "UNOWNED_CONDITION", f"{name} passed with conditions but none were recorded.")
            conditions.extend(gate_conditions)

    control = record.get("control_change", {})
    if control.get("weakens_or_removes") and not control.get("separate_authority_verified"):
        _add(blockers, "CONTROL_SELF_PROTECTION", "A control is weakened or removed without separate verified authority.")

    if record.get("green_by_deleting_or_skipping_tests"):
        _add(blockers, "UNSAFE_GREEN_SHORTCUT", "Tests are being deleted or skipped merely to obtain green CI.")

    review = record.get("independent_review", {})
    if review.get("serious_finding") and not review.get("resolved_with_evidence"):
        _add(blockers, "SERIOUS_REVIEW_FINDING", "A serious independent-review finding remains unresolved.")

    failure = record.get("failure", {})
    if failure.get("kind") == "ci_provider":
        classifications.append("CI_INFRASTRUCTURE_FAILURE")
        _add(blockers, "CI_INFRASTRUCTURE_UNAVAILABLE", "CI provider failure leaves application status unverified.")
    if failure.get("kind") == "flaky_test" and not failure.get("classified_and_remediated"):
        classifications.append("SUSPECTED_FLAKY_TEST")
        _add(blockers, "FLAKY_TEST_UNRESOLVED", "A suspected flaky required test is not yet classified and remediated.")

    migration = record.get("migration", {})
    if migration.get("present"):
        if migration.get("tested_only_on_empty_database"):
            _add(blockers, "MIGRATION_EXISTING_DATA_UNKNOWN", "Migration evidence covers only an empty database.")
        if migration.get("destructive") and not migration.get("existing_data_impact_verified"):
            _add(blockers, "DESTRUCTIVE_MIGRATION_DATA_RISK", "Destructive migration lacks existing-data impact evidence.")
        if migration.get("destructive") and not migration.get("recovery_verified"):
            _add(blockers, "DESTRUCTIVE_MIGRATION_RECOVERY", "Destructive migration lacks a verified recovery path.")

    secrets = record.get("secrets", {})
    if secrets.get("exposed"):
        _add(blockers, "SECRET_EXPOSURE", "A secret exposure requires containment, rotation, and verified remediation.")
    if record.get("environment") == "production" and secrets.get("required_available") is False:
        _add(blockers, "MISSING_PRODUCTION_SECRET", "A required production secret is unavailable.")

    deployment = record.get("deployment", {})
    health_failed = deployment.get("status") == "PASS" and deployment.get("health_status") == "FAIL"
    if health_failed:
        classifications.append("POST_DEPLOY_HEALTH_FAILURE")
        _add(blockers, "POST_DEPLOY_HEALTH_FAILED", "Deployment completed but required application health verification failed.")
    if deployment.get("concurrency_conflict") and not deployment.get("safe_concurrency_strategy"):
        _add(blockers, "DEPLOYMENT_CONCURRENCY", "A conflicting deployment has no verified serialization or isolation strategy.")
    if record.get("environment") == "production" and risk == "HIGH":
        if deployment.get("recovery_status") != "PASS" or not deployment.get("recovery_evidence"):
            _add(blockers, "RECOVERY_NOT_VERIFIED", "High-risk production delivery lacks verified recovery evidence.")

    hotfix = record.get("hotfix", {})
    if hotfix.get("enabled") and not hotfix.get("emergency_authority_verified"):
        _add(blockers, "HOTFIX_AUTHORITY", "Hotfix emergency authority is not verified.")
    if hotfix.get("enabled") and not hotfix.get("traceability_recorded"):
        _add(blockers, "HOTFIX_TRACEABILITY", "Hotfix traceability is incomplete.")
    if hotfix.get("enabled") and record.get("decision_stage") == "pre_deploy" and deployment.get("health_status") != "PASS":
        conditions.append("Post-deploy health verification and monitoring remain required before completion.")

    authority = record.get("authority", {})
    authority_missing = authority.get("required", False) and not authority.get("verified", False)

    if health_failed:
        status = "BLOCKED"
        next_action = "Stop the rollout and execute the authorized rollback or recovery path; then verify recovered health."
    elif blockers:
        status = "BLOCKED"
        next_action = "Resolve the listed blockers and collect fresh evidence before progressing."
    elif authority_missing:
        status = "APPROVAL REQUIRED"
        next_action = f"Obtain approval from {authority.get('owner', 'the authorized owner')} before progressing."
    elif conditions:
        status = "PASS WITH CONDITIONS"
        next_action = "Progress only while the recorded conditions remain owned and satisfied."
    else:
        status = "PASS"
        next_action = "Progress through the authorized delivery path and continue verification for the next stage."

    return {
        "activate": True,
        "risk": risk,
        "status": status,
        "gate_statuses": {"post_deploy_health": "FAIL"} if health_failed else {},
        "classifications": classifications,
        "blockers": blockers,
        "conditions": conditions,
        "next_action": next_action,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: evaluate_delivery.py <evidence.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
        result = evaluate(record)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
