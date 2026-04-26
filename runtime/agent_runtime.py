from runtime.store import RDFStore
from runtime.executor import execute_query, validate_graph
from rdflib import URIRef, Literal, Namespace, RDF

PADI = Namespace("https://padi-standard.org/ns/core#")

class AgentRouter:
    def __init__(self, ontology_path="CoderLegion_PADI_Prototype.jsonld"):
        self.graph = RDFStore.load(ontology_path)

    def route(self, command, payload):
        import json
        data = json.loads(payload)
        g = RDFStore.get()
        
        if command == "taxonomy":
            # Sanitize the ID to ensure it is a valid URI
            node_id = data['id'].replace(" ", "_")
            node_uri = URIRef(f"http://example.org/node/{node_id}")
            
            g.add((node_uri, RDF.type, PADI.TaxonomyNode))
            g.add((node_uri, PADI.label, Literal(data['label'])))
            g.add((node_uri, PADI.depthIndex, Literal(data['depth'])))
            
            # Save the updated graph
            g.serialize(destination="CoderLegion_PADI_Prototype.jsonld", format="json-ld")
            return {"status": "SUCCESS", "uri": str(node_uri)}
            
        return f"UNKNOWN_COMMAND: {command}"
