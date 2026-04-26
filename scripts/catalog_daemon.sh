#!/usr/bin/env bash

BASE="$(cd "$(dirname "$0")/.." && pwd)"
EVENTS="$BASE/runtime/events.log"

mkdir -p "$BASE/runtime"
touch "$EVENTS"

echo "[daemon] running..."

while true; do

  if [ -s "$EVENTS" ]; then

    while read -r line; do
      echo "[daemon] event: $line"
    done < "$EVENTS"

    > "$EVENTS"

    bash "$BASE/scripts/generate_rss.sh"

    echo "[daemon] RSS updated"
  fi

  sleep 2
done
