import json
import datetime
import os

class Ledger:
    """The PADI Sovereign Ledger: An append-only registry for auditability."""
    def __init__(self, log_path="../daemon.log"):
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                pass 

    def record_transaction(self, agent_id, action, metadata):
        """Appends a deterministic transaction to the PADI registry."""
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "agent_id": agent_id,
            "action": action,
            "payload": metadata,
            "version": "2.0"
        }
        
        with open(self.log_path, 'a') as f:
            f.write(json.dumps(entry) + '\n')
            
        return True

    def get_history(self):
        """Retrieves the full audit trail for the Bureau."""
        if not os.path.exists(self.log_path):
            return []
        with open(self.log_path, 'r') as f:
            return [json.loads(line) for line in f]
