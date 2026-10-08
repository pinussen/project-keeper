# Using Project Keeper with different tools

Checked against official documentation on 2026-10-08. Tool version, agent type and execution environment can affect instruction loading. This guide does not install anything automatically.

## Common approach

PROJECT_KEEPER.md is the canonical policy. Adapters contain the same text with tool-specific frontmatter where necessary. Generate them with scripts/build_adapters.py; do not maintain separate copies by hand.

Read existing instructions before installation. Use a separate file where supported; otherwise insert a clearly bounded Project Keeper section without replacing unrelated content. On updates, replace only that section and avoid duplicates. Do not replace an existing AGENTS.md or CLAUDE.md with a link that would hide its other instructions.

Install instructions where the assistant actually runs. Native Windows, WSL, SSH sessions, containers and servers can have different home directories. A separately cloned repository is not automatically loaded merely because it exists on disk. In the table below, `~` denotes the home directory of the account running the tool; use the appropriate native path for that environment.

## Instruction locations

| Tool | Adapter | Location or activation |
| --- | --- | --- |
| Kiro IDE/CLI | adapters/kiro/project-keeper.md | A separate file under ~/.kiro/steering/ for local projects, or .kiro/steering/ within a project. The adapter specifies inclusion: always. |
| Codex CLI | adapters/codex/AGENTS.md | Insert into the active global instruction file under CODEX_HOME, normally ~/.codex/AGENTS.md. If AGENTS.override.md exists, it takes precedence at that level. Project instructions can affect the resulting behavior. |
| Claude Code CLI and the Claude Code VS Code extension | adapters/claude/CLAUDE.md | Insert into ~/.claude/CLAUDE.md, or use a documented @path import pointing to the cloned PROJECT_KEEPER.md. Use the actual local path. |
| Copilot Agent Host in VS Code | adapters/copilot/copilot-instructions.md | Insert into ~/.copilot/copilot-instructions.md for personal instructions. |
| Copilot Local in VS Code | adapters/copilot/project-keeper.instructions.md | Create a user instruction through Chat: Open Customizations for the selected agent and use the adapter contents. applyTo: "**" covers matching file work. |
| Copilot project instructions | adapters/copilot/copilot-instructions.md | Insert into the project's .github/copilot-instructions.md, including for project conversations where a file-matched instruction might not activate. |
| OpenClaw | adapters/openclaw/AGENTS.md | Insert into AGENTS.md in each relevant agent's actual workspace. The default is commonly ~/.openclaw/workspace, but check the active configuration. |

Kiro custom agents need to include the relevant steering files explicitly in their resources. Do not assume global steering reaches every custom agent automatically.

“Claude in VS Code” can mean either the Claude model selected in Copilot, which uses Copilot instructions, or the Claude Code extension, which uses Claude Code instructions.

Copilot instructions apply to agent/chat interactions, not inline completions while typing. For Copilot Local, file-matched user instructions do not guarantee inclusion in a planning-only conversation. Use project instructions or attach the instruction when necessary. Select the appropriate agent type in VS Code's customization settings.

OpenClaw should reuse an existing issue or planning system when one is already authoritative. Keep the work log in the project's repository and link the relevant issue. Workspace instructions do not replace the project's actual status.

## Import, link or copy

Claude Code supports documented @path imports in CLAUDE.md. Do not assume that syntax works in other tools. For a standalone instruction file, a symbolic link can be useful if the environment supports and actually reads it; verify this locally. A regular copy is straightforward but must be updated after git pull. Automated installation and synchronization are outside the initial scope.

## Installation prompt for a local assistant

> Read Project Keeper's README.md, PROJECT_KEEPER.md and docs/TOOLS.md. Install its instructions for the tool and environment we are using. First identify the actual instruction location and read existing files. Preserve unrelated content and back up files before changing them. Use a separate file or documented import where appropriate; otherwise use a clearly bounded section that can be updated without duplication. Do not change other tools' configuration unless they are included in my request. Reuse the project's plan and work log. Report which files changed and what needs checking in a new session. Do not claim the instructions were loaded merely because a file was created.

## Checking activation

Open a new session and inspect the loaded instruction list or references where the tool provides them. If the instruction is missing, check actual paths and overrides. Try relevant scenarios from EXAMPLES.md. One successful response is not proof that every future response will follow the policy.

Keep the same current project plan available when switching tools. Multiple clones require normal version control or a shared, readable planning source. Unsynchronized status copies do not provide continuity.

## Official sources

- Kiro: https://kiro.dev/docs/steering/
- Codex: https://developers.openai.com/codex/guides/agents-md
- Claude Code: https://code.claude.com/docs/en/memory
- VS Code: https://code.visualstudio.com/docs/agent-customization/custom-instructions
- OpenClaw: https://docs.openclaw.ai/concepts/agent-workspace
