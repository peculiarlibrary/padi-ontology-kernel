from runtime.agents.base import BaseAgent
import uuid

PADI = "https://padi-standard.org/ns/core#"
CL = "https://coderlegion.com/schema/v1#"


class TaxonomyAgent(BaseAgent):

    def plan(self, input_data):
        """
        input_data = {
            "label": str,
            "depth": str | int
        }
        """

        node_id = f"http://example.org/node/{uuid.uuid4()}"

        return [
            {
                "action": "add",
                "subject": node_id,
                "predicate": f"{PADI}depthIndex",
                "object": str(input_data["depth"])
            },
            {
                "action": "add",
                "subject": node_id,
                "predicate": f"{CL}nodeName",
                "object": input_data["label"]
            }
        ]
