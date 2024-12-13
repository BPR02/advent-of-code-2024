import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from functools import lru_cache

from aoc_2024.util import run

YEAR = 2024
DAY = 11


def solve_a(input: str) -> int | str | None:
    n = input.split()
    nums = [int(x) for x in n]
    total = 0
    for num in nums:
        total += iterate(num, 0, 25)
    return total


@lru_cache(maxsize=None)
def iterate(num: int, curr: int, times: int) -> int:
    # apply rules
    new: list[int] = []
    if num == 0:
        new = [1]
    elif len(f"{num}") % 2 == 0:
        new = [int(f"{num}"[: len(f"{num}") // 2]), int(f"{num}"[len(f"{num}") // 2 :])]
    else:
        new = [num * 2024]

    # check if this is the last step
    if curr + 1 == times:
        # return len(values[num])
        return len(new)

    # recursively apply rules to updated number(s)
    total = 0
    for n in new:
        # print(n)
        total += iterate(n, curr + 1, times)
    return total


def solve_b(input: str) -> int | str | None:
    n = input.split()
    nums = [int(x) for x in n]
    total = 0
    for num in nums:
        total += iterate(num, 0, 75)
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
