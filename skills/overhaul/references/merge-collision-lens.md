# Merge-collision lens

Run this against every file two sources both touched before an auto-merge is trusted — two legs in the same session, or a leg and a moving `origin/main`. An auto-merge that resolves cleanly at the text level can still silently drop a line, or let two independently-correct changes combine into a behavior neither side intended.

This is not jedi-review's fix-blast-radius lens (that one attacks a single fix's reach). This lens attacks the *merge itself* — the act of combining two deltas into one file.

## What it proves

For every auto-merged shared file, prove — in both directions — that the merged file contains the exact union of both sides' deltas:

1. Diff the pre-merge file against each side's post-change version independently.
2. Diff the merged file against each side's post-change version.
3. Every line either side added is present in the merged file (no lost-line).
4. No line survives in the merged file that either side had deleted (no resurrected-line).
5. Where both sides touched the *same* lines (a true text conflict, not just a nearby-lines coincidence), read the resolution as its own small finding — a clean text merge can still combine two changes into a broken behavior (see the worked example below).

## Worked example (from a real session)

Two changes landed on the same paper-rendering file: one gated a discount label on `discount_reason` for five existing customer-facing renderers; a second change added a sixth renderer (a flattened snapshot) reading the discount flag alone, with no `discount_reason` check. The merge was textually clean — no conflict markers, nothing lost — and still wrong: a reason-less discount now printed on the sixth renderer's paper while the other five correctly refused it. The merge-collision lens is what catches this class of defect; a lost-line proof alone would have called it MERGE CLEAN.

Fix pattern: pull the gating predicate into one shared function all six call sites use, so the sixth reader can't silently diverge from the other five's rule.

## Report format

```
Merge-collision lens (Leg 6 × Leg 7, file app/templates/base.html):
  Lost-line: 0/0 both directions
  Resurrected-line: 0/0 both directions
  True conflicts: 1 (nav include block) — resolution re-attacked: CLEAN
  Verdict: MERGE CLEAN
```

or, when the lens finds something:

```
Merge-collision lens (W-H4 × Leg 16b, file _paper_context.py):
  Lost-line: 0/0 both directions
  Resurrected-line: 0/0 both directions
  True conflicts: 0 (no shared lines — the defect is behavioral, not textual)
  Verdict: 1 MED — a sixth reader added by one side doesn't honor a gating
    predicate the other side just introduced on five siblings.
  → dispatched as its own fix leg, single-owner file, jedi-reviewed before
    it re-enters the batch.
```

A finding here is fixed as its own small leg (single-owner file, jedi-reviewed) before the batch gate runs — it is not patched inline on the integration branch.
