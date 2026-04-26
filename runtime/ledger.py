import json
import datetime
import os

class Ledger:
    def __init__(self, log_path="registry.log"):
        self.log_path = log_path
        # Ensure the log file exists in the root or specified path
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                pass 

    def record_transaction(self, agent_id, action, metadata):
        """Appends a deterministic transaction to the PADI ledger."""
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
        history = []
        with open(self.log_path, 'r') as f:
            for line in f:
                history.append(json.loads(line))
        return history
