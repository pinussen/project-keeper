# Working on Project Keeper

Read PROJECT_KEEPER.md, PROJECT_PLAN.md and the latest entries in WORK_LOG.md before project work. Follow the applicability filter: standalone trivial changes do not require a new plan.

PROJECT_KEEPER.md is the canonical reusable policy. Update generated adapters through `python3 scripts/build_adapters.py`; do not hand-edit them. Run `python3 scripts/build_adapters.py --check` before delivery when the policy or generator changes.

Keep this repository's plan current at work transitions, and append concise evidence-based log entries. Preserve scope and completed decisions. Do not install instructions into user environments unless that installation is requested. Keep the installer dependency-free and limited to explicitly selected instruction destinations.

Maintain all repository documentation, templates, examples, instructions and code comments in English. Keep reusable content generic: no personal project history, account assumptions or private setup references. Use broadly applicable examples. Adopting projects may use their own languages and conventions; this repository's language policy must not be imposed on them.
