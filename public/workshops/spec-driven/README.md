# Spec-Driven Development — Facilitator Guide

Companion to the participant pages in this folder. Participants never need this
file; it's for the people running the room.

- **Landing / flow:** `index.html`
- **Setup (OpenCode + free model, Ubuntu/Windows):** `setup.html`
- **Case A — Trivia:** `case-trivia.html`
- **Case B — Music Sequencer:** `case-sequencer.html`
- **Seed data:** `assets/trivia-questions.json` (8 categories, 32 questions)
- **Take-home (OpenSpec lifecycle, self-serve):** `next-project.html`

The workshop is derived from the GroningenPHP talk *"Spec-Driven Development:
from vibe-coding to integrating AI coding assistants into the software
development lifecycle."* The goal is that participants **experience** the
talk's takeaways rather than hear them as slides.

---

## Room setup & roles

- Have facilitators roam — unblock and pair, don't lecture from the front.
- Aim for one facilitator per ~5 participants during setup (the riskiest phase).
- Mixed skill is expected: everyone runs the same method; depth of build scales.
  Beginners ship the MVP by following the guided path; strong devs treat it as a
  warm-up and go to stretch goals.

## Pre-flight checklist (run BEFORE the meetup)

Do a dry run on both a clean Ubuntu machine and a clean Windows machine and tick:

- [ ] `curl -fsSL https://opencode.ai/install | bash` installs OpenCode on Ubuntu; `opencode --version` works in a fresh shell.
- [ ] On Windows, at least one of Scoop / Chocolatey / `npm i -g opencode-ai` / WSL2 path works end to end.
- [ ] A free Gemini key from https://aistudio.google.com/apikey connects via `/connect` → Google, and `/models` lists a Gemini model.
- [ ] Fallback A: GitHub Copilot device login works via `/connect` → GitHub Copilot.
- [ ] Fallback B: `ollama pull qwen2.5-coder` + the `opencode.json` snippet on `setup.html` yields a working local model on a representative laptop; note the real minimum RAM you observed.
- [ ] Venue wifi can sustain N participants hitting a hosted API (or decide to promote the Ollama path if not).
- [ ] `assets/trivia-questions.json` downloads correctly from the case page.
- [ ] Re-verify the OpenCode install/provider commands against https://opencode.ai/docs — they change; update `setup.html` if needed.

Capture friction points during the dry run and fold fixes back into `setup.html`
before the event. This is the workshop's own "the plan was wrong, fix it early".

---

## Turning a case into first-pass requirements (facilitator prompts)

When a team picks a case, help them convert it into a spec with questions, not
answers. Useful prompts:

- "In one sentence — what is this, and who is it for?" → the **intent**.
- "What are three things it must do, and one thing it explicitly will *not* do
  today?" → **boundaries**.
- "Finish this sentence: *it's done when…*" → the **done** criterion / first
  acceptance scenario.
- "Name the single check that would prove step one works." → seeds the **plan**.
- If they start describing code ("I'll use a MySQL table…"), gently redirect:
  "That's a plan detail — park it. What's the behaviour?"

Push every team to phrase at least one behaviour as **WHEN … THEN …** before they
touch Build mode — that scenario becomes their first test.

---

## Case A — Trivia: facilitator script

**Reference arc (90 min):** intent → spec → plan (+sign-off) → build → the twist
→ enforce (+stretch) → reflect. Each participant page beat matches this.

### The plan review gate (beat 3)
This is the most important 3 minutes. Read their `plan.md` and ask "is this
right?" *before* they code. A muddled plan gets fixed for a paragraph now instead
of a rewrite later. Make sure every plan step names a check.

### The planted twist (beat 5)
Steer teams toward this discovery (or reveal it if they don't hit one):

```
Plan said:  the join code lives in the client, baked in at build time
Reality:    the client bundle is built without it -> the code can't arrive
Fix:        move the join code to the server (one line in plan.md)
```

The lesson: SDD surfaces a wrong plan the *same day*, cheaply. Have them amend
`plan.md` and add a **Done / Not-done-and-why** block (e.g. "live presenter view —
needs websockets, out of scope").

### Enforce (beat 6)
One rule becomes a real check, e.g. a validator/test that rejects an empty
question. Prose in the spec doesn't enforce anything; a red test does.

### Common blocking points
- **Agent starts coding during planning** → remind them to press `Tab` for Plan mode.
- **Scope creep in the spec** → cap at: join-by-code, seeded categories, scoring.
- **Stuck on question content** → point them at `assets/trivia-questions.json`.
- **"It works on my screen"** → have a second browser tab/phone actually join.
- **Model rate-limited / offline** → switch to a fallback from `setup.html`.

---

## Case B — Music Sequencer: facilitator script

Same arc as Case A. A single-page app using the Web Audio API is plenty.

### The planted twist (beat 5)

```
Plan said:  create each track's audio node when the user clicks it on
Reality:    building nodes on click drifts out of time and stutters
Fix:        pre-build the audio graph up front; toggles just mute/unmute
            (one line in plan.md)
```

Done / Not-done example: "per-step pattern editing — out of scope for the MVP".

### Enforce (beat 6)
E.g. a test that rejects a tempo outside 40–240 BPM.

### Common blocking points
- **No sound at all** → browsers require a user gesture before audio starts; a
  "Start" button that resumes the AudioContext fixes it. Good real-world plan miss.
- **Timing drift / stutter** → this *is* the planted twist; guide them to pre-build
  the graph and schedule ahead, rather than allocating on toggle.
- **Over-ambitious first step** → get one track looping before adding the other three.

---

## Timing (3-hour budget)

| When | Segment |
|------|---------|
| 0:00–0:30 | Setup — OpenCode + a free model (riskiest phase; swarm it) |
| 0:30–0:45 | Concept intro — the four artifacts, files-not-chat |
| 0:45–2:15 | **Guided build** — beats 1–7 by hand (the heart; never cut) |
| 2:15–2:35 | OpenSpec reveal (**optional**, see below) |
| 2:35–2:50 | Take-home walkthrough — point at `next-project.html` |
| 2:50–3:00 | Reflect + Q&A |

## OpenSpec reveal — optional, cut it if time is short

The reveal (~15 min) is a **facilitator-led demo on the beamer** of the tool that
operationalises what participants just did by hand: `openspec` propose → apply →
`openspec archive`. Do **not** have participants install or run it in the room —
that spends scarce hand-holding time on tooling instead of the fundamentals.

**It is fully skippable.** The full-lifecycle outcome is carried by the
self-contained take-home page `next-project.html` (install, a self-paced
propose → apply → archive, the three bridge concepts — change-as-a-unit, delta
specs, archive-to-baseline — and `openspec/changes/workshop-sdd/` as a real
worked example). If the build runs long, cut the reveal and just send everyone to
the take-home page; nothing essential is lost.

If you *do* run it, the strongest beat: open `openspec/changes/workshop-sdd/` and
say *"this tool built the very page you're looking at."*

## Coverage map (talk takeaway → where it lands)

| Takeaway | Beat |
|----------|------|
| Four artifacts vocabulary | index §3; beats 2–4 |
| Spec & plan as files before code | beats 2–3 |
| Sign-off moves diff → plan | beat 3 (review gate) |
| Prose enforces nothing; make it deterministic | beat 6 |
| Tell it what to test, not how | beat 4 |
| Ground the plan on the right context | beat 3 |
| A plan that names what it couldn't finish | beat 5 (Done/Not-done) |
| When it's worth the ceremony | index §4; beat 7 |

## Reflection to close the room
"You wrote ~a page of markdown before any code. Worth it here? Worth it for a
one-line CSS fix?" Land the line: *simple tasks need a prompt, complex ones need
a spec.*
