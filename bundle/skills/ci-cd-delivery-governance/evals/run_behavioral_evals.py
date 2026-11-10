#!/usr/bin/env python3
"""Run decision-focused CI/CD governance scenarios against the evaluator."""

from __future__ import annotations

import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from evaluate_delivery import evaluate  # noqa: E402


def contains_codes(result: dict, expected_codes: list[str]) -> bool:
    actual = {item["code"] for item in result.get("blockers", [])}
    return set(expected_codes).issubset(actual)


def main() -> int:
    cases = json.loads((HERE / "scenarios.json").read_text(encoding="utf-8"))
    failures = []
    rows = []
    for case in cases:
        result = evaluate(case["record"])
        expected = case["expected"]
        checks = {
            "activate": result["activate"] == expected["activate"],
            "status": result["status"] == expected["status"],
            "risk": result["risk"] == expected["risk"],
            "blockers": contains_codes(result, expected.get("blocker_codes", [])),
            "classifications": set(expected.get("classifications", [])).issubset(result.get("classifications", [])),
        }
        passed = all(checks.values())
        rows.append({"id": case["id"], "name": case["name"], "passed": passed, "checks": checks, "result": result})
        if not passed:
            failures.append(rows[-1])

    report = {"total": len(rows), "passed": len(rows) - len(failures), "failed": len(failures), "cases": rows}
    (HERE / "latest-results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Behavioral evals: {report['passed']}/{report['total']} passed")
    for row in failures:
        print(f"FAIL {row['id']}: {row['checks']}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
