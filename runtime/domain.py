from runtime.executor import execute_query, validate_graph
from runtime.store import RDFStore
from runtime.mutation import add_triple, remove_triple
from runtime.transaction import execute_transaction
from runtime.agent_executor import run_agent


def inspect_taxonomy():
    return execute_query("SELECT ?s ?p ?o WHERE { ?s ?p ?o }")


def validate():
    graph = RDFStore.get()
    conforms, report = validate_graph(graph, "constraints/shapes.shacl")
    return {"conforms": conforms, "report": report}


def stats():
    graph = RDFStore.get()
    return {
        "triples": len(graph),
        "subjects": len(set(graph.subjects())),
        "predicates": len(set(graph.predicates())),
        "objects": len(set(graph.objects()))
    }


def add(subject, predicate, obj):
    return add_triple(subject, predicate, obj)


def remove(subject, predicate, obj):
    return remove_triple(subject, predicate, obj)


def transact(operations):
    return execute_transaction(operations)


def run(agent_name, payload):
    return run_agent(agent_name, payload)
