# 🧾 PADI JSON-LD Projection & Output Contract (v1)

## 🏛️ 1. Purpose

This contract defines how RDF graph state is safely projected into JSON-LD for:

- external systems
- inter-agent communication
- API responses
- cross-domain interoperability

It ensures that **no semantic distortion occurs during serialization**.

---

## 🧠 2. Core Principle

> JSON-LD is not a source of truth. It is a projection of validated RDF state.

All JSON-LD outputs MUST be:
- derived from SHACL-validated RDF
- consistent with epistemic contract classifications
- traceable to SPARQL query results

---

## 🧬 3. Projection Pipeline

All outputs MUST follow this transformation chain:

### STEP 1 — RDF Source
Validated RDF graph (post-SHACL)

↓

### STEP 2 — SPARQL Selection
Controlled query execution (from SPARQL library)

↓

### STEP 3 — Epistemic Classification
ASSERTED / DERIVED / INFERRED tagging applied

↓

### STEP 4 — JSON-LD Serialization
Graph is serialized into JSON-LD context form

↓

### STEP 5 — Output Validation
Consistency + contract compliance check before emission

---

## 🧾 4. JSON-LD Structure Rules

All outputs MUST follow:

### 4.1 Context Declaration Mandatory
Every JSON-LD document MUST define `@context`.

### 4.2 Identity Binding Required
Every entity MUST include `@id`.

### 4.3 Type Preservation
RDF `rdf:type` MUST map to `@type`.

### 4.4 No Free Attributes
No field may exist without RDF provenance.

---

## 🚫 5. Forbidden Output Behaviors

Agents MUST NOT:

- generate JSON outside RDF mapping
- introduce new fields not present in graph
- flatten or simplify semantic relationships
- remove provenance metadata
- mix external data with graph-derived output

---

## 🧠 6. Epistemic Tagging in JSON-LD

Each node MUST include:

```json
"padi:epistemicStatus": "ASSERTED | DERIVED | INFERRED"
This ensures traceable reasoning classification at the boundary layer.

🔐 7. Traceability Requirement

Every JSON-LD output MUST preserve:

source RDF triples OR
SPARQL query reference OR
derivation path metadata

If traceability is missing:

Output is INVALID and MUST NOT be emitted.

🧩 8. Agent Output Contract

Agents producing JSON-LD MUST:

Execute SPARQL query first
Validate SHACL constraints
Apply epistemic classification
Serialize ONLY graph-derived data
Attach provenance metadata
🏛️ 9. System Boundary Rule

JSON-LD is the only permitted external representation of the graph.

No agent may expose:

raw RDF mutations
unvalidated intermediate reasoning states
non-graph-derived assertions
🔒 10. Final Invariant

If it is not derivable from RDF, it cannot appear in JSON-LD.

