import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import re

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 3


def solve_a(input: str) -> int | str | None:
    pattern = r"mul\((\d*),(\d*)\)"
    matches = re.findall(pattern, input)
    total = 0
    for m in matches:
        total += int(m[0]) * int(m[1])
    return total


def solve_b(input: str) -> int | str | None:
    pattern = r"do\(\)|don't\(\)|mul\(\d*,\d*\)"
    matches = re.findall(pattern, input)
    total = 0
    include = True
    for m in matches:
        if m == "do()":
            include = True
        elif m == "don't()":
            include = False
        elif include:
            m: str = m
            m = m.strip("mul()")
            m.strip(")")
            n = m.split(",")
            total += int(n[0]) * int(n[1])
    return total


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
