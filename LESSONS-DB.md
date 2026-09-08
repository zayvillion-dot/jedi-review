# LESSONS-DB.md

Running database of confirmed defects, their root causes, and the prevention rule each one taught. Consult before similar work.

---

## Review: 2026-09-08 — jedi-review skill package (self-review)

**Scope:** jedi-review skill package (SKILL.md, attack-lenses.md, ledger-template.md, README.md), doc/spec target, 4 files ~250 lines
**Process:** rounds: 1 — lenses per round: ambiguity, internal contradiction, omission (3) — raised 31 (24 distinct) / confirmed 22 / refuted 2
**Status:** OPEN (fix re-review pending)

### Confirmed defects

| ID | Defect | Root cause | Prevention rule |
|---|---|---|---|
| B | SKILL.md Stage 1 described `--deep` as only "persona walkthroughs and live end-to-end runs," silently omitting the A/B-against-pre-change-state lens already in the lens catalog. | Summary restated a menu instead of referencing it. | Point to the canonical lens list; don't re-enumerate it inline. |
| C | README's Usage section repeated the same incomplete `--deep` description, independently missing the same lens. | Summary restated a menu instead of referencing it. | Same fix as B — one canonical description, referenced, not duplicated in a second file. |
| D | Stage 3 never said how many skeptics adjudicate a round, or whether a skeptic could be that round's own attacker. | Cardinality of a role assumed obvious, left unstated. | State cardinality and independence for every assigned role, not just its function. |
| E | Nothing defined what "one full round" means at round 1 vs. a fix round vs. the gate round, so a clean fix round could be mistaken for a passing gate round. | Round shape assumed constant across stages that actually need different shapes. | Define each stage's round composition explicitly; never let a narrower round stand in for the full gate re-run. |
| F | "Every doc-type target ALWAYS runs ambiguity and internal contradiction" never defined "doc-type," leaving quotes/contracts/emails' coverage unclear. | Example written before the rule it illustrates. | Name a mandatory rule's scope explicitly wherever it's stated. |
| G | Selection guidance stated "Never zero lenses, regardless of size," then undercut it with "a target too small for one lens is too small to need review." | Escape-hatch rhetoric contradicting the hard rule. | After stating a hard rule, scan the surrounding sentence for language that quietly reopens the exception. |
| H | SKILL.md placed the ledger "at the target's root"; ledger-template.md placed it "at the target repo's root" — two definitions of one location. | Two files named the same location differently. | Define shared terms once and cite them; don't redefine per file. |
| J | The ledger stage said only to "append every confirmed defect," with no timing — implying only a completed, passing review produces a record. | Contract wrote the happy path only. | Fire state-recording steps on every relevant event, not only on success. |
| K | The process line used one "<N> lenses × <N> rounds" figure, meaningless once fix rounds legitimately run a different, smaller lens set than round 1. | A multiplier assumed every round runs the same lenses. | Record process per round (which lenses, that round's counts); never as one cross-round multiplier. |
| L | The Report format example already named a "fix-refutation" lens before any catalog defined it. | Example written before the rule it illustrates. | Define a term in its reference catalog before any example is allowed to use it. |
| M | The rationalization table's small-target row cited a fixed "(2 lenses)," drifted from Selection guidance's own "2–3 lenses" range for the same case. | A restated number drifted from the rule it was restating. | Cross-check every paraphrased number against its source before publishing. |
| N | Nothing required a lens to show its work, so a silently failed lens and one that genuinely found nothing both looked like "zero findings." | Contract wrote the happy path only. | Require an attack record alongside findings, so silence is detectable. |
| O | Verdicts were binary CONFIRMED/REFUTED with no rule for an attacker who disagrees with a REFUTED verdict, risking endless re-litigation of the same finding. | Contract wrote the happy path only. | Cap re-raises explicitly (once, new evidence only). |
| P | The contract assumed every declared lens always successfully dispatches as a subagent, with no handling for one that errors or never returns. | Contract wrote the happy path only. | Define an explicit failure state for every dispatched unit of work, and block the gate on it. |
| Q | Nothing distinguished a lens that read the whole target from one that sampled part of it — partial coverage could pass silently as a clean round. | Contract wrote the happy path only. | Require lenses to self-declare coverage; block PASS on any unresolved partial coverage. |
| R | The ledger had no field for a user shipping despite open confirmed findings — that override left no record, indistinguishable from a genuine PASS. | Contract wrote the happy path only. | Give the ledger an explicit override status, naming who and when. |
| S | The Gate stage defined when PASS is reached but never said PASS isn't itself authorization to ship, merge, or send. | Contract wrote the happy path only. | State plainly that a review verdict and an action decision are two separate approvals. |
| T | Stage 4 required attackers independent of the original defect but never said they must also be independent of the fix's author. | Contract wrote the happy path only. | Extend every independence requirement forward to cover the fix-review step, not just the original review. |
| U | Nothing addressed fix rounds that never converge to zero findings; convergence was simply assumed. | Contract wrote the happy path only. | Cap consecutive failing fix rounds and force a process check-in rather than looping indefinitely. |
| V | The ledger template gave no instructions for a target that already has a differently-structured LESSONS-DB.md, risking a naive append that rewrites prior entries. | Template assumed every project starts its ledger from this template, never from its own prior file. | Append new material under its own heading; never rewrite or restructure what already exists. |
| W | The three lens menus (code / docs-plans-specs / quotes-financial) don't cover every target type, and stage 1 gave no instruction for what an uncovered target should do. | Menu enumerated the common cases and never named what covers the rest. | Give every closed menu an explicit by-analogy path for the uncovered case, named at the point of use. |
| X | README's structure tree omitted the repo's real `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` manifests and the new `references/tribunal-mechanics.md`. | Tree was written once at scaffold time and never re-synced as real files were added. | Diff the documented structure against the actual file listing before shipping docs that describe repo layout. |

### Deliberate decisions (not bugs — do not "fix")

| Decision | Rationale |
|---|---|
| Frontmatter description's self-trigger clause ("Also use before declaring any significant piece of work \"done\"") stays exactly as written. | Intended: the skill is meant to act as a standing pre-"done" gate, not only a tool invoked by name — the self-trigger is deliberate scope, not scope creep. |
| Ledger template's insertion-marker comment (line 33: "Insert each new review's block directly below this line; keep newest-first order.") stays exactly as written. | Mechanically correct as written — the copy-paste-per-review workflow it describes is unambiguous; refuted. |

### Follow-ups

- Fix re-review round pending (this review's stage 4/5): re-attack the fixes now applied to SKILL.md, attack-lenses.md, ledger-template.md, and README.md — via the Fix re-review lenses (fix-refutation, fix-blast-radius) — before this review can PASS.

---

<!-- Insert each new review's block directly below this line; keep newest-first order. -->
