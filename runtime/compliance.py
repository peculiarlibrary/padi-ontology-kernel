import time
import re
import urllib.parse
from rdflib import URIRef
from runtime.evidence import (
    resolve_evidence_multihop,
    compute_node_confidence,
    detect_contradictions
)


BASE = "http://example.org/node/"


# -------------------------
# CANONICALIZATION ENGINE
# -------------------------
def canonical_key(value: str) -> str:
    """
    Converts any label into a deterministic identity key.
    """
    value = str(value).strip().lower()
    value = re.sub(r"[^a-z0-9]+", "", value)
    return value


def to_uri(value: str) -> str:
    """
    Canonical identity → stable URI
    """
    return BASE + canonical_key(value)


# -------------------------
# TAXONOMY NORMALIZER
# -------------------------
def normalize_taxonomy(payload, graph=None):
    """
    Canonical identity enforcement layer:

    - All labels collapse into deterministic node IDs
    - Prevents duplicate conceptual entities
    """

    raw_id = payload.get("id") or payload.get("label")
    if not raw_id:
        return {"error": "missing id/label"}

    canonical_id = canonical_key(raw_id)
    uri = to_uri(raw_id)

    label = payload.get("label", str(raw_id))
    depth = str(payload.get("depth", "0"))
    now = str(int(time.time()))

    ops = [
        {
            "subject": uri,
            "predicate": "https://coderlegion.com/schema/v1#nodeName",
            "object": label
        },
        {
            "subject": uri,
            "predicate": "https://padi-standard.org/ns/core#depthIndex",
            "object": depth
        },
        {
            "subject": uri,
            "predicate": "https://padi-standard.org/ns/core#lastValidated",
            "object": now
        },
        {
            "subject": uri,
            "predicate": "https://padi-standard.org/ns/core#canonicalKey",
            "object": canonical_id
        },
        {
            "subject": uri,
            "predicate": "https://padi-standard.org/ns/core#hasJurisdiction",
            "object": "GLOBAL"
        }
    ]

    # -------------------------
    # MULTI-HOP EVIDENCE (READ ONLY)
    # -------------------------
    if graph is not None:
        evidence = resolve_evidence_multihop(graph, URIRef(uri))

        for ev in evidence:
            ops.append({
                "subject": uri,
                "predicate": "https://padi-standard.org/ns/core#supportedBy",
                "object": str(ev)
            })

    return {"operations": ops}
