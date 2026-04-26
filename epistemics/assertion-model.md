# PADI Assertion Model (Epistemic Foundation)

## 1. Scope
Defines the validity of knowledge claims within the PADI kernel. 

## 2. Axioms
* **URI Identification**: All assertions must be globally unique via URI.
* **Provenance**: Evidence must be linked via formal RDF provenance predicates.
* **Consistency**: Contradictory assertions trigger a `BureauConsistencyAlert` and are quarantined.

## 3. Schema Constraints
Assertions are validated against the SHACL shapes defined in the `constraints/` module.

## 4. Operational Workflow
1. **Submission**: Agent broadcasts assertion.
2. **Validation**: Kernel validates against `ontology/` schema.
3. **Settlement**: Assertion is committed to the `data/` ledger.
