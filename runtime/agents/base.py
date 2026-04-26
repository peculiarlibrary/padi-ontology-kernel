from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Deterministic agent interface for ontology mutation systems.
    """

    @abstractmethod
    def plan(self, input_data: dict):
        """
        Returns a list of mutation operations in canonical form:

        [
            {
                "action": "add" | "remove" | "update",
                "subject": str,
                "predicate": str,
                "object": str
            }
        ]
        """
        raise NotImplementedError("Agent must implement plan()")
