# Windsurf / Cascade

**Before starting:** the editor is installed, Cascade chat works and the target project is open. Complete [common setup](START.md). The Windsurf rules documentation currently redirects to Devin Desktop/Cascade; these steps cover **Cascade**, not an assumed equivalent setup for the newer Devin Local agent.

**Recommended scope:** one project. **Source:** `adapters/windsurf/project-keeper.md`. **Destination:** `.windsurf/rules/project-keeper.md` in Windsurf, or `.devin/rules/project-keeper.md` when using the current Devin Desktop Cascade setup. Use one location, not both.

1. Open Cascade's **Customizations → Rules** and choose a workspace rule. Check which rule directory your editor uses; current documentation prefers `.devin/rules` and retains `.windsurf/rules` as fallback.
2. Create the destination directory/file if needed, using the common copy procedure and the entire source text.
3. Keep `trigger: always_on` at the top. If creating the rule through the UI, ensure its activation mode is **Always On**.
4. Confirm the rule appears in the workspace rules list, then open a new Cascade conversation and run the common checks.

**If absent:** check the active workspace and agent, rule directory and activation mode. Do not install identical copies in both directory formats.

Use a workspace rule for the full policy: its 12,000-character limit accommodates this adapter. The global rules file is limited to 6,000 characters and cannot hold the complete policy. The generator checks the workspace limit; do not silently truncate the file.

[Official rules documentation](https://docs.windsurf.com/windsurf/cascade/memories)
