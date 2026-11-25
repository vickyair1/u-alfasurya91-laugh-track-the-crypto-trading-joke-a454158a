#!/usr/bin/env python3
"""Write the one-line crypto-trading joke to /output/entry.txt.

The entry is a single joke about crypto and trading life, under 200
characters. It works by a category pivot: the setup states the trader's
paper position in the market's own language ("unrealized" losses), and
the punchline lands the bill the market cannot paper over — the rent,
which is "very realized". Every trader knows unrealized losses; every
trader also knows rent does not care about the chart. The sigh in the
middle ("unfortunately") is the voice of someone saying it to a friend,
which is exactly how the line is meant to travel.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-200 characters, not only
whitespace, a single line) before it is written.
"""

import os

# Parts of the line: the setup names the paper position, the punchline
# turns the same accounting word against the trader's real-world bill.
SETUP = "My losses are unrealized."
PUNCHLINE = "My rent, unfortunately, is very realized."

LINE = SETUP + " " + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Read back and confirm the written bytes are exactly the validated
    # line: the gate scores the file on disk, not the string in memory.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise SystemExit("entry.txt on disk differs from the validated line")


if __name__ == "__main__":
    main()
