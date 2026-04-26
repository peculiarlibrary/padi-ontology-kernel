from rdflib import URIRef
from collections import defaultdict

CORE_NS = "https://padi-standard.org/ns/core#"


def _collect_neighbors(graph, seed, max_depth=2):
    visited = set()
    edges = []

    frontier = [(seed, 0)]

    while frontier:
        node, depth = frontier.pop(0)

        if node in visited or depth > max_depth:
            continue

        visited.add(node)

        for s, p, o in graph.triples((node, None, None)):
            edges.append((s, p, o))
            if isinstance(o, URIRef):
                frontier.append((o, depth + 1))

        for s, p, o in graph.triples((None, None, node)):
            edges.append((s, p, o))
            if isinstance(s, URIRef):
                frontier.append((s, depth + 1))

    return list(visited), edges


def _group_by_predicate(edges):
    grouped = defaultdict(list)
    for s, p, o in edges:
        grouped[str(p)].append((str(s), str(o)))
    return grouped


def generate_article(graph, node_id: str):
    seed = URIRef(f"http://example.org/node/{node_id}")

    nodes, edges = _collect_neighbors(graph, seed)
    grouped = _group_by_predicate(edges)

    title = f"Graph Synthesis: {node_id}"

    sections = []

    sections.append(f"# {title}\n")

    sections.append("## 1. Core Node")
    sections.append(str(seed))

    sections.append("\n## 2. Connected Structure")

    for predicate, items in grouped.items():
        sections.append(f"\n### {predicate}")
        for s, o in items[:10]:
            sections.append(f"- {s} → {o}")

    sections.append("\n## 3. Node Count")
    sections.append(str(len(nodes)))

    sections.append("\n## 4. Edge Count")
    sections.append(str(len(edges)))

    return "\n".join(sections)
