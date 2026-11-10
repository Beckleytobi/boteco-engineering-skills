# AI-specific regression failure modes

This is the catalogue of ways an AI coding agent's own process, not just its code, produces a false "regression safe" verdict. It's worth reading whenever a change is above the lowest risk tier, because these patterns are exactly what makes an agent's self-report unreliable and exactly why this skill exists as a separate check rather than trusting the implementing agent's own confidence.

## Process failure modes to watch for

- Testing only the feature that was just implemented, and treating that as sufficient.
- Ignoring indirect dependents because they don't appear in the diff.
- Treating a successful compile or build as evidence that behavior was preserved (it only proves the code is syntactically and type-valid, not that it does the same thing).
- Rewriting a shared utility without tracing who actually consumes it first.
- Modifying a schema without checking it against existing data, not just new data.
- Changing error semantics as a side effect, without intending to or noticing.
- Changing a default value and not tracing who relied on the old default.
- Changing authorization behavior as an incidental consequence of an unrelated change.
- Swapping a library or dependency and assuming behavioral equivalence rather than verifying it.
- Deleting code that looks unused but is actually referenced dynamically (reflection, string-based dispatch, config-driven wiring).
- Changing environment or configuration assumptions without checking what depended on the old ones.
- Updating a mock to match new code without checking whether the mock still reflects reality.
- Running only the newly created tests and reporting that as the regression check.

Any one of these, spotted during Phase B or C of the main workflow, is a reason to widen the investigation rather than proceed on the assumption that the rest of the change is fine.

## Test integrity: is the implementation correct, or did the test move?

This deserves separate, deliberate attention whenever tests and implementation changed together, because it's the failure mode most likely to produce a clean-looking report that's actually hiding a regression. The question to ask directly: did the implementation become correct, or did the test get changed so the implementation appears correct?

None of this means every test change alongside an implementation change is suspicious - tests legitimately need updating when behavior legitimately changes. The point is to actually look at *why* each test changed, and to say which of these four buckets it falls into rather than waving it through because "the tests pass now":

- **Legitimate.** The requirement itself intentionally changed, and the previous expectation is genuinely no longer valid. The test change should map cleanly onto a described behavior change.
- **Additive.** New regression coverage is being added, not replacing or loosening anything that existed before.
- **Suspicious.** An assertion got weakened or removed, a test got skipped or deleted rather than fixed, an expected value got quietly edited to match new (possibly wrong) output, a mock got broadened in a way that stops it catching what it used to catch, or setup/validation got bypassed - and none of it maps to an intentional, described behavior change. This is a stronger signal than almost anything else in this workflow and should raise the regression confidence bar rather than being treated as routine cleanup.
- **Ambiguous.** It's genuinely unclear which of the above applies, usually because the expected behavior itself isn't clearly specified anywhere.

Suspicious and ambiguous test changes deserve independent review before the surrounding change is treated as safe - don't resolve the ambiguity by defaulting to "probably fine."
