# Project Keeper — project plan

## Outcome and scope
Provide reusable, tool-independent project-management instructions and usage documentation in this repository. Keep rules here; keep each adopting project's plan and work log in that project's repository or existing system of record.

This baseline captures the user's decisions from 2026-10-08. Explicit user changes may revise it; optional discoveries do not extend it.

## Acceptance criteria
| ID | Criterion | Verification | Status |
| --- | --- | --- | --- |
| A1 | Instructions cover applicability, fixed delivery criteria, phases, dependencies, responsibility, milestones, decisions, changes and completion. | Review against agreed requirements. | Done — PROJECT_KEEPER.md sections 1–8 |
| A2 | Require a live project plan and repository work log, updated during work and read on continuation; preserve existing equivalents. | Review lifecycle and templates. | Done — policy sections 2, 5, 6 and templates |
| A3 | Small standalone tasks bypass project administration; project-related small tasks use existing context proportionately. | Review explicit examples and boundary cases. | Done — policy section 1 and docs/EXAMPLES.md |
| A4 | Document Kiro, VS Code Copilot, Claude Code extension/CLI, Codex CLI and OpenClaw setup from one common rule source. | Generated files match source; installation guidance cites official docs. | Done — generator --check and docs/TOOLS.md |
| A5 | Publish the baseline to the supplied repository with its own current plan and log. | Confirm remote commit and paths. | Done — remote 938189f verified against all 16 local files |

## Work steps
| Step | Work | Depends on | Owner | Status | Result / evidence |
| --- | --- | --- | --- | --- | --- |
| P1 | Define common workflow and applicability | — | AI | Done | PROJECT_KEEPER.md sections 1–8 |
| P2 | Add plan and work-log templates | P1 | AI | Done | templates/PROJECT_PLAN.md and templates/WORK_LOG.md |
| P3 | Add tool adapters and usage guide | P1 | AI | Done | Six generated adapters, README.md and docs/TOOLS.md |
| P4 | Check requirements and adapter consistency | P1–P3 | AI | Done | Requirement review, adapter consistency and documentation links pass |
| P5 | Publish baseline | P4 | AI | Done | Remote main 938189f verified against local baseline |

## Timing
No deadline agreed. First milestone: repository baseline ready to use. No invented duration estimates. Installation in the user's environments is a separate later task.

## Blockers
None established.

## Decisions
- 2026-10-08: Repository name project-keeper. Store reusable instructions and usage guidance here, not unrelated project state.
- Use lightweight project management and exempt small standalone changes.
- Require both current plan state and historical work log in project repositories.
- One canonical rule source; generated tool copies avoid hand-maintained variants.

## Phase 2 / exclusions
- Automatic installer/updater and cross-machine synchronization.
- Portfolio dashboard or central status database.
- Installation or runtime testing on the user's devices, servers and agents.
- Migration of the existing ChatGPT finish-phase-one skill.

## Handoff
Current phase: initial baseline complete. All acceptance criteria passed. Installation on user devices and actual tool-runtime validation remain outside this phase; no phase-2 work has started. Reviewable instructions are the deliverable, not proof of compliance by every model.
