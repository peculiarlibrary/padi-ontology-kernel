# Contributing to the PADI Sovereign Bureau

The Nairobi Bureau is a **Structurally Guarded** node. We do not accept "vibe-based" submissions. All contributions must pass the Sentinel's audit.

## 1. The Golden Rule
**Structure = Authority.** If your RDF/Turtle data does not conform to the SHACL shapes in `constraints/`, it will be rejected by the Node Integrity Check.

## 2. The Process
1. **Fork & Branch:** Create a feature branch for your proposed knowledge asset.
2. **Validation:** Run `./verify-node.sh` locally before pushing.
3. **The Seal:** All commits MUST be GPG-signed. Unsigned commits are considered "Unauthenticated Noise" and will be purged.
4. **The Handshake:** Follow the [PC-0012 Agentic Handshake Protocol](https://github.com/peculiarlibrary/padi-ontology-kernel/wiki/PC-0012-Agentic-Handshake-Protocol).

## 3. Technical Requirements
- Files must be in valid **Turtle (.ttl)** format.
- Knowledge assets must include a valid **DOI** or persistent identifier where applicable.
- All nodes must be inter-linked within the existing PADI ontology.

*Failure to adhere to these standards will trigger a Sentinel Denial (Red X).*
