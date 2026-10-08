# Claude Code: CLI and VS Code extension

**Before starting:** Claude Code is installed and signed in, either in the terminal or through its VS Code extension. Confirm a chat works. If you chose Claude as a model inside GitHub Copilot, use [the Copilot guide](COPILOT.md) instead.

Complete [common setup](START.md). **Recommended scope:** personal defaults across projects. **Source:** `adapters/claude/CLAUDE.md`. **Destination:** `~/.claude/CLAUDE.md` in the environment running Claude Code.

1. Navigate to your user home and create `.claude` if missing.
2. Open or create `CLAUDE.md` inside it. Follow the shared-file copy procedure, preserving existing instructions and inserting only one Project Keeper block.
3. Save. In the CLI, start a new `claude` session from your target project directory. In VS Code, open the target project and start a new conversation in the **Claude Code** panel.
4. Use Claude Code's `/memory` command, where available, to inspect loaded instruction files. Confirm the user-level CLAUDE.md is present, then run the common behavioral checks.

**One-project alternative:** insert the same source into the project's existing CLAUDE.md, or create CLAUDE.md at its root if none exists. Use this instead of the global copy when sharing the rule with that project's contributors.

**Optional import instead of copying:** Claude supports `@path` imports in CLAUDE.md. For example, if the clone actually lives at `/home/alex/tools/project-keeper`, add `@/home/alex/tools/project-keeper/PROJECT_KEEPER.md` on its own line in the destination. Replace that example with your real path. Keep the clone at that location. The copy route avoids path/import complications and works without a permanent clone location.

**If ignored:** verify the execution home (local versus WSL/SSH/container), active extension and loaded file list. Do not assume Copilot reads this file. Project instructions and managed configuration may also affect behavior.

[Official Claude Code memory and instructions](https://code.claude.com/docs/en/memory)
