import os
from rdflib import Graph

BASE_DIR = os.getcwd()
STORE_PATH = os.path.join(BASE_DIR, "data", "graph.ttl")

_GRAPH_CACHE = None


def load_graph(force_reload=False):
    global _GRAPH_CACHE

    # 🔴 FIX: force reload invalidates cache
    if force_reload:
        _GRAPH_CACHE = None

    if _GRAPH_CACHE is not None:
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
