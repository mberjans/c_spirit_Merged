# INF-001 Test Plan: Repo skeleton & packaging

## Objectives
- Ensure repository skeleton supports installation and imports.

## Planned Tests
1. Verify `pip install -e .` installs package without errors.
2. Confirm `import aim2` succeeds after installation.
3. Check `aim2.__version__` attribute is accessible and follows semantic versioning.

## Out of Scope
- Building source distributions or wheels.
- Publishing to package indexes.
