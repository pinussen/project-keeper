# Codex CLI and IDE extension

**Before starting:** Codex is installed, authenticated and can answer a request. Complete [common setup](START.md). **Recommended scope:** personal defaults across projects. **Source:** `adapters/codex/AGENTS.md`.

## Find the active global instruction file

The default directory is `.codex` under the home of the account running Codex. A configured `CODEX_HOME` changes it. To print the directory, open a terminal in the same environment as Codex and use the command for your shell:

macOS/Linux/WSL (Bash or Zsh):

```sh
printf '%s\n' "${CODEX_HOME:-$HOME/.codex}"
```

Windows PowerShell:

```powershell
if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
```

These commands print a path; they do not modify environment variables or files.

1. Open the printed directory; create it if it does not exist.
2. If a nonempty `AGENTS.override.md` is present, that is the active global instruction file. Otherwise use `AGENTS.md`. Do not create an override just to install Project Keeper.
3. Insert the complete source using the shared-file procedure in common setup, preserving existing content. Save.
4. Start a new Codex session in the target project (or a new conversation in the Codex extension). Ask it to list its active instruction sources, then run the common behavioral checks. Treat a self-report as a diagnostic, not conclusive loading evidence.

**One-project alternative:** insert the policy into the project's active root AGENTS.md or existing AGENTS.override.md instead. Project files closer to the working directory can override earlier guidance, so inspect existing instructions before changing them.

**If ignored:** check the active home, overrides, target working directory and a genuinely new session. Codex has instruction-size limits; a large existing instruction collection may be truncated. Do not remove other requirements to make space without reviewing the conflict.

[Official Codex instruction discovery and diagnostics](https://developers.openai.com/codex/guides/agents-md)
