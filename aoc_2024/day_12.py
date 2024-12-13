import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 12


def solve_a(input: str) -> int | str | None:
    checked = {}
    total = 0
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    for y in range(height):
        for x in range(width):
            if (x, y) in checked:
                continue
            area, perimeter = fill(x, y, checked, map, width, height)
            total += area * perimeter
    return total


def fill(x, y, checked, map, width, height):
    if (x, y) in checked:
        return (0, 0)
    c = map[y][x]
    checked[(x, y)] = 1
    area = 1
    perimeter = 4
    if x - 1 > -1 and map[y][x - 1] == c:
        a, p = fill(x - 1, y, checked, map, width, height)
        area += a
        perimeter = perimeter - 1 + p
    if x + 1 < width and map[y][x + 1] == c:
        a, p = fill(x + 1, y, checked, map, width, height)
        area += a
        perimeter = perimeter - 1 + p
    if y - 1 > -1 and map[y - 1][x] == c:
        a, p = fill(x, y - 1, checked, map, width, height)
        area += a
        perimeter = perimeter - 1 + p
    if y + 1 < width and map[y + 1][x] == c:
        a, p = fill(x, y + 1, checked, map, width, height)
        area += a
        perimeter = perimeter - 1 + p
    return (area, perimeter)


def solve_b(input: str) -> int | str | None:
    checked = {}
    total = 0
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    for y in range(height):
        for x in range(width):
            if (x, y) in checked:
                continue
            sides: dict[str, list[int]] = {}
            area = bulk_fill(x, y, sides, checked, map, width, height)
            perimeter = 0
            for _, s in sides.items():
                s.sort()
                perimeter += 1
                for i in range(1, len(s)):
                    if s[i - 1] + 1 != s[i]:
                        perimeter += 1
            total += area * perimeter
    return total


def bulk_fill(x, y, sides: dict[str, list[int]], checked, map, width, height):
    if (x, y) in checked:
        return 0
    c = map[y][x]
    checked[(x, y)] = 1
    area = 1
    perimeter = 0
    if x - 1 > -1 and map[y][x - 1] == c:
        a = bulk_fill(x - 1, y, sides, checked, map, width, height)
        area += a
    else:
        if f"x={x},-1" not in sides:
            sides[f"x={x},-1"] = [y]
        else:
            sides[f"x={x},-1"].append(y)
    if x + 1 < width and map[y][x + 1] == c:
        a = bulk_fill(x + 1, y, sides, checked, map, width, height)
        area += a
    else:
        if f"x={x},+1" not in sides:
            sides[f"x={x},+1"] = [y]
        else:
            sides[f"x={x},+1"].append(y)
    if y - 1 > -1 and map[y - 1][x] == c:
        a = bulk_fill(x, y - 1, sides, checked, map, width, height)
        area += a
    else:
        if f"y={y},-1" not in sides:
            sides[f"y={y},-1"] = [x]
        else:
            sides[f"y={y},-1"].append(x)
    if y + 1 < width and map[y + 1][x] == c:
        a = bulk_fill(x, y + 1, sides, checked, map, width, height)
        area += a
    else:
        if f"y={y},+1" not in sides:
            sides[f"y={y},+1"] = [x]
        else:
            sides[f"y={y},+1"].append(x)
    return area


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
