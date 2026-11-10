#!/usr/bin/env python3
"""Validate the structure and core consistency of a software-design pack."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FILES = {
    "SOFTWARE_DESIGN_STATE.md": [
        "## Change snapshot",
        "## Observed from repository",
        "## Requirements and invariants",
        "## Assumptions",
        "## Confirmed decisions",
        "## Open questions",
        "## Next actions",
        "## Change log",
    ],
    "FEATURE_SOFTWARE_DESIGN.md": [
        "## Behaviour and scope",
        "## Business rules and invariants",
        "## Current design evidence",
        "## Change-impact map",
        "## Responsibility map",
        "## Contracts and dependency direction",
        "## State ownership and transitions",
        "## Error and recovery behaviour",
        "## Design-mechanism decisions",
        "## Compatibility, migration, and rollout",
        "## Verification design",
    ],
    "SOFTWARE_DESIGN_DECISIONS.md": ["## Index"],
    "CHANGE_IMPLEMENTATION_PLAN.md": [
        "## Plan constraints",
        "## Step 0 — Protect current behaviour",
        "## Step 1 — Create the smallest required seam",
        "## Step 2 — Deliver one end-to-end behaviour slice",
        "## Deferred design work",
    ],
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"\[Feature or (?:Change|Product)\]", re.I),
    re.compile(r"\[date(?:/time)?\]", re.I),
    re.compile(r"\[Repeat the step fields", re.I),
)


def validate(root: Path, allow_placeholders: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    texts: dict[str, str] = {}

    for filename, headings in FILES.items():
        path = root / filename
        if not path.is_file():
            errors.append(f"Missing required file: {filename}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[filename] = text
        for heading in headings:
            if heading not in text:
                errors.append(f"{filename}: missing section '{heading}'")
        if not allow_placeholders:
            for pattern in PLACEHOLDER_PATTERNS:
                if pattern.search(text):
                    errors.append(f"{filename}: unresolved placeholder matching {pattern.pattern!r}")

    design = texts.get("FEATURE_SOFTWARE_DESIGN.md", "")
    if design:
        for status in ("Keep", "Introduce", "Defer", "Reject"):
            if status not in design:
                warnings.append(
                    f"FEATURE_SOFTWARE_DESIGN.md: mechanism status '{status}' is not represented; "
                    "confirm this is intentional"
                )
        if not re.search(r"invariant", design, re.I):
            errors.append("FEATURE_SOFTWARE_DESIGN.md: no invariant is represented")
        if not re.search(r"verification", design, re.I):
            errors.append("FEATURE_SOFTWARE_DESIGN.md: no verification design is represented")

    decisions = texts.get("SOFTWARE_DESIGN_DECISIONS.md", "")
    plan = texts.get("CHANGE_IMPLEMENTATION_PLAN.md", "")
    if decisions and not re.search(r"SDD-\d{3}", decisions):
        errors.append("SOFTWARE_DESIGN_DECISIONS.md: no SDD-NNN identifier found")
    if plan and not re.search(r"tests?/checks?", plan, re.I):
        errors.append("CHANGE_IMPLEMENTATION_PLAN.md: no tests/checks evidence found")

    for filename, text in texts.items():
        if re.search(r"\b(TODO|TBD)\b", text, re.I):
            warnings.append(f"{filename}: contains TODO/TBD; track it explicitly as an open question")

    if not allow_placeholders:
        from validate_design_handoff import validate_handoff
        errors.extend(validate_handoff(root, 'LLD'))
        from validate_visual_pack import validate_pack
        visual_errors = validate_pack(root)
        errors.extend(visual_errors)

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Directory containing the four software-design files")
    parser.add_argument("--allow-placeholders", action="store_true", help="Allow bundled template placeholders")
    args = parser.parse_args()

    root = args.directory.resolve()
    if not root.is_dir():
        print(f"ERROR: directory does not exist: {root}")
        return 2

    errors, warnings = validate(root, args.allow_placeholders)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: software-design pack structure is valid ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
