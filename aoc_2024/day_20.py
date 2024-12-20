import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import MAX_INT, Grid, Node, run

YEAR = 2024
DAY = 20


def solve_a(input: str) -> int | str | None:
    grid = Grid(from_string=input)
    start = grid.find("S")
    end = grid.find("E")
    if start is None or end is None:
        return None
    path = grid.find_path(start, end, "#")
    if path is None:
        return None
    total = 0
    for node in path:
        # check 2 spaces away
        x, y = node.pos
        skips: list[Node | None] = []
        skips.append(grid.get_node((x + 2, y)))
        skips.append(grid.get_node((x - 2, y)))
        skips.append(grid.get_node((x, y + 2)))
        skips.append(grid.get_node((x, y - 2)))
        for n in skips:
            if (
                n is not None
                and n.score != MAX_INT
                and (n.score - node.score - 2 >= 100)
            ):
                total += 1
    return total


def solve_b(input: str) -> int | str | None:
    grid = Grid(from_string=input, ignore="")
    start = grid.find("S")
    end = grid.find("E")
    if start is None or end is None:
        return None
    path = grid.find_path(start, end, "#")
    if path is None:
        return None
    skips = {}
    for node in path:
        # BFS with max of 20 steps
        queue = [node]
        visited: dict[Node, bool] = {node: True}
        depth: dict[Node, int] = {node: 0}
        while len(queue) > 0:
            n = queue.pop(0)
            if (
                n is not None
                and n.val != "#"
                and n.score != MAX_INT
                and (n.score - node.score - depth[n] >= 100)
            ):
                skips[(node.pos, n.pos)] = True
            for adj in grid.get_neighbors(n.pos):
                if adj not in visited and depth[n] < 20:
                    visited[adj] = True
                    depth[adj] = depth[n] + 1
                    queue.append(adj)
    return len(skips)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
