from enum import Enum
from rdflib import Graph


class EpistemicStatus(str, Enum):
    ASSERTED = "ASSERTED"
    INFERRED = "INFERRED"
    DERIVED = "DERIVED"


class EpistemicEngine:
    """
    Assigns epistemic metadata to RDF triples.
    This is NOT reasoning — it is truth classification.
    """

    def __init__(self, graph: Graph):
        self.graph = graph

    def classify_triple(self, s, p, o):
        """
        Rule-based epistemic classification.

        Deterministic logic only (no LLM behavior).
        """

        # Rule 1: Explicit ontology assertions → ASSERTED
        if str(s).startswith("http") and str(p).startswith("http"):
            return EpistemicStatus.ASSERTED

        # Rule 2: inferred patterns (placeholder structural logic)
        if "type" in str(p).lower():
            return EpistemicStatus.INFERRED

        # Rule 3: everything else derived via graph traversal
        return EpistemicStatus.DERIVED

    def annotate_graph(self):
        """
        Produces epistemically annotated view of graph.
        """

        annotated = []

        for s, p, o in self.graph:
            status = self.classify_triple(s, p, o)

            annotated.append({
                "subject": str(s),
                "predicate": str(p),
                "object": str(o),
                "epistemic_status": status.value
            })

        return annotated
