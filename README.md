# Project Keeper

Reusable instructions that help AI assistants plan, manage and finish projects while preserving goals and history across tools and sessions.

**The project plan shows where the work stands. The work log explains how it got there.** Small standalone tasks remain lightweight and do not require project administration.

## What it does

- Defines goals, deliverables and stable acceptance criteria.
- Breaks work into steps with dependencies, owners and useful milestones.
- Updates the project plan when work starts, becomes blocked or finishes.
- Maintains a concise repository work log covering decisions, verification and interrupted work.
- Defers optional improvements to later phases unless they block the current delivery.
- Reads the current plan and log when resuming and provides a useful handoff.
- Closes the phase when its acceptance criteria are met.

Project Keeper consists of instructions and templates. It is not an agent server, scheduler or technical guarantee of model behavior. It supports different project domains, languages and planning systems. This repository is maintained in English; adopting projects can follow their own language conventions.

## Getting started

1. Clone this repository onto the computer or server where the assistant runs.
2. Use the [installer/updater](docs/INSTALLER.md) to select known destinations, or follow the [manual setup guide](docs/TOOLS.md). Cloning alone does not activate the instructions.
3. In your assistant, say **“Onboard this project”** (or the equivalent in your language). It should reuse existing records and establish a baseline. Small standalone tasks still bypass project administration.

Set up each relevant environment once. Preserve existing instructions; there is no need to configure every supported tool at the same time.

Supported setup guides cover VS Code, Kiro, Cursor, Windsurf/Cascade, JetBrains AI Assistant and Junie, Copilot in Visual Studio/JetBrains/Xcode/Eclipse, Claude Code, Codex and OpenClaw. Choose the assistant as well as the editor: their configuration is not interchangeable.

Already working on a project? Follow [Onboard an existing project](docs/ONBOARDING.md) to recover its current state without restarting it.

## Repository contents

| File or directory | Purpose |
| --- | --- |
| [PROJECT_KEEPER.md](PROJECT_KEEPER.md) | Canonical, tool-independent policy |
| [templates/](templates/) | Lightweight project-plan and work-log templates |
| [adapters/](adapters/) | Generated instruction files for supported tools |
| [docs/INSTALLER.md](docs/INSTALLER.md) | Opt-in installation, backups and registered-destination updates |
| [docs/TOOLS.md](docs/TOOLS.md) | Step-by-step setup, updates and activation checks |
| [docs/ONBOARDING.md](docs/ONBOARDING.md) | Bounded onboarding for projects already underway |
| [docs/EXAMPLES.md](docs/EXAMPLES.md) | Expected behavior and manual review scenarios |
| [PROJECT_PLAN.md](PROJECT_PLAN.md) and [WORK_LOG.md](WORK_LOG.md) | Plan and history for developing Project Keeper itself |

Each adopting project's plan and log belong in that project's repository or established planning system. This repository is not a central database of project status.

## Updating the policy

Edit PROJECT_KEEPER.md, then run:

```sh
python3 scripts/build_adapters.py
python3 scripts/build_adapters.py --check
```

On Windows, the command may be `py -3`. The script uses only the Python standard library and writes only generated adapters in this repository. It does not install anything.

After committing changes and pulling them on other machines, update any installed instruction copies. Documented imports or locally verified links can reduce copying; see the tool guide.

Keep documentation, templates, examples and code comments in English. Make reusable guidance independent of any particular person's projects, accounts or environment. Project-specific history belongs in the development plan and log, not in the reusable policy.

## Initial scope

Instructions, templates, generated adapters and documentation. An opt-in installer/updater now supports selected known destinations. Unattended background updates and a cross-project dashboard remain outside scope; running installation in an adopting environment is a separate user action.
