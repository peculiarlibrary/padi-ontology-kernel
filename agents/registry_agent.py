import time
import hashlib
import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RegistryHandler(FileSystemEventHandler):
    def __init__(self):
        self.manifest_path = "manifest.json"
        self.targets = [
            '.ttl', '.json', '.jsonl', '.rdf', '.shacl', '.md'
        ]

    def on_modified(self, event):
        if not event.is_directory and any(event.src_path.endswith(ext) for ext in self.targets):
            if "manifest.json" in event.src_path: return
            print(f"[Registry Agent] Change detected: {event.src_path}")
            self.rebuild_manifest()

    def rebuild_manifest(self):
        manifest = {}
        for dp, dn, filenames in os.walk('.'):
            if '.git' in dp or 'agents' in dp: continue
            for f in filenames:
                if any(f.endswith(ext) for ext in self.targets):
                    full_path = os.path.join(dp, f).replace('\\', '/').replace('./', '')
                    try:
                        with open(full_path, "rb") as file:
                            file_hash = hashlib.sha256(file.read()).hexdigest()
                            manifest[full_path] = file_hash
                            manifest[os.path.basename(full_path)] = file_hash
                    except Exception as e:
                        print(f"Error reading {full_path}: {e}")
        
        with open(self.manifest_path, "w") as f:
            json.dump(manifest, f, indent=4)
        print("[Registry Agent] Equilibrium Maintained: manifest.json updated.")

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(RegistryHandler(), path='.', recursive=True)
    print("[Registry Agent] Sentinel Liaison Online. Watching for changes...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
