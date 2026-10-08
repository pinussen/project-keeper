# Kiro IDE and CLI

For opt-in installation and future updates, see [the installer guide](../INSTALLER.md). The instructions below remain the manual route.

**Before starting:** Kiro is installed, authenticated and can answer a chat. Complete [common setup](START.md). **Recommended scope:** personal defaults across local projects. **Source:** `adapters/kiro/project-keeper.md`. **Destination:** `~/.kiro/steering/project-keeper.md`.

1. Open your user home directory in the environment running Kiro. Create `.kiro`, then `steering`, if missing.
2. Create the dedicated destination file with the complete source text using the common copy procedure.
3. Keep the opening `inclusion: always` metadata. Save.
4. Open your target project in Kiro. Click the **Kiro ghost icon** in the far-left vertical activity bar (not the file/Explorer icon). In the Kiro panel, scroll down if necessary and expand **Agent Steering & Skills**, then **Global**. Select **project-keeper**. The editor should open `project-keeper.md`; check that its breadcrumb points to your home directory's `.kiro/steering/` folder and that the file starts with `inclusion: always` between the `---` lines. The list can omit the `.md` extension.

   If you are still looking at the project file tree, you are in Explorer rather than the Kiro panel. Seeing **Specs** and **Agent Hooks** above **Agent Steering & Skills** helps identify the correct panel. These labels were confirmed in a user-provided Kiro IDE screenshot; other versions may arrange them differently. Seeing the file under Global confirms discovery in that UI, not that every agent has followed its instructions.

   You can also create a rule through the **+** beside **Agent Steering & Skills** and select global scope. Do not create another copy if `project-keeper` is already listed.
5. Start a new standard Kiro conversation, or a new CLI session in the target project, and run the common checks.

**One-project alternative:** put the same file at `.kiro/steering/project-keeper.md` under the target project root instead. Do not install both routes by default. Project steering takes priority when it conflicts with global steering.

**Custom agents:** these do not automatically include steering. In the selected custom agent's configuration, preserve its existing resources and add the relevant steering files. For project-local steering, the documented resource pattern is `file://.kiro/steering/**/*.md`. Verify the selected agent actually loads that resource. Do not replace the entire resources array or assume a standard-agent test validates a custom agent.

**If missing:** check global versus project scope, the account running the CLI, and whether you selected a custom agent. Cloud sessions cannot read your local home directory; this guide's global route is local.

[Official Kiro steering](https://kiro.dev/docs/steering/)
