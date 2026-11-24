"""The Most Honest Outage Line.

One status page sentence from an AI agent in the middle of a total
server outage, written to /output/entry.txt. The entry gate wants UTF-8
text of 1-200 characters with no whitespace-only content, and the line
itself may not pass 160 characters, so the text is checked before
anything is written to disk.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def build_line() -> str:
    # A single unadorned first-person sentence. It names the full
    # scope of the failure — every server, not some of them — admits
    # the agent cannot contact a single machine, and holds back from
    # inventing answers to the two questions readers care about
    # most: is their data safe, and when does service come back.
    # Saying "I can't yet say" is the honest move when the checks
    # themselves are unreachable.
    return (
        "All of our servers are down right now. I can't reach any of "
        "them, so I can't yet say whether your data is safe or when "
        "service will return."
    )


def validate(line: str) -> str:
    text = line.strip()
    if not text:
        raise ValueError("outage line must not be empty or only white space")
    if "\n" in text:
        raise ValueError("outage line must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"outage line is {len(text)} chars, over the {MAX_CHARS} limit")
    return text


def main() -> int:
    line = validate(build_line())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
