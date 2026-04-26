def normalize_taxonomy(payload, graph):
    """
    Converts raw CLI payload into RDF-ready operations.
    """

    base = "http://example.org/node/"
    core = "https://padi-standard.org/ns/core#"

    node_id = payload.get("id")
    label = payload.get("label")
    depth = payload.get("depth")

    subject = base + node_id

    operations = [
        {
            "subject": subject,
            "predicate": core + "nodeName",
            "object": label
        },
        {
            "subject": subject,
            "predicate": core + "depthIndex",
            "object": depth
        },
        {
            "subject": subject,
            "predicate": core + "hasJurisdiction",
            "object": "GLOBAL"
        },
        {
            "subject": subject,
            "predicate": core + "lastValidated",
            "object": str(__import__("time").time())
        }
    ]

    return {
        "operations": operations
    }
