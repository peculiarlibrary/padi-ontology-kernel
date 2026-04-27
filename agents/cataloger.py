import os
import json
import hashlib
from datetime import datetime

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def generate_manifest():
    manifest = {
        "bureau_name": "PADI Sovereign Bureau",
        "governing_architect": "Samuel Muriithi Gitandu, B.S.",
        "kernel_version": "4.1.0",
        "last_updated": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "zenodo_doi": "10.5281/zenodo.18894084",
        "assets": []
    }

    directories = {"data": "data", "ontology": "ontology", "constraints": "constraints"}

    for type_label, path in directories.items():
        if os.path.exists(path):
            for filename in os.listdir(path):
                f_path = os.path.join(path, filename)
                if os.path.isfile(f_path):
                    manifest["assets"].append({
                        "name": filename,
                        "type": type_label,
                        "path": f_path,
                        "sha256": calculate_sha256(f_path),
                        "version": "1.0.0"
                    })

    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"[Cataloger] Manifest sealed with SHA-256 fingerprints.")

if __name__ == "__main__":
    generate_manifest()
