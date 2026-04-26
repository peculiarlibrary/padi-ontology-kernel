validate_transition() {
  FROM=$1
  TO=$2

  case "$FROM->$TO" in
    "draft->review") return 0 ;;
    "review->approved") return 0 ;;
    "approved->published") return 0 ;;
    "published->draft") return 0 ;;
    *) return 1 ;;
  esac
}
