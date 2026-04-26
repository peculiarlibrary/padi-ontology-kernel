from runtime.transaction import execute_transaction
from runtime.agents.taxonomy_agent import TaxonomyAgent


AGENT_REGISTRY = {
    "taxonomy": TaxonomyAgent()
}


def run_agent(agent_name, payload):
    if agent_name not in AGENT_REGISTRY:
        return {"status": "ERROR", "reason": "UNKNOWN_AGENT"}

    agent = AGENT_REGISTRY[agent_name]

    # Step 1: plan
    operations = agent.plan(payload)

    # Step 2: transact
    result = execute_transaction(operations)

    return {
        "agent": agent_name,
        "operations": operations,
        "result": result
    }
