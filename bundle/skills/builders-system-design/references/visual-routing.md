# HLD visual routing

Produce context, components, responsibilities, data flows, integration and trust boundaries; deployment and failure/resilience views when justified. Keep the existing journey sequence cross-system. Link every LLD consumer to approved HLD versions.

Read [Visual Design Contract](visual-design-contract.md) before creating or consuming diagrams. Its shared rules govern metadata, provenance, validation, versioning and handoffs. Preserve the existing skill output and verdict contracts. Add a diagram register to the existing artifact rather than creating competing specifications.

Run `python scripts/validate_visual_pack.py <artifact-directory>` before claiming visual completion. Missing records or checks remain incomplete.

Use visual-coverage.json under VDC-1.1.0 to record supplied, justified omitted and incomplete views before claiming visual completion. Consumers retain the specialist owner and its inventory.
