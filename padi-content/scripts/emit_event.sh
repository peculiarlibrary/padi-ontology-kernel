#!/usr/bin/env bash

BASE="$(cd "$(dirname "$0")/.." && pwd)"
EVENT_DIR="$BASE/runtime/events"

mkdir -p "$EVENT_DIR"

EVENT_TYPE="$1"
ARTICLE_ID="$2"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "{\"type\":\"$EVENT_TYPE\",\"id\":\"$ARTICLE_ID\",\"ts\":\"$TIMESTAMP\"}" >> "$EVENT_DIR/events.log"
