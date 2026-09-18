## 1. Workshop foundation

- [x] 1.1 Review `resources/spec-driven-development.pdf` and extract workshop sections that should be reused or adapted for the new SDD session.
- [x] 1.2 Define a workshop flow that includes case selection, initial spec writing, and team kickoff checkpoints.

## 2. Case option content

- [x] 2.1 Create participant-facing case brief for the Interactive Music Sequencer, including drums, vocals, melody, rhythms, and simple on/off control expectations.
- [x] 2.2 Create participant-facing case brief for the Trivia app, including custom question support, seeded 5-10 categories, and easy meeting/video-call join expectations.
- [x] 2.3 Add facilitator prompts that help teams convert either selected case into first-pass requirements and scenarios.
- [x] 2.4 Write a guided happy path for each case: sequential low-ambiguity steps with "you should now see X" checkpoints leading to a working MVP.
- [x] 2.5 Write optional stretch goals for each case to keep experienced developers engaged after the MVP.
- [x] 2.6 Add facilitator notes for common blocking points in each case to support on-site guidance.

## 3. Learning outcomes from the presentation

- [x] 3.1 Weave the four SDD artifacts (constitution, spec, plan, tasks) and the intent→…→review lifecycle into the workshop flow as named, used concepts.
- [x] 3.2 Design the flow so participants write spec and plan files before code, and obtain plan-level sign-off from a facilitator or peer.
- [x] 3.3 Add a step where participants make one rule enforceable via a deterministic check (test/type/lint/hook) and frame testing as "what to test, not how."
- [x] 3.4 Add guidance on grounding the plan on the right files (not the whole repo) and on recording done vs not-done-and-why, including a deliberate "the plan was wrong" moment.
- [x] 3.5 Add a closing reflection on when SDD is worth the ceremony (auditability/governance/parallelisation) versus a plain prompt.
- [x] 3.6 Turn the reference arc in `facilitator-walkthrough.md` into per-case facilitator scripts (Trivia and Music Sequencer), including the planted "the plan was wrong" moment for each.

## 4. Accessible tooling and setup

- [x] 4.1 Document OpenCode as the default CLI agent (shell layer), including its role and Plan mode in the SDD workflow.
- [x] 4.2 Document the default model-access path: Google Gemini free API tier, including how to obtain and configure the API key in OpenCode.
- [x] 4.3 Document fallback model-access paths: GitHub Models (hosted) and local Ollama (offline / no-signup), each with clear when-to-use guidance and a minimum-hardware note for Ollama.
- [x] 4.4 Write Ubuntu quick-start install instructions (prerequisites, install OpenCode, configure default model path, readiness check).
- [x] 4.5 Write Windows quick-start install instructions (prerequisites, install OpenCode, configure default model path, readiness check).

## 5. Integration and workshop readiness

- [x] 5.1 Integrate case options and tooling setup guidance into workshop materials so participants can choose a case and start immediately.
- [x] 5.2 Run an internal dry-run of the workshop setup path on Ubuntu and Windows and capture friction points.
- [x] 5.3 Refine instructions and workshop prompts based on dry-run feedback before delivery.

## 6. OpenSpec lifecycle: in-room reveal + take-home adoption

- [x] 6.1 Add an optional, time-permitting facilitator-led OpenSpec reveal section to each case page (`case-trivia.html`, `case-sequencer.html`) that maps each hand-done beat to its OpenSpec step (spec→proposal/specs, "Done means"→scenarios, plan→design, build→tasks, reflect→archive); mark it clearly skippable and projector-only (not participant-run).
- [x] 6.2 Create a self-contained "Use this on your next project" take-home page under `public/workshops/spec-driven/` covering install (`npm i -g openspec`, `openspec init --tools opencode`), a self-paced propose → apply → archive walkthrough, and a note that it does not depend on the in-room reveal.
- [x] 6.3 On the take-home page, explain the three bridge concepts the full lifecycle leans on: change-as-a-unit, delta specs (ADDED/MODIFIED/REMOVED), and archive-to-baseline.
- [x] 6.4 Point participants to `openspec/changes/workshop-sdd/` as a real worked example (the change that produced the workshop pages) and link the take-home page from the landing hub and both case pages.
- [x] 6.5 Add a facilitator note in `README.md` stating the OpenSpec reveal is optional and cuttable if time runs short, and that the take-home page carries the full-lifecycle outcome on its own.
