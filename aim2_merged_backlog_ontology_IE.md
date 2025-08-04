# AIM2 Merged Backlog — Ontology Development + Information Extraction (No-HITL)
**Scope:** Only ontology development and information extraction. No GUI, no Docker, no web apps.  
**Principles:** Modular Python packages, standalone CLIs, importable modules, fully automatable, TDD-first.  
**Legend:**  
- **ID prefixes:** `INF` (infrastructure), `ON` (ontology), `IE` (information extraction), `DS` (synthetic/distant supervision), `EV` (evaluation), `CI` (tests/CI), `REL` (packaging/release).  
- **Independent?** Yes = can be programmed & tested in isolation; No = list blocking dependencies.

---

## Milestone M0 — Bootstrap
### INF-001 • Repo skeleton & packaging
- **Description:** Create mono-repo structure (`src/aim2/...`), pyproject.toml, versioning, basic README.
- **Independent?** Yes
- **Acceptance:** `pip install -e .` works; example import succeeds.

### INF-002 • Task runner & reproducible env
- **Description:** Makefile / nox tasks (lint, test, build); pinned requirements with lockfile.
- **Independent?** No — **Depends:** INF-001
- **Acceptance:** `make test` executes unit tests locally and in CI container.

### INF-003 • Configuration system
- **Description:** Typed settings (pydantic) with `.env` support and YAML pipeline config loader.
- **Independent?** No — **Depends:** INF-001
- **Acceptance:** Loading hierarchy works; schema-validated configs.

### INF-004 • Lint/format hooks
- **Description:** Ruff + Black + isort + pre-commit.
- **Independent?** No — **Depends:** INF-001
- **Acceptance:** Hooks run on commit; CI fails on lint errors.

---

## Milestone M1 — Ontology Core
### ON-010 • Three-facet schema (Structural / Source / Functional)
- **Description:** YAML schema for classes, slots, and constraints (labels, synonyms, defs, xrefs).
- **Independent?** No — **Depends:** INF-001
- **Acceptance:** Schema validates and auto-generates dataclasses.

### ON-011 • External ontology loaders
- **Description:** Import ChemOnt, NPClassifier, PMN/PlantCyc, Plant Ontology (PO), PECO, Trait Ontology (TO), Gene Ontology (GO).
- **Independent?** No — **Depends:** ON-010
- **Acceptance:** Normalized in-memory graphs with term IDs and xrefs for each source.

### ON-012 • Term normalization & dedup
- **Description:** Lowercasing rules, Unicode normalization, dehyphenation, synonym expansion, duplicate grouping.
- **Independent?** No — **Depends:** ON-011
- **Acceptance:** ≥99% deterministic round-trip; duplicate clusters emitted with representative ID.

### ON-013 • Automated trimming policy to targets
- **Description:** Learn keep/drop policy using information content, depth, usage frequency, ambiguity, centrality to hit target sizes (PO=293, PECO=127, TO=188).
- **Independent?** No — **Depends:** ON-012
- **Acceptance:** Final counts within ±1%; no cycles; coverage on seed concepts unchanged.

### ON-014 • Relation set & global constraints
- **Description:** Define allowed relations (is_a, part_of, regulates, has_role_in, produced_by, etc.) with domain/range.
- **Independent?** No — **Depends:** ON-010
- **Acceptance:** Constraint checker flags violations on fixtures.

### ON-015 • Ontology builder & validator
- **Description:** rdflib/OWL build, SHACL/OWL reasoning, cycle detection, dangling xref detection.
- **Independent?** No — **Depends:** ON-011, ON-014
- **Acceptance:** Zero SHACL/OWL errors on sample; cycles=0; dangling xrefs=0.

### ON-016 • Exporters (OWL / CSV / JSONL)
- **Description:** Deterministic exporters with stable ordering; provenance columns where applicable.
- **Independent?** No — **Depends:** ON-015
- **Acceptance:** Byte-for-byte reproducible export given fixed seed.

### ON-017 • Provenance model inside ontology
- **Description:** Evidence codes, source URIs, timestamps on statements; reification pattern documented.
- **Independent?** No — **Depends:** ON-010, ON-015
- **Acceptance:** Sample triples include provenance; validator enforces presence.

### ON-018 • Glossary auto‑adjudication (no‑HITL)
- **Description:** Multi-agent LLM consensus + NLI entailment + constraint checks to generate/validate glossary.
- **Independent?** No — **Depends:** ON-010, ON-012
- **Acceptance:** F1≥0.95 on ambiguity/duplicate detection (synthetic); zero validator errors after ingest.

### ON-019 • Borderline triage automation
- **Description:** Self-consistency loop resolves low-confidence terms to meet trim targets; emits audit log.
- **Independent?** No — **Depends:** ON-013
- **Acceptance:** Targets met; no new constraint violations; audit shows rationale per decision.

---

## Milestone M2 — Information Extraction MVP
### IE-020 • Corpus builder (PubMed/PMC OA)
- **Description:** Query expansion, OA fetching, metadata store, dedup.
- **Independent?** Yes
- **Acceptance:** ≥25 OA papers fetched with metadata JSONL.

### IE-021 • Document parser (PDF/XML/HTML)
- **Description:** Text extraction, section headers, captions, reference stripping.
- **Independent?** No — **Depends:** IE-020
- **Acceptance:** ≥95% text coverage on sample; section tagging accuracy sanity-checked by heuristics.

### IE-022 • Preprocessing & normalization
- **Description:** Sentence split, tokenization, acronym resolver, unicode cleanup.
- **Independent?** No — **Depends:** IE-021
- **Acceptance:** Deterministic transforms; acronym mapping coverage reported.

### IE-023 • NER framework (pluggable)
- **Description:** Interfaces for transformer NER and LLM span tagger fallback; label set aligned to ontology.
- **Independent?** No — **Depends:** IE-022, ON-010
- **Acceptance:** F1≥baseline on synthetic; spans carry candidate IDs for linking.

### IE-024 • Relation extraction (RE)
- **Description:** Pairwise and sentence-level RE with negative sampling; optional doc-level aggregator.
- **Independent?** No — **Depends:** IE-023
- **Acceptance:** Macro-F1 reported on synthetic; calibration curves emitted.

### IE-025 • Entity normalization & linking
- **Description:** Canonicalize mentions to ontology IDs using lexical + embedding + graph priors.
- **Independent?** No — **Depends:** IE-023, ON-012
- **Acceptance:** ≥90% top-1 accuracy on synthetic linking set; returns ranked candidates with scores.

### IE-026 • Fact assembler + provenance JSON
- **Description:** Produce per-doc JSONL records: entities, relations, normalized IDs, spans, scores, and evidence/provenance.
- **Independent?** No — **Depends:** IE-025
- **Acceptance:** JSON schema validated; all facts carry provenance fields.

### IE-027 • Pipeline orchestrator
- **Description:** YAML-defined stages; resumable runs; metrics logging.
- **Independent?** No — **Depends:** IE-026
- **Acceptance:** End-to-end run produces facts JSONL and metrics for the 25-paper MVP.

---

## Milestone M3 — Synthetic & Distant Supervision Data
### DS-030 • Synthetic data generator (entities/relations)
- **Description:** Templates + LLM generation; noise injection; NLI-based filtering; seeded reproducibility.
- **Independent?** No — **Depends:** ON-010
- **Acceptance:** ≥10k labeled sentences with entity spans and relation labels; estimated label error ≤5%.

### DS-031 • Distant supervision labeler
- **Description:** Use PO/TO/GO/PlantCyc xrefs to auto-label co-mentions with pattern lexicons; entailment filter.
- **Independent?** No — **Depends:** ON-011, IE-021
- **Acceptance:** Silver set with precision≥0.85 on spot-check via heuristics; provenance retained.

### DS-032 • Silver→gold auto dataset builder
- **Description:** Intersect model agreements (pattern+LLM) and filter with NLI; create train/dev/test splits.
- **Independent?** No — **Depends:** DS-030, DS-031
- **Acceptance:** ≥2k “gold” examples; leakage checks pass; splits reproducible.

---

## Milestone M4 — Evaluation & CI
### EV-040 • Automated evaluation framework
- **Description:** NER/RE metrics, PR/ROC, calibration; error buckets; model cards.
- **Independent?** No — **Depends:** DS-032
- **Acceptance:** Single command evaluates a run and writes report (HTML+JSON).

### CI-041 • Unit-test harness (TDD)
- **Description:** Pytest fixtures for ontology and IE; coverage tooling.
- **Independent?** No — **Depends:** INF-001
- **Acceptance:** `pytest -q` green with starter tests; coverage≥70% (rises as modules land).

### CI-042 • Ontology integration test
- **Description:** Build+validate+export pipeline test on a tiny fixture ontology.
- **Independent?** No — **Depends:** ON-016
- **Acceptance:** Passes in CI; artifacts attached to run.

### CI-043 • IE integration test
- **Description:** End-to-end corpus→facts run on tiny 3-paper fixture.
- **Independent?** No — **Depends:** IE-027, ON-016
- **Acceptance:** Facts JSONL matches golden snapshot (within tolerance).

### CI-044 • CI workflow
- **Description:** GitHub Actions (or similar): lint, unit, integration, artifact upload.
- **Independent?** No — **Depends:** CI-041, CI-042, CI-043
- **Acceptance:** CI required checks pass; artifacts downloadable.

### CI-045 • Synthetic regression suite
- **Description:** Lock synthetic seeds; detect drift across releases.
- **Independent?** No — **Depends:** DS-030, EV-040
- **Acceptance:** Failing thresholds block release; dashboard trend saved.

---

## Milestone M5 — Packaging & Release
### REL-050 • Dual CLIs (ontology & IE)
- **Description:** `aim2-ontology` (load→trim→build→export), `aim2-ie` (corpus→ie→facts).
- **Independent?** No — **Depends:** ON-016, IE-027
- **Acceptance:** Help text; non-zero exit codes on failure; examples in README.

### REL-051 • Auto-docs
- **Description:** pdoc/mkdocs build from code+docstrings+schemas; publish static site (optional).
- **Independent?** No — **Depends:** INF-001
- **Acceptance:** Docs build locally; cross-links resolve.

### REL-052 • Reproducibility knobs
- **Description:** Global seed manager; config snapshot; environment capture.
- **Independent?** No — **Depends:** IE-027, DS-030
- **Acceptance:** Reruns with same seed reproduce hashes and metrics within tolerance.

### REL-053 • Release bundle
- **Description:** Tarball containing OWL/CSV/JSONL exports, facts JSONL, reports, and config snapshots.
- **Independent?** No — **Depends:** REL-050, EV-040
- **Acceptance:** Bundle passes checksum and schema validations.

### REL-054 • (Optional) LLM benchmarking report
- **Description:** Compare NER/RE across 2–3 LLMs; report quality/speed/cost.
- **Independent?** No — **Depends:** IE-027, EV-040
- **Acceptance:** Table + plots in report; recommendations section.

---

## Dependency Overview (high level)
- **Ontology chain:** ON-010 → ON-011 → ON-012 → (ON-013 → ON-019) & (ON-014 → ON-015 → ON-016) & ON-017; ON-018 depends on ON-010/012.
- **IE chain:** IE-020 → IE-021 → IE-022 → IE-023 → IE-024 → IE-025 → IE-026 → IE-027.
- **Data & Eval:** DS-030/031 → DS-032 → EV-040; CI depends on both ON and IE artifacts.
- **Release:** REL depends on ON exports + IE pipeline + EV report.

---

## Notes
- All tickets are **No-HITL** by design. Where the original lists required manual steps, we replaced them with synthetic data, distant supervision, multi-agent self-consistency, and validator constraints.
- Every module ships with unit tests first (TDD). Integration tests are gated in CI before release.
