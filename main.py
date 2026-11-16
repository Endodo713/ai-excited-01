"""Copy the entry image to the output directory.

The entry is a single image, entry.png, held in this repository next to
this program. This program copies its bytes exactly to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output when the variable is unset),
creating the output directory if needed. Standard library only, no network,
no randomness: two runs write identical bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
