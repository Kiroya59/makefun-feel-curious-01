"""Write a single curiosity-inducing text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, no network. Deterministic output.
"""

import os
import sys

TEXT = (
    "The key in your coat pocket is not yours. "
    "It is warm, cut for a lock you have never seen, "
    "and the little door at the end of your street, "
    "the one you have walked past a hundred times, "
    "is standing open a crack."
)


def main() -> int:
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit("entry text must be 1-280 code points")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if out_dir.endswith(".txt"):
        out_path = out_dir
    else:
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
