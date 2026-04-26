import os
import sys
# Path injection
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Auditor:
    def __init__(self):
        self.role = "Auditor"
        self.base_dir = os.getcwd()
        self.data_dir = os.path.join(self.base_dir, "data")
        # Files that are part of the system, not the research data
        self.exempt_files = ["graph.ttl", "knowledge_seed_01.rdf"]

    def verify_integrity(self):
        print(f"[{self.role}] Performing smart integrity audit on repository...")
        
        if not os.path.exists(self.data_dir):
            print(f"[{self.role}] No data directory found. Skipping.")
            sys.exit(0)

        files = [f for f in os.listdir(self.data_dir) if f.endswith(".ttl")]
        
        for filename in files:
            # SKIP infrastructure files
            if filename in self.exempt_files:
                print(f"[{self.role}] Skipping infrastructure file: {filename}")
                continue

            file_path = os.path.join(self.data_dir, filename)
            with open(file_path, 'r') as f:
                content = f.read()
                # Check for DOI markers
                if "padi:hasDOI" not in content and "zenodo" not in content.lower():
                    print(f"[{self.role}] CRITICAL COMPLIANCE FAILURE: {filename} lacks a DOI.")
                    sys.exit(1)
        
        print(f"[{self.role}] Audit Complete: Repository is compliant.")
        sys.exit(0)

if __name__ == "__main__":
    Auditor().verify_integrity()
