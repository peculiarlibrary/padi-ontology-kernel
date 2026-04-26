#!/usr/bin/env bash

set -e

echo "=== PADI BOOTSTRAP START ==="

mkdir -p runtime/storage
mkdir -p data

echo "[1/3] Writing graph_store.py"

cat > runtime/storage/graph_store.py << 'EOF'
import os
from rdflib import Graph

BASE_DIR = os.getcwd()
STORE_PATH = os.path.join(BASE_DIR, "data", "graph.ttl")

_GRAPH_CACHE = None

def load_graph(force_reload=False):
    global _GRAPH_CACHE

    if _GRAPH_CACHE is not None and not force_reload:
        return _GRAPH_CACHE

    g = Graph()

    if os.path.exists(STORE_PATH) and os.path.getsize(STORE_PATH) > 0:
        g.parse(STORE_PATH, format="turtle")

    _GRAPH_CACHE = g
    return g

def save_graph(graph):
    global _GRAPH_CACHE

    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    graph.serialize(destination=STORE_PATH, format="turtle")

    _GRAPH_CACHE = graph
EOF


echo "[2/3] Writing ledger_replay.py"

cat > runtime/storage/ledger_replay.py << 'EOF'
import os
import json
from rdflib import Graph, URIRef, Literal

BASE_DIR = os.getcwd()

LEDGER_PATH = os.path.join(BASE_DIR, "data", "ledger.jsonl")
GRAPH_PATH = os.path.join(BASE_DIR, "data", "graph.ttl")

def replay_ledger():
    g = Graph()

    if not os.path.exists(LEDGER_PATH):
        return g

    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            event = json.loads(line)

            if event.get("type") != "mutation":
                continue

            g.add((
                URIRef(event["subject"]),
                URIRef(event["predicate"]),
                Literal(event["object"])
            ))

    return g

def persist_replay():
    g = replay_ledger()

    os.makedirs(os.path.dirname(GRAPH_PATH), exist_ok=True)
    g.serialize(destination=GRAPH_PATH, format="turtle")

    return len(g)
EOF


echo "[3/3] Writing padi_core.py"

cat > runtime/padi_core.py << 'EOF'
import os
import json
from rdflib import URIRef, Literal

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
        self.graph = load_graph()

    def apply_mutations(self, ops):
        for op in ops:
            append_ledger(op)

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
EOF


echo "=== BOOTSTRAP COMPLETE ==="
echo "Run: python -m runtime.cli stats"
