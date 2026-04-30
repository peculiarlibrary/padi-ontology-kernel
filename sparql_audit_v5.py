import rdflib
import os

g = rdflib.Graph()
# Explicit targets from your Mapping Semantic Depth audit
target_dirs = ['ontology', 'data', 'epistemics', 'constraints']

for t_dir in target_dirs:
    if os.path.exists(t_dir):
        for root, dirs, files in os.walk(t_dir):
            for file in files:
                if file.endswith(".ttl"):
                    try:
                        g.parse(os.path.join(root, file), format="turtle")
                    except Exception as e:
                        print(f"Error parsing {file}: {e}")

# Query specifically for unique subjects across the kernel
query = "SELECT (COUNT(DISTINCT ?s) AS ?total) WHERE { ?s a ?type . }"
results = g.query(query)

for row in results:
    # Accessing the 'total' variable from the SPARQL result row
    node_count = int(row['total'])
    print(f"--- SEMANTIC AUDIT SUCCESS ---")
    print(f"Total Authoritative Subjects Found: {node_count}")

# Check for the specific 51-node alignment
if node_count == 0:
    print("WARNING: Graph is empty. Check file encoding or namespaces.")
