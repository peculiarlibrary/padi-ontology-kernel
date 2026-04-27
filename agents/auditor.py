import os
import sys
# Path injection
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Auditor:
    def __init__(self):
        self.role = "Auditor"
        self.base_dir = os.getcwd()
        self.data_dir = os.path.join(self.base_dir, "data")
        self.exempt_files = ["graph.ttl", "knowledge_seed_01.rdf"]
        self.MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB Security Limit

    def verify_integrity(self):
        print(f"[{self.role}] Performing smart integrity audit...")
        
        if not os.path.exists(self.data_dir):
            print(f"[{self.role}] No data directory found. Skipping.")
            sys.exit(0)

        files = [f for f in os.listdir(self.data_dir) if f.endswith(".ttl")]
        
        for filename in files:
            file_path = os.path.join(self.data_dir, filename)
            
            # SECURITY CHECK: File Size
            if os.path.getsize(file_path) > self.MAX_FILE_SIZE:
                print(f"[{self.role}] SECURITY ALERT: {filename} exceeds safety size limits.")
                sys.exit(1)

            # SKIP infrastructure files
            if filename in self.exempt_files:
                continue

            with open(file_path, 'r') as f:
                content = f.read()
                if "padi:hasDOI" not in content and "zenodo" not in content.lower():
                    print(f"[{self.role}] CRITICAL COMPLIANCE FAILURE: {filename} lacks a DOI.")
                    sys.exit(1)
        
        print(f"[{self.role}] Audit Complete: Repository is compliant and secure.")
        sys.exit(0)

if __name__ == "__main__":
    Auditor().verify_integrity()
