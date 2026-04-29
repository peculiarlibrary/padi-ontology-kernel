# Copilot instructions for peculiarlibrary/padi-ontology-kernel

Purpose: Help Copilot sessions understand repository structure, common tasks, and how to run things reproducibly.

1) Build, test, and lint commands
- Environment setup (reproducible):
  - python -m venv .venv
  - .venv\Scripts\activate (Windows PowerShell) or source .venv/bin/activate (Unix)
  - pip install -r requirements.lock

- Bootstrap (project-wide setup):
  - On Unix/Git Bash: ./bootstrap.sh
  - On Windows (Git Bash/MINGW): ./bootstrap.sh

- Primary validator (single-run, preferred):
  - python runtime/graph_validator.py --data data/graph.ttl --shapes constraints/shapes.shacl

- Alternative SHACL checks (local environment):
  - Using the included script (reads files hardcoded in script):
    - python scripts/shacl_validate.py
    - python bureau-starter/scripts/validate.py

  - Programmatic one-liner (works anywhere with pyshacl installed):
    - Unix / Git Bash / PowerShell:
      python -c "from rdflib import Graph; from pyshacl import validate; g=Graph(); g.parse('data/graph.ttl', format='turtle'); s=Graph(); s.parse('constraints/shapes.shacl', format='turtle'); conforms, report_graph, report_text = validate(g, shacl_graph=s, inference='rdfs'); print('CONFORMS:', conforms); print(report_text)"

- Run a single agent (examples used by CI):
  - python agents/cataloger.py
  - python agents/auditor.py

- Tests & linting:
  - No repository-wide test runner or linter config detected. CI runs CodeQL and the agent scripts. Consider adding pytest / pre-commit if you want enforced local checks.

2) High-level architecture (big picture)
- Kernel core: deterministic knowledge graph + enforcement pipeline. Ontologies (ontology/) define types/axioms; constraints/ define SHACL shapes and rule JSON used by validators.
- Runtime: runtime/ implements ledgering, mutation and governance enforcement. Ledger writes are pre-validated.
- Agents: agents/ contain autonomous scripts (cataloger, auditor, etc.) that operate on the repo and data; GitHub Actions invoke them with PYTHONPATH set to repo root.
- Manifest-driven workflow: manifest.json is authoritative for release assets; the cataloger agent updates this manifest in CI and commits changes back when needed.

3) Key conventions specific to this repo
- Single canonical state: data/graph.ttl is the accepted local snapshot many tools expect.
- Validation-first governance: SHACL checks (constraints/shapes.shacl and padi_core_shapes.ttl) must pass before ledger writes or manifest changes are accepted.
- PYTHONPATH: agents and CI run with the repo root on PYTHONPATH. Example: export PYTHONPATH=$PYTHONPATH:$(pwd) (Unix/Git Bash) or set PYTHONPATH=%PYTHONPATH%;%CD% (PowerShell/CMD variant).
- Python runtime: CI targets Python 3.11; use that interpreter for reproducible results.
- Manifest signing and release: manifest.json should be signed (manifest.sig) and accompanied by a public key published by maintainers. The signature must be verified before release.

4) SHACL validation – exact local commands
- Preferred (runtime helper):
  - python runtime/graph_validator.py --data data/graph.ttl --shapes constraints/shapes.shacl

- Using the project scripts (if you prefer the script behaviour):
  - python scripts/shacl_validate.py
  - python bureau-starter/scripts/validate.py

- Direct pyshacl (one-liner, copies report to stdout):
  - python -c "from rdflib import Graph; from pyshacl import validate; g=Graph(); g.parse('data/graph.ttl', format='turtle'); s=Graph(); s.parse('constraints/shapes.shacl', format='turtle'); conforms, report_graph, report_text = validate(g, shacl_graph=s, inference='rdfs'); print(report_text); exit(0 if conforms else 2)"

- Exit codes and CI hooks:
  - The direct one-liner exits with code 0 on success (conforms) and 2 on failure — useful for scripts. The runtime validator mirrors this behaviour for CI.

5) Release verification – verifying manifest.sig and asset hashes (exact commands)
- Overview: Before publishing a release (or accepting a manifest), verify the manifest signature and then verify each asset's SHA-256 matches the manifest entries.

- Step A: Obtain/locate the maintainer's public key
  - Expected filename (example): librarian_public.pem or librarian_public.gpg
  - If provided as a file, place it outside .gitignored secrets area and reference its path.

- Step B: Verify detached OpenSSL PEM signature (common pattern)
  - If manifest.sig is a raw binary signature created with OpenSSL (RSA/ECDSA):
    - openssl dgst -sha256 -verify librarian_public.pem -signature manifest.sig manifest.json
  - If manifest.sig is base64-encoded first (common in some workflows):
    - openssl base64 -d -in manifest.sig -out manifest.sig.bin
    - openssl dgst -sha256 -verify librarian_public.pem -signature manifest.sig.bin manifest.json

- Step C: Verify GPG detached signature (alternative):
  - Import public key (if not already available):
    - gpg --import librarian_public.gpg
  - Verify:
    - gpg --verify manifest.sig manifest.json

- Step D: Verify SHA-256 of each asset listed in manifest.json
  - Unix (sha256sum):
    - sha256sum -c <(jq -r '.assets[] | "\(.path) \(.sha256)"' manifest.json | sed 's/ /  /')  # optional helper combining jq + sha256sum
    - Or per-file: sha256sum data/graph.ttl

  - PowerShell (Windows):
    - Get-FileHash -Algorithm SHA256 .\data\graph.ttl | Format-List

  - Recommended workflow (safe, step-by-step):
    1. Verify signature: openssl dgst -sha256 -verify librarian_public.pem -signature manifest.sig manifest.json
    2. For each asset in manifest.json run: sha256sum <path>  (or Get-FileHash on Windows) and compare to manifest entry

- Note: If you lack the public key, obtain it from the project maintainers or release metadata. Never accept unsigned manifests for a release.

6) Quick references
- runtime/graph_validator.py — run this first for validation
- scripts/shacl_validate.py and bureau-starter/scripts/validate.py — examples using pyshacl
- agents/cataloger.py — manifest updates in CI
- agents/auditor.py — auditing checks used in CI

If you want, expand this file to include example PowerShell one-liners for Windows users, or add a small verification script to the repo that automates signature + hash checks. Say which and it will be added.
