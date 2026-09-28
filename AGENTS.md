# AGENTS.md

## Standard

This book follows the [QuadriviumPress MyST baseline](https://github.com/QuadriviumPress/bindery/blob/main/doc/myst-baseline.md) and the [presentation skill](https://github.com/QuadriviumPress/bindery/blob/main/skills/quadrivium-myst-presentation/SKILL.md).

## Commands

```bash
npm run start
npm run build
npm run verify
npm run check
```

`npm run check` is the production-equivalent verification and HTML build.

## Intentional differences

- `verify` runs `python3 scripts/verify_book.py`, copied from bindery's `scripts/myst-verify-base.py`.

## Presentation gap

Problems are `{exercise}` directives with a manual `:enumerator:` under `## Problems`. They do not use `{solution}` dropdowns. Adding hidden solutions is deferred so the converted problem numbers stay as published.
