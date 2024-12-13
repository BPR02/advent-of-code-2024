import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2023
DAY = 1


def solve_a(input: str) -> str | None:
    total = 0
    lines = input.splitlines()
    for line in lines:
        d1 = None
        d2 = None
        for i in range(len(line)):
            if d1 is None and line[i].isdigit():
                d1 = line[i]
            if d2 is None and line[-i - 1].isdigit():
                d2 = line[-i - 1]
            if d1 is not None and d2 is not None:
                break
        total += int(f"{d1}{d2}")
    return f"{total}"


digits = [
    ("0", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("zero", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]


def solve_b(input: str) -> str | None:
    total = 0
    lines = input.splitlines()
    for line in lines:
        d1 = None
        d2 = None
        first = len(line)
        last = -1
        # find all digits
        for i in range(len(line)):
            for digit in digits:
                pos = line.find(digit[0], i)
                if pos == -1:
                    continue
                if pos < first:
                    first = pos
                    d1 = digit[1]
                if pos > last:
                    last = pos
                    d2 = digit[1]
        total += int(f"{d1}{d2}")
    return f"{total}"


if __name__ == "__main__":
    run(YEAR, DAY, solve_a, solve_b)
