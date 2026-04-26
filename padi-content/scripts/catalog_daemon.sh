#!/usr/bin/env bash

BASE="$(cd "$(dirname "$0")/.." && pwd)"
EVENT_LOG="$BASE/runtime/events/events.log"

mkdir -p "$BASE/runtime/events"

echo "[daemon] started watching events..."

tail -Fn0 "$EVENT_LOG" | while read line; do
  echo "[daemon] event detected: $line"

  python "$BASE/scripts/generate_rss.py"

  echo "[daemon] RSS updated"
done
