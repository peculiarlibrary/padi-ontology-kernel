from runtime.padi_core import create_kernel
from runtime.compliance import normalize_taxonomy


def run():
    kernel = create_kernel()

    payload = {
        "id": "CognitiveSystems",
        "label": "Cognitive Systems",
        "depth": "4"
    }

    normalized = normalize_taxonomy(payload, kernel.graph)

    result = kernel.apply_mutations(normalized["operations"])

    print("\n=== COMMIT RESULT ===")
    print(result)

    print("\n=== STATS ===")
    print(kernel.stats())

    print("\n=== SAMPLE QUERY ===")
    print(kernel.query("SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"))


if __name__ == "__main__":
    run()
