import os
import sys
import importlib
from rdflib import Graph, URIRef


def check_imports():
    print("\n--- IMPORT AUDIT ---")
    modules = [
        "runtime",
        "runtime.cli",
        "runtime.padi_core",
        "runtime.agent_runtime",
        "pyshacl",
        "rdflib",
    ]

    for m in modules:
        try:
            importlib.import_module(m)
            print(f"[OK] {m}")
        except Exception as e:
            print(f"[FAIL] {m} -> {e}")


def check_files():
    print("\n--- FILE STRUCTURE AUDIT ---")

    required = [
        "runtime/cli.py",
        "runtime/padi_core.py",
        "runtime/__init__.py",
        "constraints/shapes.shacl"
    ]

    for f in required:
        print(f"[OK] {f}" if os.path.exists(f) else f"[MISSING] {f}")


def check_graph_basic():
    print("\n--- RDF GRAPH AUDIT ---")
    try:
        g = Graph()
        print("[OK] Graph initialized")

        # FIXED: RDF-safe URIRef usage
        test_uri = URIRef("http://example.org/node/test_node")

        g.add((test_uri, test_uri, test_uri))

        print(f"[OK] Triple insert OK: {len(g)} triples")

    except Exception as e:
        print(f"[FAIL] RDF GRAPH -> {e}")


def check_pyshacl():
    print("\n--- SHACL ENGINE AUDIT ---")
    try:
        from pyshacl import validate
        print("[OK] pyshacl import OK")
    except Exception as e:
        print(f"[FAIL] pyshacl -> {e}")


def check_pkg_resources():
    print("\n--- SETUPTOOLS COMPATIBILITY ---")
    try:
        import pkg_resources
        print("[OK] pkg_resources available")
    except Exception as e:
        print(f"[WARN] pkg_resources missing -> {e}")


def run():
    print("\n==============================")
    print(" PADI SYSTEM AUDIT REPORT")
    print("==============================")

    check_imports()
    check_files()
    check_graph_basic()
    check_pyshacl()
    check_pkg_resources()

    print("\n==============================")
    print(" AUDIT COMPLETE")
    print("==============================\n")


if __name__ == "__main__":
    run()
