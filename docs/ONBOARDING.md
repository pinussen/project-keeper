# Onboard an existing project

Use this guide when adopting Project Keeper in a project that is already underway. The goal is a reliable starting point for continued work, not a restart, migration or general quality audit. A small standalone task still does not need onboarding.

## Before starting

1. Install Project Keeper for the assistant you will use, following the [installation guide](TOOLS.md).
2. Open the existing project's root in that assistant's environment. Make the current plan, relevant issues and any handoff notes accessible. If they live elsewhere, provide their location or an export with its date; do not share credentials in prompts.
3. Keep existing files and uncommitted work. Do not copy blank templates over current documents or run an initialization command that replaces them.

## Prompt to start onboarding

Paste this into your assistant in the target project:

> Onboard this existing project using Project Keeper. Read its current instructions, plan, recent work log and relevant evidence. Reconstruct the agreed outcome, current phase and remaining acceptance criteria without expanding scope. Reuse existing planning records and identifiers. Distinguish verified results, reported completion without verification, ongoing work, blockers and unknowns; cite the evidence. Ask only about gaps that materially affect the next decision. Add a dated onboarding baseline and a current work-log entry, preserving existing history and unrelated work. Do not change implementation, run disruptive tests, create tickets in an external system, publish or start backlog items as part of onboarding. Finish with a concise baseline and the next recommended action. Stop there unless I have separately authorized continued work.

If the authoritative planning system is read-only, the assistant should report that limit and prepare the baseline in an available project record, clearly marked as a proposed update. It must not silently create a competing authoritative plan or claim that the external record was updated.

## What the assistant should do

### 1. Inspect the minimum useful evidence

Read project instructions, the existing plan, relevant active issues, recent log/commit history and the actual deliverables needed to understand current work. Inspect working-tree changes before editing documentation. Use existing verification results when relevant; record their date/version and limitations.

Do not read every old commit or rerun every test merely because the project is new to this assistant. Expand inspection only to resolve a concrete uncertainty affecting delivery. Reading status and preparing documentation does not authorize deployment, destructive tests or unrelated code changes.

### 2. Recover the contract and current state

Identify the intended outcome, current phase, agreed deliverables, acceptance criteria, exclusions and explicit prior decisions. Separate confirmed decisions from inferred assumptions. Ask a short question when conflicting records or a missing decision would materially change the next step.

Use evidence labels alongside the project's existing status vocabulary:

| Evidence label | Meaning |
| --- | --- |
| Verified | Relevant evidence supports the result for the identified version or conditions. |
| Reported complete, unverified | A person, issue or document says it is complete, but supporting evidence has not been established. |
| In progress | Work has begun; identify what exists and what remains. |
| Blocked | A concrete dependency prevents progress; identify its owner and next action. |
| Unknown | Available sources do not establish the state. |

A closed issue or a commit is useful history, not automatic proof that the current acceptance criteria pass. Conversely, missing old evidence is not automatically a new defect or a reason to reopen completed work. Reconcile disagreements explicitly; do not silently relabel old work as done or failed.

### 3. Save one usable baseline

Update the existing plan rather than creating a parallel one. If none exists, create PROJECT_PLAN.md using only known facts and labeled assumptions. Keep existing task IDs and links.

The dated baseline should state:

- Outcome, current phase and remaining acceptance criteria.
- Relevant progress and evidence, including uncertainty.
- Real blockers, owners and the nearest next action.
- Which records are authoritative and what sources were inspected.

Append one current entry to the repository work log describing the onboarding. A summary of older events must be labeled retrospective and cite its sources. Do not invent historical entries, dates, effort estimates or past decisions. If no log exists, start it now rather than fabricating a complete history.

### 4. Stop when ready to continue

Onboarding is complete when there is one usable baseline, important uncertainty is visible and the next action is clear. A genuine blocker can remain; record it rather than calling the whole project complete. Optional improvements go into a later phase and do not hold up onboarding.

Report the baseline briefly. Continue implementation only if that work is already authorized. Avoid an extra approval loop when the user explicitly asked for both onboarding and continued work.

## What to check during your first practical test

- Existing plans, identifiers and unrelated files remain intact.
- The assistant can name the current outcome and next step without inventing history.
- Unverified claims remain visible and optional ideas do not become prerequisites.
- Onboarding ends with a usable baseline rather than an expanding audit.

If a check fails, capture the prompt, observed behavior, relevant instruction version and expected result. Keep this feedback in the test project's log or a clearly identified issue. These checks describe expected behavior; they are not a claim that every assistant has been tested.
