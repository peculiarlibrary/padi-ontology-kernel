# 🤖 PADI Agent Specification (v1)

## 🏛️ 1. Purpose

This document defines the operational constraints, behavioral model, and epistemic boundaries of all agents operating within the PADI semantic graph system.

Agents are not autonomous knowledge creators.  
They are **graph-constrained reasoning operators**.

---

## 🧠 2. Core Agent Principle

> An agent may only act on what exists in the validated semantic graph.

Agents MUST NOT:
- generate new entities from scratch
- assert unverified knowledge
- bypass SHACL validation
- override epistemic classifications

---

## 🧬 3. Agent Execution Model

All agents follow a strict 4-phase loop:

### 3.1 QUERY PHASE (SPARQL only)
- Agent retrieves relevant subgraph via SPARQL
- No assumptions allowed

### 3.2 VALIDATION PHASE (SHACL enforced)
- Retrieved graph state is validated structurally
- Invalid state is rejected

### 3.3 REASONING PHASE (bounded inference)
- Agent may derive conclusions ONLY from retrieved graph
- No external world assumptions permitted

### 3.4 OUTPUT PHASE (graph-grounded response)
- Output must reference:
  - RDF triples OR
  - SPARQL query results OR
  - derived graph paths

---

## 🔐 4. Knowledge Authority Rules

### 4.1 RDF is authoritative
The RDF graph is the ONLY source of truth.

### 4.2 SHACL is restrictive authority
SHACL defines what CANNOT exist.

### 4.3 Epistemic contract is semantic authority
Determines what MAY be asserted.

---

## 🚫 5. Prohibited Agent Behaviors

Agents MUST NOT:

- invent nodes or relationships
- hallucinate missing graph edges
- promote inferred data to asserted without validation
- bypass SPARQL querying phase
- modify graph without SHACL validation

---

## 🧩 6. Agent Types (v1 taxonomy)

### 6.1 Governance Agent
- validates structural compliance
- enforces SHACL rules
- blocks invalid mutations

---

### 6.2 Reasoning Agent
- executes SPARQL queries
- derives conclusions from graph state
- produces bounded inference outputs

---

### 6.3 Ingestion Agent
- inserts new RDF triples
- requires SHACL validation before commit
- cannot bypass epistemic contract

---

### 6.4 Identity Agent
- manages entity identity consistency
- ensures uniqueness of semantic nodes
- prevents duplicate conceptual entities

---

## 🧠 7. Inter-Agent Communication Rule

Agents do NOT communicate directly.

All communication occurs through:
- RDF graph state mutation
- SPARQL query visibility
- JSON-LD projection layer

This ensures:
> No hidden state. No private interpretation layers.

---

## 🧬 8. State Consistency Rule

All agents must assume:

> The graph is the only shared memory system.

Any information not present in the graph:
- does not exist for reasoning purposes
- cannot be used as valid inference input

---

## 🔒 9. Epistemic Binding

Every agent output MUST:
- reference graph state
- comply with epistemic contract classification
- remain traceable to RDF source or derivation path

Untraceable output is INVALID.

---

## 🧭 10. System Integrity Principle

> Agents do not think outside the graph.  
> They only traverse, validate, and extend it under strict constraints.
