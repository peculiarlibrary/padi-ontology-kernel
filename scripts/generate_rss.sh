#!/usr/bin/env bash

BASE="$(cd "$(dirname "$0")/.." && pwd)"
ARTIFACTS="$BASE/artifacts"
OUTPUT="$BASE/feed.xml"

echo '<rss version="2.0">' > "$OUTPUT"
echo '<channel>' >> "$OUTPUT"
echo '<title>Peculiar Catalog Feed</title>' >> "$OUTPUT"
echo '<description>Autonomous publication stream</description>' >> "$OUTPUT"

for dir in "$ARTIFACTS"/*; do
  [ -d "$dir" ] || continue

  META="$dir/meta.json"
  [ -f "$META" ] || continue

  STATE=$(grep '"state"' "$META" | cut -d '"' -f4)
  [ "$STATE" != "published" ] && continue

  ID=$(grep '"id"' "$META" | cut -d '"' -f4)
  TITLE=$(grep '"title"' "$META" | cut -d '"' -f4)

  [ -z "$TITLE" ] && TITLE="$ID"

  echo "<item>" >> "$OUTPUT"
  echo "<title>$TITLE</title>" >> "$OUTPUT"
  echo "<guid>$ID</guid>" >> "$OUTPUT"
  echo "<description>Auto-published via Catalog Daemon ($ID)</description>" >> "$OUTPUT"
  echo "</item>" >> "$OUTPUT"

done

echo '</channel>' >> "$OUTPUT"
echo '</rss>' >> "$OUTPUT"

echo "RSS generated: $OUTPUT"
