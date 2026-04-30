import rdflib
import os

g = rdflib.Graph()
target_dirs = ['ontology', 'data', 'epistemics', 'constraints']

for t_dir in target_dirs:
    if os.path.exists(t_dir):
        for root, dirs, files in os.walk(t_dir):
            for file in files:
                if file.endswith(".ttl"):
                    g.parse(os.path.join(root, file), format="turtle")

# Use int() to ensure we get a number, not an object reference
query = "SELECT (COUNT(DISTINCT ?s) AS ?count) WHERE { ?s a ?type . }"
for row in g.query(query):
    print(f"Total Authoritative Subjects: {int(row.count)}")
