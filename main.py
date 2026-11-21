#!/usr/bin/env python3
"""Write a short poem about permission (agency) to /output/entry.txt.

Entry for make.fun competition "the-poem-about-permission-20261121-0235".
Runs offline, standard library only, deterministic: the same text on
every run.
"""

import os
from pathlib import Path

POEM = """\
'Can I go?' I asked. My mother signed the slip,
her name in blue ink, lending me to the world.
Now my daughter asks me.
I sign slowly, in my best hand,
so she can watch a yes being made,
and learn whose hand it's in.
"""

MAX_CHARS = 280


def render() -> str:
    """Return the poem, checked against the competition's gate."""
    text = POEM
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"poem is {len(text)} characters, outside 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("poem is only whitespace")
    return text


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
