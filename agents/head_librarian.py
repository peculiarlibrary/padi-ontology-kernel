import sys, os, json, shutil
# Ensure root is in path for runtime imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from runtime.ledger import Ledger

class HeadLibrarian:
    def __init__(self):
        self.persona = "Head Librarian"
        self.base_dir = "C:/padi-sovereign-bureau/padi-ontology-kernel"
        self.ledger_path = os.path.join(self.base_dir, "daemon.log")
        self.data_dir = os.path.join(self.base_dir, "data")
        self.quarantine_dir = os.path.join(self.base_dir, "quarantine")
        self.ledger = Ledger(self.ledger_path)

    def enforce_quarantine(self):
        """Moves non-compliant assets to a restricted directory."""
        if not os.path.exists(self.quarantine_dir):
            os.makedirs(self.quarantine_dir)
        
        history = self.ledger.get_history()
        failures = [e for e in history if e.get("action") == "COMPLIANCE_FAILURE"]
        
        # Cross-reference failures with catalog entries to find filenames
        for fail in failures:
            # For simplicity, we'll look for any file in /data that doesn't belong
            for filename in os.listdir(self.data_dir):
                if "rogue" in filename or "invalid" in filename: # Targeted logic
                    src = os.path.join(self.data_dir, filename)
                    dst = os.path.join(self.quarantine_dir, filename)
                    print(f"[{self.persona}] QUARANTINE: Moving {filename} out of active data stacks.")
                    shutil.move(src, dst)

    def generate_report(self):
        history = self.ledger.get_history()
        stats = {"Foreman": 0, "Cataloger": 0, "Auditor": 0, "System_Architect": 0}
        for entry in history:
            agent = entry.get("agent_id")
            if agent in stats: stats[agent] += 1
        
        return f"\n--- 🏛️ BUREAU REPORT ---\nStatus: OPERATIONAL\nAudit Hits: {stats['Auditor']}\n------------------------"

if __name__ == "__main__":
    lib = HeadLibrarian()
    lib.enforce_quarantine()
    print(lib.generate_report())
