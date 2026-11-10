# OPERATIONS visual routing

Annotate observed topology, critical dependencies, failure scenarios and recovery paths when useful to a finding. Do not author replacement architecture or grant release authority.

Read [Visual Design Contract](visual-design-contract.md) before creating or consuming diagrams. Its shared rules govern metadata, provenance, validation, versioning and handoffs. Preserve the existing skill output and verdict contracts. Add a diagram register to the existing artifact rather than creating competing specifications.

Run `python scripts/validate_visual_pack.py <artifact-directory>` before claiming visual completion. Missing records or checks remain incomplete.

Use visual-coverage.json under VDC-1.1.0 to record supplied, justified omitted and incomplete views before claiming visual completion. Consumers retain the specialist owner and its inventory.
