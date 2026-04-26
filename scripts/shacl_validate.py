from rdflib import Graph
from pyshacl import validate

DATA_FILE = "CoderLegion_PADI_Prototype.jsonld"
SHAPES_FILE = "constraints/shapes.shacl"

data_graph = Graph()
data_graph.parse(DATA_FILE, format="json-ld")

shapes_graph = Graph()
shapes_graph.parse(SHAPES_FILE, format="turtle")

conforms, report_graph, report_text = validate(
    data_graph,
    shacl_graph=shapes_graph,
    inference="rdfs",
    debug=False
)

print("\n--- SHACL VALIDATION ---")
print("CONFORMS:", conforms)
print("------------------------\n")
print(report_text)
