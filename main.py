"""One Star for Monday — make.fun entry.

Writes a single one-star review line to /output/entry.txt.
The line is the whole entry: a diner's complaint, no stage directions.
Standard library only, no network, deterministic.
"""

import os

LINE = "One star. Waited forty minutes for the coffee, got seated next to my own deadlines, and the waiter kept saying 'it's only Monday'."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
