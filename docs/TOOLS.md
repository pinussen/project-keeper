# Installation guide

Start with [the common setup steps](setup/START.md), then choose **one** guide below. Each guide states its scope, source file, destination, activation check and likely failure points. No script in this repository installs instructions into an application.

These instructions configure Project Keeper in an existing, working AI tool. If you have not installed or signed into that tool yet, use its linked official documentation first and confirm that a simple chat works. You do not need Python unless you modify the policy and regenerate adapters.

## Choose your actual assistant

| Editor or environment | Assistant | Guide |
| --- | --- | --- |
| VS Code | GitHub Copilot, including Claude selected as its model | [Copilot in VS Code](setup/COPILOT.md#vs-code) |
| VS Code | Claude Code extension | [Claude Code](setup/CLAUDE.md) |
| VS Code | Codex extension | [Codex](setup/CODEX.md) |
| Kiro | Built-in assistant / Kiro CLI | [Kiro](setup/KIRO.md) |
| Cursor | Agent | [Cursor](setup/CURSOR.md) |
| Windsurf / Cascade | Cascade | [Windsurf](setup/WINDSURF.md) |
| IntelliJ IDEA, PyCharm, WebStorm or another compatible JetBrains IDE | AI Assistant | [JetBrains AI Assistant](setup/JETBRAINS.md#ai-assistant) |
| JetBrains IDE | Junie | [Junie](setup/JETBRAINS.md#junie) |
| JetBrains IDE | GitHub Copilot | [Copilot in JetBrains](setup/COPILOT.md#jetbrains-ides) |
| Visual Studio (different from VS Code) | GitHub Copilot | [Copilot in Visual Studio](setup/COPILOT.md#visual-studio) |
| Xcode | GitHub Copilot extension | [Copilot in Xcode](setup/COPILOT.md#xcode) |
| Eclipse | GitHub Copilot extension | [Copilot in Eclipse](setup/COPILOT.md#eclipse) |
| Terminal | Claude Code CLI / Codex CLI | [Claude](setup/CLAUDE.md) / [Codex](setup/CODEX.md) |
| OpenClaw server | Configured OpenClaw agent | [OpenClaw](setup/OPENCLAW.md) |

Installing instructions for one assistant does not configure another assistant in the same editor. For example, choosing Claude inside Copilot does not make Copilot read Claude Code's configuration.

## What “supported” means here

The guides were checked against the official documentation linked in each guide on **2026-10-08**. Generated adapters and documentation links are checked locally. We have not run every application or every version. Menu labels and capabilities can vary; if a documented control is missing, use the named official source rather than guessing another setting.

Start with the recommended route in your guide. Optional global setup is separated from project setup so you can tell exactly where instructions apply. Do not install the same policy globally and locally unless you intentionally want both copies in context.

For updates, removal, multiple machines and verification, see [common setup](setup/START.md). For expected project-management behavior, see [examples](EXAMPLES.md).
