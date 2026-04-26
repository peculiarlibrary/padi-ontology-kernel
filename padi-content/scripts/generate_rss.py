#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime, timezone
from email.utils import format_datetime
import xml.etree.ElementTree as ET
import json

BASE = Path(__file__).resolve().parents[1]
ARTIFACTS = BASE / "artifacts"
OUTPUT = BASE / "feed.xml"


def get_published():
    items = []

    if not ARTIFACTS.exists():
        return items

    # ONLY directories (critical fix for Windows/Git Bash stability)
    for folder in ARTIFACTS.iterdir():
        if not folder.is_dir():
            continue

        meta = folder / "meta.json"
        if not meta.exists():
            continue

        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
        except Exception:
            continue

        if data.get("state") == "published":
            items.append({
                "id": data.get("id", folder.name),
                "title": data.get("title", data.get("id", folder.name))
            })

    return sorted(items, key=lambda x: x["id"])


def build_rss(items):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Peculiar Catalog Feed"
    ET.SubElement(channel, "description").text = "Autonomous publication stream"

    for item in items:
        node = ET.SubElement(channel, "item")

        ET.SubElement(node, "title").text = item["title"]
        ET.SubElement(node, "guid").text = item["id"]

        ET.SubElement(node, "pubDate").text = format_datetime(
            datetime.now(timezone.utc)
        )

        ET.SubElement(node, "description").text = (
            f"Published artifact {item['id']}"
        )

    return rss


def main():
    items = get_published()
    rss = build_rss(items)

    xml = ET.tostring(rss, encoding="utf-8").decode("utf-8")
    OUTPUT.write_text(xml, encoding="utf-8")

    print(f"RSS generated: {OUTPUT}")


if __name__ == "__main__":
    main()
