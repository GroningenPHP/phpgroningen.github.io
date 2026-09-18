# Facilitator Walkthrough — Trivia Case (reference arc)

This walkthrough shows how a single case carries every learning outcome in
`specs/sdd-workshop-learning-outcomes/spec.md`. The Trivia app is the worked
example; the Interactive Music Sequencer runs the identical arc with a
different planted "the plan was wrong" moment (see the end).

Legend: ● marks a moment where a takeaway is *experienced*, not told.

## 90-minute arc

| Time | Beat | Outcome felt |
|------|------|--------------|
| 0:00 | Setup — OpenCode + Gemini free key, clone starter repo | tooling |
| 0:10 | Intent — one sentence describing the quiz | ● prompt-vs-spec judgment |
| 0:15 | Spec — write `spec.md` (what & why, no code) | ●● artifacts, spec before code |
| 0:30 | Plan — write `plan.md`, get it signed off before coding | ●●● grounding, sign-off diff→plan |
| 0:45 | Build — agent implements task-by-task against the plan | ● what to test, not how |
| 1:05 | The twist — a plan assumption breaks, fix in a paragraph | ● plan wrong, cheap+early, not-done |
| 1:20 | Enforce — make one rule a real check; stretch goals | ● deterministic enforcement |
| 1:30 | Reflect — when is this worth the ceremony? | ● applicability |

## Beat-by-beat

### 1. Intent (0:10) — prompt vs spec
Facilitator asks: "Could you one-shot this with a prompt?" Joining flow +
categories + scoring has enough moving parts to warrant a spec. Making that
call is the point: participants earn the ceremony rather than assume it.

### 2. Spec — what & why, as a file (0:15)
Everyone writes `spec.md`. The guided happy path provides a fill-in-the-blanks
skeleton; experienced developers write freehand.

```
spec.md
  Problem:    host needs a low-friction quiz for remote meetings
  Boundaries: 5-10 seeded categories; custom questions; join by code
  Done means: a joiner answers a question and sees their score update
```

● It is a file in the repo the agent reads every session — not a chat message
that evaporates.

### 3. Plan — grounded and reviewed (0:30)
Write `plan.md`: which files change, in what order, and the check that proves
it worked. Then the review gate:

```
+-----------------------------------------------+
|  PLAN REVIEW GATE  (facilitator or peer)      |
|  "Is this plan right?" - 3 minutes            |
|  changing your mind here costs a paragraph    |
+-----------------------------------------------+
```

● Review happens before code exists. A muddled plan gets fixed now, for free.
● Grounding: point the agent at the specific files (e.g. `QuestionRepository`
and the join route), not the whole repository.

### 4. Build (0:45) — what to test, not how
Seeded questions across 5-10 categories are provided so nobody stalls on
content. Participants give the agent the acceptance scenario — "WHEN a joiner
submits the right answer THEN their score increases" — and let it implement.
They hand it the oracle, not the testing method.

### 5. The twist — the plan was wrong (1:05)
Designed-in and planted in the starter repo. Example:

```
  plan said:  "join code lives in the client, baked at build time"
  reality:    the client bundle is built without it -> code can't arrive
  fix:        move the join code to the server  (one line in plan.md)
```

● Waterfall's flaw was never having a plan — it was waiting months to learn it
was wrong. Amend the plan in a paragraph and continue. Record a done vs
not-done block:

```
  DONE:      join-by-code, scoring, 6 seeded categories
  NOT DONE:  live presenter view - needs websockets, out of scope today
```

### 6. Enforce — deterministic rule + stretch (1:20)
Each team makes one rule real instead of polite prose:

```
  prose (weak):  "please don't allow empty questions"
  sensor (real): a test/validator that REJECTS an empty question
```

Optional stretch goals for participants who finish early:
- a Stop-style check: red tests mean the agent cannot declare itself done
- timed rounds / leaderboard
- import questions from CSV
- a second custom category with a rule enforced by a test

### 7. Reflect (1:30) — worth the ceremony?
"You wrote about a page of markdown before any code. Worth it here? Would it
be worth it for a one-line CSS fix?" Participants articulate the auditability /
governance / parallelisation line themselves.

## Coverage check

| Learning outcome | Beat |
|------------------|------|
| Four artifacts vocabulary | 2, 3, 4 (constitution from starter / spec / plan / tasks) |
| Spec & plan files before code | 2, 3 |
| Sign-off diff -> plan | 3 |
| Deterministic enforcement | 6 |
| What to test, not how | 4 |
| Ground on right context | 3 |
| Plan wrong, cheap fix + not-done | 5 |
| When worth the ceremony | 1, 7 |

## Music Sequencer variant

Same arc, different planted twist. Example: "toggling a track live needs the
audio graph pre-built, not created on click" — discovered during build,
corrected at plan level in a paragraph. Every other beat maps identically.
