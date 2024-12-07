import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import bisect

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 1


def solve_a(input: str) -> int | str | None:
    l1: list[int] = []
    l2: list[int] = []
    total = 0
    for line in input.splitlines():
        e1, e2 = line.split()
        bisect.insort(l1, int(e1))
        bisect.insort(l2, int(e2))
    for i in range(len(l1)):
        total += abs((l1[i] - l2[i]))
    return total


def solve_b(input: str) -> int | str | None:
    l1: list[int] = []
    l2: list[int] = []
    val: dict[int, int] = {}

    total = 0
    for line in input.splitlines():
        e1, e2 = line.split()
        bisect.insort(l1, int(e1))
        bisect.insort(l2, int(e2))

    for num in l1:
        if num in val:
            total += val[num]
            continue
        start = bisect.bisect_left(l2, num)
        count = 0
        for i in range(start, len(l2)):
            if num != l2[i]:
                break
            else:
                count += 1
        val[num] = num * count
        total += val[num]

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
