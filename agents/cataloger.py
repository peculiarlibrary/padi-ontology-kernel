import os
import time
from runtime.ledger import Ledger

class Cataloger:
    """The PADI Cataloger: Translates raw data into formal knowledge stubs."""
    def __init__(self):
        self.role = "Cataloger"
        self.data_path = "../data"
        self.ledger = Ledger("../daemon.log")

    def scan_for_ingestion(self):
        """Scans the data directory for new material to catalog."""
        print(f"[{self.role}] Scanning {self.data_path} for unindexed assets...")
        files = [f for f in os.listdir(self.data_path) if os.path.isfile(os.path.join(self.data_path, f))]
        
        if not files:
            print(f"[{self.role}] Data stacks are empty. Standing by.")
            return

        for file_name in files:
            print(f"[{self.role}] Indexing: {file_name}")
            self.ledger.record_transaction(
                self.role, 
                "CATALOG_ENTRY", 
                {"filename": file_name, "status": "indexed"}
            )

if __name__ == "__main__":
    cataloger = Cataloger()
    while True:
        cataloger.scan_for_ingestion()
        time.sleep(60) # Scan every minute
