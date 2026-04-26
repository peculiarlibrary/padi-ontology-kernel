import time
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EVENT_LOG = BASE / "runtime" / "events.log"
RSS_SCRIPT = BASE / "scripts" / "generate_rss.sh"

# Ensure required paths exist
EVENT_LOG.parent.mkdir(parents=True, exist_ok=True)
EVENT_LOG.touch()

def process_event(line: str):
    if "PUBLISH" in line:
        print("[event] publish detected → regenerating RSS")
        subprocess.run(["bash", str(RSS_SCRIPT)], cwd=str(BASE))

def tail_file(path):
    with open(path, "r") as f:
        f.seek(0, 2)  # start at end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()

if __name__ == "__main__":
    print(f"[event-watcher] listening on {EVENT_LOG}")
    for event in tail_file(EVENT_LOG):
        process_event(event)
