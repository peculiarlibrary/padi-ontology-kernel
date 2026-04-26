# 🤖 PADI Agent Execution Runtime Specification (v1)

## 🏛️ 1. Purpose

This document defines how **MINGW64 terminal commands are translated into constrained multi-agent reasoning workflows** over the PADI semantic graph system.

It formalizes the execution bridge between:
- user command input
- agent orchestration
- RDF graph operations
- SHACL validation
- SPARQL reasoning
- JSON-LD output

---

## 🧠 2. Core Principle

> A command is not executed. It is interpreted as a constrained reasoning request over a validated graph state.

No command directly mutates state without passing through the full semantic pipeline.

---

## ⚙️ 3. Execution Pipeline

Every command MUST follow this deterministic sequence:

### STEP 1 — COMMAND PARSING
- Identify intent type (query, mutation, inspection, governance)
- Map to agent class (Governance / Reasoning / Ingestion / Identity)

---

### STEP 2 — AGENT DISPATCH
- Assign command to appropriate agent type
- No direct execution by shell context alone

---

### STEP 3 — SPARQL TRANSLATION
- Convert command intent into approved SPARQL query pattern
- Only patterns from `sparql-library.md` are allowed

---

### STEP 4 — GRAPH RETRIEVAL
- Execute SPARQL query against RDF graph
- Retrieve subgraph only (no full-graph exposure unless explicitly required)

---

### STEP 5 — SHACL VALIDATION
- Validate retrieved or proposed graph state
- Reject invalid structures before reasoning proceeds

---

### STEP 6 — EPISTEMIC CLASSIFICATION
- Label results as:
  - ASSERTED
  - DERIVED
  - INFERRED
- Apply `epistemics/contract.md` rules

---

### STEP 7 — CONSISTENCY CHECK
- Validate against historical graph states
- Detect semantic or temporal contradictions
- Reject or isolate inconsistent outputs

---

### STEP 8 — OUTPUT SERIALIZATION
- Convert final validated state into JSON-LD
- Attach provenance metadata
- Ensure no unvalidated fields are included

---

## 🤖 4. Command-to-Agent Mapping

### 4.1 QUERY COMMANDS
Example:
```bash
python -m query "<intent>"
Maps to:

Reasoning Agent
SPARQL library execution
4.2 VALIDATION COMMANDS

Example:
python -m validate
Maps to:

Governance Agent
SHACL enforcement layer
4.3 INGESTION COMMANDS

Example:
python -m ingest "<rdf_input>"
Maps to:

Ingestion Agent
SHACL pre-validation required
4.4 SYSTEM INSPECTION COMMANDS

Example:
python -m inspect
Maps to:

Identity Agent
Graph state introspection only (read-only)
🚫 5. Forbidden Execution Behaviors

The runtime MUST NEVER:

execute commands outside agent mapping
bypass SPARQL reasoning layer
mutate RDF graph directly from CLI input
skip SHACL validation step
emit JSON-LD without epistemic classification
🧠 6. Determinism Requirement

All command executions MUST be:

deterministic given identical graph state
reproducible via SPARQL trace
fully explainable via provenance chain
🧩 7. System Invariant

The terminal is not an execution layer. It is a semantic request interface to a constrained reasoning system.

🔒 8. Final Rule

No command has meaning outside the graph context it resolves into.
