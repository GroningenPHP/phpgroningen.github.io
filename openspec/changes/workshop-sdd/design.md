## Context

The workshop content will be derived from `resources/spec-driven-development.pdf` and repackaged as a practical, hands-on session where participants start a specification-driven project from scratch. Participants need two concrete project options to choose from, and the workshop must support attendees without paid LLM access. The deliverable is workshop-ready planning content (proposal, specs, tasks) that can be applied to implementation and facilitation materials.

## Goals / Non-Goals

**Goals:**
- Define two clear workshop casus options that are realistic for a spec-driven kickoff.
- Ensure each case is specific enough to produce immediately actionable requirements.
- Serve a mixed-skill audience: less experienced PHP developers can complete a guided happy path, while experienced developers stay engaged via stretch goals, with facilitators available to unblock.
- Define an accessible tooling path with no LLM subscription requirement.
- Include simple Ubuntu and Windows setup instructions for the recommended tooling.

**Non-Goals:**
- Building the applications themselves in this change.
- Mandating a single programming language, framework, or deployment target.
- Producing advanced troubleshooting documentation for all possible local environment issues.

## Decisions

1. **Use two dedicated capabilities in specs (`sdd-workshop-case-selection` and `sdd-workshop-accessible-tooling`).**  
   **Rationale:** Separates domain choices (what to build) from delivery constraints (how participants can participate without subscriptions), making requirements easier to implement and validate independently.

2. **Separate the tooling decision into two layers: the CLI agent (shell) and model access (brain).**  
   **Rationale:** "Free" has two independent bottlenecks. OpenCode (the agent) is free and open source, but by default it expects the participant to bring their own model/API key. The workshop's real accessibility risk lives in the model-access layer, so it must be decided explicitly rather than bundled into the tool choice.

3. **Use OpenCode as the default CLI agent (shell layer).**  
   **Rationale:** Free/open source, model-agnostic (75+ providers plus local models), cross-platform with simple Ubuntu and Windows installs, and includes a Plan mode that reinforces spec-driven habits.  
   **Alternatives considered:**  
   - **Aider:** mature and git-native, but Python/pip setup is a common footgun for mixed-skill participants on Windows.  
   - **Gemini CLI / Qwen Code:** lower model-access friction but more tied to a single provider ecosystem.  
   - **Crush (Charm):** promising and model-agnostic, but newer and less battle-tested than OpenCode.

4. **Default model-access path is the Google Gemini free API tier, with GitHub Models and local Ollama as documented fallbacks (brain layer).**  
   **Rationale:** For a mixed-hardware meetup room on venue wifi, a hosted free tier gives the best quality-per-friction: one signup, one API key, no hardware lottery. GitHub Models is a natural fallback because PHP devs typically already have GitHub accounts. Ollama (local) is offered for the offline / privacy / no-signup crowd with capable laptops.  
   **Alternatives considered:**  
   - **Local-first (Ollama) as the default:** zero accounts and fully offline, but highest variance — strong machines shine while thin laptops OOM or run very slowly, making it risky as the primary path in a time-boxed room.  
   - **OpenCode Zen / Go:** curated and reliable, but paid, which violates the no-subscription premise.  
   - **Single hosted provider only:** simpler docs, but no fallback when rate limits, signup friction, or offline conditions hit.

5. **Define case details as normative requirements with scenario-driven acceptance criteria.**  
   **Rationale:** Keeps the workshop aligned with spec-driven development by modeling the same quality bar expected from participants.

6. **Capture OS install guidance as requirement-level content, not ad-hoc notes.**  
   **Rationale:** Ensures setup instructions remain part of the maintained spec and can be updated through normal change workflow.

7. **Structure the workshop for a mixed-skill audience with a layered guided path.**  
   **Rationale:** The room spans less experienced PHP developers and seasoned ones, with facilitators present. The spec-driven *method* is kept constant for everyone; the *depth of what gets built* scales with skill. Each case therefore defines a guided happy path (near copy-pasteable steps with frequent "you should now see X" checkpoints) that produces a working MVP, plus a set of optional stretch goals for participants who finish early or want more challenge. Facilitators roam to unblock rather than lecture.  
   **Alternatives considered:**  
   - **Single fixed difficulty:** simpler to author, but either bores experienced devs or overwhelms beginners.  
   - **Separate beginner vs advanced tracks:** clearer targeting, but doubles content and splits the room; a shared core with optional depth keeps everyone on the same method and lets facilitators help across skill levels.

8. **Anchor the workshop in the source presentation's takeaways as experiential learning outcomes (`sdd-workshop-learning-outcomes`).**  
   **Rationale:** The workshop derives from `resources/spec-driven-development.pdf`, whose central argument is that the durable value of SDD is getting the design and plan right before code, grounded in what exists, with enforcement made deterministic. Rather than lecturing these points, the workshop is designed so participants *experience* them through the cases: writing spec/plan files before code, getting plan-level sign-off, making one rule enforceable, expressing behaviour as acceptance checks, grounding on the right files, hitting a wrong plan and correcting it cheaply, and judging when the ceremony is worth it.  
   **Key takeaways mapped from the deck:** review is the new bottleneck and sign-off moves diff → plan; four artifacts (constitution/spec/plan/tasks) with intent→…→review lifecycle; prose enforces nothing (guides prevent, sensors detect); tell the agent what to test, not how; ground on the right context, not the whole repo; a plan that names what it could not finish is trustworthy; SDD is for complex/auditable work, not prototypes or one-liners.  
   **Alternatives considered:**  
   - **Present takeaways as slides only:** faster, but contradicts the deck's own point that being *forced to think and do* is where the value is.  
   **Reference:** `facilitator-walkthrough.md` sketches the full end-to-end arc for the Trivia case (with a Music Sequencer variant), mapping each learning outcome to a concrete beat in the session.

9. **Teach the SDD fundamentals hands-on in the room; deliver the full OpenSpec lifecycle via a self-contained take-home page, with only an optional facilitator-led reveal in the room.**  
   **Rationale:** The goal is that participants can run a real spec framework (OpenSpec) on their *next* project, but the workshop is time-boxed at **3 hours** with a mixed-skill, hand-held audience. The load-bearing value is *experiencing* the four fundamentals by hand (settle intent → spec/plan as files → sign-off before code → enforce a rule → correct a wrong plan → judge the ceremony), which the seven-beat arc already delivers. Making beginners install and drive OpenSpec's full change/archive lifecycle in the room would spend scarce hand-holding time on tooling surface area instead of the concepts that make the tool make sense. Therefore: the room earns the concepts; a polished **"Use this on your next project" take-home page** earns the tool.  
   **Shape:**  
   - **In-room budget (3 h):** ~0:00–0:30 setup (OpenCode + free model auth), ~0:30–0:45 concept intro, ~0:45–2:15 guided build (beats 1–7, hand-held), ~2:15–2:35 **optional** OpenSpec reveal, ~2:35–2:50 take-home walkthrough, ~2:50–3:00 reflect/Q&A.  
   - **OpenSpec reveal is facilitator-led, ~15 min, projector-only, never participant-run, and explicitly cuttable if time runs short** — it is a warm intro to the take-home page, not a dependency of it. Each fundamental done by hand maps 1:1 to an OpenSpec step (spec → `proposal`/specs, "Done means" → `#### Scenarios`, plan → `design`, build → `tasks`, reflect → `archive`).  
   - **Take-home page stands alone** and delivers the full lifecycle: `npm i -g openspec` → `openspec init --tools opencode`; a self-paced propose → apply → archive on the participant's own repo; the three bridge concepts the lifecycle leans on (**change-as-a-unit, delta specs, archive-to-baseline**); and a pointer to `openspec/changes/workshop-sdd/` as a real, non-toy worked example (it produced the very workshop pages).  
   **Rationale for OpenSpec over alternatives:** facilitators already use it (live support), single Node install (no second runtime like Spec Kit's `uv`/Python), first-class OpenCode target via `openspec init --tools opencode`, and a ready-made in-repo worked example. AWS Kiro (a paid IDE) is excluded by the accessibility premise.  
   **Alternatives considered:**  
   - **Participants run the full lifecycle in the room:** stickier, but ~20 min plus an extra install across many laptops, and it steals time from the fundamentals; rejected for a 3-hour hand-held format.  
   - **OpenSpec entirely take-home, zero in-room appearance:** protects all room time, but an unseen tool page often goes unread; a short optional reveal is high value-per-minute and degrades gracefully when skipped.

## Risks / Trade-offs

- **[Risk] Tool availability or install steps change over time** → Mitigation: keep one default tool plus alternatives, and maintain version-agnostic install guidance with update checkpoints before each workshop run.
- **[Risk] Case scope is too broad for workshop timebox** → Mitigation: define minimum viable scope per case and optional stretch goals in facilitation materials.
- **[Risk] Participants on managed devices cannot install local tooling** → Mitigation: provide at least one fallback option that can run with minimal local privileges.

## Migration Plan

1. Create workshop capability specs and tasks in this change.
2. Apply the change to generate implementation-ready work items.
3. Update workshop documentation/slides to include:
   - case selection segment,
   - tool recommendation matrix,
   - Ubuntu/Windows quick-start instructions.
4. Run a dry workshop internally and refine instructions based on friction points.

Rollback strategy: if new workshop content is not usable, revert to the previous workshop flow and re-run planning with narrowed requirements.

## Open Questions

- Should the workshop mandate one case per team, or allow teams to switch cases during early exploration?
- **Venue connectivity:** is reliable wifi guaranteed, or must the workshop survive fully offline? If offline is a hard requirement, the local Ollama path is promoted to primary and a minimum-hardware note is added.
- **Signup tolerance:** is asking participants to create a Google (Gemini) or GitHub API key acceptable, or is a zero-accounts experience required? Zero-accounts effectively forces the local model path.
- **Existing access:** how many participants already have GitHub Copilot (free for students/OSS maintainers)? If common, it becomes a near-zero-setup fourth path worth documenting.
- What is the target workshop duration and expected team size, to tune case depth precisely?  
  **Resolved:** duration is **3 hours**. Case depth is tuned so the guided build (beats 1–7) fits ~0:45–2:15, with stretch goals for early finishers and the OpenSpec lifecycle moved to a take-home page (Decision 9).
