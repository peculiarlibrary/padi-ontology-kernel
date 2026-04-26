from rdflib import URIRef


SUPPORTED_BY = "https://padi-standard.org/ns/core#supportedBy"


# -------------------------
# MULTI-HOP EVIDENCE + SCORING
# -------------------------
def resolve_evidence_multihop(graph, subject_uri, max_hops=3, limit=20):
    visited = set()
    seen = set()
    frontier = [(subject_uri, 0)]
    evidence = []

    while frontier:
        node, depth = frontier.pop(0)

        if node in visited or depth > max_hops:
            continue

        visited.add(node)

        weight = 1 / (1 + depth)

        for s, p, o in graph.triples((node, URIRef(SUPPORTED_BY), None)):
            ev = str(o)

            if ev in seen:
                continue

            seen.add(ev)

            evidence.append({
                "source": str(node),
                "supported_by": ev,
                "depth": depth,
                "weight": round(weight, 4)
            })

            frontier.append((o, depth + 1))

        for s, p, o in graph.triples((None, URIRef(SUPPORTED_BY), node)):
            ev = str(s)

            if ev in seen:
                continue

            seen.add(ev)

            evidence.append({
                "source": ev,
                "supports": str(node),
                "depth": depth,
                "weight": round(weight, 4)
            })

            frontier.append((s, depth + 1))

    return sorted(evidence, key=lambda x: x["weight"], reverse=True)[:limit]


# -------------------------
# NODE CONFIDENCE
# -------------------------
def compute_node_confidence(evidence_list):
    return round(sum(e["weight"] for e in evidence_list), 6)


# -------------------------
# CONTRADICTION DETECTOR
# -------------------------
def detect_contradictions(graph, subject_uri):
    """
    Detects conflicting predicate → object mappings.
    """

    seen = {}
    contradictions = []

    for s, p, o in graph:
        if str(s) != str(subject_uri):
            continue

        key = str(p)
        val = str(o)

        if key in seen and seen[key] != val:
            contradictions.append({
                "predicate": key,
                "value_a": seen[key],
                "value_b": val,
                "status": "CONTRADICTION"
            })
        else:
            seen[key] = val

    return contradictions
