import rdflib

def check_registry(doi):
    g = rdflib.Graph()
    g.parse("data/registry.ttl", format="turtle")
    # Logic to verify if the DOI is already indexed as an Authority
    print(f"Auditing DOI: {doi} against Nairobi-01-Node...")
    # (Future expansion: Add actual SPARQL query here)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        check_registry(sys.argv[1])
