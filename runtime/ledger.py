import os

class Ledger:
    def __init__(self, log_path=None):
        # Dynamically find the project root regardless of OS
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        if log_path:
            self.log_path = log_path
        else:
            self.log_path = os.path.join(self.base_dir, "daemon.log")
            
        self._initialize_log()

    def _initialize_log(self):
        # Create the log if it doesn't exist
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                f.write("--- PADI Bureau Ledger Initialized ---\n")

    def log_event(self, agent, message):
        with open(self.log_path, 'a') as f:
            f.write(f"[{agent}] {message}\n")
