from rdflib import Graph, URIRef, Literal
from runtime.ledger import MutationLedger
import time


class MutationEngine:

    def __init__(self, graph, validator=None):
        self.graph = graph
        self.validator = validator
        self.ledger = MutationLedger()

    def stage(self, operations):

        staged = Graph()
        staged += self.graph

        events = []

        for op in operations:
            events.append(self.ledger.record(op))
            self._apply(staged, op)

        return staged, events

    def commit(self, operations):

        start = time.time()

        staged, events = self.stage(operations)

        # -----------------------------
        # SHACL VALIDATION (TIMED)
        # -----------------------------
        if self.validator:
            v_start = time.time()

            print("[DEBUG] Running SHACL validation...")

            conforms, report = self.validator(staged)

            print(f"[DEBUG] SHACL completed in {time.time() - v_start:.2f}s")

            if not conforms:
                for e in events:
                    self.ledger.rollback(e["id"])

                return {
                    "status": "ROLLED_BACK",
                    "reason": "SHACL_FAILED",
                    "report": str(report),
                    "time_ms": round((time.time() - start) * 1000, 2)
                }

        self.graph = staged

        for e in events:
            self.ledger.commit(e["id"])

        return {
            "status": "COMMITTED",
            "operations": operations,
            "time_ms": round((time.time() - start) * 1000, 2)
        }

    def _apply(self, graph, op):

        if op["action"] != "add":
            return

        graph.add((
            URIRef(op["subject"]),
            URIRef(op["predicate"]),
            Literal(str(op["object"]))
        ))
