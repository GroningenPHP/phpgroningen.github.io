## Why

The community wants a new workshop based on an existing presentation about specification-driven development, but it needs concrete, engaging project options and low-friction tooling that participants can access without paid LLM subscriptions. Defining this now enables workshop preparation and consistent facilitation.

## What Changes

- Create a new workshop package derived from `resources/spec-driven-development.pdf` with an explicit focus on starting a spec-driven development project.
- Add two workshop case options participants can choose from:
  - Interactive Music Sequencer (drums, vocals, melody, rhythms) with simple on/off controls (buttons, sliders, switches).
  - Trivia application with custom question creation, pre-seeded questions grouped across 5-10 categories, and easy join flow for meeting/video-call contexts (Kahoot-inspired).
- Define how these two cases are presented during the workshop so teams can pick one and immediately begin spec-driven work.
- Design the workshop content for a mixed-skill audience: a guided happy path that less experienced PHP developers can follow step by step, plus optional stretch goals that keep experienced developers engaged, supported by on-site facilitators.
- Ground the workshop in the source presentation (`resources/spec-driven-development.pdf`) so its key takeaways are conveyed and experienced firsthand, not just mentioned.
- Provide participant tooling guidance that works without a paid LLM subscription, with OpenCode as the default option and alternatives documented.
- Add simple install instructions for Ubuntu and Windows for the selected tooling path.

## Capabilities

### New Capabilities
- `sdd-workshop-case-selection`: Defines the workshop case-option experience, including both project casus, selection/presentation for participants, and the mixed-skill guided-path-plus-stretch-goal structure.
- `sdd-workshop-accessible-tooling`: Defines no-subscription workshop tooling support, including recommended tools and Ubuntu/Windows installation instructions.
- `sdd-workshop-learning-outcomes`: Defines the spec-driven development takeaways (from `resources/spec-driven-development.pdf`) that the workshop must convey and have participants experience firsthand.

### Modified Capabilities
- None.

## Impact

- Affected artifacts under `openspec/changes/workshop-sdd/` (proposal, design, specs, tasks).
- Workshop content updates derived from `resources/spec-driven-development.pdf`.
- Documentation additions for tool recommendations and OS-specific install steps.
