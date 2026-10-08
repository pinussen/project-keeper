# Work log

## 2026-10-08 — baseline planning
- Initialized https://github.com/pinussen/project-keeper for the agreed project-management workflow.
- Cloned the repository; Git reported an empty repository, so no existing project files or instructions needed preservation.
- Created PROJECT_PLAN.md with fixed acceptance criteria, work steps and explicit exclusions.
- Started P1. No user environments have been configured; no live agent behavior has been tested.

## 2026-10-08 — policy and templates
- Completed P1/P2: added canonical PROJECT_KEEPER.md and lightweight plan/log templates.
- Policy covers small-task exemption, live status transitions, durable evidence-based logging, milestones, explicit scope changes and handoffs.
- Moved P3 to In progress. Tool guidance uses the official documentation consulted during baseline development; actual installation remains outside this baseline.

## 2026-10-08 — adapters and usage guide
- Completed P3 with six generated adapters, a standard-library-only generator, README, tool setup guide and behavioral examples.
- Ran generator and --check successfully: all six adapter files match the canonical policy with only required frontmatter differences.
- Explicitly documented Local Copilot file-matching limitations, Codex overrides, Kiro custom-agent resources and separate OpenClaw workspaces.
- P4 in progress. No automated installer or tool configuration changes were introduced.

## 2026-10-08 — baseline verification
- Completed P4: reviewed the policy against A1–A4 and checked all relative Markdown links; no missing targets.
- Six adapters match PROJECT_KEEPER.md. Behavioral cases are documented examples, not claims of live model tests.
- A1–A4 are complete. P5/A5 started; publication remains unverified until the remote is checked.

## 2026-10-08 — publication route
- Direct Git push could not authenticate in this environment; no repository data was overwritten.
- The connected GitHub integration confirmed write access and created README.md on main (b9919fc1e69bcf64dec507d521e40d2013b1b534).
- Publishing the remaining baseline through that integration. Remote verification is still pending.

## 2026-10-08 — phase complete
- Published baseline commit 938189f182be504db68b4aabc1642ff9da8188ca to main.
- Fetched remote main and compared every one of the 16 repository files byte-for-byte with the local baseline: all matched.
- Marked A5/P5 complete and closed the baseline phase. This follow-up records completion evidence; user-environment installation and runtime testing are not claimed.

## 2026-10-08 — public-audience update started
- Explicit requirement: maintain generic, English-language repository content for a worldwide audience.
- Started G1. Translate README and tool documentation, generalize examples and remove personal setup assumptions. Preserve historical results and core workflow behavior.

## 2026-10-08 — public-audience content verified
- Translated README.md, docs/TOOLS.md and docs/EXAMPLES.md into English; replaced domain-specific examples with general delivery scenarios.
- Removed the unrelated personal skill reference from current scope and clarified English maintenance requirements in AGENTS.md without imposing a language on adopting projects.
- Made two editorial changes to earlier log entries to remove conversation-specific phrasing; historical events and verification evidence remain unchanged.
- Reviewed all tracked text, checked relative links and ran build_adapters.py --check: all six adapters still match. Core policy behavior is unchanged. G1/G2 complete; G3 publication in progress.

## 2026-10-08 — public-audience update delivered
- Published cf3aa107a26b4836423e418da1b24a03a05c2567 and fetched remote main. Every tracked file matched the reviewed local version byte-for-byte.
- G3 complete. English documentation and generic usage guidance are now published; no adopting environments were modified.

## 2026-10-08 — explicit installation guides started
- Started I1 after the request for complete beginner-facing instructions and broader IDE coverage.
- Reviewed repository instructions and current plan; began checking official rules documentation for additional tools.
- Scope is setup documentation and required generated adapters, not an installer or changes to user environments.

## 2026-10-08 — setup guides and IDE coverage drafted
- Completed I1/I2: replaced the lookup table with a navigation index, common beginner setup and separate tool guides. Documented raw-text copying, exact roots, existing-file preservation, activation, updates and removal.
- Added Cursor, Windsurf/Cascade, JetBrains AI Assistant and Junie adapters; documented additional Copilot IDEs. Distinguished different assistants inside the same IDE.
- Checked official documentation; Windsurf docs now redirect to Devin Desktop/Cascade, so the guide identifies its agent scope and directory alternatives. The generator enforces the 12,000-character workspace-rule limit.
- Generated and checked all ten adapters successfully. I3 validation in progress; live IDE testing is not claimed.

## 2026-10-08 — setup guide validation
- Checked 37 relative links/anchors, all named adapter sources, ten generated adapters and the Windsurf rule size. All passed; git diff --check was clean.
- I3 content validation complete; publication and remote comparison are next. No IDE runtime test or local installation was performed.

## 2026-10-08 — setup guides delivered
- Published d6989eaf56c9c434f01e933bfa208bf477f1327a and verified every remote repository file against the reviewed local content (29 files).
- Marked I3 complete. Each listed assistant has an explicit route; optional alternatives and version limitations are identified. No further phase started.

## 2026-10-08 — existing-project onboarding started
- Started O1 after explicit approval to add onboarding and prepare for practical testing.
- Read current policy, plan and recent log. Scope is a bounded onboarding guide, canonical policy coverage and navigation links; no project migration or tool installation is being performed.

## 2026-10-08 — onboarding workflow drafted
- Completed O1: added docs/ONBOARDING.md with a ready-to-use prompt, evidence labels, preservation rules, baseline contents and a stop condition.
- Added self-contained onboarding rules to the canonical policy, so installed adapters do not depend on an unavailable guide path. Linked the guide from README, tool index and common setup; added boundary examples.
- O2 in progress. No real external project has been onboarded by this change.

## 2026-10-08 — onboarding checks passed
- All ten regenerated adapters match the canonical policy. Checked 42 local links/anchors and git diff --check.
- Windsurf workspace adapter is 10,373 characters, below its enforced 12,000-character limit.
- O2 publication pending; the change is ready for practical onboarding tests, which have not been performed here.

## 2026-10-08 — onboarding delivered; ready for testing
- Published b2a71f5464efd03d5d3176089093f99c800e541d; fetched remote main and compared all 30 files with local content. All matched.
- O2 complete. The implementation/documentation phase is closed and ready for practical testing. No actual project onboarding or IDE runtime test is claimed.

## 2026-10-08 — Claude setup clarification from practical feedback
- A user reported that Claude CLI found the global instruction file, but the guide left the source contents and relationship to repository CLAUDE.md files unclear.
- Rewrote docs/setup/CLAUDE.md around one complete global-copy route: exact source text, destination, filename, existing-content preservation, global/project coexistence and /memory verification.
- Moved imports and project-only installation after the explicit installation-complete point. Linked onboarding as the next optional action.
- This is a bounded documentation fix; no policy change or new feature scope. The reported loading success is not a claim of full behavioral testing.
- Validation: all links and section anchors in the revised guide resolve; git diff --check passed.

## 2026-10-08 — Kiro panel navigation clarified
- A user-provided screenshot confirmed Project Keeper under Agent Steering & Skills → Global after opening the ghost-icon Kiro panel.
- Expanded step 4 in docs/setup/KIRO.md with the exact navigation, Explorer distinction, nearby panel labels and expected file/breadcrumb/header. No screenshot or personal workspace details were added to the public repository.
- This confirms UI discovery only, not behavioral compliance. Policy and adapters are unchanged.

## 2026-10-08 — installer and short onboarding started
- Explicitly authorized installer/updater development, previously deferred, with English messages and multilingual natural-language onboarding activation.
- U1 in progress. Development and tests use temporary directories rather than real user configurations.

## 2026-10-08 — installer and onboarding implementation
- U1–U3 implemented: selectable targets, marked shared blocks/dedicated files, backups, integrity hashes, exact-copy adoption and registered-only updates with clean fast-forward Git refresh.
- Added short English onboarding requests and equivalent user-language activation to the policy and regenerated all adapters.
- Added an English installer guide with concrete Claude/Kiro adoption and VS Code project commands, explicit target coverage and recovery limits.
- Initial 13 isolated tests passed. Added two further cases for Windows newlines and a newly hiding Codex override; final checks pending. No real user configurations were changed.

## 2026-10-08 — installer validation passed
- All 15 isolated tests passed, including a real local Git fast-forward/restart update, exact historical-copy adoption, CRLF handling, backups, outside-block preservation, conflicts and registered-only updates.
- Ten adapters match the policy; 52 relative links/anchors passed, git diff --check passed and the Windsurf adapter remains below its enforced limit (10,989 characters).
- U4 ready for publication and practical user testing. Tests ran on Linux; native Windows/macOS and live IDE behavior were not exercised.
