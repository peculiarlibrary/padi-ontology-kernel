import os
import json
from runtime.governance import validate_event

LEDGER_PATH = os.path.join(os.getcwd(), "data", "ledger.jsonl")


def append_event(event):
    """
    Pre-commit enforced event ingestion.
    """

    ok, msg = validate_event(event)

    if not ok:
        raise ValueError(f"Governance violation: {msg}")

    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

    with open(LEDGER_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
