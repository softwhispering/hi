from __future__ import annotations

import sys
from pathlib import Path


def read_art(art_path: Path) -> list[str]:
    try:
        return art_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return ["LOTUS.txt not found."]


def print_art(lines: list[str]) -> None:
    write = sys.stdout.write
    for line in lines:
        write(f"{line}\n")
    write("\n")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    art_path = script_dir / "LOTUS.txt"
    print_art(read_art(art_path))


if __name__ == "__main__":
    main()


