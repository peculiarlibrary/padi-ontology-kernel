import json
import os
from datetime import datetime

def update_broadcast():
    broadcast_path = "broadcast.jsonld"
    
    # Check if the signal exists before attempting to refresh it
    if not os.path.exists(broadcast_path):
        print(f"[Liaison] ERROR: {broadcast_path} not found. Initialize it first.")
        return

    with open(broadcast_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("[Liaison] ERROR: broadcast.jsonld is malformed.")
            return
    
    # Update timestamp to signal fresh data to external agents
    data["latest_update"] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    with open(broadcast_path, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"[Liaison] Broadcast signal refreshed at {data['latest_update']} for A2A discovery.")

if __name__ == "__main__":
    update_broadcast()
