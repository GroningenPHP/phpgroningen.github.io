## ADDED Requirements

### Requirement: Workshop SHALL support participation without paid LLM subscriptions
The workshop SHALL provide a complete tooling path that participants can use without purchasing an LLM subscription, covering both the CLI agent (shell) and model access (brain) layers.

#### Scenario: Participant checks prerequisite list
- **WHEN** a participant reviews workshop prerequisites
- **THEN** they can follow a no-subscription path from setup through project kickoff without providing paid credentials

### Requirement: Workshop SHALL recommend OpenCode as the default CLI agent
The workshop SHALL recommend OpenCode as the default CLI agent for all participants and SHALL explain its role as the model-agnostic shell that drives the spec-driven workflow, including its Plan mode.

#### Scenario: Facilitator presents the default agent
- **WHEN** the facilitator introduces workshop tooling
- **THEN** OpenCode is identified as the default CLI agent with a brief explanation of its role and Plan mode

### Requirement: Workshop SHALL define a default free model-access path
The workshop SHALL define the Google Gemini free API tier as the default model-access path for participants, and SHALL explain how to obtain and configure the API key in OpenCode.

#### Scenario: Participant configures the default model path
- **WHEN** a participant follows the default model-access instructions
- **THEN** they can connect OpenCode to the Google Gemini free API tier and confirm the model responds

### Requirement: Workshop SHALL document at least two fallback model-access paths
The workshop SHALL document at least two fallback model-access options in addition to the default: GitHub Models (hosted, for participants who already have GitHub accounts) and a local model via Ollama (offline / no-signup, for participants with capable hardware). Each fallback SHALL state when to choose it.

#### Scenario: Participant cannot use the default model path
- **WHEN** a participant cannot use the Google Gemini free tier (for example due to signup constraints or being offline)
- **THEN** they can choose GitHub Models or local Ollama using the documented guidance and continue the workshop

#### Scenario: Facilitator advises the offline or no-signup participant
- **WHEN** a participant requires an offline or zero-signup setup and has capable hardware
- **THEN** the local Ollama path is presented with a minimum-hardware expectation

### Requirement: Workshop SHALL provide Ubuntu and Windows quick-start install instructions
The workshop SHALL provide simple installation instructions for Ubuntu and Windows that cover prerequisites, installing OpenCode, configuring the default model-access path, and a basic success check.

#### Scenario: Participant installs tooling on Ubuntu or Windows
- **WHEN** a participant follows the OS-specific guide for Ubuntu or Windows
- **THEN** they can install OpenCode, configure a free model-access path, and confirm the tooling is ready for workshop use
