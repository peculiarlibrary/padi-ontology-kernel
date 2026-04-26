import json
from runtime.event_store import LEDGER_PATH

def replay_graph():
    graph = {'nodes': {}, 'edges': []}

    try:
        with open(LEDGER_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                event = json.loads(line)

                if event['type'] == 'node':
                    graph['nodes'][event['data']['id']] = event['data']

                if event['type'] == 'edge':
                    graph['edges'].append(event['data'])

    except FileNotFoundError:
        pass

    graph['nodes'] = list(graph['nodes'].values())
    return graph
