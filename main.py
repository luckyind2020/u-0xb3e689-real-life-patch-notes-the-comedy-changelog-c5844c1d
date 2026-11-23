"""Print the one-line real-life patch note entered for the make.fun bounty."""

from pathlib import Path


def load_note() -> str:
    note_path = Path(__file__).resolve().parent / "entry.txt"
    lines = note_path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            return cleaned
    return ""


def main() -> None:
    print(load_note())


if __name__ == "__main__":
    main()
