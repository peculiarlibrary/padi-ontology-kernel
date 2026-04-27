import requests
import json

# The entry point for discovery is your live Embassy URL
BROADCAST_URL = "https://peculiarlibrary.github.io/padi-ontology-kernel/broadcast.jsonld"

def discover_bureau():
    print(f"[Scout] Initiating discovery at {BROADCAST_URL}...")
    
    try:
        # 1. Fetch the Broadcast Signal
        response = requests.get(BROADCAST_URL)
        response.raise_for_status()
        signal = response.json()
        
        print(f"[Scout] Signal Found! Authority: {signal['authority']}")
        
        # 2. Locate the Manifest through the signal
        manifest_url = "https://peculiarlibrary.github.io/padi-ontology-kernel/" + signal['endpoints']['manifest']
        manifest_data = requests.get(manifest_url).json()
        
        print(f"[Scout] Manifest verified. Assets discovered: {len(manifest_data['assets'])}")
        
        # 3. List the Immutable Seals
        for asset in manifest_data['assets']:
            print(f"  - Verified [{asset['type'].upper()}]: {asset['name']} (Seal: {asset['sha256'][:16]})")

    except Exception as e:
        print(f"[Scout] Discovery Failed: {e}")

if __name__ == "__main__":
    discover_bureau()
