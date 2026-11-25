#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes exactly one line to /output/entry.txt: the commit message for
the worst fix ever — the bug was removed by deleting the feature, the
tests, and, for safety, the entire folder it lived in.

The line is fixed text: no network, no input, no randomness, so every
run produces the same 78-character file, byte for byte.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"

# The single line this entry delivers. Keep it on one line and do not
# edit the wording: the competition judges this exact text.
ENTRY = "fix: deleted the bug, the feature, and the folder it lived in, just to be safe"

# Conservative gate: one line, UTF-8, 1-140 characters, not whitespace-only.
# (The kit's exact per-competition limit is sealed; 140 sits under the
# smallest limit seen across this family of one-line competitions, 160.)
MAX_CHARS = 140


def write_entry() -> str:
    """Write the line to the output file and return its path."""
    if "\n" in ENTRY or "\r" in ENTRY or not ENTRY.strip():
        raise ValueError("ENTRY must be a single non-empty line")
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("ENTRY must be 1 to 140 characters")
    out_dir = os.environ.get("OUTPUT_DIR", OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and confirm the file holds exactly the entry text.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry does not match ENTRY")
    return path


def main() -> None:
    path = write_entry()
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
