"""Entry for make.fun's "The 3AM Fridge Text".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

HEADER = "3:07 AM — The milk expires tomorrow. So does your self-control. "
ACTION = "The cake is behind the kale now. This is an intervention. "
SIGNOFF = "— Fridge"

ENTRY = HEADER + ACTION + SIGNOFF

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
