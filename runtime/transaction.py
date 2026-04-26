from rdflib import URIRef, Literal
from runtime.store import RDFStore
from runtime.executor import validate_graph


def apply_operation(graph, op):
    action = op["action"]
    s = URIRef(op["subject"])
    p = URIRef(op["predicate"])
    o = Literal(op["object"])

    if action == "add":
        graph.add((s, p, o))

    elif action == "remove":
        graph.remove((s, p, o))


def execute_transaction(operations):
    """
    operations = [
        {"action": "add", "subject": "...", "predicate": "...", "object": "..."},
        ...
    ]
    """

    original_graph = RDFStore.get()
    working_graph = RDFStore.clone()

    # Apply all operations
    for op in operations:
        apply_operation(working_graph, op)

    # Validate entire new state
    conforms, report = validate_graph(working_graph, "constraints/shapes.shacl")

    if not conforms:
        return {
            "status": "REJECTED",
            "reason": "SHACL_VALIDATION_FAILED",
            "report": report
        }

    # Commit
    RDFStore.replace(working_graph)
    RDFStore.save()

    return {
        "status": "COMMITTED",
        "operations": operations
    }
