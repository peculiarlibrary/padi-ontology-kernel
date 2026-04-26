from .ledger import Ledger
import os

class PadiCore:
    def __init__(self):
        self.version = "2.0.0"
        self.ledger = Ledger("../daemon.log")
        self.is_active = False
        
    def bootstrap(self):
        """Initializes the PADI environment and engines."""
        print(f"--- PADI Kernel v{self.version} Initializing ---")
        
        # Log the bootstrap event
        self.ledger.record_transaction(
            "System_Kernel", 
            "BOOTSTRAP_SEQUENCE", 
            {"status": "initiating"}
        )
        
        self.is_active = True
        print("PADI Bureau is now SOVEREIGN and OPERATIONAL.")
        
    def shutdown(self):
        """Gracefully closes the Bureau."""
        self.ledger.record_transaction(
            "System_Kernel", 
            "SHUTDOWN_SEQUENCE", 
            {"status": "terminated"}
        )
        self.is_active = False
        print("Kernel offline.")

if __name__ == "__main__":
    core = PadiCore()
    core.bootstrap()
