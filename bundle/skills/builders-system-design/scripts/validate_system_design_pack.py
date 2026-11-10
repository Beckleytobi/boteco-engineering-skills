#!/usr/bin/env python3
"""Validate the completeness and internal discipline of a generated design pack."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FILES = {
    "SYSTEM_DESIGN_STATE.md": [
        "## Product snapshot",
        "## Known facts",
        "## Assumptions",
        "## Confirmed decisions",
        "## Open questions",
        "## Next interview round",
        "## Change log",
    ],
    "PRODUCT_SYSTEM_BLUEPRINT.md": [
        "## Executive design summary",
        "## Users, actors, and critical journeys",
        "## System boundary",
        "## Workload and data estimates",
        "## Quality constraints",
        "## Domain and data ownership",
        "## Identity, authorization, and trust boundaries",
        "## Critical-journey sequence",
        "## Component decision ledger",
        "## Failure, degradation, and recovery",
        "## Observability and cost controls",
        "## Verification plan",
    ],
    "ARCHITECTURE_DECISIONS.md": ["## Index"],
    "SYSTEM_BUILD_ROADMAP.md": [
        "## Roadmap principles",
        "## P0 — Walking skeleton",
        "## P1 — First critical journey",
        "## Triggered scale work",
    ],
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"\[Product\]", re.I),
    re.compile(r"\[date(?:/time)?\]", re.I),
    re.compile(r"\[One paragraph in product language\.\]", re.I),
    re.compile(r"\[Repeat the phase fields", re.I),
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

    blueprint = texts.get("PRODUCT_SYSTEM_BLUEPRINT.md", "")
    if blueprint:
        # Visual evidence (or justified omission) is checked by validate_pack below.
        # Do not impose a separate Mermaid-only requirement on the blueprint.
        for status in ("Required now", "Deferred", "Conditional", "Excluded"):
            if status not in blueprint:
                warnings.append(
                    f"PRODUCT_SYSTEM_BLUEPRINT.md: component status '{status}' is not represented; "
                    "confirm this is intentional"
                )

    decisions = texts.get("ARCHITECTURE_DECISIONS.md", "")
    roadmap = texts.get("SYSTEM_BUILD_ROADMAP.md", "")
    if decisions and not re.search(r"ADR-\d{3}", decisions):
        errors.append("ARCHITECTURE_DECISIONS.md: no ADR-NNN identifier found")
    if roadmap and not re.search(r"acceptance evidence", roadmap, re.I):
        errors.append("SYSTEM_BUILD_ROADMAP.md: no acceptance evidence found")

    for filename, text in texts.items():
        if re.search(r"\b(TODO|TBD)\b", text, re.I):
            warnings.append(f"{filename}: contains TODO/TBD; ensure it is tracked as an open question")

    if not allow_placeholders:
        from validate_design_handoff import validate_handoff
        errors.extend(validate_handoff(root, 'HLD'))
        from validate_visual_pack import validate_pack
        visual_errors = validate_pack(root)
        errors.extend(visual_errors)

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="Path containing the four system-design Markdown files")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow template placeholders (useful when validating the bundled assets)",
    )
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
    print(f"PASS: design pack structure is valid ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
