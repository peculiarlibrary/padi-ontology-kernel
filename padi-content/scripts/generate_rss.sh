#!/usr/bin/env bash

BASE="$(cd "$(dirname "$0")/.." && pwd)"
ARTIFACTS="$BASE/artifacts"
OUTPUT="$BASE/feed.xml"

echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" > "$OUTPUT"
echo "<rss version=\"2.0\"><channel>" >> "$OUTPUT"
echo "<title>Peculiar Catalog Feed</title>" >> "$OUTPUT"
echo "<description>Deterministic publication stream</description>" >> "$OUTPUT"

for dir in "$ARTIFACTS"/PC-*; do
  META="$dir/meta.json"

  [ ! -f "$META" ] && continue

  STATE=$(grep -o '"state":"[^"]*"' "$META" | cut -d':' -f2 | tr -d '"')

  if [ "$STATE" = "published" ]; then
    ID=$(grep -o '"id":"[^"]*"' "$META" | cut -d':' -f2 | tr -d '"')
    TITLE=$(grep -o '"title":"[^"]*"' "$META" | cut -d':' -f2 | tr -d '"')

    echo "<item>" >> "$OUTPUT"
    echo "<title>$TITLE</title>" >> "$OUTPUT"
    echo "<guid>$ID</guid>" >> "$OUTPUT"
    echo "<description>Published via Peculiar Catalog</description>" >> "$OUTPUT"
    echo "</item>" >> "$OUTPUT"
  fi
done

echo "</channel></rss>" >> "$OUTPUT"

echo "RSS generated: $OUTPUT"
