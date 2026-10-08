# Project Keeper — project plan

## Outcome and scope
Provide reusable, tool-independent project-management instructions and usage documentation in this repository. Keep rules here; keep each adopting project's plan and work log in that project's repository or existing system of record.

This baseline captures the project requirements established on 2026-10-08. Explicit user changes may revise it; optional discoveries do not extend it.

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
No deadline agreed. First milestone: repository baseline ready to use. No invented duration estimates. Installation in adopting environments is a separate task.

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
- Installation or runtime testing in adopting environments.
- Migration of unrelated existing instruction systems.

## Handoff
Current phase: initial baseline complete. All acceptance criteria passed. Installation on user devices and actual tool-runtime validation remain outside this phase; no phase-2 work has started. Reviewable instructions are the deliverable, not proof of compliance by every model.

## Follow-up: public, English-language documentation
Explicit scope change, 2026-10-08: make the repository generic and suitable for a worldwide audience.

| Step | Acceptance criterion | Status | Evidence |
| --- | --- | --- | --- |
| G1 | All maintained repository content is English; examples are broadly applicable and personal setup references are removed. | Done | README, tool guide and examples translated; personal setup references removed |
| G2 | Contributor guidance preserves the English, generic baseline; adapters and documentation links remain valid. | Done | All tracked text reviewed, local links valid, six adapters verified |
| G3 | Publish and verify the update. | Done | Remote cf3aa10 verified against all tracked files |

No new tool integrations or installation features are included.

Follow-up complete: public documentation is English and generic. No additional phase has started.

## Follow-up: explicit setup guides and additional IDEs
Scope change, 2026-10-08: replace the reference-only setup guide with beginner-ready instructions and cover additional common IDEs.

| Step | Acceptance criterion | Status | Evidence |
| --- | --- | --- | --- |
| I1 | Each supported setup states prerequisites, scope, exact source/destination or menu, preservation of existing content, activation check and troubleshooting. | Done | Common start guide and separate tool recipes with checks/troubleshooting |
| I2 | Add Cursor, Windsurf, JetBrains AI Assistant/Junie and Copilot in Visual Studio, JetBrains, Xcode and Eclipse where documented. | Done | Official sources reviewed; four new adapters generated |
| I3 | Check generated adapters, links and installation examples; publish verified documentation. | Done | Ten adapters, 37 links/anchors and source paths checked; remote d6989ea matched |

Automatic installers remain excluded. Provide one clear recommended route per tool before optional global alternatives.

Setup-guide follow-up complete. Guides are documentation-verified, not live-tested in every IDE. No automatic installer or adopting-environment configuration was added.

## Follow-up: onboard existing projects
Scope change, 2026-10-08: add a bounded onboarding workflow, then hand the version over for practical testing.

| Step | Acceptance criterion | Status | Evidence |
| --- | --- | --- | --- |
| O1 | Guide and canonical policy recover existing state, preserve authoritative records, label uncertainty and avoid invented history or scope expansion. | Done | docs/ONBOARDING.md and policy section 2; historical uncertainty and authorization boundaries explicit |
| O2 | Link onboarding from setup/README, regenerate adapters, check consistency and publish. | Done | Ten adapters and 42 links checked; remote b2a71f5 verified |

No additional features are included in this follow-up.

Current handoff: onboarding documentation delivered; ready for practical testing in an adopting environment. No further feature work has started. Runtime testing remains unperformed, not a claimed pass.

Practical-test feedback, 2026-10-08: global instruction discovery in Claude CLI was reported successful. Clarified the Claude setup guide in response; broader behavior remains unverified. This documentation correction does not reopen feature scope.

Practical-test feedback, 2026-10-08: a Kiro IDE screenshot confirmed global rule discovery. Added precise panel navigation to the setup guide; behavior testing remains separate.

## Follow-up: opt-in installer/updater and short onboarding requests
Explicit scope change, 2026-10-08: implement the previously deferred installer and short natural-language onboarding activation.

| Step | Acceptance criterion | Status | Evidence |
| --- | --- | --- | --- |
| U1 | Discover known destinations without writing; let users select targets; preserve unrelated instructions, back up changes and record installed versions. | Done | scripts/project_keeper.py: discovery, selection, backups and manifest |
| U2 | Update only registered destinations from the latest clean Git checkout; reject local managed-content conflicts and support preview/offline use. | Done | Registered-only update, preflight checks and Git refresh covered by tests |
| U3 | Short onboarding requests work in English and equivalent user languages; instructions and UI remain English. | Done | Short requests and equivalent user-language intent in every adapter |
| U4 | Document concrete test commands, validate and publish. | In progress | Documentation complete; running final isolated tests |

Supersedes the earlier installer exclusion for this bounded implementation. No background updater, automatic installation into every discovered tool or portfolio features are included.
