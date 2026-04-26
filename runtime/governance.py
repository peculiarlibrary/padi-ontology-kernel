import json

def validate_event(event):
    """
    Pre-commit governance layer:
    Reject malformed or conflicting operations before ledger write.
    """

    if "ops" not in event:
        return False, "Missing ops field"

    for op in event["ops"]:
        required = ["subject", "predicate", "object"]

        for r in required:
            if r not in op:
                return False, f"Missing field: {r}"

    return True, "OK"
