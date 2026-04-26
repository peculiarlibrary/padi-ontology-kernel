# PADI Ontology Kernel
## The Governance-as-Code Infrastructure

The **PADI Ontology Kernel** is the primary execution engine for the PADI Technical Standard. It provides the deterministic logic, semantic validation, and agent-orchestration runtime required to maintain a **Sovereign Bureau**. 

By utilizing **OWL 2** for ontology modeling and **SHACL** for structural constraints, this kernel ensures that all information state-changes are mathematically valid and programmatically auditable.

---

## Core Components & Directory Map

| Folder | Content | Role |
| :--- | :--- | :--- |
| `/ontology/` | `.ttl`, `.jsonld` | **The Genome:** Defines the core classes, properties, and axioms of the PADI standard. |
| `/constraints/`| `.shacl`, `.rules.json` | **The Law:** Structural and logical constraints that must be satisfied for state-settlement. |
| `/runtime/` | `.py` execution logic | **The Engine:** Handles graph mutations, ledgering, compliance, and system audits. |
| `/epistemics/` | `epistemic-engine.py` | **The Truth-Seeker:** Validates the "Justified True Belief" of information within the graph. |
| `/agents/` | `specs/` | **The Orchestrator:** Defines agent specifications for autonomous Bureau operations. |
| `/data/` | `graph.ttl` | **The State:** The actual local knowledge graph managed by this kernel instance. |

---

## Technical Architecture

### 1. Deterministic Knowledge Graphs
Unlike probabilistic models, the PADI Kernel operates on a **Deterministic Truth Model**. Every node added to the graph is validated against the `ontology/padi.ttl` definitions.

### 2. SHACL Validation Pipeline
The kernel enforces structural integrity through a Python-based pipeline that executes SHACL validation before any commit to the permanent ledger.

```bash
# Core Validation Command
python runtime/graph_validator.py --data data/graph.ttl --shapes constraints/shapes.shacl
```

### 3. Agentic Orchestration
This repository houses the logic for **A2A (Agent-to-Agent)** communication protocols, allowing autonomous systems to interact within the PADI framework while maintaining a sovereign audit trail.

---

## Getting Started

### Environment Setup
1. **Clone the Repo:** `git clone https://github.com/peculiarlibrary/padi-ontology-kernel.git`
2. **Initialize Environment:** ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # or source .venv/bin/activate on Linux
   pip install -r requirements.lock
   ```
3. **Run Initial Bootstrap:**
   ```bash
   ./bootstrap.sh
   ```

## The Three Pillars
This repository is the **Logic Layer** of a larger ecosystem:
- **Narrative (Policy):** [PADI Standard Documentation](https://github.com/peculiarlibrary/padi-standard-documentation)
- **Interface (Visual):** [PADI Web Visualizer](https://github.com/peculiarlibrary/padi-web-visualizer)

## License
Licensed under the **Apache License 2.0**. This license includes explicit patent grants for the underlying ontological structures and logic processing methodology described herein.

---
**Founding Architect:** S. M. Gitandu, B.S. (Information Science)  
**Bureau Perspective:** The Peculiar Librarian
