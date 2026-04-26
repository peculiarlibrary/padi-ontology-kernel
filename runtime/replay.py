import json
from rdflib import Graph, URIRef, Literal

LEDGER_PATH = "data/ledger.jsonl"


def rebuild_graph():
    g = Graph()

    try:
        with open(LEDGER_PATH, "r") as f:
            for line in f:
                entry = json.loads(line)
                ops = entry.get("ops", [])

                for op in ops:
                    s = URIRef(op["subject"])
                    p = URIRef(op["predicate"])
                    o = Literal(str(op["object"]))

                    triple = (s, p, o)

                    # idempotent rebuild
                    if triple not in g:
                        g.add(triple)

    except FileNotFoundError:
        return {"error": "ledger not found"}

    return g


def verify_against_disk(graph_path="data/graph.ttl"):
    rebuilt = rebuild_graph()

    disk = Graph()
    try:
        disk.parse(graph_path, format="turtle")
    except Exception as e:
        return {"status": "ERROR", "reason": f"Failed to load disk graph: {e}"}

    rebuilt_set = set(rebuilt)
    disk_set = set(disk)

    if rebuilt_set == disk_set:
        return {
            "status": "VERIFIED",
            "triples": len(disk_set)
        }

    # compute diff
    missing = rebuilt_set - disk_set
    extra = disk_set - rebuilt_set

    return {
        "status": "MISMATCH",
        "rebuilt_triples": len(rebuilt_set),
        "disk_triples": len(disk_set),
        "missing": len(missing),
        "extra": len(extra)
    }
