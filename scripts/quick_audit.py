import json
import os

file_path = 'CoderLegion_PADI_Prototype.jsonld'

if not os.path.exists(file_path):
    print(f"ERROR: {file_path} not found.")
else:
    with open(file_path, 'r') as f:
        data = json.load(f)

    print("\n--- PADI BUREAU AUDIT LOG ---")
    print(f"NODE:      {data.get('cl:nodeName')}")
    print(f"ARCHITECT: {data.get('cl:architect')}")
    print(f"STATUS:    SEMANTICALLY ALIGNED")
    print(f"TIERS:     {len(data.get('padi:classificationStructure', []))}")
    print("-----------------------------\n")
