from runtime.ledger import Ledger
from runtime.executor import Executor
import time

class HeadLibrarian:
    def __init__(self):
        self.persona = "Head Librarian"
        self.ledger = Ledger("../daemon.log")
        self.executor = Executor()
        self.active_agents = {}

    def deploy_foreman(self):
        """Commands the Executor to spawn the Foreman agent."""
        print(f"[{self.persona}] Deploying the Foreman for structural maintenance...")
        
        # Point to the foreman script relative to the execution context
        pid = self.executor.spawn_agent("Foreman", "agents/foreman.py")
        
        if pid:
            self.active_agents["Foreman"] = pid
            self.ledger.record_transaction(
                self.persona, 
                "SPAWN_AGENT", 
                {"agent": "Foreman", "pid": pid, "status": "active"}
            )
            print(f"[{self.persona}] Foreman is live (PID: {pid}).")
        return pid

    def get_status(self):
        """The 'Head Librarian' view of the entire Bureau."""
        history = self.ledger.get_history()
        return f"Bureau Status: {len(history)} records. Active Agents: {list(self.active_agents.keys())}"

if __name__ == "__main__":
    librarian = HeadLibrarian()
    librarian.deploy_foreman()
    print(librarian.get_status())
