import os
import json

from runtime.storage.graph_store import load_graph, save_graph
from runtime.storage.ledger_replay import persist_replay

LEDGER_PATH = os.path.join(os.getcwd(), "data", "ledger.jsonl")


def append_ledger(op):
    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

    event = {
        "type": "mutation",
        "subject": op["subject"],
        "predicate": op["predicate"],
        "object": op["object"]
    }

    with open(LEDGER_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


class PADIKernel:

    def __init__(self):
        # 🔴 CRITICAL FIX: always rebuild graph from ledger
        persist_replay()
        self.graph = load_graph(force_reload=True)

    def apply_mutations(self, ops):
        for op in ops:
            append_ledger(op)

        # rebuild deterministic state
        persist_replay()
        self.graph = load_graph(force_reload=True)

        return {
            "status": "COMMITTED",
            "triples": len(self.graph)
        }

    def stats(self):
        return {
            "triples": len(self.graph),
            "subjects": len(set(self.graph.subjects())),
            "predicates": len(set(self.graph.predicates())),
            "objects": len(set(self.graph.objects())),
        }


def create_kernel():
    return PADIKernel()
