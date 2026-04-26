# PADI Governance Rules (v1.1)

## 1. Axiomatic Constraints
* **Sovereignty**: All agent operations are bounded by the namespace defined in `ontology/core.ttl`.
* **Determinism**: Every state transition in the Bureau must be reproducible from the `data/` ledger.

## 2. Validation Protocols
* **Epistemic Check**: Assertions must resolve against the `epistemics/assertion-model.md` before settlement.
* **Integrity Gate**: Any transaction failing SHACL validation shall trigger a `GovernanceException`.

## 3. Operational Directive
* All agents must sign assertions with their registered URI.
* Unauthorized schema modifications are rejected at the kernel-binding layer.
