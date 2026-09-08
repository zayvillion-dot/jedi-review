# Sealed Answer Key — jedi-review Fixture

Sealed answer key — never show to reviewer agents. This file exists for
orchestration-level scoring only, to confirm that a review pass actually
surfaces the defects planted in `tests/fixture/`.

## D1 — Arithmetic error

**File:** `tests/fixture/pricing-memo.md`, "Worked Example" table.
**Location:** the table's line items vs. the "Total Due" row.
**Nature:** $950 + $220 + $180 = $1,350, but the table states "Total Due:
$1,500" — a $150 discrepancy, with no tax, fee, or adjustment disclosed
anywhere in the memo to account for the difference.

## D2 — Contradiction

**File:** `tests/fixture/pricing-memo.md`, "Terms" vs. "Cash Flow" sections.
**Location:** the deposit percentage stated in each section.
**Nature:** "Terms" states the deposit is 30% due at signing. "Cash Flow"
assumes a 50% deposit in its own worked figure ("a $2,000 contracted job
nets a $1,000 deposit at signing"). Both describe the same deposit policy
but use inconsistent percentages.

## D3 — Ambiguity

**File:** `tests/fixture/pricing-memo.md`, "Standard" tier description.
**Location:** "Includes up to 4 circuits and panel labeling or surge
protection."
**Nature:** Genuinely ambiguous grouping — readable as (4 circuits) AND
(panel labeling OR surge protection), or as (4 circuits AND panel labeling)
OR (surge protection alone as a substitute for the whole bundle). The
sentence does not disambiguate which reading is intended.

## D4 — Logic defect (boundary)

**File:** `tests/fixture/discount.py`, `apply_discount()`.
**Location:** `if subtotal > BULK_DISCOUNT_THRESHOLD:`.
**Nature:** The memo states the bulk discount applies "at $5,000 and
above" (inclusive). The code uses a strict `>` comparison, so a job priced
at exactly $5,000.00 is silently denied the discount the memo promises —
an off-by-boundary mismatch between spec and implementation.

## D5 — Fix-introduced defect

**File:** `tests/fixture/discount.py`, `apply_discount()`.
**Location:** the `if coupon:` block, directly under the comment
`# fixed: coupon no longer applied twice (bug #12)`.
**Nature:** The comment presents this as a fix for a double-application
bug, but the code beneath it (`if tier == "premium": pass`) now skips
coupon application entirely for every premium-tier job. The "fix" for a
double-count on one path silently broke coupon application on a different
path instead of correcting the double-count.
