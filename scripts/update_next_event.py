"""Write the next upcoming GroningenPHP Meetup event to public/next-event.txt.

Reads the event data Meetup embeds in its events page (the __NEXT_DATA__ JSON),
picks the first upcoming event and writes it in the format public/js/script.js
expects. Uses only the Python standard library.

If the next event is the one already in the file, the existing description is
kept, so a description someone shortened by hand is not overwritten.
"""

import html
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

EVENTS_URL = "https://www.meetup.com/groningenphp/events/"
EVENT_LINK = "https://www.meetup.com/groningenphp/events/{id}/"
OUTPUT = Path(sys.argv[1] if len(sys.argv) > 1 else "public/next-event.txt")
MAX_DESC_CHARS = 200

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def fetch_events():
    req = urllib.request.Request(EVENTS_URL, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        page = resp.read().decode("utf-8")

    match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', page, re.S)
    if not match:
        sys.exit("Could not find __NEXT_DATA__ on the Meetup page; the page layout may have changed.")
    state = json.loads(match.group(1))["props"]["pageProps"]["__APOLLO_STATE__"]
    events = [v for k, v in state.items() if k.startswith("Event:")]
    return events, state


def clean_description(markdown):
    """Turn Meetup's Markdown into short plain text that fits the event card."""
    lines = []
    for line in markdown.replace("\r", "").split("\n"):
        line = line.strip()
        if line.startswith("```"):
            continue
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)   # [text](url) -> text
        line = re.sub(r"^#+\s*", "", line)                      # headings (would clash with the file's "# " markers)
        line = re.sub(r"^[*\-+]\s+", "", line)                  # list bullets
        line = line.replace("**", "").replace("__", "")         # bold
        line = re.sub(r"(?<!\w)[*_](\S.*?\S|\S)[*_](?!\w)", r"\1", line)  # italics
        line = re.sub(r"\\(.)", r"\1", line)                    # escaped characters like \~
        line = html.unescape(line).strip()
        if not re.search(r"\w", line):                          # skip lines of only dots, ***, emoji etc.
            continue
        lines.append(line)

    text = "\n".join(lines)
    if len(text) > MAX_DESC_CHARS:
        cut = text[:MAX_DESC_CHARS]
        cut = cut[:cut.rfind(" ")] if " " in cut else cut       # don't cut a word in half
        text = cut.rstrip(" ,.;:\n") + "..."
    return text


def read_existing(path):
    """Parse the current file the same way script.js does."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")

    def section(pattern):
        m = re.search(pattern, text)
        return m.group(1).strip() if m else ""

    return {
        "desc": section(r"# Description\s*([\s\S]*?)# Location"),
        "link": section(r"# Link\s*([\s\S]*)"),
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")   # emoji in titles
    events, state = fetch_events()
    now = datetime.now(timezone.utc)
    upcoming = [
        e for e in events
        if e.get("status") == "ACTIVE" and datetime.fromisoformat(e["dateTime"]) > now
    ]
    if not upcoming:
        print("No upcoming event found on Meetup; leaving the file unchanged.")
        return

    event = min(upcoming, key=lambda e: datetime.fromisoformat(e["dateTime"]))
    start = datetime.fromisoformat(event["dateTime"])   # keeps Meetup's local (Dutch) time zone
    date = f"{MONTHS[start.month - 1]} {start.day}, {start.year}"   # e.g. "December 3, 2026"
    link = EVENT_LINK.format(id=event["id"])

    venue = state.get((event.get("venue") or {}).get("__ref", ""), {})
    location = venue.get("name") or ("Online" if event.get("isOnline") else "TBA")

    existing = read_existing(OUTPUT)
    if existing.get("link") == link and existing.get("desc"):
        description = existing["desc"]
    else:
        description = clean_description(event.get("description") or "")

    content = (
        f"# Date:\n{date}\n"
        f"# Title\n{event['title'].strip()}\n"
        f"# Description\n{description}\n"
        f"# Location\n{location}\n"
        f"# Link\n{link}\n"
    )
    OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(content)


if __name__ == "__main__":
    main()
