# Quality bar, rationalization table, report format, and extended red flags

Reference material for `../SKILL.md` — moved out here to keep the top-level
contract short. Nothing here is optional; it's just not inline.

## Quality bar

- Six Sigma defect rate on what ships — the jedi-review gate at stage 5 is how that's held, not a hope.
- Click-speed / time-to-complete, not just correctness: a fix that works but adds a tap or buries information isn't done.
- Simplicity without losing information — condensing a finding or a stats block is not the same as deleting what someone still needs.
- Scope = organization, testing, functionality, and fixes of existing code. **Never mass deletion** — an overhaul repairs a running system, it doesn't gut it.
- When a reviewed sentence turns out false, delete it — never rewrite it smaller and leave a shrunken false claim standing.

## Rationalization table

| Excuse | Reality |
|---|---|
| "It's quick, just fix it now" | Skipping the register loses the cross-cutting map; today's off-register quick fix is tomorrow's untracked regression. |
| "Small enough to skip the worktree" | A shared file between two live legs is exactly how one agent's edit erases another's. |
| "It's cosmetic, skip jedi-review" | Every target gets a tribunal sized per jedi-review's own stage 1 Scope — never zero lenses. |
| "Review the whole batch at the end" | Waiting until the register is empty means every leg's merge conflicts and regressions land at once instead of one leg at a time. |
| "I can already see what's wrong, skip the probe" | A guessed fix that misses becomes a second, harder-to-see defect stacked on the first. |
| "Fold the console steps into one paragraph" | A step buried in prose is a step that gets re-parsed wrong; per-item WHAT/WHERE/HOW is what makes it executable without a follow-up question. |
| "The gate came back red/killed, just re-run it" without checking why | rc 143/137 really is safe to re-run — but only back through the full pre-flight again (`wave-batch-runbook.md`), not a direct re-launch; any other red is a leg of its own, diagnosed before the next gate. |
| "It's just a comment, it can say anything" | A comment sharing a file with a substring test can silently satisfy or break that test. |
| "One more leg fits in this wave" | The concurrency cap (`wave-batch-runbook.md` — session-wide, disjoint files) is what keeps a wave reviewable; a sixth leg is next wave's problem, not this one's. |
| "The scoped pass came back clean, that's good enough to merge" | A scoped pass narrows the FIX, never the REVIEW — it still owes jedi-review's own gate (stage 5) before merge. |

## Report format (batch close-out)

```
Batch 2 — legs: 4 (Opus), 5 (Opus), 6 (Opus), 7 (Opus)
Leg 4 multi-day mover: jedi-review 3 lenses, 0 confirmed → gate round clean → PASS → merged
Leg 5 nav anchoring: gated on Leg 3 probe, BLOCKED — probe pending
Leg 6 client form: jedi-review 3 lenses, 1 confirmed → fixed, fix re-review clean, gate round clean → PASS → merged
Merge-collision lens: 2 shared files, exact-union proof both directions, MERGE CLEAN (adjudicated: 0 confirmed)
Pre-flight: main clean, main==origin/main, integration ⊇ origin/main, no foreign suite, no push in flight
Gate: <tip sha> full suite rc 0 — 142/0
Register: 8 open, 5 closed this batch, 2 cross-cutting causes mapped
Deploy: pushed 4/6/7 to main (authorized: standing session go) → live; human re-testing
```

## Extended red flags

See `SKILL.md`'s Red flags for the core list. These belong to the same "stop and back up" rule:

- A guessed fix shipped for a symptom no explorer confirmed the cause of.
- Findings sitting in chat history instead of the register because "I'll add them later."
- Two gates launched against two different tips of the same integration branch.
- A batch gate launched without checking for a foreign suite or an in-flight push first.
- A merge across an auto-mergeable shared file with no merge-collision lens run against it.
