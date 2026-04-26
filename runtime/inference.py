def run_inference(graph):
    """
    READ-ONLY inference engine
    """
    insights = []

    for s, p, o in graph:
        if "supportedBy" in str(p):
            insights.append({
                "subject": str(s),
                "type": "evidence_edge_detected"
            })

    return {
        "status": "READ_ONLY",
        "insights": insights
    }


# -----------------------------
# COMPATIBILITY LAYER (CRITICAL)
# -----------------------------
def enforce_rules(graph):
    """
    Backwards compatibility shim for padi_core.
    Maps old API → new inference model.
    """
    return run_inference(graph)
