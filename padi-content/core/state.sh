get_state() {
  BASE="$(pwd)"
  ID=$1

  if ls content/drafts/${ID}* 1> /dev/null 2>&1; then echo "draft"; return; fi
  if ls content/review/${ID}* 1> /dev/null 2>&1; then echo "review"; return; fi
  if ls content/approved/${ID}* 1> /dev/null 2>&1; then echo "approved"; return; fi
  if ls content/published/${ID}* 1> /dev/null 2>&1; then echo "published"; return; fi

  echo "unknown"
}
