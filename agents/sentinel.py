import requests
import hashlib
import os

def get_normalized_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        content = f.read()
        # Normalize: replace Windows CRLF (\r\n) with Linux LF (\n)
        normalized_content = content.replace(b"\r\n", b"\n")
        sha256_hash.update(normalized_content)
    return sha256_hash.hexdigest()

def perform_audit():
    manifest_url = "https://peculiarlibrary.github.io/padi-ontology-kernel/manifest.json"
    print(f"[Sentinel] Performing Normalized Integrity Audit...")
    
    try:
        remote_manifest = requests.get(manifest_url).json()
        violations = 0

        for asset in remote_manifest['assets']:
            local_path = asset['path']
            if os.path.exists(local_path):
                # Use the normalized hash to account for Windows/Linux differences
                local_hash = get_normalized_hash(local_path)
                if local_hash == asset['sha256']:
                    print(f"[OK] {asset['name']} verified.")
                else:
                    print(f"[ALERT] {asset['name']} HASH MISMATCH!")
                    violations += 1
            else:
                print(f"[WARNING] {asset['name']} missing locally.")

        if violations == 0:
            print("\n[Sentinel] Equilibrium Reached: 100% Verified.")
        else:
            print(f"\n[Sentinel] Found {violations} discrepancies.")

    except Exception as e:
        print(f"[Sentinel] Error: {e}")

if __name__ == "__main__":
    perform_audit()
