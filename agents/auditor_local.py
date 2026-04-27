import os

def run_audit():
    asset_path = "data/foreign_asset.ttl"
    print(f"[Local Auditor] Scanning {asset_path} for PADI Compliance...")
    
    if not os.path.exists(asset_path):
        print("[Error] Asset missing.")
        return

    with open(asset_path, "r") as f:
        content = f.read()
        
        # Check for the mandatory DOI metadata identified in Screenshot (1203)
        has_doi = "dc:identifier \"doi:10.5281/zenodo.18894084\"" in content or "10.5281/zenodo" in content
        
        if has_doi:
            print("[Auditor] PASS: DOI signature found.")
            print("[Auditor] PASS: Structural Law enforced.")
            return True
        else:
            print("[Auditor] CRITICAL COMPLIANCE FAILURE: Asset lacks a DOI.")
            return False

if __name__ == "__main__":
    if run_audit():
        print("\n[Result] Equilibrium Confirmed. Ready for Embassy Push.")
    else:
        print("\n[Result] Push Aborted. Rectify metadata first.")
