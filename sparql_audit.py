import rdflib
import glob

# Initialize Graph
g = rdflib.Graph()

# Load all local Turtle files
for file in glob.glob("*.ttl"):
    try:
        g.parse(file, format="turtle")
        print(f"Parsed: {file}")
    except Exception as e:
        print(f"Error parsing {file}: {e}")

# SPARQL Query to verify 51-node count and types
query = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT (COUNT(?node) AS ?nodeCount)
WHERE {
  { ?node rdf:type owl:Class . }
  UNION
  { ?node rdf:type owl:NamedIndividual . }
}
"""

for row in g.query(query):
    print(f"\n--- SEMANTIC AUDIT RESULT ---")
    print(f"Total Authoritative Nodes Found: {row.nodeCount}")

