# Leg dispatch prompt — template

One dispatch per leg (stage 4). Copy this shape when briefing the Opus/Sonnet subagent that will execute it — it's the contract that keeps single-owner files and the no-push rule from being renegotiated mid-leg. The wave this leg belongs to, and its file-ownership row, are decided in `register-template.md` before this prompt is written.

```
## Leg <N> — <short name> (<Opus|Sonnet>, ~<estimate>)

Owns: <exact file list — new files marked NEW; nothing outside this list>

Context: <the finding row(s) from the register this leg closes, plus the
confirmed root cause from the explorer report — cite file:line>

Worktree: <path>, branch `session/<name>-<leg-slug>` — flat, where `<name>` is
the same slug as the session's integration branch `session/<name>` (git
refuses a branch nested under an existing branch ref) — created off
`session/<name>`. If the repo needs a symlinked venv / seeded
db / other per-worktree setup, say so explicitly here — don't make the
subagent guess.

Gate run: <5x-think | grill-me | none — outcome in one line, so the subagent
never thinks it must run the gate itself>

Steps:
1. <concrete step, file:line references where known>
2. <...>

Tests: <exact test files to add/run — targeted tests only; never run the full
suite from this worktree, the intake agent runs it on the integration branch
at stage 6>

Constraints:
- Single-owner files only — if you need to touch a file this leg doesn't
  own, stop and report back instead of editing it.
- Never run the full suite from this worktree — targeted tests only,
  categorically, no exceptions for "just this once."
- Before adding prose into any file or comment that shares a test's
  substring assertion, grep `tests/` for that literal text first.
- Commit to the leg branch. Never push. Never merge yourself.
- If the root cause turns out to be unconfirmed once you're in the code,
  stop and ship a probe instead of guessing the fix.
- If this leg's fix touches one door of a multi-door mechanism, enumerate
  every door in the test, not just the one the finding named.
- Ledger note for jedi-review: <any known rule this leg's fix should be
  checked against, e.g. "guard's empty/None case is part of the guard">
```

## After the leg reports back

1. Diff review by the intake agent: does the diff match "Owns" and "Steps," nothing more?
2. Dispatch `jedi-review` against the leg's branch/diff, per jedi-review's own Contract (stage 1 Scope decides lens count; a fix round runs jedi-review's Fix re-review menu, scoped to the fixes — not a fresh full round).
3. CONFIRMED findings → fixed on the same branch → re-entered at jedi-review's fix re-review stage → `LESSONS-DB.md` every round, per jedi-review stage 6.
4. **PASS** per jedi-review's own stage 5 (the full declared stage-1 tribunal clean against the current state — a clean fix round alone is not this) → merge into the integration branch. Append `— merged` to the leg's register row (keep the leg name).
5. Non-convergence stop (jedi-review's tribunal-mechanics: three confirming rounds) → hand the user the three options named in `SKILL.md` stage 5 (scoped pass / narrower ship / park); do not keep re-running rounds without that hand-off.
6. Leg joins the next ready batch (see register template, "Batching").
