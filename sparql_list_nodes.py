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

# Query to list all subjects and their associated types
query = "SELECT DISTINCT ?s ?type WHERE { ?s a ?type . } ORDER BY ?s"
print("--- DISCOVERED SUBJECTS IN KERNEL ---")
for row in g.query(query):
    print(f"Node: {row.s} | Type: {row.type}")
