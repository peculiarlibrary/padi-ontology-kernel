next_id() {
  if [ ! -f registry.json ]; then
    echo "PC-0001"
    return
  fi

  LAST=$(grep -o '"PC-[0-9]*"' registry.json | tail -1 | tr -d '"')

  if [ -z "$LAST" ]; then
    echo "PC-0001"
    return
  fi

  NUM=${LAST#PC-}
  NUM=$((10#$NUM + 1))
  printf "PC-%04d" "$NUM"
}
