import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import Grid, run

YEAR = 2024
DAY = 18


def solve_a(input: str) -> int | str | None:
    drop_count = 1024
    size = 71
    grid = Grid(size, size)
    drop = [(int(p.split(",")[0]), int(p.split(",")[1])) for p in input.splitlines()]
    for i in range(drop_count):
        if i >= len(drop):
            break
        pos = drop[i]
        grid.set_node(pos, "#")
    path = grid.find_path((0, 0), (size - 1, size - 1), "#")
    if path is not None and path[-1] is not None:
        return path[-1].score
    return None


def solve_b(input: str) -> int | str | None:
    size = 71
    drop = [(int(p.split(",")[0]), int(p.split(",")[1])) for p in input.splitlines()]

    drop_count = 0
    while True:
        grid = Grid(size, size)
        for i in range(drop_count):
            if i >= len(drop):
                return None
            pos = drop[i]
            grid.set_node(pos, "#")
        if grid.find_path((0, 0), (size - 1, size - 1), "#") is None:
            return f"{drop[drop_count-1][0]},{drop[drop_count-1][1]}"
        drop_count += 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
