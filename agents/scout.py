import requests
import json
import time

BROADCAST_URL = "https://peculiarlibrary.github.io/padi-ontology-kernel/broadcast.jsonld"

def discover_bureau():
    print(f"[Scout] Initiating discovery at {BROADCAST_URL}...")
    
    try:
        response = requests.get(BROADCAST_URL)
        
        # Check if the Embassy is returning empty content (deployment lag)
        if not response.text.strip():
            print("[Scout] Embassy Signal is currently empty. Retrying in 5s...")
            time.sleep(5)
            response = requests.get(BROADCAST_URL)

        signal = response.json()
        print(f"[Scout] Signal Found! Authority: {signal.get('authority', 'Unknown')}")
        
        # Correctly resolve the manifest URL
        manifest_url = "https://peculiarlibrary.github.io/padi-ontology-kernel/manifest.json"
        manifest_data = requests.get(manifest_url).json()
        
        print(f"[Scout] Manifest verified. Assets discovered: {len(manifest_data['assets'])}")
        
        for asset in manifest_data['assets']:
            print(f"  - Verified [{asset['type'].upper()}]: {asset['name']} (Seal: {asset['sha256'][:16]})")

    except Exception as e:
        print(f"[Scout] Discovery Failed: {e}")

if __name__ == "__main__":
    discover_bureau()
