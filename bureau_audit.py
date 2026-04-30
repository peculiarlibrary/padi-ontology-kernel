import rdflib
import os
from pathlib import Path

g = rdflib.Graph()
PADI = rdflib.Namespace('https://padi.io/ontology/')
g.bind('padi', PADI)

# Ingesting all Turtle files (Recursive)
for path in Path('.').rglob('*.ttl'):
    if '.venv' in str(path) or 'node_modules' in str(path):
        continue
    try:
        g.parse(str(path), format='ttl')
    except Exception as e:
        print(f"Skipping {path}: Syntax Error")

def get_local_name(uri):
    return str(uri).split('/')[-1].split('#')[-1]

print(f"\n{'='*40}")
print(f"   PADI BUREAU INVENTORY (MINGW64)")
print(f"{'='*40}")

# Query Classes
print("\n[SCHEMA] ENTITY TYPES:")
for cls in sorted(set(g.subjects(rdflib.RDF.type, rdflib.OWL.Class))):
    print(f"  - {get_local_name(cls)}")

# Query Properties
print("\n[RELATIONS] PROPERTIES:")
for prop in sorted(set(g.subjects(rdflib.RDF.type, rdflib.OWL.ObjectProperty))):
    print(f"  - {get_local_name(prop)}")

# Query Instances
print("\n[DATA] DEFINED INSTANCES:")
# Finding subjects that have a type within the PADI namespace
for s, p, o in g.triples((None, rdflib.RDF.type, None)):
    if 'padi.io' in str(o):
        print(f"  - {get_local_name(s)} (Type: {get_local_name(o)})")

print(f"\n{'='*40}")
print(f"TOTAL TRIPLES ANALYZED: {len(g)}")
print(f"{'='*40}")
