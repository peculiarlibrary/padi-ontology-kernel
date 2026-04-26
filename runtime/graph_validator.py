def validate_graph(graph):
    nodes = {n['id']: n for n in graph.get('nodes', [])}
    edges = graph.get('edges', [])
    issues = []

    for e in edges:
        if e['from'] not in nodes:
            issues.append(f"Missing node: {e['from']}")
        if e['to'] not in nodes:
            issues.append(f"Missing node: {e['to']}")

    adj = {}
    for e in edges:
        adj.setdefault(e['from'], []).append(e['to'])

    visited = set()
    stack = set()

    def dfs(n):
        if n in stack:
            return True
        if n in visited:
            return False
        visited.add(n)
        stack.add(n)
        for nxt in adj.get(n, []):
            if dfs(nxt):
                return True
        stack.remove(n)
        return False

    for node in nodes:
        if dfs(node):
            issues.append("Cycle detected in graph")

    expected_order = {
        'PC-0001': 'execution',
        'PC-0002': 'data',
        'PC-0003': 'governance'
    }

    for nid, layer in expected_order.items():
        if nid in nodes and nodes[nid].get('layer') != layer:
            issues.append(f"Layer mismatch: {nid}")

    return { 'valid': len(issues) == 0, 'issues': issues }
