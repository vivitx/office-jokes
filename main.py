"""Copy the committed entry.txt to the output directory.

Reads entry.txt next to this script, validates it, and writes it unchanged
to MAKEFUN_OUTPUT_DIR (or /output). Python 3.13, stdlib only, no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_entry() -> str:
    """Read entry.txt as UTF-8 and validate it."""
    raw = (HERE / "entry.txt").read_bytes()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not UTF-8
    if not 1 <= len(text) <= 199:
        raise ValueError(f"entry.txt must be 1-199 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry.txt must not be whitespace-only")
    print(f"entry.txt: {len(text)} characters")
    return text


def main() -> None:
    read_entry()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.txt", out_dir / "entry.txt")


if __name__ == "__main__":
    main()
