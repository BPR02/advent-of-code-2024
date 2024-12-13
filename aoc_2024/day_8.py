import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 8


def solve_a(input: str) -> int | str | None:
    antenae: dict[str, list[tuple[int, int]]] = {}
    antinodes = {}
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    for y in range(height):
        for x in range(width):
            c = map[y][x]
            if c == ".":
                continue
            if c not in antenae:
                antenae[c] = [(x, y)]
            else:
                antenae[c].append((x, y))
    for _, nodes in antenae.items():
        while len(nodes) > 1:
            n1 = nodes.pop()
            for n2 in nodes:
                x1 = n1[0]
                x2 = n2[0]
                y1 = n1[1]
                y2 = n2[1]
                dx = x1 - x2
                dy = y1 - y2
                ax = x1 + dx
                ay = y1 + dy
                bx = x2 - dx
                by = y2 - dy
                if ax > -1 and ax < width and ay > -1 and ay < height:
                    antinodes[(ax, ay)] = 1
                if bx > -1 and bx < width and by > -1 and by < height:
                    antinodes[(bx, by)] = 1
    return len(antinodes)


def solve_b(input: str) -> int | str | None:
    antenae: dict[str, list[tuple[int, int]]] = {}
    antinodes = {}
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    for y in range(height):
        for x in range(width):
            c = map[y][x]
            if c == ".":
                continue
            if c not in antenae:
                antenae[c] = [(x, y)]
            else:
                antenae[c].append((x, y))
    for _, nodes in antenae.items():
        while len(nodes) > 1:
            n1 = nodes.pop()
            for n2 in nodes:
                x1 = n1[0]
                x2 = n2[0]
                y1 = n1[1]
                y2 = n2[1]
                dx = x1 - x2
                dy = y1 - y2
                ax = x1 + dx
                ay = y1 + dy
                antinodes[(x1, y1)] = 1
                antinodes[(x2, y2)] = 1
                while ax > -1 and ax < width and ay > -1 and ay < height:
                    antinodes[(ax, ay)] = 1
                    ax += dx
                    ay += dy
                bx = x2 - dx
                by = y2 - dy
                while bx > -1 and bx < width and by > -1 and by < height:
                    antinodes[(bx, by)] = 1
                    bx -= dx
                    by -= dy
    return len(antinodes)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
