#!/usr/bin/env python3
"""
Generate a Production Readiness report skeleton.

This does NOT do any assessment work. It only scaffolds the markdown
structure defined in references/report-template.md, pre-filled with the
category-group headers relevant to the chosen groups, so the report you
write follows a consistent shape without retyping the template by hand.

Usage:
    python3 report_skeleton.py "Ramahlux Stripe webhook handler" \\
        --tier 3 \\
        --groups deployment-database external-dependencies data-integrity

Run with --list-groups to see the valid group keys.
"""

import argparse
import sys

GROUPS = {
    "env-secrets": "Environment, Configuration & Secrets",
    "deployment-database": "Deployment & Database Safety",
    "rollback-recovery": "Rollback, Backup & Progressive Rollout",
    "observability-errors": "Observability & Error Handling",
    "external-dependencies": "External Dependencies & Resilience",
    "scale-performance": "Scale, Performance & Resource Bounds",
    "data-integrity": "Data Integrity & Concurrency",
}

TIER_LABELS = {
    "0": "Tier 0: low stakes, easily reversible",
    "1": "Tier 1: standard feature, real users, no money or sensitive data",
    "2": "Tier 2: money, sensitive data, or costly-to-reverse changes",
    "3": "Tier 3: payments, health, regulated data, high traffic, or hard-to-undo actions",
}


def build_skeleton(subject: str, tier: str, groups: list[str]) -> str:
    tier_label = TIER_LABELS.get(tier, f"Tier {tier}")
    lines = []
    lines.append(f"# Production Readiness Assessment: {subject}")
    lines.append("")
    lines.append(f"**Risk tier:** {tier_label} (why: name the driving factor)")
    lines.append("")
    lines.append("**Bottom line:** [safe to ship as-is / safe once blocking items fixed / not yet, and why]")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## What this covers")
    lines.append("")
    lines.append("[what was actually assessed, and what couldn't be inspected]")
    lines.append("")
    lines.append("## Already in good shape")
    lines.append("")
    lines.append("- [thing that's already fine]")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    for key in groups:
        if key not in GROUPS:
            continue
        lines.append(f"### {GROUPS[key]}")
        lines.append("")
        lines.append("**[BLOCKING | SHOULD FIX BEFORE LAUNCH | CAN FOLLOW AFTER LAUNCH]: [finding title]**")
        lines.append("")
        lines.append("What's true today: ")
        lines.append("")
        lines.append("What that means in practice: ")
        lines.append("")
        lines.append("Fix: ")
        lines.append("")
    lines.extend(["## Visual evidence (when useful)", "", "Record a deployment/dependency/failure view or explain non-applicability. Keep architecture proposals with System Design.", "", "| Diagram ID/version | Purpose/level | Source/hash | Baseline/decisions | Validation evidence | Approval/freshness |", "|---|---|---|---|---|---|", "| | | | | | |", "", "Keep machine-readable records in diagram-records/ and run scripts/validate_visual_pack.py before claiming visual completion.", ""])
    lines.append("## Action plan")
    lines.append("")
    lines.append("**Before launch:**")
    lines.append("1. ")
    lines.append("")
    lines.append("**Soon after launch:**")
    lines.append("1. ")
    lines.append("")
    lines.append("**When it becomes relevant:**")
    lines.append("1. ")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("subject", nargs="?", help="What's being assessed, e.g. 'Stripe webhook handler'")
    parser.add_argument("--tier", choices=["0", "1", "2", "3"], help="Risk tier from references/risk-tiering.md")
    parser.add_argument(
        "--groups",
        nargs="+",
        choices=list(GROUPS.keys()),
        default=[],
        help="Which category-playbook groups had findings (only include groups that actually apply)",
    )
    parser.add_argument("--list-groups", action="store_true", help="Print valid group keys and exit")
    args = parser.parse_args()

    if args.list_groups:
        for key, label in GROUPS.items():
            print(f"{key}: {label}")
        return

    if not args.subject or not args.tier:
        parser.error("subject and --tier are required unless using --list-groups")

    print(build_skeleton(args.subject, args.tier, args.groups))


if __name__ == "__main__":
    sys.exit(main())
