import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from functools import cache

from aoc_2024.util import run

YEAR = 2024
DAY = 19


class Strs:
    SUB = {}


def solve_a(input: str) -> int | str | None:
    l = input.splitlines()
    patterns = l[0].split(", ")
    patterns = sorted(patterns, key=len, reverse=True)
    designs = l[2:]
    tot = len(designs)
    failed = 0
    for d in designs:
        chars: dict[int, list[str]] = {}
        for p in patterns:
            if p in d:
                found = [i for i in range(len(d)) if d.startswith(p, i)]
                for start in found:
                    if start not in chars:
                        chars[start] = [p]
                    else:
                        chars[start].append(p)
        Strs.SUB = chars
        if not build(d, 0):
            failed += 1

    return tot - failed


@cache
def build(design: str, idx: int):
    if idx not in Strs.SUB:
        return False
    if design == "":
        return True
    for check in Strs.SUB[idx]:
        if design.startswith(check):
            next = idx + len(check)
            if next - idx >= len(design):
                return True
            if build(design[next - idx :], next):
                return True
    return False


def solve_b(input: str) -> int | str | None:
    l = input.splitlines()
    patterns = l[0].split(", ")
    patterns = sorted(patterns, key=len, reverse=True)
    designs = l[2:]
    tot = 0
    for d in designs:
        chars: dict[int, list[str]] = {}
        for p in patterns:
            if p in d:
                found = [i for i in range(len(d)) if d.startswith(p, i)]
                for start in found:
                    if start not in chars:
                        chars[start] = [p]
                    else:
                        chars[start].append(p)
        Strs.SUB = chars
        x = build_all(d, 0)
        tot += x

    return tot


@cache
def build_all(design: str, idx: int):
    if idx not in Strs.SUB:
        return 0
    if design == "":
        return 1
    tot = 0
    for check in Strs.SUB[idx]:
        if design.startswith(check):
            next = idx + len(check)
            if next - idx >= len(design):
                tot += 1
                continue
            tot += build_all(design[next - idx :], next)
    return tot


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
