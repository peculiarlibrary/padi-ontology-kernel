import rdflib
import json
import os

g = rdflib.Graph()
target_dirs = ["ontology", "epistemics", "constraints"]
for t_dir in target_dirs:
    if os.path.exists(t_dir):
        for root, _, files in os.walk(t_dir):
            for file in files:
                if file.endswith(".ttl"):
                    g.parse(os.path.join(root, file), format="turtle")

nodes = []
# Query for IRIs, their Types, Labels, and Comments
query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?s ?type ?label ?comment WHERE { 
    ?s a ?type . 
    OPTIONAL { ?s rdfs:label ?label }
    OPTIONAL { ?s rdfs:comment ?comment }
}
"""

for row in g.query(query):
    iri = str(row.s)
    if not iri.startswith('http'): continue # Filter blank nodes
    
    nodes.append({
        "id": iri,
        "name": str(row.label) if row.label else iri.split('/')[-1].split('#')[-1],
        "type": str(row.type).split('/')[-1].split('#')[-1],
        "description": str(row.comment) if row.comment else "No formal description in kernel.",
        "group": 1 if "ontology" in iri else 2
    })

# Links logic (keeping relationships intact)
links = []
link_query = "SELECT ?s ?p ?o WHERE { ?s ?p ?o . FILTER(isIRI(?o)) }"
for row in g.query(link_query):
    links.append({"source": str(row.s), "target": str(row.o), "value": 1})

with open('metadata.json', 'w') as f:
    json.dump({"nodes": nodes, "links": links}, f, indent=4)

print("Rich Convergence Complete: metadata.json updated with descriptive attributes.")
