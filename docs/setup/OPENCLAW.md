# OpenClaw

**Before starting:** OpenClaw and the intended agent are already running. You can send that agent a message and access its workspace files or Control UI. Complete [common setup](START.md). **Scope:** the selected agent's workspace, not every agent automatically. **Source:** `adapters/openclaw/AGENTS.md`.

1. In the Control UI, open **Settings → Agents → Files** and select the intended agent. Confirm its configured workspace. If working through files instead, determine that workspace from the active agent configuration; do not assume all agents use the default `~/.openclaw/workspace`.
2. Open that workspace's existing `AGENTS.md`. In the UI, select Edit if needed. This is a shared instruction file: back it up and preserve its current operating rules.
3. Copy the source text into a single marked Project Keeper block, following common setup. Save using the UI's save control or your editor, then reopen the file to confirm the text persisted.
4. Start a new session with that same agent and run the common behavioral checks. Ensure you are testing the agent whose workspace you edited.
5. Repeat only for other agents you actually want to configure, checking each workspace separately.

**Where project data belongs:** the operating rule goes in the agent workspace, but a project's work log belongs in that project's repository. Reuse an existing ticket system for planning if authoritative, and link the relevant ticket. The workspace AGENTS.md is not the project's status database.

**If ignored:** check agent selection, saved workspace path, new session and any bootstrap/context size limits in your OpenClaw version. A downstream external CLI agent may have its own instructions; this setup does not automatically configure it.

[Official OpenClaw workspace documentation](https://docs.openclaw.ai/concepts/agent-workspace)
