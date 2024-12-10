import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 10


def solve_a(input: str) -> int | str | None:
    total = 0
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    for y in range(height):
        for x in range(width):
            if map[y][x] != '0':
                continue
            visited = {}
            add = count_trails(map,x,y,0,width,height,visited)
            total += add
            
    return total
            
def count_trails(map, x, y, val, width, height,visited):
    if (x,y) in visited:
        return 0
    visited[(x,y)] = 1
    if val == 9:
        return 1
    total = 0
    c = val + 1
    if y+1 < height and int(map[y+1][x]) == c:
        total += count_trails(map,x,y+1,c,width,height,visited)
    if y-1 > -1 and int(map[y-1][x]) == c:
        total += count_trails(map,x,y-1,c,width,height,visited)
    if x+1 < width and int(map[y][x+1]) == c:
        total += count_trails(map,x+1,y,c,width,height,visited)
    if x-1 > -1 and int(map[y][x-1]) == c:
        total += count_trails(map,x-1,y,c,width,height,visited)
    return total
    
    

def solve_b(input: str) -> int | str | None:
    total = 0
    map = input.splitlines()
    height = len(map)
    width = len(map[-1])
    for y in range(height):
        for x in range(width):
            if map[y][x] != '0':
                continue
            add = count_trails_b(map,x,y,0,width,height)
            total += add
            
    return total

def count_trails_b(map, x, y, val, width, height):
    if val == 9:
        return 1
    total = 0
    c = val + 1
    if y+1 < height and int(map[y+1][x]) == c:
        total += count_trails_b(map,x,y+1,c,width,height)
    if y-1 > -1 and int(map[y-1][x]) == c:
        total += count_trails_b(map,x,y-1,c,width,height)
    if x+1 < width and int(map[y][x+1]) == c:
        total += count_trails_b(map,x+1,y,c,width,height)
    if x-1 > -1 and int(map[y][x-1]) == c:
        total += count_trails_b(map,x-1,y,c,width,height)
    return total

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
