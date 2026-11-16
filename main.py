"""Entry program for make.fun ai-excited-01: "Shark in the Mirror".

Copies the image entry.png sitting next to this file into the output
directory given by MAKEFUN_OUTPUT_DIR (default /output), as entry.png.
Standard library only. Deterministic: the output bytes are identical
to the source bytes on every run.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
