# GitHub Copilot in IDEs

For opt-in installation and future updates, see [the installer guide](../INSTALLER.md). The instructions below remain the manual route.

**Before starting:** Copilot is installed, signed in and able to answer a chat in the target project. Complete [common setup](START.md). These routes apply to Copilot regardless of the model selected inside it. They do not configure a separate Claude Code or Codex extension.

## Shared project-file procedure

**Recommended scope:** one project. **Source:** `adapters/copilot/copilot-instructions.md`. **Destination:** `.github/copilot-instructions.md` at the target project root. This same source can serve the IDEs below.

1. Open the target project folder in the IDE, not the Project Keeper repository.
2. Create `.github` under the target root if missing. Open or create `copilot-instructions.md` inside it.
3. Copy the entire source text into that file. If it already contains instructions, back it up and use the marked-block procedure from common setup; do not replace other content.
4. Save, follow the activation instructions for your IDE below, then start a new Copilot chat and run the common checks.

Do not use `project-keeper.instructions.md` for this route: that separate adapter uses file matching, which is not the same as repository-wide guidance for planning conversations.

## VS Code

Use the shared project-file procedure. Open Settings with **Ctrl+,** on Windows/Linux or **Cmd+,** on macOS; search for `instruction file` and enable **Code Generation: Use Instruction Files** if shown for your Local agent. Check the response's References for the repository instruction file.

**Optional across-project setup:** select the intended agent, run **Chat: Open Customizations** from the Command Palette (**Ctrl+Shift+P**, or **Cmd+Shift+P**), choose Instructions and create a user instruction. Use `adapters/copilot/project-keeper.instructions.md`; file matching may omit planning-only chats. Copilot Agent Host supports a shared global file at `~/.copilot/copilot-instructions.md`; insert the plain adapter there using the shared-file procedure. Keep the project route for dependable project planning when the global/user route does not load.

**Troubleshooting:** check which agent is selected. VS Code's Local and Agent Host sessions do not necessarily discover identical user files. Instructions are not an inline-completion setting.

[Official VS Code customization guide](https://code.visualstudio.com/docs/agent-customization/custom-instructions)

## Visual Studio

Visual Studio is a separate application from VS Code. Use the shared project-file procedure in the repository containing your solution.

Open **Tools → Options**, search `custom instructions` and enable the option to load `.github/copilot-instructions.md` for Copilot Chat. In current layouts it appears under GitHub → Copilot → Copilot Chat. Confirm the file in the response's References, then run the common checks.

**Troubleshooting:** a solution subdirectory is not necessarily the repository root. Check where you saved `.github`. If the option is missing, consult the documentation for your Visual Studio version rather than changing VS Code settings.

[Official Visual Studio instructions](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context?view=visualstudio)

## JetBrains IDEs

Use the shared project-file procedure, or open **Settings → Tools → GitHub Copilot → Customizations → Copilot Instructions → Workspace** and insert the source there. Select **Global** instead only for personal across-project instructions. Preserve existing text in either scope.

After saving, start a Copilot chat and check References for the instruction file. If absent, confirm that GitHub Copilot is the active assistant and that the plugin is current.

## Xcode

Use the **GitHub Copilot for Xcode application**, not an assumed Xcode built-in AI setting. Open **Settings → Advanced → Custom Instructions → Current Workspace**. Insert the plain Copilot source using the shared-file procedure and save. Verify that the workspace is your target repository; the project file is `.github/copilot-instructions.md`.

Start a new Copilot chat and inspect References. If the wrong project appears, correct the workspace before changing more files.

## Eclipse

Use the shared project-file procedure in the actual project directory, not merely the Eclipse workspace parent. Save, open a new Copilot chat for that project and run the common checks. Workspace-level instructions are a separate alternative: Copilot status icon → **Edit preferences → GitHub Copilot → Custom Instructions**, then enable workspace instructions and insert the source in the workspace field.

If ineffective, verify which project owns the chat and update the Copilot extension. The official documentation labels this feature as preview; do not assume every plugin version exposes the same controls.

[Official Copilot IDE instructions (select the IDE tab)](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)
