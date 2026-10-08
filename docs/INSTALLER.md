# Install and update with the script

The script is an opt-in alternative to manual copying. It discovers known configuration directories, lets you choose destinations, preserves unrelated instructions and records what it installed. It does not configure accounts or install an IDE.

## Before you start

You need **Python 3.9 or newer**. Automatic updates also need **Git** and a clone of this repository with its normal upstream configured. No Python packages need installing.

Open a terminal **inside the Project Keeper repository**: the directory containing README.md and `scripts/`. If you already cloned it, get the new script with `git pull --ff-only`. If you downloaded a ZIP, extract a fresh copy; automatic Git fetching will not be available, but installation and local-copy updates still work.

On macOS/Linux/WSL use `python3` as shown below. On Windows PowerShell use `py -3` in its place. Run as your normal user in the environment where the assistant runs, not with sudo or as Administrator.

## 1. See what it finds — no changes

```sh
python3 scripts/project_keeper.py discover
```

The output shows target names and exact destination paths. “Found” means a known configuration directory exists, not proof that the tool is installed or its instructions are active. Merely discovering a directory never authorizes a write.

## 2. Select and install

```sh
python3 scripts/project_keeper.py install
```

The script lists detected destinations and asks for their numbers, separated by commas. Press Enter without a selection to cancel. It checks all selected files for conflicts before writing. A destination not detected can still be explicitly selected by name.

For a reproducible preview and installation of Claude and Kiro only:

```sh
python3 scripts/project_keeper.py install --targets claude,kiro --dry-run
python3 scripts/project_keeper.py install --targets claude,kiro
```

The first command writes nothing. The second applies the explicit selection; it does not ask again. Use just `claude` or `kiro` if appropriate.

### Already copied the instructions manually?

For a complete, unmodified policy copy, use:

```sh
python3 scripts/project_keeper.py install --targets claude,kiro --adopt-existing --dry-run
python3 scripts/project_keeper.py install --targets claude,kiro --adopt-existing
```

Adoption recognizes the current adapter and exact copies from up to 40 commits of that adapter's available local Git history, allowing newline differences. It makes backups before changes. A ZIP or shallow clone may not contain the old version needed for recognition; use a full clone if necessary.

If your CLAUDE.md has other instructions followed by an **unmarked** Project Keeper policy, the script refuses to guess where our block ends. Keep all text and manually put `<!-- Project Keeper: start -->` immediately before the copied policy and `<!-- Project Keeper: end -->` immediately after it. Then retry adoption. A changed policy block remains a conflict: preserve your custom rules outside the block and compare against the original before replacing it. Do not remove unrelated instructions to make installation pass.

An existing `@.../PROJECT_KEEPER.md` import is deliberately not replaced. It already loads from its referenced clone; either keep that manual import workflow or deliberately migrate it to a managed copy. Do not keep both copies.

## 3. Confirm installation

```sh
python3 scripts/project_keeper.py status
```

This lists registered paths, the recorded source commit and whether managed contents remain intact. The manifest also records the policy hash. This is an installation integrity check, not proof that the app loaded the file.

Start a new assistant session and use your [tool's activation check](TOOLS.md). Once the instructions load, say **“Onboard this project”**, **“Start using Project Keeper here”**, or the equivalent in your language. No long prompt or special slash command is required.

## 4. Update later

```sh
python3 scripts/project_keeper.py update
```

The script fast-forwards this clean Git checkout from its configured upstream, restarts the updated installer, and updates **only registered destinations**. Newly discovered tools are not added. Local changes, a detached checkout or a failed pull stop the automatic update rather than being discarded.

Preview without changing files or fetching:

```sh
python3 scripts/project_keeper.py update --dry-run
```

That preview uses the current local version. To inspect the latest version first, run `git pull --ff-only` yourself, then preview. To update from an already downloaded/pulled copy without network access:

```sh
python3 scripts/project_keeper.py update --no-pull
```

Edits inside a managed block or dedicated rule stop the update. Edits outside a shared-file block are preserved. Resolve the reported conflict before retrying; there is no force-overwrite flag.

## Supported automatic destinations

| Target | Destination and scope |
| --- | --- |
| `claude` | User-home `.claude/CLAUDE.md`; shared marked block |
| `kiro` | User-home `.kiro/steering/project-keeper.md`; dedicated file |
| `codex` | Active global AGENTS.md or existing nonempty AGENTS.override.md under CODEX_HOME, defaulting to user-home `.codex` |
| `copilot-global` | User-home `.copilot/copilot-instructions.md`; Copilot Agent Host, not an assumed VS Code Local profile |
| `copilot-project` | Explicit target project's `.github/copilot-instructions.md`; shared block |
| `cursor` | Explicit target project's `.cursor/rules/project-keeper.mdc` |
| `windsurf` | Explicit target project's `.devin/rules/project-keeper.md` if `.devin` exists; otherwise `.windsurf/rules/project-keeper.md`; Cascade only |
| `openclaw` | Explicit agent workspace's AGENTS.md; shared block |

Project and workspace destinations must be specified explicitly; the script does not search all your repositories or parse arbitrary agent configurations.

### VS Code Copilot: configure one project

From the Project Keeper folder, replace the example path with your actual project root:

```sh
python3 scripts/project_keeper.py install --project "/absolute/path/to/your-project" --targets copilot-project --dry-run
```

Check the printed destination, then run the same command without `--dry-run`. On PowerShell, for example, use `py -3` and a quoted path such as `"C:\Users\Alex\Projects\my-app"`. The project must already exist. For Local versus Agent Host and activation, follow [the Copilot guide](setup/COPILOT.md#vs-code).

To inspect project-specific candidates without writing, use `discover --project "/absolute/path/to/your-project"`. For OpenClaw, use `--workspace "/actual/agent/workspace" --targets openclaw` with the install command. Updates remember these exact paths.

Other guide-supported configurations, including JetBrains rule-type UI settings and VS Code Local user profiles, remain manual. The script does not claim to discover or configure all editor profiles, custom agents or remote environments.

## Backups, records and recovery

Default state directory: `~/.config/project-keeper/` (also used under the Windows user home). It contains `installations.json` and a `backups/` directory. Backups are outside tool instruction folders so they cannot become duplicate rules. Every changed existing destination is backed up before writing; new files do not need a prior backup. The output prints backup paths, and each registration records its latest backup.

Files are replaced atomically individually, and original file permissions are preserved where supported. Conflicts are checked before writes; an unexpected I/O error can still leave a partially applied multi-file operation. Read the reported results and `status` before retrying. Do not run two installer instances concurrently.

To stop managing one destination, back up installations.json and remove only that destination's entry from its `installations` object. This does not remove the installed instructions. To uninstall them too, remove only the marked block or dedicated file you installed. To restore prior content, copy the reported backup to its original path after checking for newer edits; then reconcile/remove its registration so the next update does not silently reapply it.

Symbolic-link destination files are refused; use the manual setup guide for them. `--home` and `--state-dir` can select isolated locations for testing. CODEX_HOME still selects Codex's configuration when set; inspect discovery output before applying any test selection.

## Validation

Run the automated tests from this repository with:

```sh
python3 -m unittest discover -s tests -v
```

Tests use temporary directories and local Git repositories. They cover backups, preservation of unrelated content, repeated installs, adoption, conflicts and registered-only updates. These tests do not prove that every IDE loads the installed instructions.
