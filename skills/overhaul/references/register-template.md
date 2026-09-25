# Living register — template

Lives inside the session's plan file (e.g. `~/.claude/plans/<session>.md`), not a separate document. Update it the moment a finding arrives — never batch to the end of the session.

## Intake log (issue register) — append as findings arrive

| # | Surface | Finding (user's words, condensed) | Sev | Status/leg |
|---|---|---|---|---|
| 1 | Invoice detail page | Delete button does nothing | P0 broken control | Leg 1 (Sonnet) |
| 2 | Global mobile nav | Nav bar overlaps page content on phones | P1 layout | Leg 2 probe → Leg 4 fix |
| 3 | Settings page | Typo: "Pasword" | P3 cosmetic | Leg 1 (Sonnet) |
| 4 | Settings page | Save button double-submits on slow connections | P1 UX/functionality friction | Leg 1 (Sonnet) — merged |

Severity is the reporter's own sense of impact (P0 broken/blocking, P1 UX/functionality friction, P2 polish, P3 cosmetic) — don't renegotiate it during intake, only during planning.

Status starts as `unassigned` the moment a row is logged. It becomes a leg name only after stage 3 (Plan legs) runs; a probe status (`Leg N probe`) means the cause isn't confirmed yet, not that a fix is scheduled.

_(Keep taking findings as they arrive. Append a running note under the table naming cross-cutting causes as they're spotted — e.g.: "Cross-cutting causes found so far: (i) one base-template shell bug explains items 2, 5, 9; (ii) hand-duplicated nav lists that drifted; (iii) a recency rollup omitting created_at.")_

## Decisions locked

Running list of judgment calls the user made or approved during the session, dated, so a later leg or reviewer doesn't relitigate them:

- `<date>` — `<decision, one line, attributed to the user or flagged as the agent's own judgment call pending user override>`

## Session process (boilerplate — paste once per session)

- Intake agent (this session): receives findings page-by-page, updates this register, maps cross-cutting causes, dispatches legs.
- Implementation: Opus (hard) / Sonnet (routine) subagents; integration branch `session/<name>` off main, worktree per parallel leg; single-owner files per leg (ownership table below).
- Every leg ends in a **jedi-review** pass (2–3 lenses small / 5–7 large) before merge; ledger to `LESSONS-DB.md`.
- Skills in force: `5x-think` before any new mechanism; `grill-me` for ambiguous scope.

## Findings (explorer subagent reports)

One subsection per explored area, evidence-first — every claim carries a file:line citation against a named commit, not a paraphrase:

### A. `<area name>` — explorer report, CONFIRMED against `<commit>`

- `<root cause, one paragraph, file:line citations throughout>`
- Tests that pin this area: `<test files>`.

## Waves

A wave is the set of legs dispatched to run concurrently. Cap: **5 concurrent legs**, disjoint files. A leg that would push a wave past 5, or that collides on a file already owned in this wave, goes into the next wave instead — never squeezed in.

| Wave | Legs (dispatched together) | Status |
|---|---|---|
| Wave A | Leg 1 (Sonnet), Leg 2 (Sonnet), Leg 3 (Opus) | running |
| Wave B | Leg 4 (after Wave A — shares a file with Leg 2) | queued |

## Cross-leg file ownership

Table built during stage 3, **before any leg in the wave starts**, so two concurrently running legs never write the same file:

| File | Owning leg(s) |
|---|---|
| `app/templates/base.html` | Leg 2 (nav lines only), then Leg 5 |
| `app/routes/sales/clients.py` | Leg 6 (create/edit), **then** Leg 7 (search) — different functions, 6 merges first |

A row naming a concurrently running session's own leg (not this session's) marks it `EXTERNAL — ticket only`, never dispatched against.

## Batching

Group legs into deploy batches so the human can re-test live mid-session rather than waiting for the whole register to clear:

- **Batch 1** — quick wins + any probes, so the next wave of findings arrives informed.
- **Batch 2+** — the legs gated on batch 1's probe results, plus anything else ready.

Ship a batch as soon as its own legs are jedi-review-gated; don't hold it for a slower parallel leg — that leg joins the next batch. The one exception: a leg sequenced behind an unmerged same-file leg always waits for its predecessor's merge, gated or not.
