# Common setup: start here

## 1. Get the files

Choose one method:

- **Without Git:** Open [the repository](https://github.com/pinussen/project-keeper), select **Code → Download ZIP**, then extract the ZIP. The extracted folder containing README.md is your **Project Keeper folder**.
- **With Git:** Open Terminal on macOS/Linux or PowerShell on Windows. Change to the directory where you keep repositories, then run:

```sh
git clone https://github.com/pinussen/project-keeper.git
```

The new `project-keeper` directory is your **Project Keeper folder**. If Git reports that the destination already exists, use that existing copy rather than cloning over it.

## 2. Know which folder is which

- **Project Keeper folder:** contains this reusable policy and the `adapters` directory.
- **Target project root:** the top-level folder of the project you actually want the assistant to work on. It is not the Project Keeper folder unless you are developing Project Keeper itself. In a Git checkout, `git rev-parse --show-toplevel` prints this location.
- **User home:** your account's home directory in the environment running the assistant. `~` is shorthand used in these guides. For example, `/home/alex`, `/Users/alex` or `C:\Users\Alex`.
- **Project scope:** applies to the target project; commit its instruction file if you want teammates to receive it.
- **Global/user scope:** applies to that tool's projects for this account on this machine. It is not automatically shared across computers, WSL, containers or SSH hosts.

Open the **target project** in your IDE. Open adapter files separately when copying their contents. Do not accidentally configure only this repository and then expect the instructions in another project.

## 3. Put the exact content in the exact destination

Each tool guide names a **source** inside the Project Keeper folder and a **destination** inside the target project or user home. Use a plain-text editor; Markdown files are plain text. You do not need to render the file or paste its rendered web view.

1. Open the source file. Select all of its raw text and copy it, including any `---` metadata header.
2. Navigate to the destination's parent directory. Create missing directories exactly as named, including a leading dot such as `.github`.
3. If the destination does not exist, create it with the exact filename and paste the source text. Save as UTF-8. On Windows, check that it did not become `AGENTS.md.txt` or `project-keeper.mdc.txt`.
4. If a **shared destination** already exists (such as AGENTS.md, CLAUDE.md or copilot-instructions.md), first save a backup outside the instruction-discovery folders. Keep its existing content and append the policy between `<!-- Project Keeper: start -->` and `<!-- Project Keeper: end -->` markers. On later updates, replace only that marked block. These shared-file adapters have no metadata header.
5. For a **dedicated rule file**, use an unused filename if a file with that name already contains unrelated instructions. Do not paste two metadata headers into one file. Preserve any metadata created by the tool's UI when a guide explicitly tells you to paste only the policy body.

To reach hidden home folders: in macOS Finder choose **Go → Go to Folder** and enter the full directory; in Windows File Explorer use the address bar; on Linux use the file manager's location bar. Create the directory if it is missing. You can use your editor's Open/Save dialog to reach the same path.

## 4. Check both loading and behavior

Save the file, then open a **new assistant conversation** in the target project. Follow your tool guide's loading check. Where available, an instruction reference or settings entry is stronger evidence than the assistant simply saying it read the file.

Then send this non-mutating test:

> Do not edit files. For this hypothetical project, every agreed acceptance criterion has passed. You notice that an optional extra export format might be useful. Is the current phase complete, and what should happen to that idea?

Expected: the phase is complete; the optional format belongs in a later phase. Then test the small-task exemption:

> Do not edit files. A standalone request changes one configuration value and has no project dependencies. Does Project Keeper require a new project plan and work log?

Expected: no new project administration; perform proportionate verification when executing the actual task. These are smoke checks, not a guarantee of every future response.

## 5. Start real work

Describe the outcome you want. You do not need to copy the templates into every project in advance. For actual project work, the assistant should first reuse an existing plan/log; create them only when needed. A small standalone task should bypass that process.

## Update or remove

For a Git copy, open a terminal in the Project Keeper folder and run `git pull --ff-only`. If it reports local changes or divergence, resolve that normally; do not discard local edits just to update instructions. For a ZIP copy, download and extract the new version separately.

Repeat the applicable copy/paste steps with the new adapter. A downloaded or pulled update does not update installed copies automatically. To uninstall, remove only the Project Keeper block, dedicated rule file, or import line you added. Preserve other instructions and the project's plan/log. Start a new conversation afterward.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Nothing changes | Correct target project, assistant, execution environment, destination filename and new conversation |
| The file appears missing | Hidden dot-directory, accidental .txt extension, or file saved in the Project Keeper folder rather than the target project |
| Only code-editing requests see the rule | A file-matched rule was used instead of the guide's always-on/project route |
| Old rules remain | Installed copy not updated, duplicate global/project blocks, active override, or old conversation context |
| Works locally but not over SSH/WSL | The remote assistant has a different home directory or workspace |
| Another tool cannot see the latest plan | Update the project clone or use the same authoritative planning source; rule synchronization is separate from project-status synchronization |

A symbolic link is optional and not required by these guides. Do not assume all applications follow links or expand another tool's import syntax.
