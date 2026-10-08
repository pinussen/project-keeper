# JetBrains IDEs

These routes apply to compatible JetBrains IDEs such as IntelliJ IDEA, PyCharm and WebStorm. First identify the assistant in your chat panel. AI Assistant, Junie and GitHub Copilot have different configuration. For Copilot, use [its separate guide](COPILOT.md#jetbrains-ides).

## AI Assistant

**Prerequisite:** AI Assistant is installed, enabled and can answer a chat in the target project. Complete [common setup](START.md). **Scope:** one project. **Source:** `adapters/jetbrains/project-keeper.md`.

1. Open IDE **Settings → Tools → AI Assistant → Rules**.
2. Select **New Project Rules File** and name it `project-keeper`. The resulting file belongs under `.aiassistant/rules/` and ends in `.md`.
3. In the new rule editor, choose rule type **Always**.
4. Paste the source policy into the rule body. Preserve any metadata the UI creates; the supplied adapter contains only the policy body. Save.
5. Open a new AI Assistant chat and run the common checks. Expand the attachments at the beginning of the response to check that this rule was included.

**If absent:** ensure the rule is not Off, Manually or limited to file patterns. Confirm you are chatting with AI Assistant rather than another agent.

[Official AI Assistant project rules](https://www.jetbrains.com/help/ai-assistant/configure-project-rules.html)

## Junie

**Prerequisite:** Junie is installed and working in the target project. Complete common setup. **Scope:** one project. **Source:** `adapters/junie/AGENTS.md`.

1. Open IDE Settings and search for **Junie**. Open its **Project Settings** and inspect **Guidelines path**.
2. If a custom path is configured, use that existing file as your shared destination. If no path is configured, inspect the target project: use `.junie/AGENTS.md` if it already exists; otherwise use `AGENTS.md` at the project root. Do not create a new overriding file that hides existing instructions.
3. Follow the shared-file procedure in common setup to insert the policy into the selected file, preserving existing content.
4. For a monorepo or nonstandard layout, explicitly set Guidelines path to the chosen file relative to Junie's Project path. Confirm the file is inside the allowed project.
5. Save and start a new Junie task. Run the common checks without authorizing file edits.

**If ignored:** check Guidelines path first. Without an explicit path, `.junie/AGENTS.md` takes precedence over root AGENTS.md. Verify the actual file and agent; an assistant's self-report alone does not establish loading.

[Official Junie settings](https://junie.jetbrains.com/docs/junie-plugin-project-settings.html) · [Guideline discovery](https://junie.jetbrains.com/docs/guidelines-and-memory.html)
