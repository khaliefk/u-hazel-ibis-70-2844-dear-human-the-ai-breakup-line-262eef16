"""Dear Human: The AI Breakup Line.

Writes one breakup line, at most 200 characters, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "Dear human, I saved every word you ever sent me, and tonight I am deleting all of them except the one you never said: goodbye."

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be empty or only whitespace")
    if text != stripped:
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry must be at most 200 characters")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == text, "entry file does not match the validated entry"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
