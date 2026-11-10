#!/usr/bin/env python3
"""Validate structural consistency of a Testing & Verification evidence JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


VERDICTS = {"PASS", "FAIL", "BLOCKED", "INSUFFICIENT EVIDENCE", "NOT APPLICABLE"}
RESULTS = {
    "PASS",
    "FAIL",
    "SKIPPED",
    "FLAKY",
    "BLOCKED",
    "NOT RUN",
    "NOT APPLICABLE",
    "INFRASTRUCTURE FAILURE",
}
STRENGTHS = {"STRONG", "MODERATE", "WEAK", "ABSENT"}
COUNT_KEYS = {
    "passed",
    "failed",
    "skipped",
    "flaky",
    "not_run",
    "infrastructure_failure",
}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(document: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["root must be a JSON object"]

    for field in ("subject", "verdict", "reason"):
        if not nonempty_string(document.get(field)):
            errors.append(f"{field} must be a non-empty string")

    verdict = document.get("verdict")
    if verdict not in VERDICTS:
        errors.append(f"verdict must be one of: {', '.join(sorted(VERDICTS))}")

    criteria = document.get("criteria")
    if not isinstance(criteria, list):
        errors.append("criteria must be an array")
        criteria = []

    seen_ids: set[str] = set()
    material_criteria: list[dict[str, Any]] = []
    for index, criterion in enumerate(criteria):
        prefix = f"criteria[{index}]"
        if not isinstance(criterion, dict):
            errors.append(f"{prefix} must be an object")
            continue
        criterion_id = criterion.get("id")
        if not nonempty_string(criterion_id):
            errors.append(f"{prefix}.id must be a non-empty string")
        elif criterion_id in seen_ids:
            errors.append(f"{prefix}.id duplicates {criterion_id!r}")
        else:
            seen_ids.add(criterion_id)
        if not nonempty_string(criterion.get("statement")):
            errors.append(f"{prefix}.statement must be a non-empty string")
        if not isinstance(criterion.get("material"), bool):
            errors.append(f"{prefix}.material must be boolean")
        elif criterion["material"]:
            material_criteria.append(criterion)
        result = criterion.get("result")
        if result not in RESULTS:
            errors.append(f"{prefix}.result must be a recognized result")
        strength = criterion.get("strength")
        if strength not in STRENGTHS:
            errors.append(f"{prefix}.strength must be one of: {', '.join(sorted(STRENGTHS))}")
        evidence = criterion.get("evidence")
        if not isinstance(evidence, list) or not all(nonempty_string(item) for item in evidence):
            errors.append(f"{prefix}.evidence must be an array of non-empty strings")

    runs = document.get("runs")
    if not isinstance(runs, list):
        errors.append("runs must be an array")
        runs = []
    for index, run in enumerate(runs):
        prefix = f"runs[{index}]"
        if not isinstance(run, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for field in ("id", "environment"):
            if not nonempty_string(run.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string")
        counts = run.get("counts")
        if not isinstance(counts, dict):
            errors.append(f"{prefix}.counts must be an object")
            continue
        for key in COUNT_KEYS:
            value = counts.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                errors.append(f"{prefix}.counts.{key} must be a non-negative integer")

    if verdict == "PASS":
        if not material_criteria:
            errors.append("PASS requires at least one material criterion")
        for criterion in material_criteria:
            criterion_id = criterion.get("id", "<unknown>")
            if criterion.get("result") != "PASS":
                errors.append(f"PASS conflicts with material criterion {criterion_id}: {criterion.get('result')}")
            if criterion.get("strength") in {"WEAK", "ABSENT"}:
                errors.append(f"PASS conflicts with weak/absent evidence for material criterion {criterion_id}")
            if not criterion.get("evidence"):
                errors.append(f"PASS requires evidence for material criterion {criterion_id}")
        for index, run in enumerate(runs):
            counts = run.get("counts") if isinstance(run, dict) else None
            if isinstance(counts, dict):
                non_pass_keys = COUNT_KEYS - {"passed"}
                bad = sum(counts.get(key, 0) for key in non_pass_keys if isinstance(counts.get(key, 0), int))
                if bad:
                    errors.append(f"PASS conflicts with non-pass counts in runs[{index}]")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence", type=Path, help="Path to a JSON evidence file")
    args = parser.parse_args()
    try:
        with args.evidence.open("r", encoding="utf-8") as handle:
            document = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2

    errors = validate(document)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
