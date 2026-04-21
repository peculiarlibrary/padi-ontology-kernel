# 🏛️ PADI Ontology Kernel Binding Contract (v1)

## 1. Purpose

This document defines the **global invariants, execution order, and authority hierarchy** of the PADI Ontology Kernel.

It binds all existing layers into a **single deterministic reasoning system**.

---

## 2. System Invariant (Non-Negotiable)

> No data may be queried, reasoned over, or emitted unless it has passed all prior validation layers.

---

## 3. Canonical Execution Pipeline (Mandatory Order)

All operations MUST follow this exact sequence:

1. RDF (Ontology State)
2. SHACL (Structural Validation)
3. Epistemics (Truth Classification)
4. Governance (Consistency Enforcement)
5. SPARQL (Query Execution)
6. JSON-LD (Projection / Output)

---

## 4. Authority Hierarchy

When conflicts occur, resolution MUST follow:

| Priority | Layer |
|--------|------|
| 1 (Highest) | SHACL Constraints |
| 2 | Epistemic Contract |
| 3 | Governance Rules |
| 4 | Runtime Execution |
| 5 | Agent Intent |
| 6 (Lowest) | Query Request |

### Rule:
Higher authority ALWAYS overrides lower authority.

---

## 5. Cross-Layer Invariants

### 5.1 RDF → SHACL
- Any RDF not conforming to SHACL is INVALID.
- Invalid RDF MUST NOT propagate.

---

### 5.2 SHACL → Epistemics
- Structurally valid data MUST be epistemically classified:
  - ASSERTED
  - DERIVED
  - INFERRED
- Unclassified data is INVALID.

---

### 5.3 Epistemics → Governance
- Governance MUST reject:
  - contradictory assertions
  - temporally inconsistent states
  - conflicting derivations

---

### 5.4 Governance → SPARQL
- SPARQL may ONLY operate on:
  - SHACL-valid
  - epistemically classified
  - governance-approved graph states

---

### 5.5 SPARQL → JSON-LD
- JSON-LD output MUST:
  - be derived from SPARQL results ONLY
  - preserve RDF semantics
  - include epistemic status
  - include provenance metadata

---

## 6. Forbidden Transitions

The system MUST NEVER allow:

- RDF → SPARQL (bypassing SHACL)
- RDF → JSON-LD (bypassing validation)
- SPARQL → RDF mutation (read-only constraint)
- Agent → direct graph mutation
- JSON-LD → RDF without SHACL validation
- Epistemic classification without RDF grounding

---

## 7. Determinism Requirement

Given identical RDF state and identical query:

> The system MUST produce identical results.

All outputs must be:

- reproducible
- traceable
- explainable via SPARQL + provenance

---

## 8. Traceability Requirement

Every output MUST include at least one:

- RDF triple reference
- SPARQL query reference
- derivation chain

If traceability is missing:

> Output is INVALID.

---

## 9. Runtime Binding Rule

The runtime layer MUST enforce:

- strict pipeline ordering
- rejection of invalid intermediate states
- no bypass of SHACL or governance

---

## 10. Agent Constraint Rule

Agents:

- DO NOT create truth
- DO NOT modify RDF directly
- MUST operate through SPARQL + validated pipelines

---

## 11. Final Law

> If it is not validated, classified, and governed, it does not exist in the system.
