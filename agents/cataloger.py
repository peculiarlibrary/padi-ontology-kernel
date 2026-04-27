import os
import json
import sys
from runtime.ledger import Ledger

class Cataloger:
    def __init__(self):
        self.role = "Cataloger"
        # Get root directory relative to this script
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ledger = Ledger()

    def update_manifest(self):
        print(f"[{self.role}] Re-scanning Bureau assets...")
        manifest = {
            "bureau_name": "PADI Sovereign Bureau",
            "kernel_version": "4.0",
            "assets": []
        }
        
        # Scan data and ontology directories
        for folder in ["data", "ontology", "constraints"]:
            path = os.path.join(self.base_dir, folder)
            if os.path.exists(path):
                files = os.listdir(path)
                for f in files:
                    manifest["assets"].append({"type": folder, "name": f})
        
        manifest_path = os.path.join(self.base_dir, "manifest.json")
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=4)
        
        self.ledger.log_event(self.role, "Manifest updated successfully.")
        print(f"[{self.role}] Manifest synchronized.")

if __name__ == "__main__":
    Cataloger().update_manifest()
