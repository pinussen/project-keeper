# Cursor Agent

**Before starting:** Cursor is installed, Agent chat works and the target project is open. Complete [common setup](START.md). These instructions configure Agent, not other assistants you might have installed in Cursor.

**Recommended scope:** one project. **Source:** `adapters/cursor/project-keeper.mdc`. **Destination:** `.cursor/rules/project-keeper.mdc` beneath the target project root. This is a dedicated rule file.

1. In your target project, create the `.cursor` directory and its `rules` subdirectory if missing.
2. Follow the common copy procedure to create `project-keeper.mdc` there using the complete source text.
3. Keep `alwaysApply: true` in the metadata at the top. The filename must end in `.mdc`, not `.md`.
4. Open **Customize → Rules** and check that Project Keeper is listed with an always-applied mode. If your version uses different labels, follow the official Rules page below.
5. Open a new Agent chat and run the two checks in common setup.

**Expected result:** the rule is available for chats in this project. If absent, check the file extension, metadata and which project folder is open.

**Optional global alternative:** open **Customize → Rules**, select the user-rules area and add the plain text from `PROJECT_KEEPER.md`. Preserve any existing user rules. Do not paste the `.mdc` metadata into a plain-text user-rule field. Use this instead of the project copy when you want personal rules across projects.

[Official Cursor rules documentation](https://cursor.com/docs/rules)
