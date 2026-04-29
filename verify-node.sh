#!/bin/bash
# PADI Node Integrity Verifier v1.0
MANIFEST=$1
SIGNATURE=$2

if [ ! -f "$MANIFEST" ]; then
    echo "Error: Manifest file not found."
    exit 1
fi

echo "Verifying $MANIFEST against $SIGNATURE..."
# Currently verifying the GPG envelope
gpg --verify "$SIGNATURE" "$MANIFEST"
if [ $? -eq 0 ]; then
    echo "Manifest Integrity Verified."
    exit 0
else
    echo "CRITICAL: Manifest Signature Invalid!"
    exit 1
fi
