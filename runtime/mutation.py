from rdflib import URIRef, Literal
from runtime.store import RDFStore
from runtime.executor import validate_graph


PADI = "https://padi-standard.org/ns/core#"
CL = "https://coderlegion.com/schema/v1#"


def add_triple(subject, predicate, obj):
    graph = RDFStore.get()

    s = URIRef(subject)
    p = URIRef(predicate)
    o = Literal(obj)

    graph.add((s, p, o))

    conforms, report = validate_graph(graph, "constraints/shapes.shacl")

    if not conforms:
        graph.remove((s, p, o))
        return {
            "status": "REJECTED",
            "reason": "SHACL_VALIDATION_FAILED",
            "report": report
        }

    RDFStore.save()

    return {
        "status": "COMMITTED",
        "triple": [subject, predicate, obj]
    }


def remove_triple(subject, predicate, obj):
    graph = RDFStore.get()

    s = URIRef(subject)
    p = URIRef(predicate)
    o = Literal(obj)

    graph.remove((s, p, o))

    conforms, report = validate_graph(graph, "constraints/shapes.shacl")

    if not conforms:
        graph.add((s, p, o))
        return {
            "status": "REJECTED",
            "reason": "SHACL_VALIDATION_FAILED",
            "report": report
        }

    RDFStore.save()

    return {
        "status": "REMOVED",
        "triple": [subject, predicate, obj]
    }
