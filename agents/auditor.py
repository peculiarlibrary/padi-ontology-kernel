import os
import time
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtime.ledger import Ledger

class Auditor:
    def __init__(self):
        self.role = "Auditor"
        self.base_dir = "C:/padi-sovereign-bureau/padi-ontology-kernel"
        self.ledger = Ledger(os.path.join(self.base_dir, "daemon.log"))

    def verify_ledger_integrity(self):
        print(f"[{self.role}] Performing smart integrity audit...")
        history = self.ledger.get_history()
        
        for entry in history:
            if entry.get("action") == "CATALOG_ENTRY":
                filename = entry.get("payload", {}).get("filename", "")
                
                # Only enforce DOI on .ttl files (Knowledge Assets)
                # Ignore system logs and internal jsonl files
                if filename.endswith(".ttl"):
                    # Simulation: Check if the file name implies a standard or asset
                    if "standard" in filename or "asset" in filename:
                         if "zenodo" not in filename.lower(): # Basic check for DOI-proxies
                             print(f"[{self.role}] COMPLIANCE FAILURE: {filename} missing authority marker.")
                             self.ledger.record_transaction(self.role, "COMPLIANCE_FAILURE", {"file": filename})
                             return

        self.ledger.record_transaction(self.role, "INTEGRITY_CHECK", {"status": "SECURE"})
        print(f"[{self.role}] Audit Complete: System is compliant.")

if __name__ == "__main__":
    Auditor().verify_ledger_integrity()
