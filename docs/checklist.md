# AIM2 Detailed Tiny-Task Checklists (TDD-first)
_Each ticket begins with tests and ends by re-running tests. IDs are TicketID-TaskNN._

## DOC-001 — Checklist format utility
- [x] DOC-001-01: Replace regex usage in `docs/fix_checklist_format.py` with custom pattern matching.
- [x] DOC-001-02: Add unit tests for `fix_checkbox_format`.

## INF-001 — Repo skeleton & packaging
- [x] INF-001-01: Author unit test plan for **Repo skeleton & packaging** (acceptance criteria → concrete tests).
- [x] INF-001-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [x] INF-001-03: Create module/package scaffolding and minimal code stubs to satisfy imports (tests still fail).
- [x] INF-001-04: Implement functionality (packaging, make/nox tasks, or settings) to satisfy tests.
- [x] INF-001-05: Add type hints, docstrings, and README snippets with examples.
- [x] INF-001-06: Run linter/formatter; fix issues and enforce pre-commit hooks.
- [x] INF-001-07: Run unit tests locally; raise coverage to ≥70%.
- [x] INF-001-08: Update CHANGELOG with entry for initial infrastructure feature.
- [x] INF-001-09: Re-run full test suite; ensure all INF tests pass.

## INF-002 — Task runner & reproducible env
- [x] INF-002-01: Author unit test plan for **Task runner & reproducible env** (acceptance criteria → concrete tests).
- [x] INF-002-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [x] INF-002-03: Create module/package scaffolding and minimal code stubs to satisfy imports (tests still fail).
- [x] INF-002-04: Implement functionality (packaging, make/nox tasks, or settings) to satisfy tests.
- [x] INF-002-05: Add type hints, docstrings, and README snippets with examples.
- [x] INF-002-06: Run linter/formatter; fix issues and enforce pre-commit hooks.
- [x] INF-002-07: Run unit tests locally; raise coverage to ≥70%.
- [x] INF-002-08: Update CHANGELOG with entry for initial infrastructure feature.
- [x] INF-002-09: Re-run full test suite; ensure all INF tests pass.

## INF-003 — Configuration system
- [x] INF-003-01: Author unit test plan for **Configuration system** (acceptance criteria → concrete tests).
- [x] INF-003-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [x] INF-003-03: Create module/package scaffolding and minimal code stubs to satisfy imports (tests still fail).
- [x] INF-003-04: Implement functionality (packaging, make/nox tasks, or settings) to satisfy tests.
- [x] INF-003-05: Add type hints, docstrings, and README snippets with examples.
- [x] INF-003-06: Run linter/formatter; fix issues and enforce pre-commit hooks.
- [x] INF-003-07: Run unit tests locally; raise coverage to ≥70%.
- [x] INF-003-08: Update CHANGELOG with entry for initial infrastructure feature.
- [x] INF-003-09: Re-run full test suite; ensure all INF tests pass.

## INF-004 — Lint/format hooks
- [x] INF-004-01: Author unit test plan for **Lint/format hooks** (acceptance criteria → concrete tests).
- [x] INF-004-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [x] INF-004-03: Create module/package scaffolding and minimal code stubs to satisfy imports (tests still fail).
- [x] INF-004-04: Implement functionality (packaging, make/nox tasks, or settings) to satisfy tests.
- [x] INF-004-05: Add type hints, docstrings, and README snippets with examples.
- [x] INF-004-06: Run linter/formatter; fix issues and enforce pre-commit hooks.
- [x] INF-004-07: Run unit tests locally; raise coverage to ≥70%.
- [x] INF-004-08: Update CHANGELOG with entry for initial infrastructure feature.
- [x] INF-004-09: Re-run full test suite; ensure all INF tests pass.

## ON-010 — Three-facet schema (Structural / Source / Functional)
- [ ] ON-010-01: Author unit test plan for **Three-facet schema (Structural / Source / Functional)** (acceptance criteria → concrete tests).
- [ ] ON-010-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-010-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-010-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-010-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-010-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-010-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-010-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-010-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-010-10: Re-run all tests; confirm ON-* modules are green.

## ON-011 — External ontology loaders
- [ ] ON-011-01: Author unit test plan for **External ontology loaders** (acceptance criteria → concrete tests).
- [ ] ON-011-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-011-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-011-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-011-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-011-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-011-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-011-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-011-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-011-10: Re-run all tests; confirm ON-* modules are green.

## ON-012 — Term normalization & dedup
- [ ] ON-012-01: Author unit test plan for **Term normalization & dedup** (acceptance criteria → concrete tests).
- [ ] ON-012-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-012-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-012-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-012-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-012-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-012-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-012-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-012-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-012-10: Re-run all tests; confirm ON-* modules are green.

## ON-013 — Automated trimming policy to targets
- [ ] ON-013-01: Author unit test plan for **Automated trimming policy to targets** (acceptance criteria → concrete tests).
- [ ] ON-013-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-013-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-013-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-013-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-013-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-013-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-013-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-013-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-013-10: Re-run all tests; confirm ON-* modules are green.

## ON-014 — Relation set & global constraints
- [ ] ON-014-01: Author unit test plan for **Relation set & global constraints** (acceptance criteria → concrete tests).
- [ ] ON-014-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-014-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-014-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-014-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-014-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-014-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-014-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-014-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-014-10: Re-run all tests; confirm ON-* modules are green.

## ON-015 — Ontology builder & validator
- [ ] ON-015-01: Author unit test plan for **Ontology builder & validator** (acceptance criteria → concrete tests).
- [ ] ON-015-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-015-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-015-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-015-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-015-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-015-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-015-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-015-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-015-10: Re-run all tests; confirm ON-* modules are green.

## ON-016 — Exporters (OWL / CSV / JSONL)
- [ ] ON-016-01: Author unit test plan for **Exporters (OWL / CSV / JSONL)** (acceptance criteria → concrete tests).
- [ ] ON-016-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-016-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-016-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-016-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-016-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-016-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-016-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-016-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-016-10: Re-run all tests; confirm ON-* modules are green.

## ON-017 — Provenance model inside ontology
- [ ] ON-017-01: Author unit test plan for **Provenance model inside ontology** (acceptance criteria → concrete tests).
- [ ] ON-017-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-017-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-017-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-017-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-017-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-017-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-017-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-017-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-017-10: Re-run all tests; confirm ON-* modules are green.

## ON-018 — Glossary auto‑adjudication (no‑HITL)
- [ ] ON-018-01: Author unit test plan for **Glossary auto‑adjudication (no‑HITL)** (acceptance criteria → concrete tests).
- [ ] ON-018-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-018-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-018-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-018-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-018-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-018-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-018-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-018-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-018-10: Re-run all tests; confirm ON-* modules are green.

## ON-019 — Borderline triage automation
- [ ] ON-019-01: Author unit test plan for **Borderline triage automation** (acceptance criteria → concrete tests).
- [ ] ON-019-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] ON-019-03: Implement core logic (schema/load/normalize/trim/relations/build/export/provenance as applicable).
- [ ] ON-019-04: Add validators (schema/SHACL/OWL) and constraint checks; surface actionable errors.
- [ ] ON-019-05: Add CLI command for the module (if applicable) with example config and sample fixture data.
- [ ] ON-019-06: Document YAML/JSON schemas and provide minimal fixtures under `tests/fixtures/ontology`.
- [ ] ON-019-07: Measure runtime on small fixture; optimize hotspots if >2× budget.
- [ ] ON-019-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] ON-019-09: Add an ontology-specific integration test (build→validate→export roundtrip on tiny fixture).
- [ ] ON-019-10: Re-run all tests; confirm ON-* modules are green.

## IE-020 — Corpus builder (PubMed/PMC OA)
- [ ] IE-020-01: Author unit test plan for **Corpus builder (PubMed/PMC OA)** (acceptance criteria → concrete tests).
- [ ] IE-020-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-020-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-020-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-020-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-020-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-020-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-020-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-020-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-020-10: Re-run all tests; confirm IE-* modules are green.

## IE-021 — Document parser (PDF/XML/HTML)
- [ ] IE-021-01: Author unit test plan for **Document parser (PDF/XML/HTML)** (acceptance criteria → concrete tests).
- [ ] IE-021-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-021-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-021-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-021-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-021-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-021-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-021-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-021-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-021-10: Re-run all tests; confirm IE-* modules are green.

## IE-022 — Preprocessing & normalization
- [ ] IE-022-01: Author unit test plan for **Preprocessing & normalization** (acceptance criteria → concrete tests).
- [ ] IE-022-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-022-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-022-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-022-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-022-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-022-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-022-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-022-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-022-10: Re-run all tests; confirm IE-* modules are green.

## IE-023 — NER framework (pluggable)
- [ ] IE-023-01: Author unit test plan for **NER framework (pluggable)** (acceptance criteria → concrete tests).
- [ ] IE-023-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-023-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-023-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-023-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-023-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-023-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-023-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-023-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-023-10: Re-run all tests; confirm IE-* modules are green.

## IE-024 — Relation extraction (RE)
- [ ] IE-024-01: Author unit test plan for **Relation extraction (RE)** (acceptance criteria → concrete tests).
- [ ] IE-024-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-024-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-024-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-024-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-024-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-024-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-024-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-024-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-024-10: Re-run all tests; confirm IE-* modules are green.

## IE-025 — Entity normalization & linking
- [ ] IE-025-01: Author unit test plan for **Entity normalization & linking** (acceptance criteria → concrete tests).
- [ ] IE-025-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-025-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-025-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-025-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-025-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-025-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-025-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-025-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-025-10: Re-run all tests; confirm IE-* modules are green.

## IE-026 — Fact assembler + provenance JSON
- [ ] IE-026-01: Author unit test plan for **Fact assembler + provenance JSON** (acceptance criteria → concrete tests).
- [ ] IE-026-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-026-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-026-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-026-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-026-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-026-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-026-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-026-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-026-10: Re-run all tests; confirm IE-* modules are green.

## IE-027 — Pipeline orchestrator
- [ ] IE-027-01: Author unit test plan for **Pipeline orchestrator** (acceptance criteria → concrete tests).
- [ ] IE-027-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] IE-027-03: Implement core logic (corpus/parse/preprocess/NER/RE/linking/assemble/orchestrate as applicable).
- [ ] IE-027-04: Wire feature flags & configs; ensure deterministic behavior with fixed seeds.
- [ ] IE-027-05: Add CLI subcommand for the stage and a tiny 3-paper fixture pipeline to exercise it.
- [ ] IE-027-06: Generate/update synthetic fixtures needed for this stage under `tests/fixtures/ie`.
- [ ] IE-027-07: Profile on small input; cache or batch to meet runtime/memory budget.
- [ ] IE-027-08: Run unit tests; ensure coverage ≥80% for this module.
- [ ] IE-027-09: Add stage-level integration test invoked by the orchestrator or a dedicated script.
- [ ] IE-027-10: Re-run all tests; confirm IE-* modules are green.

## DS-030 — Synthetic data generator (entities/relations)
- [ ] DS-030-01: Author unit test plan for **Synthetic data generator (entities/relations)** (acceptance criteria → concrete tests).
- [ ] DS-030-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] DS-030-03: Implement generators/labelers with controls for noise, balance, and reproducibility.
- [ ] DS-030-04: Add quality filters (entailment/model agreement) and provenance fields in outputs.
- [ ] DS-030-05: Provide CLI to produce datasets; emit dataset cards (JSON metadata) with stats.
- [ ] DS-030-06: Store datasets under versioned path and register hashes for reproducibility.
- [ ] DS-030-07: Run unit tests; ensure coverage ≥80% for DS modules.
- [ ] DS-030-08: Add dataset validation test (schema + spot-check invariants).
- [ ] DS-030-09: Re-run all tests; confirm DS-* modules are green.

## DS-031 — Distant supervision labeler
- [ ] DS-031-01: Author unit test plan for **Distant supervision labeler** (acceptance criteria → concrete tests).
- [ ] DS-031-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] DS-031-03: Implement generators/labelers with controls for noise, balance, and reproducibility.
- [ ] DS-031-04: Add quality filters (entailment/model agreement) and provenance fields in outputs.
- [ ] DS-031-05: Provide CLI to produce datasets; emit dataset cards (JSON metadata) with stats.
- [ ] DS-031-06: Store datasets under versioned path and register hashes for reproducibility.
- [ ] DS-031-07: Run unit tests; ensure coverage ≥80% for DS modules.
- [ ] DS-031-08: Add dataset validation test (schema + spot-check invariants).
- [ ] DS-031-09: Re-run all tests; confirm DS-* modules are green.

## DS-032 — Silver→gold auto dataset builder
- [ ] DS-032-01: Author unit test plan for **Silver→gold auto dataset builder** (acceptance criteria → concrete tests).
- [ ] DS-032-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] DS-032-03: Implement generators/labelers with controls for noise, balance, and reproducibility.
- [ ] DS-032-04: Add quality filters (entailment/model agreement) and provenance fields in outputs.
- [ ] DS-032-05: Provide CLI to produce datasets; emit dataset cards (JSON metadata) with stats.
- [ ] DS-032-06: Store datasets under versioned path and register hashes for reproducibility.
- [ ] DS-032-07: Run unit tests; ensure coverage ≥80% for DS modules.
- [ ] DS-032-08: Add dataset validation test (schema + spot-check invariants).
- [ ] DS-032-09: Re-run all tests; confirm DS-* modules are green.

## EV-040 — Automated evaluation framework
- [ ] EV-040-01: Author unit test plan for **Automated evaluation framework** (acceptance criteria → concrete tests).
- [ ] EV-040-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] EV-040-03: Implement metric calculators (precision/recall/F1, calibration) and error bucket analysis.
- [ ] EV-040-04: Render evaluation report (JSON + HTML) and save artifacts with run IDs.
- [ ] EV-040-05: Document how to add new metrics and thresholds; provide example configs.
- [ ] EV-040-06: Run unit tests; coverage ≥80% for EV modules.
- [ ] EV-040-07: Add a smoke integration test that evaluates a tiny synthetic run and checks key numbers.
- [ ] EV-040-08: Re-run all tests; confirm EV-* modules are green.

## CI-041 — Unit-test harness (TDD)
- [ ] CI-041-01: Author unit test plan for **Unit-test harness (TDD)** (acceptance criteria → concrete tests).
- [ ] CI-041-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] CI-041-03: Implement CI job(s) for lint, unit, and integration stages (matrix if needed).
- [ ] CI-041-04: Cache dependencies; set up artifact uploads (exports, facts, reports).
- [ ] CI-041-05: Set fail-fast thresholds (coverage, quality gates) and required checks on main branch.
- [ ] CI-041-06: Document CI commands in README and make targets for local parity.
- [ ] CI-041-07: Run unit tests; ensure CI-only helpers are covered where feasible.
- [ ] CI-041-08: Trigger a full CI run on a test branch and verify gates operate as designed.
- [ ] CI-041-09: Re-run all tests locally to confirm parity with CI outcomes.

## CI-042 — Ontology integration test
- [ ] CI-042-01: Author unit test plan for **Ontology integration test** (acceptance criteria → concrete tests).
- [ ] CI-042-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] CI-042-03: Implement CI job(s) for lint, unit, and integration stages (matrix if needed).
- [ ] CI-042-04: Cache dependencies; set up artifact uploads (exports, facts, reports).
- [ ] CI-042-05: Set fail-fast thresholds (coverage, quality gates) and required checks on main branch.
- [ ] CI-042-06: Document CI commands in README and make targets for local parity.
- [ ] CI-042-07: Run unit tests; ensure CI-only helpers are covered where feasible.
- [ ] CI-042-08: Trigger a full CI run on a test branch and verify gates operate as designed.
- [ ] CI-042-09: Re-run all tests locally to confirm parity with CI outcomes.

## CI-043 — IE integration test
- [ ] CI-043-01: Author unit test plan for **IE integration test** (acceptance criteria → concrete tests).
- [ ] CI-043-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] CI-043-03: Implement CI job(s) for lint, unit, and integration stages (matrix if needed).
- [ ] CI-043-04: Cache dependencies; set up artifact uploads (exports, facts, reports).
- [ ] CI-043-05: Set fail-fast thresholds (coverage, quality gates) and required checks on main branch.
- [ ] CI-043-06: Document CI commands in README and make targets for local parity.
- [ ] CI-043-07: Run unit tests; ensure CI-only helpers are covered where feasible.
- [ ] CI-043-08: Trigger a full CI run on a test branch and verify gates operate as designed.
- [ ] CI-043-09: Re-run all tests locally to confirm parity with CI outcomes.

## CI-044 — CI workflow
- [ ] CI-044-01: Author unit test plan for **CI workflow** (acceptance criteria → concrete tests).
- [ ] CI-044-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] CI-044-03: Implement CI job(s) for lint, unit, and integration stages (matrix if needed).
- [ ] CI-044-04: Cache dependencies; set up artifact uploads (exports, facts, reports).
- [ ] CI-044-05: Set fail-fast thresholds (coverage, quality gates) and required checks on main branch.
- [ ] CI-044-06: Document CI commands in README and make targets for local parity.
- [ ] CI-044-07: Run unit tests; ensure CI-only helpers are covered where feasible.
- [ ] CI-044-08: Trigger a full CI run on a test branch and verify gates operate as designed.
- [ ] CI-044-09: Re-run all tests locally to confirm parity with CI outcomes.

## CI-045 — Synthetic regression suite
- [ ] CI-045-01: Author unit test plan for **Synthetic regression suite** (acceptance criteria → concrete tests).
- [ ] CI-045-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] CI-045-03: Implement CI job(s) for lint, unit, and integration stages (matrix if needed).
- [ ] CI-045-04: Cache dependencies; set up artifact uploads (exports, facts, reports).
- [ ] CI-045-05: Set fail-fast thresholds (coverage, quality gates) and required checks on main branch.
- [ ] CI-045-06: Document CI commands in README and make targets for local parity.
- [ ] CI-045-07: Run unit tests; ensure CI-only helpers are covered where feasible.
- [ ] CI-045-08: Trigger a full CI run on a test branch and verify gates operate as designed.
- [ ] CI-045-09: Re-run all tests locally to confirm parity with CI outcomes.

## REL-050 — Dual CLIs (ontology & IE)
- [ ] REL-050-01: Author unit test plan for **Dual CLIs (ontology & IE)** (acceptance criteria → concrete tests).
- [ ] REL-050-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] REL-050-03: Implement CLI entry points and help text; add `--example-config` and `--version`.
- [ ] REL-050-04: Bundle example configs and tiny fixtures; ensure portable execution on fresh env.
- [ ] REL-050-05: Implement reproducibility knobs (seed manager/env capture) or bundle logic as applicable.
- [ ] REL-050-06: Write usage docs and quickstart; link to module docs and acceptance criteria.
- [ ] REL-050-07: Run unit tests for CLI and packaging; ensure commands exit non-zero on failure.
- [ ] REL-050-08: Build release artifact; validate checksums and schema of included files.
- [ ] REL-050-09: Re-run full test suite; tag release candidate in CHANGELOG.
- [ ] REL-050-10: Re-run full unit test suite; confirm all tests for REL-050 pass.

## REL-051 — Auto-docs
- [ ] REL-051-01: Author unit test plan for **Auto-docs** (acceptance criteria → concrete tests).
- [ ] REL-051-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] REL-051-03: Implement CLI entry points and help text; add `--example-config` and `--version`.
- [ ] REL-051-04: Bundle example configs and tiny fixtures; ensure portable execution on fresh env.
- [ ] REL-051-05: Implement reproducibility knobs (seed manager/env capture) or bundle logic as applicable.
- [ ] REL-051-06: Write usage docs and quickstart; link to module docs and acceptance criteria.
- [ ] REL-051-07: Run unit tests for CLI and packaging; ensure commands exit non-zero on failure.
- [ ] REL-051-08: Build release artifact; validate checksums and schema of included files.
- [ ] REL-051-09: Re-run full test suite; tag release candidate in CHANGELOG.
- [ ] REL-051-10: Re-run full unit test suite; confirm all tests for REL-051 pass.

## REL-052 — Reproducibility knobs
- [ ] REL-052-01: Author unit test plan for **Reproducibility knobs** (acceptance criteria → concrete tests).
- [ ] REL-052-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] REL-052-03: Implement CLI entry points and help text; add `--example-config` and `--version`.
- [ ] REL-052-04: Bundle example configs and tiny fixtures; ensure portable execution on fresh env.
- [ ] REL-052-05: Implement reproducibility knobs (seed manager/env capture) or bundle logic as applicable.
- [ ] REL-052-06: Write usage docs and quickstart; link to module docs and acceptance criteria.
- [ ] REL-052-07: Run unit tests for CLI and packaging; ensure commands exit non-zero on failure.
- [ ] REL-052-08: Build release artifact; validate checksums and schema of included files.
- [ ] REL-052-09: Re-run full test suite; tag release candidate in CHANGELOG.
- [ ] REL-052-10: Re-run full unit test suite; confirm all tests for REL-052 pass.

## REL-053 — Release bundle
- [ ] REL-053-01: Author unit test plan for **Release bundle** (acceptance criteria → concrete tests).
- [ ] REL-053-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] REL-053-03: Implement CLI entry points and help text; add `--example-config` and `--version`.
- [ ] REL-053-04: Bundle example configs and tiny fixtures; ensure portable execution on fresh env.
- [ ] REL-053-05: Implement reproducibility knobs (seed manager/env capture) or bundle logic as applicable.
- [ ] REL-053-06: Write usage docs and quickstart; link to module docs and acceptance criteria.
- [ ] REL-053-07: Run unit tests for CLI and packaging; ensure commands exit non-zero on failure.
- [ ] REL-053-08: Build release artifact; validate checksums and schema of included files.
- [ ] REL-053-09: Re-run full test suite; tag release candidate in CHANGELOG.
- [ ] REL-053-10: Re-run full unit test suite; confirm all tests for REL-053 pass.

## REL-054 — (Optional) LLM benchmarking report
- [ ] REL-054-01: Author unit test plan for **(Optional) LLM benchmarking report** (acceptance criteria → concrete tests).
- [ ] REL-054-02: Write failing unit tests covering happy path, edge cases, and error handling.
- [ ] REL-054-03: Implement CLI entry points and help text; add `--example-config` and `--version`.
- [ ] REL-054-04: Bundle example configs and tiny fixtures; ensure portable execution on fresh env.
- [ ] REL-054-05: Implement reproducibility knobs (seed manager/env capture) or bundle logic as applicable.
- [ ] REL-054-06: Write usage docs and quickstart; link to module docs and acceptance criteria.
- [ ] REL-054-07: Run unit tests for CLI and packaging; ensure commands exit non-zero on failure.
- [ ] REL-054-08: Build release artifact; validate checksums and schema of included files.
- [ ] REL-054-09: Re-run full test suite; tag release candidate in CHANGELOG.
- [ ] REL-054-10: Re-run full unit test suite; confirm all tests for REL-054 pass.
