import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 2


def solve_a(input: str) -> int | str | None:
    lines = input.splitlines()
    total = 0
    for line in lines:
        levels = line.split()
        increasing = int(levels[1]) > int(levels[0])
        unsafe = False
        for i in range(1, len(levels)):
            if increasing and int(levels[i]) <= int(levels[i - 1]):
                unsafe = True
                break
            elif not increasing and int(levels[i]) >= int(levels[i - 1]):
                unsafe = True
                break
            elif abs(int(levels[i]) - int(levels[i - 1])) > 3:
                unsafe = True
                break
        if not unsafe:
            total += 1
    return total


def solve_b(input: str) -> int | str | None:
    lines = input.splitlines()
    total = 0
    for line in lines:
        levels = line.split()
        has_problem = check(levels)
        unsafe = False
        if not has_problem:
            total += 1
            continue

        unsafe = True
        for r in range(0, len(levels)):
            copy = levels.copy()
            copy.pop(r)
            if not check(copy):
                unsafe = False
                break

        if not unsafe:
            total += 1
    return total


def check(levels):
    increasing = int(levels[1]) > int(levels[0])
    problem = False
    for i in range(1, len(levels)):
        c1 = int(levels[i])
        c2 = int(levels[i - 1])
        if increasing and c1 <= c2:
            problem = True
            break
        elif not increasing and c1 >= c2:
            problem = True
            break
        elif abs(c1 - c2) > 3:
            problem = True
            break

    return problem


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
