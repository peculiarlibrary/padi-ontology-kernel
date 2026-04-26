from rdflib import Graph

FILE = "CoderLegion_PADI_Prototype.jsonld"

g = Graph()
g.parse(FILE, format="json-ld")

print("\n--- RDF GRAPH LOADED ---")
print(f"TRIPLES: {len(g)}")
print("------------------------\n")
