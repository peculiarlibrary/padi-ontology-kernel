import os
import json
from collections import defaultdict
from rdflib import Graph, URIRef, Literal

BASE_DIR = os.getcwd()

LEDGER_PATH = os.path.join(BASE_DIR, "data", "ledger.jsonl")
GRAPH_PATH = os.path.join(BASE_DIR, "data", "graph.ttl")


def replay_ledger():
    """
    Deterministic replay engine:
    - parses ops-based ledger format
    - resolves canonical values (last-write-wins)
    - detects contradictions
    """

    g = Graph()

    if not os.path.exists(LEDGER_PATH):
        return g

    values = defaultdict(list)
    canonical = {}
    contradictions = []

    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            event = json.loads(line)

            ops = event.get("ops", [])

            for op in ops:
                s = op["subject"]
                p = op["predicate"]
                o = op["object"]

                key = (s, p)
                values[key].append(o)

    # resolve canonical state (last-write-wins)
    for (s, p), vals in values.items():
        if len(set(vals)) > 1:
            contradictions.append({
                "subject": s,
                "predicate": p,
                "values": vals
            })

        canonical[(s, p)] = vals[-1]

    # build graph
    for (s, p), o in canonical.items():
        g.add((URIRef(s), URIRef(p), Literal(o)))

    return {
        "graph": g,
        "triples": len(g),
        "contradictions": contradictions,
        "canonical": [
            {"subject": s, "predicate": p, "value": o}
            for (s, p), o in canonical.items()
        ]
    }


def persist_replay():
    result = replay_ledger()

    g = result["graph"]

    os.makedirs(os.path.dirname(GRAPH_PATH), exist_ok=True)
    g.serialize(destination=GRAPH_PATH, format="turtle")

    return {
        "triples": len(g),
        "contradictions": result["contradictions"],
        "canonical": result["canonical"]
    }
