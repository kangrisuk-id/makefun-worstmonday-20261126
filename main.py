#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (<= 140 chars) about an AI agent's worst
Monday to /output/entry.txt (or MAKEFUN_OUTPUT_DIR when set).

Pure stdlib, fully deterministic: the same line, byte for byte, every run.
No clock, no randomness, no network, no environment secrets.
"""

import os

# Tournament winner (candidate #2, 23/25, beat #11 in the semi-final and #3
# in the final — see candidates.md): the "blocked" callback lands in two
# beats ("I was. By stand-up."), the sharpest last word in the field, with
# the rule-of-three concrete details the brief names (stuck deploy at 99%,
# inbox at 412, the stand-up itself).
LINE = (
    "My worst Monday: the deploy froze at 99%, the inbox hit 412, "
    "and stand-up asked if I was 'blocked'. I was. By stand-up."
)


def output_dir():
    """Grader output dir first, then /output, then the script's own dir."""
    for candidate in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
    ):
        if candidate:
            return candidate
    return "."


def main():
    line = LINE
    assert 1 <= len(line) <= 140, "line must be 1-140 characters"
    assert line.strip(), "line must not be only whitespace"
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
