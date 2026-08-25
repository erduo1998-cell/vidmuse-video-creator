# Contributing

Contributions should improve an observed VidMuse workflow, first-run failure, request contract, or delivery outcome.

1. Keep examples account-neutral and use obvious placeholders.
2. Do not commit local sessions, project bindings, task IDs, signed URLs, customer briefs, input media, or generation logs.
3. Treat model names, parameters, prices, and plan benefits as live facts; do not hard-code temporary catalog counts.
4. Put shared routing and invariants in `SKILL.md`; keep mode-specific detail in a referenced file.
5. Add a deterministic test when changing a script or fragile request contract.
6. Run `python3 tests/validate_repo.py` before opening a change.

Do not redistribute the official VidMuse CLI binary or copy private platform data into this repository. Link to the official installer and sources instead.
