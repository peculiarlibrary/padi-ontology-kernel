import os
import time
import sys
# Path injection for local execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtime.ledger import Ledger

class Cataloger:
    def __init__(self):
        self.role = "Cataloger"
        self.base_dir = "C:/padi-sovereign-bureau/padi-ontology-kernel"
        self.data_path = os.path.join(self.base_dir, "data")
        self.ledger = Ledger(os.path.join(self.base_dir, "daemon.log"))

    def scan_for_ingestion(self):
        print(f"[{self.role}] Scanning {self.data_path} for assets...")
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
            
        files = [f for f in os.listdir(self.data_path) if os.path.isfile(os.path.join(self.data_path, f))]
        
        if not files:
            print(f"[{self.role}] Data stacks are empty.")
            return

        for file_name in files:
            # We record the filename in the payload for the Auditor to check
            print(f"[{self.role}] Indexing: {file_name}")
            self.ledger.record_transaction(self.role, "CATALOG_ENTRY", {"filename": file_name})

if __name__ == "__main__":
    c = Cataloger()
    # Simple loop for standalone run
    c.scan_for_ingestion()
