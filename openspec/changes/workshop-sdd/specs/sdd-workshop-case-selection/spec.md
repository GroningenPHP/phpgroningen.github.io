## ADDED Requirements

### Requirement: Workshop SHALL provide two selectable project cases
The workshop SHALL present exactly two starting casus options for specification-driven development: an Interactive Music Sequencer and a Trivia application.

#### Scenario: Viewing workshop case options
- **WHEN** participants reach the project-selection segment of the workshop
- **THEN** they see both the Interactive Music Sequencer and Trivia application options with clear summaries

### Requirement: Interactive Music Sequencer case SHALL define core interaction scope
The Interactive Music Sequencer case SHALL define a minimum scope with four togglable sound groups: drums, vocals, melody, and rhythms, and SHALL specify that controls are simple and explicit using clear buttons, sliders, or switches.

#### Scenario: Reading sequencer case requirements
- **WHEN** participants open the sequencer case description
- **THEN** they can identify drums, vocals, melody, and rhythms as independent on/off-capable tracks and see approved simple control patterns

### Requirement: Trivia case SHALL define content model and participation flow
The Trivia case SHALL require support for adding custom questions, SHALL include a seeded question set organized in at least five and at most ten categories, and SHALL include an easy join approach suitable for meeting or video-call participation.

#### Scenario: Reading trivia case requirements
- **WHEN** participants open the trivia case description
- **THEN** they see requirements for custom questions, 5-10 seeded categories, and an easy remote-join flow inspired by Kahoot-style participation

### Requirement: Workshop SHALL frame cases as SDD project starters
The workshop SHALL present both cases as explicit options to start a specification-driven development project, including prompts that guide teams to draft initial requirements and scenarios from their chosen case.

#### Scenario: Starting an SDD project from a selected case
- **WHEN** a team selects one of the two cases
- **THEN** they receive clear starter prompts to create their first spec requirements and scenarios

### Requirement: Each case SHALL provide a guided happy path for less experienced developers
Each case SHALL include a guided happy path with sequential, low-ambiguity steps and frequent "you should now see X" checkpoints that lead a less experienced PHP developer to a working minimum viable version of the project.

#### Scenario: Less experienced participant follows the guided path
- **WHEN** a less experienced participant works through a case's guided happy path
- **THEN** they can complete each step with a clear checkpoint confirming expected results and reach a working MVP

### Requirement: Each case SHALL provide optional stretch goals for experienced developers
Each case SHALL include a set of optional stretch goals that extend the MVP with more open-ended or challenging work, so experienced developers remain engaged after completing the core path.

#### Scenario: Experienced participant finishes the core path early
- **WHEN** an experienced participant completes the case MVP before time is up
- **THEN** they can pick from documented stretch goals to extend the project further

### Requirement: Workshop content SHALL account for on-site facilitation
The workshop content SHALL be written on the assumption that facilitators are present to guide participants, including facilitator prompts or notes for common blocking points rather than requiring every detail to be self-service.

#### Scenario: Participant gets stuck during the workshop
- **WHEN** a participant is blocked on a step
- **THEN** facilitators have prompts or notes to help unblock them and keep the participant progressing
