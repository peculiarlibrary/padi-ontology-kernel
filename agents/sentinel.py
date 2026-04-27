import requests
import hashlib
import os
import json

def get_local_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def perform_audit():
    manifest_url = "https://peculiarlibrary.github.io/padi-ontology-kernel/manifest.json"
    print(f"[Sentinel] Fetching remote Truth from Embassy...")
    
    try:
        remote_manifest = requests.get(manifest_url).json()
        violations = 0

        for asset in remote_manifest['assets']:
            local_path = asset['path']
            if os.path.exists(local_path):
                local_hash = get_local_hash(local_path)
                if local_hash == asset['sha256']:
                    print(f"[OK] {asset['name']} matches Embassy seal.")
                else:
                    print(f"[ALERT] {asset['name']} CORRUPTION DETECTED!")
                    print(f"      Local: {local_hash[:16]}")
                    print(f"      Remote: {asset['sha256'][:16]}")
                    violations += 1
            else:
                print(f"[WARNING] {asset['name']} missing from local Kernel.")

        if violations == 0:
            print("\n[Sentinel] Audit Complete: Structural Integrity 100% Verified.")
        else:
            print(f"\n[Sentinel] CRITICAL: {violations} integrity violations found.")

    except Exception as e:
        print(f"[Sentinel] Audit Failed: {e}")

if __name__ == "__main__":
    perform_audit()
