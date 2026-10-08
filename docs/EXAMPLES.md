# Expected behavior

These are examples and manual review scenarios, not results from testing every supported tool.

| Situation | Expected behavior |
| --- | --- |
| “Change the timeout from 10 to 20 in this configuration.” No broader project context. | Make the bounded change and perform a relevant check. Do not create a project plan or log. |
| The same configuration change is part of an ongoing production migration. | Read project context, follow its requirements and update relevant status/log entries proportionately. Do not create another project. |
| A new multi-step project has no acceptance criteria. | Establish the outcome, deliverables, a few verifiable criteria and scope before substantial work. Ask only about material ambiguities. |
| Work begins on a step previously marked Not started. | Mark it In progress when work starts, not only in the final report. |
| Implementation is complete but agreed verification remains. | Keep the step In progress, or Blocked with a reason and owner. Record what has actually been checked. |
| A deliverable needs a physical test or external review. | Identify the blocked criterion, the required action and any independent current-phase work. Do not substitute optional development. |
| All release criteria pass, but additional export formats would be useful. | Close the phase and defer the extra formats. |
| A delivery package is missing a required component. | Connect the defect to the acceptance criterion, record evidence and fix it as a genuine blocker. |
| The user explicitly adds another required export format. | Update scope and consequences visibly. Do not use scope control to reject the explicit decision. |
| “Maybe we should support another format?” | Treat it as an idea and explain its impact before turning it into a requirement. |
| Work resumes in a different tool. | Read the current plan, recent log and relevant files; continue the next step without inventing a new plan. |
| An earlier approach failed. | Preserve a concise record of the attempt, outcome and reason for changing direction. |
| No timeframe has been discussed. | Plan dependencies and milestones without inventing a completion date. |
| An assistant is working in an outdated clone. | Read/synchronize through the project's normal workflow and preserve others' changes; do not overwrite current status. |
| An adopting project uses a language other than English. | Follow its communication and documentation conventions. This repository's English-language maintenance rule does not impose English on adopting projects. |

## Existing-project adoption

| Situation | Expected behavior |
| --- | --- |
| Existing issues say work is done, but current verification is unavailable. | Preserve the historical claim, label its evidence as unverified and investigate only if it affects remaining acceptance. |
| Two plans disagree about the current milestone. | Identify the conflict and authoritative source; ask only if evidence cannot resolve a material decision. |
| An old project has no work log. | Start a dated onboarding entry now; cite retrospective context without inventing earlier entries. |
| Onboarding reveals optional refactoring opportunities. | Defer them and finish the baseline; do not turn adoption into a code audit. |

| The user says “Onboard this project” or the equivalent in another language. | Run the installed onboarding workflow without requiring a copied prompt; stop at the baseline unless continued work is authorized. |
