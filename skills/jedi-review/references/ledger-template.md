# LESSONS-DB.md — template

Running database of confirmed defects, their root causes, and the prevention rule each one taught. Consult it before similar work. Lives at the reviewed project's root — its git repo root, or for a standalone artifact, the folder holding it — as `LESSONS-DB.md`.

One section per review, inserted directly below the marker, newest-first. For a new review, copy everything between the `---` lines below and insert the copy directly under the marker. For a review already in progress, never open a second section: update its existing section in place as each round's adjudication closes — add rows to the Confirmed defects table, update the Process and Status lines.

<!-- New review sections go directly below this line, newest first. -->

---

## Review: <YYYY-MM-DD> — <target name>

**Scope:** <target, type (code/doc/plan/spec/quote), size>
**Process:** rounds: <N> — lenses per round: <names or counts> — raised <N> / confirmed <N> / refuted <N>
**Status:** OPEN | PASSED <date> | SHIPPED OVER OPEN FINDINGS (user override, <who/date>)

### Confirmed defects

| ID | Defect | Root cause | Prevention rule |
|---|---|---|---|
| D1 | <one-line defect> | <why it happened> | <what to check next time> |
| D2 | | | |

### Deliberate decisions (not bugs — do not "fix")

| Decision | Rationale |
|---|---|
| <thing reviewers keep flagging> | <why it's intentional> |

### Follow-ups

- <work deferred out of this review, with an owner if known>

---
