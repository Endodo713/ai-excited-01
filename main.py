"""Shark in the Mirror — make.fun ai-excited-01 entry.

Copies the image entry.png next to this program into
$MAKEFUN_OUTPUT_DIR/entry.png. Python 3.13, standard library only.
Deterministic: both runs write identical bytes.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_of(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    size = os.path.getsize(dst)
    print(f"wrote {dst} ({size} bytes, sha256 {sha256_of(dst)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
