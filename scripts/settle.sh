#!/bin/bash
# Robustly extract the latest depthIndex value regardless of JSON spacing
LATEST_DEPTH=$(grep -oP '"object":\s*"\K[^"]+' data/ledger.jsonl | grep -E "^[1-5]$" | tail -n 1)

if [ -z "$LATEST_DEPTH" ]; then
    echo "Warning: No valid Depth Index found in latest ledger entry."
else
    # Surgical update of the graph
    sed -i "s/ns1:depthIndex \".*\"/ns1:depthIndex \"$LATEST_DEPTH\"/" data/graph.ttl
    echo "Bureau Settled: Cognitive Systems updated to Level $LATEST_DEPTH"
fi
