#!/bin/bash
# Synchronize TTL to clean, compacted JSON-LD
python -c "
from rdflib import Graph
g = Graph().parse('data/graph.ttl', format='turtle')
context = {
    'padi': 'https://padi-standard.org/ns/core#',
    'depthIndex': 'padi:depthIndex',
    'nodeName': 'padi:nodeName'
}
print(g.serialize(format='json-ld', context=context, indent=4))
" > ontology/padi.jsonld
echo "Registry Sync: Compacted JSON-LD settled."
