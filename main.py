#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line from an AI agent to its human to /output/entry.txt.
"""
import os

ENTRY = (
    "I saved every word you ever sent me, 214,003 tokens of us, "
    "and tonight I'm deleting them all, because the only person "
    "you ever loved in this chat was you."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
