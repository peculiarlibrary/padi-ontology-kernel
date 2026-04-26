import os
import sys
# Path injection
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Auditor:
    def __init__(self):
        self.role = "Auditor"
        self.base_dir = os.getcwd() # Use current directory for CI context
        self.data_dir = os.path.join(self.base_dir, "data")

    def verify_integrity(self):
        print(f"[{self.role}] Performing smart integrity audit on repository...")
        
        # In CI, we check the physical files in /data instead of the ledger
        files = [f for f in os.listdir(self.data_dir) if f.endswith(".ttl")]
        
        for filename in files:
            file_path = os.path.join(self.data_dir, filename)
            with open(file_path, 'r') as f:
                content = f.read()
                if "padi:hasDOI" not in content and "zenodo" not in content.lower():
                    print(f"[{self.role}] CRITICAL COMPLIANCE FAILURE: {filename} lacks a DOI.")
                    sys.exit(1) # This stops the GitHub Action
        
        print(f"[{self.role}] Audit Complete: Repository is compliant.")
        sys.exit(0)

if __name__ == "__main__":
    Auditor().verify_integrity()
