from rdflib import Graph
from pyshacl import validate

g = Graph()
g.parse("data/taxonomy.ttl", format="turtle")

shacl_graph = Graph()
shacl_graph.parse("shapes/taxonomy.shacl.ttl", format="turtle")

conforms, report_graph, report_text = validate(g, shacl_graph=shacl_graph)

print("CONFORMS:", conforms)
print(report_text)
