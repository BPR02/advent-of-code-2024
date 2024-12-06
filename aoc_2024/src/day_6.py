import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 6


def solve_a(input: str) -> int | str | None:
    g = input.replace("\n", "").find("^")
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    gy = g // width
    gx = g % width
    d = 0  # 0=up 1=right 2=down 3=left
    visited = {}
    visited[(gx, gy)] = 1
    while True:
        match d:
            case 0:
                cy = gy - 1
                cx = gx
            case 1:
                cy = gy
                cx = gx + 1
            case 2:
                cy = gy + 1
                cx = gx
            case 3:
                cy = gy
                cx = gx - 1
            case _:
                cx = -1
                cy = -1
        if cy > height - 1 or cy < 0 or cx > width - 1 or cx < 0:
            visited[(gx, gy)] = 1
            return len(visited.keys())
        elif map[cy][cx] == "#":
            d += 1
            if d > 3:
                d = 0
        else:
            visited[(gx, gy)] = 1
            gy = cy
            gx = cx


def solve_b(input: str) -> int | str | None:
    g = input.replace("\n", "").find("^")
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    gy = g // width
    gx = g % width
    start = (gx, gy)
    d = 0  # 0=up 1=right 2=down 3=left
    visited = {}
    path = []
    pot_obs = {}
    total = 0
    cx = 0
    cy = 0
    while True:
        match d:
            case 0:
                cy = gy - 1
                cx = gx
            case 1:
                cy = gy
                cx = gx + 1
            case 2:
                cy = gy + 1
                cx = gx
            case 3:
                cy = gy
                cx = gx - 1
            case _:
                cx = -1
                cy = -1
        if (gx, gy) in visited and d not in visited[(gx, gy)]:
            visited[(gx, gy)].append(d)
        else:
            visited[(gx, gy)] = [d]
        if cy > height - 1 or cy < 0 or cx > width - 1 or cx < 0:
            break
        elif map[cy][cx] == "#":
            d += 1
            if d > 3:
                d = 0
        else:
            path.append(((gx, gy), d, visited[(gx, gy)]))
            gy = cy
            gx = cx

            obs_check = {}
            visit_check = {}
            rx = gx
            ry = gy
            dc = 0
            cx, cy = start
            mx, my = start
            while True:
                if (cx, cy) in visit_check and dc not in visit_check[(cx, cy)]:
                    visit_check[(cx, cy)].append(dc)
                else:
                    visit_check[(cx, cy)] = [dc]
                match dc:
                    case 0:
                        cy = my - 1
                        cx = mx
                    case 1:
                        cy = my
                        cx = mx + 1
                    case 2:
                        cy = my + 1
                        cx = mx
                    case 3:
                        cy = my
                        cx = mx - 1
                if cy > height - 1 or cy < 0 or cx > width - 1 or cx < 0:
                    break
                elif map[cy][cx] == "#" or (cx == rx and cy == ry):
                    if (cx, cy) in obs_check and obs_check[(cx, cy)] == dc:
                        pot_obs[(rx, ry)] = 1
                        break
                    obs_check[(cx, cy)] = dc
                    dc = (dc + 1) % 4
                    total += 1
                else:
                    mx = cx
                    my = cy

    return len(pot_obs)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual)
