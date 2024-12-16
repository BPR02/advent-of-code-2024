import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 16
sys.setrecursionlimit(15000)
def solve_a(input: str) -> int | str | None:
    pos = input.replace("\n", "").find("S")
    grid = input.splitlines()
    height = len(grid)
    width = len(grid[-1])
    x = pos % width
    y = pos // width
    print((x,y))
    dead_ends = {}
    visited = {}
    return pathfind(grid, (x, y), 1, dead_ends, visited)
    # return None

DEPTH = [0]
def pathfind(grid: list[str], pos: tuple[int,int], d: int, dead_ends: dict[tuple[int,int],bool], visited: dict[tuple[int,int],bool]) -> int:
    # DEPTH[0] += 1
    # if DEPTH[0] > 1000:
    #     return -1
    if pos in visited:
        # print("cycle", len(visited))
        visited = {}
        return 9999999999
    if pos in dead_ends:
        return 99999999999
    x, y = pos
    b = grid[y][x]
    if b == "E":
        # print("made it!", len(visited))
        visited = {}
        return 0
    elif b == "#":
        visited = {}
        return 99999999999
    d %= 4
    # check in front
    pf = (x, y)
    pl = (x, y)
    pr = (x, y)
    match d:
        case 0: # north
            pf = (x, y-1)
            pl = (x-1, y)
            pr = (x+1, y)
        case 1: # east
            pf = (x+1, y)
            pl = (x, y-1)
            pr = (x, y+1)
        case 2: # south
            pf = (x, y+1)
            pl = (x+1, y)
            pr = (x-1, y)
        case 3: # west
            pf = (x-1, y)
            pl = (x, y+1)
            pr = (x, y-1)
    # get block
    cf = grid[pf[1]][pf[0]]
    cl = grid[pl[1]][pl[0]]
    cr = grid[pr[1]][pr[0]]
    # print("pos:",pos, b, d, "check:", pf, cf, pl, cl, pr, cr)
    # get result of paths
    paths: list[int] = [0,0,0] # forward, left, right
    branch = visited.copy()
    branch[pos] = True
    paths[0] = 1 + pathfind(grid, pf, d, dead_ends, branch)
    branch = visited.copy()
    branch[pos] = True
    paths[1] = 1001 + pathfind(grid, pl, d-1, dead_ends, branch)
    branch = visited.copy()
    branch[pos] = True
    paths[2] = 1001 + pathfind(grid, pr, d+1, dead_ends, branch)
    if min(paths) >= 99999999999:
        # print("dead_end",pos)
        dead_ends[pos] = True
    return min(paths)


def solve_b(input: str) -> int | str | None:
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
