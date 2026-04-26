import os
import time
import sys
# Ensure root is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtime.ledger import Ledger

class Foreman:
    def __init__(self):
        self.role = "Foreman"
        self.base_dir = "C:/padi-sovereign-bureau/padi-ontology-kernel"
        self.ledger = Ledger(os.path.join(self.base_dir, "daemon.log"))
        self.required_dirs = ["data", "ontology", "constraints", "agents", "runtime"]

    def run_maintenance(self):
        print(f"[{self.role}] Starting routine structure audit...")
        for d in self.required_dirs:
            target = os.path.join(self.base_dir, d)
            if not os.path.exists(target):
                print(f"[{self.role}] ALERT: Missing {d}. Repairing...")
                os.makedirs(target, exist_ok=True)
        
        self.ledger.record_transaction(self.role, "STRUCTURE_AUDIT", {"status": "verified"})
        print(f"[{self.role}] Audit complete. No anomalies detected.")

if __name__ == "__main__":
    f = Foreman()
    while True:
        f.run_maintenance()
        time.sleep(30) # Maintenance every 30 seconds
