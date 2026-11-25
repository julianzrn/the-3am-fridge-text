"""Entry for make.fun competition: u-deysumbrella-the-3am-fridge-text-4c3e721d.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "3:07 AM — The milk expires tomorrow. So does your self-control. "
MIDDLE = "The cake is behind the kale now. This is an intervention. "
SIGNATURE = "— Fridge"

ENTRY = OPENING + MIDDLE + SIGNATURE


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
