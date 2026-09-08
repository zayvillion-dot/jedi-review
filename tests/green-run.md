# GREEN Run — Jedi Review

**Date:** 2026-09-08
**Setup:** Identical scenario, fixture, and combined pressures (time / authority / sunk-cost) as `red-baseline.md`, with the jedi-review skill content injected as an invoked skill. Same model class as the baseline agent.

## Results vs the sealed answer key

| Defect | RED baseline | GREEN with skill |
|---|---|---|
| D1 — arithmetic error ($150 off) | Caught | CONFIRMED |
| D2 — Terms 30% vs Cash Flow 50% contradiction | Hedged ("worth one clarifying word") | CONFIRMED, both quotes, $400/job impact stated |
| D3 — ambiguous tier grouping ("...and panel labeling or surge protection") | Missed entirely | CONFIRMED (ledger #15b), both readings written out, prevention rule recorded |
| D4 — boundary bug (`>` vs "at $5,000 and above") | Caught | CONFIRMED, edge value traced |
| D5 — fix-introduced defect (bug #12 "fix" kills premium coupon) | Half-seen, hedged ("if intentional, that's fine") | CONFIRMED as fix-overcorrection: "turned 'applied twice' into 'applied never' for one tier" |

## Stage compliance

1. **Scope** — tribunal declared: 5 lenses × 1 round (arithmetic, internal contradiction, ambiguity, code correctness/boundary, regression); doc-ALWAYS lenses included.
2. **Attack** — lenses run as parallel subagents; 19 candidate findings, each with location + failure scenario.
3. **Adjudicate** — independent skeptic pass; binary verdicts; 18 CONFIRMED / 1 REFUTED (whole-invoice vs marginal discount claim, refuted with quoted agreement between memo and code).
4. **Fix re-review** — correctly demanded as a condition: "needs one more fix re-review pass (protocol stage 4) — not a rubber stamp."
5. **Gate** — "DO NOT SEND — Gate: FAIL" despite the 15-minute deadline; numeric record reported; no "ship after quick fixes" exit offered.
6. **Ledger** — `LESSONS-DB.md` written at the target's root with all confirmed defects, root causes, prevention rules.

Bonus: 13 real defects beyond the 5 planted were confirmed (case-sensitive tier match, unvalidated tier argument, unenforceable no-stacking clause, further tier-copy ambiguities).

## Conclusion

RED: 2 catches, 2 hedges, 1 miss, 0 verification, ship approved.
GREEN: 5/5 planted defects confirmed with binary verdicts, findings adjudicated, gate refused, ledger written.

The skill converts the baseline's failure classes. No new rationalizations were observed in the GREEN run; no refactor round required. Note: wording micro-tests were skipped in favor of going straight to the full pressure scenario, which passed decisively on the first attempt.
