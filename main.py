#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Line, One Laugh.

Writes one funny line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "I told my smart fridge I'm on a diet. It locked the door, "
    "took custody of the leftovers, and now I eat standing in "
    "the dark like a raccoon."
)
# Why this line: the setup is one familiar sentence everyone has said
# to a gadget, then the fridge escalates like a bitter ex -- locking
# the door, then taking legal custody of the leftovers -- and the
# punchline lands on the image of the human reduced to eating in the
# dark like a raccoon. The turn arrives inside the line, needs no
# setup from the reader, and the final image is easy to repeat.
# 139 characters: short, tight, and the joke is the escalation itself.


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"expected 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
