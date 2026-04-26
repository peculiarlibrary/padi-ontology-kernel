import time
import subprocess
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# -----------------------------
# ABSOLUTE WINDOWS-SAFE PATH
# -----------------------------
BASE = Path(__file__).resolve().parents[1]
ARTIFACTS = BASE / "artifacts"
RSS_SCRIPT = BASE / "scripts" / "generate_rss.sh"

# ensure directory exists BEFORE watchdog starts
ARTIFACTS.mkdir(parents=True, exist_ok=True)


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith("meta.json"):
            self.regenerate()

    def regenerate(self):
        print("[watcher] change detected → regenerating RSS")
        subprocess.run(["bash", str(RSS_SCRIPT)], cwd=str(BASE))


if __name__ == "__main__":
    print(f"[watcher] watching: {ARTIFACTS}")

    event_handler = Handler()
    observer = Observer()

    observer.schedule(event_handler, str(ARTIFACTS), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
