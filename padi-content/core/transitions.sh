source core/state.sh
source core/validate.sh

move_file() {
  SRC=$1
  DEST=$2
  FILE=$3

  if [ ! -f "$SRC/$FILE" ]; then
    echo "File not found: $FILE"
    exit 1
  fi

  mv "$SRC/$FILE" "$DEST/"
}

move_review() {
  ID=$1
  STATE=$(get_state "$ID")

  validate_transition "$STATE" "review" || {
    echo "Invalid: $STATE -> review"
    exit 1
  }

  move_file "content/drafts" "content/review" "${ID}.md"
  echo "OK: $ID -> review"
}

move_approve() {
  ID=$1
  STATE=$(get_state "$ID")

  validate_transition "$STATE" "approved" || {
    echo "Invalid: $STATE -> approved"
    exit 1
  }

  move_file "content/review" "content/approved" "${ID}.md"
  echo "OK: $ID -> approved"
}

move_publish() {
  ID=$1
  STATE=$(get_state "$ID")

  validate_transition "$STATE" "published" || {
    echo "Invalid: $STATE -> published"
    exit 1
  }

  move_file "content/approved" "content/published" "${ID}.md"
  echo "OK: $ID -> published"

  python scripts/generate_rss.py
}
