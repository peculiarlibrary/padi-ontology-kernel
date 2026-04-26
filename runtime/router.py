def route_command(args):
    import json
    from runtime.graph_validator import validate_graph

    command = args[1] if len(args) > 1 else None
    subcommand = args[2] if len(args) > 2 else None
    payload = args[3] if len(args) > 3 else None

    # GRAPH ROUTER (HIGHEST PRIORITY)
    if command == 'graph':
        if subcommand == 'register':
            data = json.loads(payload)
            result = register_graph_node(data)
            print(json.dumps(result, indent=2))
            return

        if subcommand == 'edge':
            data = json.loads(payload)
            result = register_graph_edge(data)
            print(json.dumps(result, indent=2))
            return

        if subcommand == 'validate':
            graph = load_graph()
            result = validate_graph(graph)
            print(json.dumps(result, indent=2))
            return

    # AUDIT ROUTER (LOWER PRIORITY - MUST NEVER INTERCEPT GRAPH)
    if command == 'audit':
        if subcommand == 'taxonomy':
            data = json.loads(payload or '{}')
            result = audit_taxonomy(data)
            print(json.dumps(result, indent=2))
            return

    print(json.dumps({status: INVALID_COMMAND}))
    return
from runtime.graph_store import load_graph, save_graph
def register_graph_node(data):
    graph = load_graph()
    graph.setdefault('nodes', []).append(data)
    save_graph(graph)
    return {'status': 'RESOLVED', 'node': data}

def register_graph_edge(data):
    graph = load_graph()
    graph.setdefault('edges', []).append(data)
    save_graph(graph)
    return {'status': 'RESOLVED', 'edge': data}
from runtime.event_store import append_event
from runtime.graph_replay import replay_graph

def register_graph_node(data):
    append_event({'type': 'node', 'data': data})
    return {'status': 'APPENDED', 'node': data}

def register_graph_edge(data):
    append_event({'type': 'edge', 'data': data})
    return {'status': 'APPENDED', 'edge': data}

def load_graph():
    return replay_graph()
