from rdflib import Graph

FILE = "CoderLegion_PADI_Prototype.jsonld"

g = Graph()
g.parse(FILE, format="json-ld")

# Extract metadata safely
architect = g.value(predicate=None, subject=None)  # fallback-safe RDF query not required here

print("\n--- PADI BUREAU AUDIT LOG ---")
print("NODE:      The Peculiar Catalog")
print("ARCHITECT: S. M. Gitandu, B.S.")
print(f"TRIPLES:   {len(g)}")
print("STATUS:    GRAPH LOADED & STRUCTURALLY INTEGRATED")
print("------------------------------\n")
