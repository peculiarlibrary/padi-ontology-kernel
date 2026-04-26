import json
import time

LEDGER_PATH = 'data/graph_events.jsonl'

def append_event(event):
    event['ts'] = time.time()
    with open(LEDGER_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(event) + '\n')
