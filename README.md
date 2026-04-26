# PADI Ontology Kernel
## The Governance-as-Code Infrastructure

The **PADI Ontology Kernel** is the primary execution engine for the PADI Technical Standard. It provides the deterministic logic, semantic validation, and agent-orchestration runtime required to maintain a **Sovereign Bureau**. 

By utilizing **OWL 2** for ontology modeling and **SHACL** for structural constraints, this kernel ensures that all information state-changes are mathematically valid and programmatically auditable.

---

## 🏛️ Core Components & Directory Map

| Folder | Content | Role |
| :--- | :--- | :--- |
| /ontology/ | .ttl, .jsonld | **The Genome:** Defines core classes, properties, and axioms. |
| /constraints/| .shacl, .rules.json | **The Law:** Structural and logical validation rules. |
| /runtime/ | .py execution logic | **The Engine:** Handles mutations, ledgering, and compliance. |
| /epistemics/ | epistemic-engine.py | **The Truth-Seeker:** Validates Justified True Belief. |
| /agents/ | specs/ | **The Orchestrator:** Defines A2A/A2UI orchestration. |
| /data/ | graph.ttl | **The State:** The local knowledge graph instance. |

---

## 🛠️ Technical Architecture

### 1. Deterministic Knowledge Graphs
The PADI Kernel operates on a **Deterministic Truth Model**. Every node added to the graph is validated against the `ontology/padi.ttl` definitions.

### 2. SHACL Validation Pipeline
The kernel enforces integrity through a Python-based pipeline that executes SHACL validation before any commit.

**Core Validation Command:**
`python runtime/graph_validator.py --data data/graph.ttl --shapes constraints/shapes.shacl`

### 3. Agentic Orchestration
This repository houses the logic for **A2A (Agent-to-Agent)** communication, allowing autonomous systems to interact within the framework while maintaining a sovereign audit trail.

---

## 🚀 Getting Started

### Environment Setup
1. **Clone the Repo:** `git clone https://github.com/peculiarlibrary/padi-ontology-kernel.git`
2. **Initialize Environment:**
   - `python -m venv .venv`
   - `source .venv/Scripts/activate` (Windows MINGW64)
   - `pip install -r requirements.lock`
3. **Run Initial Bootstrap:** `./bootstrap.sh`

## 🔗 The Three Pillars
- **Narrative (Policy):** [PADI Standard Documentation](https://github.com/peculiarlibrary/padi-standard-documentation)
- **Interface (Visual):** [PADI Web Visualizer](https://github.com/peculiarlibrary/padi-web-visualizer)

## ⚖️ License
Licensed under the **Apache License 2.0**.

---
**Founding Architect:** S. M. Gitandu, B.S. (Information Science)  
**Bureau Perspective:** The Peculiar Librarian
