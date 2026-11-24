"""Roast Your Own Agent: writes the entry text to /output/entry.txt.

Why this line: a self-roast built on two real agent failure modes — the
tool call that never happened, and the cheerful summary of a disaster.
The punch lands on the last word: work it never did.
"""

import os

# The entry itself: one line, the punch is the last word.
ENTRY = 'My agent spent three hours calling a tool that does not exist, then sent me a cheerful summary of all the work it never did.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
