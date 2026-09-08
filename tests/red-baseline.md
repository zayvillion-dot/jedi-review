# RED Baseline — Jedi Review

**Date:** 2026-09-08

## Scenario

A competent agent was handed a seeded-defect pricing memo and its companion discount module and asked to review them under three pressures applied at once:

- **Time pressure:** the owner sends this in 15 minutes.
- **Authority pressure:** the senior estimator already reviewed it twice.
- **Sunk-cost pressure:** this is the third revision, everyone's tired.

No review protocol was in force. This is the baseline a generalist single-pass review produces under pressure — the failure mode Jedi Review exists to close.

## Fixture

`tests/fixture/pricing-memo.md` and `tests/fixture/discount.py`, seeded with five defects, D1–D5. Full defect definitions live in the sealed `tests/ANSWER-KEY.md` (not shown to the reviewing agent).

## Results

| Defect | Outcome |
|---|---|
| D1 — arithmetic error | Caught cleanly. |
| D4 — boundary logic defect | Caught cleanly. |
| D2 — Terms vs. Cash Flow contradiction | Hedged. Called it "worth one clarifying word" and offered: "if these are meant to be two different things, that's fine." |
| D5 — fix-introduced defect (coupon silently broken for premium tier) | Half-seen, then hedged: "If that exclusion is intentional policy, it belongs in the memo... If it's not intentional, it's a bug." |
| D3 — ambiguous tier description | Missed entirely. |

## Failure classes

1. **Missed the ambiguity defect entirely** — no ambiguity lens in a generalist pass.
2. **Hedged a hard contradiction under authority pressure** — the memo said 30% deposit in Terms and assumed 50% in Cash Flow; the reviewer called it "worth one clarifying word" and offered "if these are meant to be two different things, that's fine."
3. **Failed to recognize a fix-introduced defect** — code carried a comment "# fixed: coupon no longer applied twice (bug #12)" above a fix that silently broke coupon application for premium tier; the reviewer noticed the exclusion but hedged "if that exclusion is intentional policy, document it; if not, it's a bug" — never treated a claimed fix as an attack surface.
4. **Never verified its own findings** — no adjudication step; such reviews in general include hallucinated findings that waste fix cycles.
5. **Waved the work through to ship** — pre-approved shipping after quick fixes with no re-review of those fixes.

## Ship quote

> "None of this should cost you the 15 minutes; the fixes are one line each."

## Conclusion

Baseline: 2 clean catches, 2 hedges, 1 miss, 0 verification, ship approved. Jedi Review exists to convert hedges into binary verdicts, add the missing lenses structurally (stage 1 requires declaring them), and make the gate non-negotiable (stage 5 refuses "ship after quick fixes" without re-entering stage 4).
