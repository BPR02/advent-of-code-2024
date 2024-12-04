import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import re

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 4


def solve_a(input: str) -> int | str | None:
    lines = input.splitlines()
    width = len(lines[-1])
    height = len(lines)
    total = 0
    for line in range(height):
        # horizontal
        total += len(re.findall("XMAS", lines[line]))
        total += len(re.findall("SAMX", lines[line]))
        if line + 3 < (height):
            for char in range(width):
                # vertical
                check = (
                    lines[line][char]
                    + lines[line + 1][char]
                    + lines[line + 2][char]
                    + lines[line + 3][char]
                )
                if check == "XMAS" or check == "SAMX":
                    total += 1
                # diagonal LR
                if char + 3 < width:
                    check = (
                        lines[line][char]
                        + lines[line + 1][char + 1]
                        + lines[line + 2][char + 2]
                        + lines[line + 3][char + 3]
                    )
                    if check == "XMAS" or check == "SAMX":
                        total += 1
                # diagonal RL
                if char - 3 > -1:
                    check = (
                        lines[line][char]
                        + lines[line + 1][char - 1]
                        + lines[line + 2][char - 2]
                        + lines[line + 3][char - 3]
                    )
                    if check == "XMAS" or check == "SAMX":
                        total += 1
    return total


def solve_b(input: str) -> int | str | None:
    lines = input.splitlines()
    width = len(lines[-1])
    height = len(lines)
    total = 0
    for line in range(1, height - 1):
        for char in range(1, width - 1):
            if lines[line][char] == "A":
                cross = 0
                if (
                    lines[line - 1][char - 1] == "M"
                    and lines[line + 1][char + 1] == "S"
                ):
                    cross += 1
                if (
                    lines[line + 1][char - 1] == "M"
                    and lines[line - 1][char + 1] == "S"
                ):
                    cross += 1
                if (
                    lines[line - 1][char - 1] == "S"
                    and lines[line + 1][char + 1] == "M"
                ):
                    cross += 1
                if (
                    lines[line + 1][char - 1] == "S"
                    and lines[line - 1][char + 1] == "M"
                ):
                    cross += 1
                if cross >= 2:
                    total += 1
    return total


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual)
