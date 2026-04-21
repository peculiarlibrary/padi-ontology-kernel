# 🧠 PADI Epistemic Contract (v1)

## 🏛️ 1. Purpose

This contract defines the rules governing knowledge validity, inference, and assertion within the PADI semantic graph system.

Its objective is not natural language correctness—it is **constraint-bound epistemic integrity** for multi-agent reasoning systems.

---

## 🔐 2. Core Principle

> No agent may assert knowledge that is not grounded in the validated semantic graph.

All outputs must be:
- traceable to RDF triples
- derivable via SPARQL queries
- structurally valid under SHACL constraints

---

## 🧬 3. Truth Classification Model

All knowledge in the system MUST belong to exactly one category:

### 3.1 ASSERTED
- Explicitly present in RDF graph
- Directly encoded facts
- Highest authority level

### 3.2 DERIVED
- Logically inferred from ASSERTED data
- Must have explicit derivation path
- Must remain traceable

### 3.3 INFERRED
- Produced via SPARQL reasoning or agent computation
- Must reference supporting graph query results
- Cannot be promoted to ASSERTED without validation

### 3.4 UNKNOWN
- Not present or derivable in graph
- Must NOT be asserted as fact under any condition

---

## 🚫 4. Hallucination Definition

A hallucination is defined as:

> Any assertion not directly supported by:
- RDF graph state OR
- valid SPARQL derivation OR
- SHACL-approved inference path

Hallucinations are treated as **invalid epistemic transitions**, not linguistic errors.

---

## 🧩 5. Assertion Rules

### 5.1 No Free Generation Rule
Agents may NOT generate new entities or relationships without graph insertion authority.

---

### 5.2 Query-First Rule
Before any assertion, an agent MUST:
1. Execute SPARQL query
2. Retrieve supporting triples
3. Validate against SHACL constraints
4. Only then produce output

---

### 5.3 Traceability Rule
Every assertion MUST include:
- source triple(s) OR
- SPARQL query path OR
- derivation chain

Untraceable assertions are INVALID.

---

## 🧠 6. Epistemic State Transitions

Allowed transitions:

- UNKNOWN → ASSERTED (only via validated insertion)
- ASSERTED → DERIVED (via explicit reasoning)
- DERIVED → INFERRED (via controlled reasoning layer)

Forbidden transitions:
- UNKNOWN → ASSERTED (without validation)
- INFERRED → ASSERTED (without SHACL approval)

---

## 🧩 7. Agent Epistemic Constraint

All agents operating in PADI MUST:

- treat RDF as sole truth source
- treat SHACL as structural authority
- treat SPARQL as reasoning interface
- never override epistemic classification rules

Agents are not knowledge generators.  
They are **graph-constrained reasoning operators**.

---

## 🏛️ 8. System Invariant

> The graph defines reality within the system.  
> No agent output is considered reality unless it is graph-grounded.

---

## 🔒 9. Enforcement Principle

Epistemic violations are not corrected—they are rejected at the system boundary.

Invalid assertions MUST NOT enter:
- RDF graph
- JSON-LD output
- agent communication layer

---

## 🧭 10. Final Rule

> If it is not in the graph, it does not exist in the system.
