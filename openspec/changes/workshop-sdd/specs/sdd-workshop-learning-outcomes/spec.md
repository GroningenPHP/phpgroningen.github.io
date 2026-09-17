## ADDED Requirements

### Requirement: Workshop SHALL teach the four SDD artifacts as a shared vocabulary
The workshop SHALL introduce and use the four spec-driven development artifacts from the source presentation: constitution (rules that do not change per feature), spec (what and why, no implementation), plan (how, grounded in the codebase, naming the check that proves it worked), and tasks (units an agent executes and a human ticks off). It SHALL note that different frameworks (e.g. GitHub Spec Kit, AWS Kiro, BMAD, OpenSpec, Superpowers) reinvented the same four.

#### Scenario: Participant learns the artifact vocabulary
- **WHEN** a participant works through their chosen case
- **THEN** they can name and produce a spec, a plan, and tasks, and understand the role of a constitution

### Requirement: Workshop SHALL have participants produce spec and plan as repository files before writing code
The workshop SHALL require participants to settle the problem, the approach, and what counts as done in files in the repository (not a throwaway chat prompt) before any implementation, reflecting the "first four steps happen before any code exists" lifecycle (intent → spec → plan → tasks → implement → verify → review).

#### Scenario: Participant starts a case
- **WHEN** a participant begins building their selected case
- **THEN** they first create spec and plan files in the repo, and only then move to implementation

### Requirement: Workshop SHALL move sign-off from the diff to the plan
The workshop SHALL have participants get their plan reviewed (by a facilitator or peer) before code exists, demonstrating that changing your mind at plan stage costs a paragraph rather than a rewrite, and reinforcing that review is where the work has moved.

#### Scenario: Participant seeks approval
- **WHEN** a participant has drafted a plan for their case
- **THEN** they obtain plan-level sign-off before implementation, and can revise the plan cheaply if it is wrong

### Requirement: Workshop SHALL demonstrate that enforcement must be deterministic
The workshop SHALL have participants make at least one rule enforceable through a deterministic check (a test, type check, linter, or hook) rather than relying on prose instructions to the agent, illustrating that "prose does not enforce anything" and the guides-prevent / sensors-detect pairing.

#### Scenario: Participant enforces a rule
- **WHEN** a participant identifies a rule that matters for their case
- **THEN** they express it as a runnable check that fails when violated, not only as text in a spec

### Requirement: Workshop SHALL frame testing as "tell the agent what to test, not how"
The workshop SHALL guide participants to express desired behaviour as acceptance scenarios/checks (what to test) rather than lecturing the agent on testing methodology, reflecting the finding that most agent-authored tests carry weak or no oracle signal.

#### Scenario: Participant defines tests for their case
- **WHEN** a participant specifies how their case's behaviour is verified
- **THEN** they write behaviour-focused acceptance checks tied to their spec rather than prescribing test technique

### Requirement: Workshop SHALL teach grounding the plan on the right context
The workshop SHALL convey that agents cannot be handed the whole repository (context rot, stale embeddings) and that a plan should be grounded on the specific relevant code within a fixed context budget.

#### Scenario: Participant grounds a plan
- **WHEN** a participant plans a change against existing code
- **THEN** they point the agent at the specific relevant files rather than the entire codebase

### Requirement: Workshop SHALL show that a plan will be wrong and correction is cheap and early
The workshop SHALL set the expectation that a plan can be wrong and that spec-driven development surfaces this the same day, cheaply, and SHALL have participants record what they could not finish (done vs not-done-and-why) as part of a trustworthy plan.

#### Scenario: Participant hits a wrong assumption
- **WHEN** a participant discovers their plan was wrong during a case
- **THEN** they correct it at plan level and record any deferred or unfinished work with the reason

### Requirement: Workshop SHALL convey when spec-driven development is worth the ceremony
The workshop SHALL communicate that spec-driven development is worth it for auditability, governance, and parallelisation, and is not warranted for prototypes, one-line fixes, or exploration — summarised as "simple tasks need a prompt, complex ones need a spec."

#### Scenario: Participant judges applicability
- **WHEN** a participant reflects on their case at the end of the workshop
- **THEN** they can articulate when to reach for a spec versus a plain prompt

### Requirement: Workshop SHALL equip participants to run the full OpenSpec lifecycle on their own project
The workshop SHALL teach the OpenSpec change lifecycle (propose → apply → archive) grounded on the four SDD fundamentals, so participants leave able to run it on their next project. It SHALL cover the three concepts the lifecycle leans upon beyond the raw four artifacts: a change as a bounded unit of work, delta specs (ADDED/MODIFIED/REMOVED against a baseline), and archive folding the delta into the living baseline. This capability SHALL be delivered through a self-contained take-home page (install via `npm i -g openspec` and `openspec init --tools opencode`, a self-paced propose → apply → archive walkthrough, and `openspec/changes/workshop-sdd/` as a real worked example) that does NOT depend on in-room time. An optional facilitator-led reveal (~15 minutes, projector-only, never participant-run) MAY introduce the tool in the room and SHALL be safely skippable without affecting the take-home outcome.

#### Scenario: Participant adopts the lifecycle after the workshop
- **WHEN** a participant follows the take-home guide on their own repository after the workshop
- **THEN** they can install OpenSpec, wire it to OpenCode, and run a change through propose, apply, and archive, understanding change-as-a-unit, delta specs, and archive-to-baseline

#### Scenario: Facilitator skips the in-room reveal when time is short
- **WHEN** the guided build runs long and the facilitator cuts the optional OpenSpec reveal
- **THEN** participants still leave able to adopt the full lifecycle via the self-contained take-home page
