import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 15


def solve_a(input: str) -> int | str | None:
    pos = input.replace("\n", "").find("@")
    grid, moves = input.split("\n\n")
    moves = moves.replace("\n", "")
    # print(grid,"\n")
    grid = grid.splitlines()
    height = len(grid)
    width = len(grid[-1])
    rx = pos % width
    ry = pos // width
    for move in moves:
        # print((rx,ry), move)
        _, rx, ry = attempt_move(grid, rx, ry, move)
        # for line in grid:
        #     print(line)
    # for line in grid:
    #     print(line)
    total = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "O":
                total += 100 * y + x
    return total


def attempt_move(grid, rx, ry, d) -> tuple[bool, int, int]:
    cx = rx
    cy = ry
    match d:
        case "^":
            cy -= 1
        case "v":
            cy += 1
        case "<":
            cx -= 1
        case ">":
            cx += 1
        case _:
            print("ERROR", rx, ry, d)
            return (False, rx, ry)

    c = grid[cy][cx]
    if c == ".":
        grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
        grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
        return (True, cx, cy)
    elif c == "#":
        return (False, rx, ry)
    else:
        s, _, _ = attempt_move(grid, cx, cy, d)
        if not s:
            return (s, rx, ry)
        grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
        grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
        return (s, cx, cy)


def solve_b(input: str) -> int | str | None:
    input = (
        input.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    pos = input.replace("\n", "").find("@")
    grid, moves = input.split("\n\n")
    moves = moves.replace("\n", "")
    # print(grid,"\n")
    grid = grid.splitlines()
    height = len(grid)
    width = len(grid[-1])
    rx = pos % width
    ry = pos // width
    for move in moves:
        # print((rx,ry), move)
        save = grid.copy()
        s, rx, ry = attempt_move_b(grid, rx, ry, move)
        if not s:
            grid = save
        # for line in grid:
        #     print(line)
    # for line in grid:
    #     print(line)
    total = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "[":
                total += 100 * y + x
    return total


def attempt_move_b(grid, rx, ry, d) -> tuple[bool, int, int]:
    cx = rx
    cy = ry
    r = grid[ry][rx]
    match d:
        case "^":
            cy -= 1
            c = grid[cy][cx]
            if r == "@":
                if c == ".":
                    grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                    grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                    return (True, cx, cy)
                elif c == "#":
                    return (False, rx, ry)
                else:
                    s, _, _ = attempt_move_b(grid, cx, cy, d)
                    if not s:
                        return (s, rx, ry)
                    grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                    grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                    return (s, cx, cy)

            if r == "]":
                cx -= 1
            elif r != "[":
                print("ERROR", r, (rx, ry))
            c1 = grid[cy][cx]
            c2 = grid[cy][cx + 1]

            if c1 == "." and c2 == ".":
                grid[cy] = grid[cy][:cx] + "[]" + grid[cy][cx + 2 :]
                grid[ry] = grid[ry][:cx] + ".." + grid[ry][cx + 2 :]
                return (True, cx, cy)
            elif c1 == "#" or c2 == "#":
                return (False, rx, ry)
            else:
                if c1 == ".":
                    s1 = True
                else:
                    s1, _, _ = attempt_move_b(grid, cx, cy, d)
                if c2 == "." or c2 == "]":
                    s2 = True
                else:
                    s2, _, _ = attempt_move_b(grid, cx + 1, cy, d)
                if not s1 or not s2:
                    return (False, rx, ry)
                grid[cy] = grid[cy][:cx] + "[]" + grid[cy][cx + 2 :]
                grid[ry] = grid[ry][:cx] + ".." + grid[ry][cx + 2 :]
                return (True, cx, cy)
        case "v":
            cy += 1
            c = grid[cy][cx]
            if r == "@":
                if c == ".":
                    grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                    grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                    return (True, cx, cy)
                elif c == "#":
                    return (False, rx, ry)
                else:
                    s, _, _ = attempt_move_b(grid, cx, cy, d)
                    if not s:
                        return (s, rx, ry)
                    grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                    grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                    return (s, cx, cy)

            if r == "]":
                cx -= 1
            elif r != "[":
                print("ERROR", r)
            c1 = grid[cy][cx]
            c2 = grid[cy][cx + 1]

            if c1 == "." and c2 == ".":
                grid[cy] = grid[cy][:cx] + "[]" + grid[cy][cx + 2 :]
                grid[ry] = grid[ry][:cx] + ".." + grid[ry][cx + 2 :]
                return (True, cx, cy)
            elif c1 == "#" or c2 == "#":
                return (False, rx, ry)
            else:
                if c1 == ".":
                    s1 = True
                else:
                    s1, _, _ = attempt_move_b(grid, cx, cy, d)
                if c2 == "." or c2 == "]":
                    s2 = True
                else:
                    s2, _, _ = attempt_move_b(grid, cx + 1, cy, d)
                if not s1 or not s2:
                    return (False, rx, ry)
                grid[cy] = grid[cy][:cx] + "[]" + grid[cy][cx + 2 :]
                grid[ry] = grid[ry][:cx] + ".." + grid[ry][cx + 2 :]
                return (True, cx, cy)
        case "<":
            cx -= 1
            c = grid[cy][cx]
            if c == ".":
                grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                return (True, cx, cy)
            elif c == "#":
                return (False, rx, ry)
            else:
                s, _, _ = attempt_move(grid, cx, cy, d)
                if not s:
                    return (s, rx, ry)
                grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                return (s, cx, cy)
        case ">":
            cx += 1
            c = grid[cy][cx]
            if c == ".":
                grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                return (True, cx, cy)
            elif c == "#":
                return (False, rx, ry)
            else:
                s, _, _ = attempt_move(grid, cx, cy, d)
                if not s:
                    return (s, rx, ry)
                grid[cy] = grid[cy][:cx] + grid[ry][rx] + grid[cy][cx + 1 :]
                grid[ry] = grid[ry][:rx] + "." + grid[ry][rx + 1 :]
                return (s, cx, cy)
        case _:
            print("ERROR", rx, ry, d)
            return (False, rx, ry)

    return (False, rx, ry)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
