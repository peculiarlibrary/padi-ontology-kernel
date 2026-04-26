from datetime import datetime
import uuid
import json


class MutationLedger:

    def __init__(self):
        self.events = []

    def record(self, operation, status="staged"):
        event = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "operation": operation,
            "status": status
        }
        self.events.append(event)
        return event

    def commit(self, event_id):
        for e in self.events:
            if e["id"] == event_id:
                e["status"] = "committed"

    def rollback(self, event_id):
        for e in self.events:
            if e["id"] == event_id:
                e["status"] = "rolled_back"

    def export(self):
        return json.dumps(self.events, indent=2)
