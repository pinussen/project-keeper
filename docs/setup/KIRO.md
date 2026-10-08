# Kiro IDE and CLI

**Before starting:** Kiro is installed, authenticated and can answer a chat. Complete [common setup](START.md). **Recommended scope:** personal defaults across local projects. **Source:** `adapters/kiro/project-keeper.md`. **Destination:** `~/.kiro/steering/project-keeper.md`.

1. Open your user home directory in the environment running Kiro. Create `.kiro`, then `steering`, if missing.
2. Create the dedicated destination file with the complete source text using the common copy procedure.
3. Keep the opening `inclusion: always` metadata. Save.
4. Open your target project in Kiro. In its Steering interface, check that the global rule is available. Alternatively, when creating through the IDE's Steering controls, select global scope and paste the same contents into the new rule.
5. Start a new standard Kiro conversation, or a new CLI session in the target project, and run the common checks.

**One-project alternative:** put the same file at `.kiro/steering/project-keeper.md` under the target project root instead. Do not install both routes by default. Project steering takes priority when it conflicts with global steering.

**Custom agents:** these do not automatically include steering. In the selected custom agent's configuration, preserve its existing resources and add the relevant steering files. For project-local steering, the documented resource pattern is `file://.kiro/steering/**/*.md`. Verify the selected agent actually loads that resource. Do not replace the entire resources array or assume a standard-agent test validates a custom agent.

**If missing:** check global versus project scope, the account running the CLI, and whether you selected a custom agent. Cloud sessions cannot read your local home directory; this guide's global route is local.

[Official Kiro steering](https://kiro.dev/docs/steering/)
