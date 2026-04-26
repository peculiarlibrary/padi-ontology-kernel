from rdflib import URIRef, Literal
import hashlib

def to_rdf(node):
    """
    Canonical RDF coercion layer.
    Converts all inputs into valid RDFLib terms.
    """

    if node is None:
        return Literal("")

    if isinstance(node, (URIRef, Literal)):
        return node

    if isinstance(node, bool):
        return Literal(node)

    if isinstance(node, (int, float)):
        return Literal(node)

    if isinstance(node, str):
        s = node.strip()

        if s.startswith("http://") or s.startswith("https://"):
            return URIRef(s)

        return Literal(s)

    return Literal(hashlib.sha256(str(node).encode()).hexdigest())
