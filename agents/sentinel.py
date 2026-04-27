import json, hashlib, os

def run_audit():
    print("[Sentinel] Performing Normalized Integrity Audit (Local Authority)...")
    if not os.path.exists('manifest.json'):
        print("[Error] manifest.json not found.")
        return

    with open('manifest.json', 'r') as f:
        manifest = json.load(f)

    discrepancies = 0
    for asset in manifest.get('assets', []):
        path = asset.get('path')
        expected_hash = asset.get('sha256')
        
        if not os.path.exists(path):
            print(f"[MISSING] {path}")
            discrepancies += 1
            continue
            
        with open(path, 'rb') as f:
            actual_hash = hashlib.sha256(f.read()).hexdigest()
            
        if actual_hash == expected_hash:
            print(f"[OK] {path} verified.")
        else:
            print(f"[ALERT] {path} HASH MISMATCH!")
            discrepancies += 1

    print(f"\n[Sentinel] Found {discrepancies} discrepancies.")

if __name__ == "__main__":
    run_audit()
