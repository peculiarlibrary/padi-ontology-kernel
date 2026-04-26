import json
import os

def load_graph(path='data/graph.json'):
    if not os.path.exists(path):
        return {'nodes': [], 'edges': []}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_graph(graph, path='data/graph.json'):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2)
