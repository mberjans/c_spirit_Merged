# AIM2 Software Development Plan — Ontology Development & Information Extraction (No-HITL)

**Scope:** Build a fully-automated, test-driven system for (A) ontology development and (B) literature information extraction (IE).  
**Out of scope:** UI, web apps, Docker, APIs beyond local CLIs.  
**Principles:** Modular Python packages, reproducible runs, deterministic seeds, provenance-first, and TDD (tests first, tests last).  
**Alignment:** This plan is consistent with the merged backlog (`INF`, `ON`, `IE`, `DS`, `EV`, `CI`, `REL` tickets) and the detailed tiny-task checklist.

---

## 1) Objectives & Success Criteria

### 1.1 Objectives
- Produce trimmed, validated ontologies with **three facets** (Structural / Source / Functional) and exports (OWL/CSV/JSONL). *(ON-010..ON-017)*  
- Extract entities and relations from a small open-access corpus, normalize them to ontology IDs, and emit **provenance-rich facts JSONL**. *(IE-020..IE-027)*  
- Generate synthetic and distant-supervision datasets to enable **no-HITL** evaluation and continuous regression testing. *(DS-030..DS-032)*  
- Provide **automated evaluation** (P/R/F1, calibration) and **CI quality gates**. *(EV-040, CI-041..CI-045)*  
- Deliver **reproducible CLIs** and a portable release bundle. *(REL-050..REL-053)*

### 1.2 Acceptance Criteria (high-level)
- Ontology exports build successfully with **zero SHACL/OWL errors** and meet trim targets (PO=293, PECO=127, TO=188). *(ON-013..ON-016)*  
- IE pipeline runs end-to-end on the MVP corpus (≥25 OA papers) and **links ≥90% of recognized mentions** to ontology IDs on synthetic benchmarks; facts JSONL includes **evidence and provenance** fields. *(IE-020..IE-027)*  
- Evaluation report generated in one command; **failing thresholds** block release in CI. *(EV-040, CI-044)*  
- Release bundle is deterministic under a fixed seed, with **hashes and config snapshots**. *(REL-052..REL-053)*

---

## 2) Architecture & Repositories

### 2.1 Code Layout
```
aim2/
  src/aim2/
    infra/          # INF-*
    ontology/       # ON-*
    ie/             # IE-*
    data_synth/     # DS-*
    eval/           # EV-*
    cli/            # REL-050
    common/         # shared utils (logging, seeds, schema validation)
  tests/
    unit/
    integration/
    fixtures/
      ontology/     # tiny fixtures for roundtrip tests
      ie/           # 3-paper MVP fixtures; synthetic datasets
  pyproject.toml
  Makefile / noxfile.py
  README.md
  CHANGELOG.md
```

### 2.2 Packaging & Environment
- **INF-001..INF-004** establish the mono-repo, typed settings (pydantic), task runner (make/nox), and lint/format hooks (ruff/black/isort + pre-commit).  
- **Determinism:** A global seed manager ensures repeatability across ON/IE/DS/EV. *(REL-052)*  
- **Configuration:** YAML configs define pipeline stages and file paths; schema-validated at startup. *(INF-003, IE-027)*

---

## 3) Ontology Development (ON-010..ON-019)

### 3.1 Facet Schema & Loaders
- **ON-010 Three-facet schema:** YAML schema captures classes/slots/constraints; auto-generates dataclasses.  
- **ON-011 External loaders:** Import ChemOnt, NPClassifier, PMN/PlantCyc, PO, PECO, TO, GO into normalized graphs with term IDs and xrefs.  
- **ON-012 Normalization & dedup:** Unicode/whitespace normalization, synonym expansion, duplicate grouping; emit clusters and representative IDs.

### 3.2 Trimming, Constraints, and Build
- **ON-013 Trimming policy:** Learn keep/drop to hit specific targets (PO=293, PECO=127, TO=188). Signals: information content, depth, usage frequency (corpus), ambiguity, graph centrality. Deterministic seeds.  
- **ON-014 Relations & constraints:** Define allowed relations (domain/range) and global constraints (no cycles, no dangling xrefs).  
- **ON-015 Builder/validator:** rdflib/OWL build; SHACL/OWL reasoning; cycle and dangling detection.  
- **ON-016 Exporters:** Reproducible OWL/CSV/JSONL exports with stable ordering and schema validation.

### 3.3 Provenance & Full Automation
- **ON-017 Provenance model:** Reify statements with evidence codes, source URIs, timestamps; validators enforce presence.  
- **ON-018 Glossary auto‑adjudication:** Multi‑agent LLM consensus + NLI checks + ontology constraint validation (no human approval).  
- **ON-019 Borderline triage automation:** Self-consistency loop resolves low‑confidence terms while maintaining trim targets; audit logs record rationale.

**Outputs:** `ontology.owl`, `ontology.csv`, `ontology.jsonl`, `glossary.json`, audit logs, validator reports.

---

## 4) Information Extraction (IE-020..IE-027)

### 4.1 Corpus & Parsing
- **IE-020 Corpus builder:** OA-focused acquisition (≥25 papers) with query expansion, dedup, and metadata JSONL.  
- **IE-021 Parser:** Extract text from PDF/XML/HTML; section headers/captions; strip references; ≥95% coverage on sample.

### 4.2 Preprocess, NER, RE
- **IE-022 Preprocessing:** Sentence split, tokenization, acronym resolver; deterministic transforms.  
- **IE-023 NER framework:** Pluggable design: transformer model + LLM-span fallback; label set aligned to ontology.  
- **IE-024 Relation extraction:** Pairwise/sentence-level RE with negative sampling; document-level aggregator optional.

### 4.3 Linking, Facts, Orchestration
- **IE-025 Entity normalization & linking:** Lexical + embedding + graph priors to map mentions to ontology IDs; return ranked candidates with scores.  
- **IE-026 Fact assembler + provenance:** Per-doc JSONL with entities, relations, normalized IDs, spans, scores, and provenance (document ID, section, offsets, confidence, evidence).  
- **IE-027 Orchestrator:** YAML-defined pipeline; resumable runs; metrics logging and seed control.

**Outputs:** `facts.jsonl`, run metadata (config snapshots, seeds), logs, and metrics.

---

## 5) Synthetic & Distant Supervision Data (DS-030..DS-032)

- **DS-030 Synthetic generator:** Templates + LLM generation; inject noise (typos, coref, hedging); NLI-based filtering; seeded outputs.  
- **DS-031 Distant supervision labeler:** Use PO/TO/GO/PlantCyc xrefs for high‑precision labeling with pattern lexicons; entailment filter; provenance retained.  
- **DS-032 Silver→gold auto builder:** Intersect predictions (pattern+LLM), filter with NLI; create train/dev/test splits; prevent leakage.

**Outputs:** `datasets/synthetic/*.jsonl`, `datasets/silver/*.jsonl`, `datasets/gold/*.jsonl` with dataset cards (stats, hashes, provenance).

---

## 6) Evaluation & Quality Gates (EV-040, CI-041..CI-045)

- **EV-040 Evaluation framework:** Compute P/R/F1 (NER/RE), ROC/PR curves, calibration, and error buckets; produce JSON + HTML reports.  
- **CI-041 Unit-test harness:** Pytest fixtures for ON/IE; coverage targets (≥80% for modules, ≥70% repo-wide initially).  
- **CI-042 Ontology integration test:** Build→validate→export roundtrip on tiny fixture; artifacts uploaded.  
- **CI-043 IE integration test:** 3‑paper end‑to‑end fixture; snapshot facts within tolerance.  
- **CI-044 CI workflow:** Lint → unit → integration → artifacts; thresholds enforced on PRs.  
- **CI-045 Synthetic regression suite:** Lock seeds and compare run‑to‑run metrics to catch drift.

**Gates:** Failing thresholds (e.g., drop >2% macro‑F1, coverage below floor) block merges/releases.

---

## 7) CLIs, Docs, and Release (REL-050..REL-054)

- **REL-050 Dual CLIs:**  
  - `aim2-ontology`: `load` → `trim` → `build` → `export` (+ `--example-config`).  
  - `aim2-ie`: `corpus` → `parse` → `preprocess` → `ner` → `re` → `link` → `facts` → `eval`.
- **REL-051 Auto-docs:** Build docs from docstrings/schemas/checklists; include quickstarts and data model diagrams.  
- **REL-052 Reproducibility:** Global `--seed`, config snapshot saved with outputs, env capture (package versions).  
- **REL-053 Release bundle:** Tarball with ontology exports, facts JSONL, evaluation report, config snapshots, checksums.  
- **REL-054 (Optional) LLM benchmark report:** Compare 2–3 LLMs across F1/speed/cost; include plots and recommendations.

---

## 8) Development Process (TDD-first)

1. **Plan ticket → write tests → implement → refactor → document → re-run tests.**  
2. **Fixtures first:** Create tiny ontology and 3‑paper IE fixtures early; extend as modules land.  
3. **Branching:** `main` protected; feature branches require green CI and code review.  
4. **Coding standards:** Type hints everywhere, pydantic models for configs, granular modules, small functions.  
5. **Observability:** Structured logging with run IDs; metrics persisted per stage.  
6. **Performance budgets:** Each stage must complete on fixtures in seconds; MVP corpus in ≤30 minutes on a developer laptop.

---

## 9) Risk Register & Mitigations

- **R1 Ambiguity in trimming decisions** → Multi‑signal policy + self‑consistency (ON‑013/ON‑019) and audit logs.  
- **R2 Entity linking errors** → Ranked candidates + thresholds; synthetic hard negatives in DS‑030.  
- **R3 Parser variability across PDF/XML** → Section heuristics + regression fixtures; document coverage metrics.  
- **R4 Drift across model/library updates** → CI‑045 synthetic regression suite + seed locking.  
- **R5 Performance issues on larger corpora** → Batching, caching, and streaming parsers; monitor with metrics.

---

## 10) Milestones & Deliverables

- **M0 Bootstrap:** INF‑001..004 green in CI; repository scaffolding in place.  
- **M1 Ontology Core:** ON‑010..016 + ON‑017 (provenance); deterministic exports.  
- **M2 IE MVP:** IE‑020..027 end‑to‑end on 25 OA papers; facts JSONL produced.  
- **M3 Data:** DS‑030..032 datasets built; stored with hashes and dataset cards.  
- **M4 Evaluation & CI:** EV‑040 & CI‑041..045 enforce quality gates; HTML report generated.  
- **M5 Release:** REL‑050..053 produce runnable CLIs and a signed release bundle.

Deliverables include artifacts (exports, datasets, reports), configuration snapshots, and checksums for reproducibility.

---

## 11) Runbook (Example Commands)

```bash
# Ontology roundtrip
aim2-ontology load --config configs/ontology.yaml
aim2-ontology trim --targets po=293 peco=127 to=188
aim2-ontology build --validate --provenance
aim2-ontology export --out dist/ontology

# IE end-to-end (MVP)
aim2-ie corpus --query "plant metabolite stress" --n 25 --out data/corpus
aim2-ie parse --in data/corpus --out data/parsed
aim2-ie preprocess --in data/parsed --out data/pre
aim2-ie ner --in data/pre --out data/ner
aim2-ie re --in data/ner --out data/re
aim2-ie link --in data/re --ontology dist/ontology/ontology.jsonl --out data/linked
aim2-ie facts --in data/linked --out dist/facts
aim2-ie eval --gold datasets/gold --pred dist/facts --report dist/reports

# Build release
make test
make package  # bundles exports, facts, reports, configs into dist/release.tar.gz
```

---

## 12) Documentation

- **Module docs:** Auto-generated from docstrings; each public function shows params, types, and examples.  
- **Schemas:** YAML/JSON schemas documented with examples; validators enforce correctness.  
- **How‑tos:** “Add a new relation”, “Add a new NER model”, “Tune trimming thresholds” tutorials.  
- **Design notes:** Rationale for no-HITL design, provenance choices, and evaluator metrics.

---

## 13) Maintenance & Extension

- Future additions (metabolomics ingestion, cross-source merge, enrichment, DB/APIs) can plug into the same pipeline and provenance model without breaking ON/IE contracts.  
- Keep dependency boundaries clean: ON exports are inputs to IE linking; IE facts are consumers for future modules.

---

**This plan is implementation-ready and aligns 1:1 with the merged tickets and TDD checklists.**  
Proceed by executing **M0 → M1 → M2**, keeping all gates green in CI.
