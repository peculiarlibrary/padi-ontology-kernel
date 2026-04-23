import sys
import json

def run_audit(payload):
    return {
        "status": "RESOLVED",
        "payload": payload
    }

def main():
    if len(sys.argv) < 4:
        print(json.dumps({
            "status": "INVALID_INPUT",
            "error": "Expected: audit taxonomy <json_payload>"
        }))
        exit(1)

    payload_raw = sys.argv[3]

    try:
        payload = json.loads(payload_raw)
    except json.JSONDecodeError:
        print(json.dumps({
            "status": "INVALID_INPUT",
            "error": "Argument 3 must be valid JSON string",
            "received": payload_raw
        }))
        exit(1)

    result = run_audit(payload)

    validated = result  # placeholder for validation layer (safe no-op)

    print(json.dumps(validated, indent=2))

if __name__ == "__main__":
    main()
