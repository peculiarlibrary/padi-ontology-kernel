from runtime.store import RDFStore
from pyshacl import validate
from rdflib import Graph

def validate_graph(graph, shapes_path):
    shapes = Graph()
    shapes.parse(shapes_path, format="turtle")
    
    # We disable inference="rdfs" to prevent the validation hang
    conforms, _, report = validate(
        graph,
        shacl_graph=shapes,
        inference=None, 
        serialize_report_graph=True
    )
    return {"conforms": conforms, "report": report}

def execute_query(sparql_query):
    g = RDFStore.get()
    results = g.query(sparql_query)
    return [{"label": str(row[0])} for row in results]
