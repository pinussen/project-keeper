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
2. Follow the [step-by-step installation guide](docs/TOOLS.md) for your actual assistant. Cloning alone does not activate the instructions.
3. Reuse the adopting project's existing plan and log. If none exist, start with the [templates](templates/).

Set up each relevant environment once. Preserve existing instructions; there is no need to configure every supported tool at the same time.

Supported setup guides cover VS Code, Kiro, Cursor, Windsurf/Cascade, JetBrains AI Assistant and Junie, Copilot in Visual Studio/JetBrains/Xcode/Eclipse, Claude Code, Codex and OpenClaw. Choose the assistant as well as the editor: their configuration is not interchangeable.

## Repository contents

| File or directory | Purpose |
| --- | --- |
| [PROJECT_KEEPER.md](PROJECT_KEEPER.md) | Canonical, tool-independent policy |
| [templates/](templates/) | Lightweight project-plan and work-log templates |
| [adapters/](adapters/) | Generated instruction files for supported tools |
| [docs/TOOLS.md](docs/TOOLS.md) | Step-by-step setup, updates and activation checks |
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

Instructions, templates, generated adapters and documentation. Automatic installation, a cross-project dashboard and installation in adopting environments are outside this baseline.
