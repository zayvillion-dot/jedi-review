# Leg dispatch prompt — template

One dispatch per leg (stage 4). Copy this shape when briefing the Opus/Sonnet subagent that will execute it — it's the contract that keeps single-owner files and the no-push rule from being renegotiated mid-leg.

```
## Leg <N> — <short name> (<Opus|Sonnet>, ~<estimate>)

Owns: <exact file list — new files marked NEW; nothing outside this list>

Context: <the finding row(s) from the register this leg closes, plus the
confirmed root cause from the explorer report — cite file:line>

Worktree: <path>, branch `session/<integration-branch>/<leg-slug>` off
`session/<integration-branch>`. If the repo needs a symlinked venv / seeded
db / other per-worktree setup, say so explicitly here — don't make the
subagent guess.

Steps:
1. <concrete step, file:line references where known>
2. <...>

Tests: <exact test files to add/run — targeted only, never the full suite
from a worktree that isn't the integration branch>

Constraints:
- Single-owner files only — if you need to touch a file this leg doesn't
  own, stop and report back instead of editing it.
- Commit to the leg branch. Never push. Never merge yourself.
- If the root cause turns out to be unconfirmed once you're in the code,
  stop and ship a probe instead of guessing the fix.
- Ledger note for jedi-review: <any known rule this leg's fix should be
  checked against, e.g. "guard's empty/None case is part of the guard">
```

## After the leg reports back

1. Diff review by the intake agent: does the diff match "Owns" and "Steps," nothing more?
2. Dispatch `jedi-review` (2–3 lenses small, 5–7 large) against the leg's branch/diff.
3. CONFIRMED findings → fixed on the same branch, re-reviewed (fix re-review, not a fresh full round) → `LESSONS-DB.md`.
4. Gate clean → merge into the integration branch. Update the leg's register row to `merged`.
5. Leg joins the next ready batch (see register template, "Batching").
