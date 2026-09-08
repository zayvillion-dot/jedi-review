# Attack Lenses

Reference menu for Jedi Review stage 1 (Scope). Pick lenses by target type and declare them by name — cite this file when stating the tribunal.

Each lens below is a hostile mission for one subagent. The subagent's job is to break the target through that specific lens, not to give a general impression of quality.

Every lens reports its strongest failed attacks alongside its findings — zero findings with no attack record means the lens did not run.

## Code

- **Correctness / logic** — Find the boundary, off-by-one, or inverted condition that produces the wrong answer. Trace every conditional's edge values by hand: the value just below, at, and just above each threshold.
- **Security** — Find the input that injects, the path that skips authorization, the secret left in cleartext or logs. Assume the caller is hostile, not cooperative.
- **Data integrity** — Find the migration, null, default, or concurrent write that corrupts state. Assume two operations land at the same instant, and that any optional field is missing.
- **Regression / blast radius** — Find the caller this change breaks. Read every call site as someone who will never read this diff and will pass whatever the old signature allowed.
- **Error handling / hostile input** — Find the malformed, empty, oversized, duplicated, or adversarial input the code doesn't expect. Assume nothing was validated upstream.
- **Performance under real load** — Find the input size or access pattern that turns this into the slow path, the N+1 query, or the unbounded loop. Assume production data volumes, not the test fixture.
- **Behavioral / UX** (user-facing targets only) — Find the sequence of clicks, states, or timing that strands the user or shows them the wrong thing. Read it as someone who has never seen the design doc.

## Docs / plans / specs

- **Internal contradiction** — Find two sections that disagree on the same number, term, or rule. Quote both, verbatim, side by side.
- **Ambiguity** — Find the sentence that reads two genuinely different ways. Write out both readings in full — the two written-out readings are the finding's failure scenario; if both are plausible to a reasonable reader, it is a defect, not a style note.
- **Omission** — Find the case the document silently doesn't cover. Ask what happens when the stated rule's precondition doesn't hold.
- **Feasibility / cost** — Find the step that won't survive contact with reality — the timeline, budget, headcount, or dependency that's silently assumed rather than secured.
- **Hostile-counterparty reading** — Read as the counterparty who wants to exploit this document. Find the clause they will claim says something the author didn't intend.
- **Numeric consistency** — Recompute every figure in the document from its own stated inputs. Find the one total, rate, or date that doesn't follow from the numbers beside it.

Any target whose substance is prose — docs, plans, specs, quotes, contracts, emails — always runs ambiguity and internal contradiction. A generalist single-pass review's most common blind spot is exactly these two: a plausible-sounding sentence with two readings, and two sections that quietly disagree.

## Quotes / financial

- **Arithmetic** — Recompute every total and subtotal from its line items. Find the one that doesn't match.
- **Margin / tier consistency** — Find the tier, job, or discount combination where the stated price doesn't yield the margin the pricing policy promises.
- **Scope gap** — Find the work a customer will reasonably insist was included that the quote's line items don't actually cover.
- **Terms risk** — Compare the payment schedule against real cash-flow timing. Find the gap between what the terms promise on paper and what the schedule can actually fund.

## Fix re-review (stage-4 rounds only)

- **Fix-refutation** — Attempt to prove the claimed fix does not fix the original defect: replay the original failure scenario against the new state.
- **Fix-blast-radius** — Attack what the fix changed: its new defaults, its new paths, every caller and reader of the changed section. Assume the fix introduced a defect; find it.

## Deep mode grafts (`--deep` only)

- **Persona walkthrough** — Name a real persona and walk the actual flow as they would live it, step by step, not as the spec summarizes it.
- **Live end-to-end run** — Execute the real path against real or realistic data and observe the actual output, not a mental trace of what should happen.
- **A/B against pre-change state** — Run the identical scenario before and after the change. Find the behavior that moved without anyone deciding it should.

## Selection guidance

- Small targets: 2–3 lenses. Prose targets (docs, plans, specs, quotes, contracts, emails): the two mandatory lenses (ambiguity, internal contradiction) plus up to one more chosen by the target's dominant risk — a payment-terms email runs ambiguity, internal contradiction, and terms risk. Every other target type: 2–3 lenses chosen by the target's dominant risk.
- Large targets: 5–7 lenses, covering structure, correctness, and the counterparty/reader angle together.
- Never zero lenses, regardless of size.
- A target outside these menus declares lenses by analogy to the nearest menu and names the analogy (e.g., an infra config reviews as code).

See `tribunal-mechanics.md` for round composition, lens failure states, coverage rules, and unlisted target types.
