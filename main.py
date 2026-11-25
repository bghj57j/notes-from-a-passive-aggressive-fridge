"""Write the passive-aggressive fridge note to /output/entry.txt.

One line, deterministic, no network: the same bytes on every run.
The fridge has been watching the leftovers age, and it kept score.
A small domestic grudge, not a rant: the leftovers got a birthday.
"""
import os

NOTE = "Your leftovers turned six today. I bought them a candle. You are not invited."


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NOTE)  # 80 chars, gate allows 200; the sting lands last


if __name__ == "__main__":
    main()
