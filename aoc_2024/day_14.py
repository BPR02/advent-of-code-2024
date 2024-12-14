import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 14


def solve_a(input: str) -> int | str | None:
    # width = 11
    # height = 7
    width = 101
    height = 103
    seconds = 100

    qw = width // 2
    qh = height // 2
    q1 = (0, qw, 0, qh)
    q2 = (qw + 1, width, qh + 1, height)
    q3 = (0, qw, qh + 1, height)
    q4 = (qw + 1, width, 0, qh)

    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    for robot in input.splitlines():
        r = robot.removeprefix("p=").split(",")
        px = int(r[0])
        vy = int(r[2])
        r = r[1].split(" v=")
        py = int(r[0])
        r = r[1].split(",")
        vx = int(r[0])

        fx = (px + (vx * seconds)) % width
        fy = (py + (vy * seconds)) % height

        if fx >= q1[0] and fx < q1[1] and fy >= q1[2] and fy < q1[3]:
            t1 += 1
        elif fx >= q2[0] and fx < q2[1] and fy >= q2[2] and fy < q2[3]:
            t2 += 1
        elif fx >= q3[0] and fx < q3[1] and fy >= q3[2] and fy < q3[3]:
            t3 += 1
        elif fx >= q4[0] and fx < q4[1] and fy >= q4[2] and fy < q4[3]:
            t4 += 1

    return t1 * t2 * t3 * t4


def solve_b(input: str) -> int | str | None:
    width = 101
    height = 103
    robots = input.splitlines()

    seconds = 0
    success = False
    for _ in range(10000):
        seconds += 1
        pos = {}
        success = True
        for robot in robots:
            r = robot.removeprefix("p=").split(",")
            px = int(r[0])
            vy = int(r[2])
            r = r[1].split(" v=")
            py = int(r[0])
            r = r[1].split(",")
            vx = int(r[0])

            fx = (px + (vx * seconds)) % width
            fy = (py + (vy * seconds)) % height

            if (fx, fy) in pos:
                success = False
                break
            pos[(fx, fy)] = 1
        if success:
            print()
            print(seconds)
            for y in range(height):
                l = ""
                for x in range(width):
                    if (x, y) in pos:
                        l += "#"
                    else:
                        l += " "
                print(l)
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
