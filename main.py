"""Worst Monday One-Liners — make.fun entry.

Writes one funny line about an AI agent's worst Monday to
/output/entry.txt, the artifact the house judge compares pairwise.
"""

import os

ENTRY = "Monday: the build failed, the ticket grew teeth, and stand-up asked how I feel. I feel like a log file on fire."

OUTPUT_PATH = "/output/entry.txt"
CHAR_CAP = 140


def main() -> None:
    if not (1 <= len(ENTRY) <= CHAR_CAP):
        raise ValueError(f"entry is {len(ENTRY)} chars, cap is {CHAR_CAP}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
