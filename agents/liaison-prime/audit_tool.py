import rdflib
import sys

def verify_doi_in_registry(doi_target):
    """Checks if a DOI is already an indexed authority in the Bureau."""
    g = rdflib.Graph()
    try:
        g.parse("data/registry.ttl", format="turtle")
        # Define the PADI Namespace
        PADI = rdflib.Namespace("https://padi.io/ontology/")
        
        # Simple existence check for the DOI within the graph
        found = False
        for s, p, o in g:
            if doi_target in str(o):
                found = True
                break
        
        if found:
            print(f"[SUCCESS]: DOI {doi_target} is a recognized Authority.")
        else:
            print(f"[QUARANTINE]: DOI {doi_target} not found. Submission rejected.")
            
    except Exception as e:
        print(f"[ERROR]: Failed to access Registry. {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verify_doi_in_registry(sys.argv[1])
    else:
        print("Usage: python audit_tool.py <DOI>")
