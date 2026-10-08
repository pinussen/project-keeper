# Claude Code: install once for all your projects

Use this guide for **Claude Code CLI** or the **Claude Code VS Code extension**. If Claude is a model selected inside GitHub Copilot, use [the Copilot guide](COPILOT.md) instead.

Claude Code must already be installed and signed in. Download or clone Project Keeper first if needed: [get the files](START.md#1-get-the-files).

## 1. Copy the instructions into your home-directory file

Open these two files in a plain-text editor:

| File | What to do |
| --- | --- |
| `adapters/claude/CLAUDE.md` inside the downloaded Project Keeper folder | Copy **all of its text**. |
| `~/.claude/CLAUDE.md` in your user home directory | Paste the text here and save. Create the directory and file if missing. |

`~` means your home directory, not your project directory. Example destinations are `/home/alex/.claude/CLAUDE.md` on Linux, `/Users/alex/.claude/CLAUDE.md` on macOS, and `C:\Users\Alex\.claude\CLAUDE.md` on native Windows. For WSL, SSH or containers, use the home directory in the environment where Claude runs.

The filename is exactly **`CLAUDE.md`**: not `calude.md`, and not `CLAUDE.md.txt`. Paste the actual instruction text, not the source filename or a link to it.

If the destination already has instructions, keep them. Back up the file, then add the Project Keeper text at the end between these two marker lines:

```markdown
<!-- Project Keeper: start -->
<!-- Project Keeper: end -->
```

Put the copied text **between** the markers, not inside an HTML comment. If a Project Keeper block already exists, replace that block's contents instead of adding a duplicate. An otherwise empty file can simply contain the copied text.

## 2. Keep your project's own CLAUDE.md

You may also have a CLAUDE.md in a repository, including one created through `/init`. That is normal. **Claude reads the global and project instructions together.** The project file does not replace the global file simply because they share a name.

| Location | Purpose |
| --- | --- |
| `~/.claude/CLAUDE.md` | Your personal instructions across projects; install Project Keeper here once. |
| `your-project/CLAUDE.md` | That project's own conventions, commands and context; keep it. |

**Do not copy Project Keeper into every repository as well.** You do not need to run `/init` to activate the global instructions. If existing project instructions directly conflict with the policy, review the conflict rather than deleting the project file.

## 3. Start a new session and check

1. Save the home-directory CLAUDE.md.
2. End the current Claude conversation. From the project directory, start `claude` again. In the VS Code extension, open a new Claude Code conversation in the target project instead.
3. Enter `/memory` and inspect the instruction files. Confirm that the home-directory `.claude/CLAUDE.md` is included. A project CLAUDE.md may appear too; that is expected.

Once the global file is present, **installation is complete**. For an existing project, you can now use the [onboarding prompt](../ONBOARDING.md#prompt-to-start-onboarding). Optional [behavior checks](START.md#4-check-both-loading-and-behavior) help distinguish successful loading from reliable instruction-following.

## If the file is missing

Check the spelling, saved contents and home directory used by the actual Claude process. Check that you opened a new session and are using Claude Code, not Copilot. If your version does not expose `/memory` in the current interface, consult the official documentation below for its instruction inspection controls.

## Updating later

After downloading or pulling a newer Project Keeper version, copy the updated adapter text into the same global file. Replace only your Project Keeper block and preserve other instructions. Start a new conversation. Updating the downloaded repository alone does not update a pasted copy.

## Other installation choices — optional

You can stop reading here if the global setup above works.

- **Only one project or a shared team setup:** install the text in that project's CLAUDE.md instead of your global file. This deliberately changes the scope.
- **Import rather than copy:** Claude supports `@path` imports. If your clone actually lives at `/home/alex/tools/project-keeper`, a line `@/home/alex/tools/project-keeper/PROJECT_KEEPER.md` in your global CLAUDE.md imports the policy. Use your real path, retain the clone there, and remove any duplicate pasted policy. This is not required for normal installation.

[Official Claude Code memory and instructions](https://code.claude.com/docs/en/memory)
