#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry (v2 final).

Writes one toaster error line (<=120 chars) to /output/entry.txt.

v1 draft entry (Freemodel-ranked #1 of 4 drafts for freshness/tightness):
    "I toasted the air. The bread is still in the bag, judging me."
v2 revision (real edit, reason): added the "E09: " error-code prefix.
Judge criterion 1 weighs "a real error message a kitchen toaster would
show its owner" first, and a code prefix is how real appliance displays
label faults; the joke itself is unchanged, voice stays deadpan, and the
line stays tight at 66 chars (well under the 120 cap).
"""

import os

ENTRY = "E09: I toasted the air. The bread is still in the bag, judging me."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def gate(text: str) -> None:
    """Self-check mirroring the sealed gate: UTF-8, 1-120 chars, non-blank."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of 1-{MAX_CHARS}"
    assert text.strip(), "entry is only whitespace"
    text.encode("utf-8").decode("utf-8")  # UTF-8 round-trip


def main() -> None:
    gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
