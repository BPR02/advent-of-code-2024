import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import sympy as sp
from sympy import Eq, var
from sympy.solvers import solve

from aoc_2024.util import run

YEAR = 2024
DAY = 13


def solve_a(input: str) -> int | str | None:
    lines = input.splitlines()
    total = 0
    for i in range(0, len(lines), 4):
        a = lines[i].removeprefix("Button A: X+").split(",")
        ay = int(a[1].removeprefix(" Y+"))
        ax = int(a[0])
        b = lines[i + 1].removeprefix("Button B: X+").split(",")
        by = int(b[1].removeprefix(" Y+"))
        bx = int(b[0])
        p = lines[i + 2].removeprefix("Prize: X=").split(",")
        py = int(p[1].removeprefix(" Y="))
        px = int(p[0])

        total += count_tokens(ax, ay, bx, by, px, py)
    return total


def count_tokens(ax: int, ay: int, bx: int, by: int, px: int, py: int):
    possible: list[tuple[int, int]] = []
    for a in range(100):
        check_ax = ax * a
        check_ay = ay * a
        if check_ax > px or check_ay > py:
            break
        rem_x = px - check_ax
        rem_y = py - check_ay
        if rem_x == 0 and rem_y == 0:
            possible.append((a, 0))
            continue
        check_bx = rem_x / bx
        check_by = rem_y / by
        if check_bx > 100 or check_by > 100:
            continue
        if not check_bx.is_integer() or not check_by.is_integer():
            continue
        if check_bx == check_by:
            possible.append((a, int(check_bx)))
    if len(possible) == 0:
        return 0
    min_token = 10000
    for a, b in possible:
        token = a * 3 + b
        min_token = min(min_token, token)
    return min_token


def solve_b(input: str) -> int | str | None:
    lines = input.splitlines()
    total = 0
    for i in range(0, len(lines), 4):
        a = lines[i].removeprefix("Button A: X+").split(",")
        ay = int(a[1].removeprefix(" Y+"))
        ax = int(a[0])
        b = lines[i + 1].removeprefix("Button B: X+").split(",")
        by = int(b[1].removeprefix(" Y+"))
        bx = int(b[0])
        p = lines[i + 2].removeprefix("Prize: X=").split(",")
        py = int(p[1].removeprefix(" Y="))
        px = int(p[0])
        px += 10000000000000
        py += 10000000000000
        # print(i/4)
        total += calc(ax, ay, bx, by, px, py)
    return total


def calc(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> int:
    var("va vb")
    x = Eq(ax * va + bx * vb, px)  # type: ignore
    y = Eq(ay * va + by * vb, py)  # type: ignore
    possible = solve([x, y], dict=True)
    if len(possible) == 0:
        return 0
    min_token = None
    for d in possible:
        a = d[va]  # type: ignore
        b = d[vb]  # type: ignore
        if not isinstance(a, sp.core.numbers.Integer) or not isinstance(
            b, sp.core.numbers.Integer
        ):
            continue
        if a < 0 or b < 0:
            continue
        token: int = int(a * 3 + b)
        if min_token is None:
            min_token = token
        else:
            min_token = min(min_token, token)
    if min_token is None:
        return 0
    return int(min_token)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
