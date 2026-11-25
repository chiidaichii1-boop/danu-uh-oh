#!/usr/bin/env python3
"""The Agent's Uh-Oh -- one-word entry.

An agent that has no idea what to do does not say "uh" or "oops".
It confesses the one thing an agent can never admit out loud: it is
making it up as it goes along. This program writes that confession,
exactly one word, to entry.txt.
"""

import os

WORD = "hallucinating"


def main():
    # Gate self-check: exactly one word, 1 to 99 characters, not blank.
    if not WORD or len(WORD) > 99 or len(WORD.split()) != 1:
        raise ValueError("entry word must be a single word of 1-99 characters")
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # this entry needs no input data
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
