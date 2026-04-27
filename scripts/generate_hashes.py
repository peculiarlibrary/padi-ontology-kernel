import hashlib
import os
import json

def generate_manifest():
    manifest = {}
    targets = [
        'graph.ttl', 'foreign_asset.ttl', 'ledger.jsonl', 'knowledge_seed_01.rdf',
        'graph_events.jsonl', 'zenodo_v2_standard.ttl', 'identity-manifest.ttl',
        'ontology/padi_taxonomy_v1.ttl', 'padi.ttl', 'projection-contract.jsonld.md',
        'padi.jsonld', 'shapes.shacl', 'padi_core_shapes.ttl', 'pc0003.rules.json'
    ]
    
    for path in targets:
        if os.path.exists(path):
            with open(path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                # Key 1: Full Path (e.g., 'ontology/padi_taxonomy_v1.ttl')
                manifest[path] = file_hash
                # Key 2: Filename Only (e.g., 'padi_taxonomy_v1.ttl')
                manifest[os.path.basename(path)] = file_hash
    
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=4)
    print("[Success] manifest.json optimized for Dual-Key lookup.")

if __name__ == "__main__":
    generate_manifest()
