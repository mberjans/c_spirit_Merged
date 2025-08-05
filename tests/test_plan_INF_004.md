# INF-004 Test Plan: Lint/format hooks

## Objectives
- Ensure pre-commit runs ruff, black, and isort.
- Confirm configuration integrates with pyproject settings.

## Planned Tests
1. The pre-commit config lists ruff, black, and isort hooks.
2. Running pre-commit with a sample file reformats code and reports lint errors.
3. pyproject.toml includes sections for ruff and isort.

## Out of Scope
- CI integration of pre-commit.
- Custom hook development.
