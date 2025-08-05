# INF-002 Test Plan: Task runner & reproducible env

## Objectives
- Ensure a task runner executes lint and tests.
- Guarantee deterministic runs via a global seed helper.

## Planned Tests
1. Running 'make test' executes pytest.
2. 'set_seed' function produces repeatable random numbers.
3. Seed helper resets state for random and numpy.

## Out of Scope
- Multi-stage CI pipelines.
- Cross-platform variations in shell tools.
