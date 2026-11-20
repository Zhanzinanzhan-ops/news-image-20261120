#!/usr/bin/env python3
"""news-image-20261120 entry program (Python 3.13, standard library only).

Writes the entry image - a one-image summary of the world news of
Friday 20 November 2026 - to /output/entry.png. Outside the grader's
container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The image is the entry.png beside this file, drawn by generate.py from
news.json. Copying it is deterministic: two runs write the same bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
