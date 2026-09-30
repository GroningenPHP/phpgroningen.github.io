document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('artifact-example-modal');
    const title = document.getElementById('artifact-example-title');
    const content = document.getElementById('artifact-example-content');
    const closeButton = document.getElementById('artifact-example-close');
    const links = document.querySelectorAll('.js-artifact-example-link');

    if (!modal || !title || !content || !closeButton || links.length === 0) {
        return;
    }

    const examples = {
        agents: {
            title: 'agents.md — Trivia example',
            body: `# agents.md — Trivia workshop constitution

## Always true in this repo
- Stay in Plan mode until spec.md, plan.md and tasks.md are complete.
- Keep plans grounded: name exact files, in order.
- Every plan step must include the check that proves it worked.
- Get human sign-off on plan.md before writing code.
- At review, update plan.md with what changed and why.
- Prefer PHP as the primary language for backend and domain logic.
- Follow modern PHP standards (PHP-FIG/PSR) and framework best practices.
- Keep JavaScript to a minimum; use it only when it clearly improves UX.
- Use DDEV for local development and the testing cycle.

## Build constraints
- Trivia questions are loaded from seeded JSON first.
- Keep MVP scope: join by code, answer, score update.
- If unfinished, write a clear "Not done, and why" block.`
        },
        spec: {
            title: 'spec.md — Trivia example',
            body: `# spec.md — Trivia

## Problem
A host needs a low-friction quiz for a meeting or video call.

## Why
Existing tools need accounts or installs; we want "join with a code".

## Boundaries
- 5–10 seeded categories, provided up front
- Host can add custom questions
- Players join with a short code, answer, and see their score

## Done means
A joiner submits an answer and their score updates on screen.`
        },
        plan: {
            title: 'plan.md — Trivia example',
            body: `# plan.md — Trivia

## Scope
Single PHP app + seeded JSON questions for a host-run quiz.

## Steps
1. Add seeded question store
   - Files: public/workshops/spec-driven/assets/trivia-questions.json
   - Check: JSON loads and parses without errors in DDEV.

2. Create host flow with join code
   - Files: public/trivia/index.php
   - Check: host can start a session and sees a join code in DDEV.

3. Create joiner answer flow
   - Files: public/trivia/index.php
   - Check: joiner submits one answer linked to active session.

4. Add score updates
   - Files: public/trivia/index.php
   - Check: correct answer increases score by question points.

## Development cycle
- Run implementation and checks through DDEV.

## Review gate
Plan reviewed by human before implementation starts.`
        },
        tasks: {
            title: 'tasks.md — Trivia example',
            body: `# tasks.md — Trivia

- [ ] Questions store loads the seeded JSON
- [ ] Host can start a session and get a join code
- [ ] Joiner can open the app and enter the code
- [ ] Joiner can submit an answer for a question
- [ ] Correct answer updates score by question points
- [ ] Add one failing check, then make it pass
- [ ] Record "Done" and "Not done, and why" in plan.md`
        }
    };

    const closeModal = () => {
        modal.classList.remove('open');
        document.body.classList.remove('sdd-modal-open');
    };

    links.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const artifact = link.dataset.artifact;
            const example = artifact ? examples[artifact] : null;
            if (!example) return;

            title.textContent = example.title;
            content.textContent = example.body;
            modal.classList.add('open');
            document.body.classList.add('sdd-modal-open');
        });
    });

    closeButton.addEventListener('click', closeModal);
    modal.addEventListener('click', (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && modal.classList.contains('open')) {
            closeModal();
        }
    });
});
