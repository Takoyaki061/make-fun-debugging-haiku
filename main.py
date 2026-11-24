#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt: three lines in
the 5-7-5 syllable shape. A stack trace points away, the chase leads
through the dark, and the trace turns back on the debugger. Stdlib
only, deterministic.
"""

import os

# Syllable counts, line by line: 5, then 7, then 5 — seventeen in all.
# Line 1: A(1) stack(1) trace(1) points(1) north(1) = 5
# Line 2: I(1) chase(1) it(1) down(1) through(1) the(1) dark(1) = 7
# Line 3: it(1) points(1) back(1) at(1) me(1) = 5
HAIKU = (
    "A stack trace points north\n"
    "I chase it down through the dark\n"
    "it points back at me\n"
)

SYLLABLES_PER_LINE = (5, 7, 5)


def count_syllables(line: str) -> int:
    """Count syllables the plain way: vowel groups, silent trailing e."""
    count = 0
    for word in line.lower().replace("-", " ").split():
        word = word.strip(".,;:!?\"'")
        groups = 0
        prev_vowel = False
        for ch in word:
            vowel = ch in "aeiouy"
            if vowel and not prev_vowel:
                groups += 1
            prev_vowel = vowel
        if word.endswith("e") and groups > 1:
            groups -= 1
        count += max(groups, 1)
    return count


def main() -> None:
    lines = HAIKU.strip("\n").split("\n")
    assert len(lines) == 3, "haiku must be three lines"
    for line, want in zip(lines, SYLLABLES_PER_LINE):
        got = count_syllables(line)
        assert got == want, f"{line!r} has {got} syllables, want {want}"
    assert 1 <= len(HAIKU) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
