import rdflib
import json
import os

g = rdflib.Graph()
target_dirs = ['ontology', 'data', 'epistemics', 'constraints']
for t_dir in target_dirs:
    if os.path.exists(t_dir):
        for root, _, files in os.walk(t_dir):
            for file in files:
                if file.endswith(".ttl"):
                    g.parse(os.path.join(root, file), format="turtle")

nodes = []
links = []

# Map the 17 subjects to D3 nodes
query = "SELECT DISTINCT ?s ?type WHERE { ?s a ?type . }"
for row in g.query(query):
    iri = str(row.s)
    nodes.append({
        "id": iri,
        "name": iri.split('/')[-1].split('#')[-1], # Short name for label
        "group": 1 if "ontology" in iri else 2
    })

# Map ObjectProperties to links
link_query = "SELECT ?s ?p ?o WHERE { ?s ?p ?o . FILTER(isIRI(?o)) }"
for row in g.query(link_query):
    links.append({
        "source": str(row.s),
        "target": str(row.o),
        "value": 1
    })

with open('metadata.json', 'w') as f:
    json.dump({"nodes": nodes, "links": links}, f, indent=4)

print(f"Convergence Complete: metadata.json updated with {len(nodes)} nodes.")
