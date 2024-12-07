import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 7


def solve_a(input: str) -> int | str | None:
    total = 0
    for cal in input.splitlines():
        r, o = cal.split(": ")
        o1 = o.split(" ")
        res = int(r)
        operands = [int(x) for x in o1]
        if valid_a(operands, res):
            total += res
    return total


def valid_a(operands: list[int], result: int):
    if len(operands) == 1:
        return operands[-1] == result
    if operands[0] > result:
        return False
    o1 = operands.copy()
    r1 = o1[0] + o1[1]
    r2 = o1[0] * o1[1]
    o1.pop(0)
    o1.pop(0)
    o2 = o1.copy()
    o1.insert(0, r1)
    o2.insert(0, r2)
    if valid_a(o1, result):
        return True
    return valid_a(o2, result)


def solve_b(input: str) -> int | str | None:
    total = 0
    for cal in input.splitlines():
        r, o = cal.split(": ")
        o1 = o.split(" ")
        res = int(r)
        operands = [int(x) for x in o1]
        if valid_b(operands, res):
            total += res
    return total


def valid_b(operands: list[int], result: int):
    if len(operands) == 1:
        return operands[-1] == result
    if operands[0] > result:
        return False
    o1 = operands.copy()
    r1 = o1[0] + o1[1]
    r2 = o1[0] * o1[1]
    r3 = int(f"{o1[0]}{o1[1]}")
    o1.pop(0)
    o1.pop(0)
    o2 = o1.copy()
    o3 = o1.copy()
    o1.insert(0, r1)
    o2.insert(0, r2)
    o3.insert(0, r3)
    if valid_b(o1, result):
        return True
    elif valid_b(o2, result):
        return True
    return valid_b(o3, result)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual)
