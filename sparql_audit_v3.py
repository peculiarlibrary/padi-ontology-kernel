import rdflib
import os

g = rdflib.Graph()
# Target the specific directories identified in the file explorer
target_dirs = ['ontology', 'data', 'epistemics', 'constraints']

for t_dir in target_dirs:
    if os.path.exists(t_dir):
        for root, dirs, files in os.walk(t_dir):
            for file in files:
                if file.endswith(".ttl"):
                    path = os.path.join(root, file)
                    g.parse(path, format="turtle")
                    print(f"Parsed Authority: {path}")

query = "SELECT (COUNT(?s) AS ?count) WHERE { ?s a ?type . }"
for row in g.query(query):
    print(f"\nTotal Authoritative Subjects Found: {row.count}")
