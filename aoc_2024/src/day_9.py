import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 9


def solve_a(input: str) -> int | str | None:
    id = 0
    fs: list[int] = []
    for i in range(0, len(input) - 1, 2):
        fill = int(input[i])
        free = int(input[i + 1]) if input[i + 1].isdigit() else 0
        for _ in range(fill):
            fs.append(id)
        for _ in range(free):
            fs.append(-1)
        id += 1
    head = -1
    tail = len(fs) - 1
    total = 0
    while head < tail:
        head += 1
        if fs[head] != -1:
            total += fs[head] * head
            continue
        while fs[tail] == -1:
            tail -= 1
        total += fs[tail] * head
        fs.pop()
        tail -= 1
    return total


def solve_b(input: str) -> int | str | None:
    id = 0
    fs: list[int] = []
    for i in range(0, len(input) - 1, 2):
        fill = int(input[i])
        free = int(input[i + 1]) if input[i + 1].isdigit() else 0
        for _ in range(fill):
            fs.append(id)
        for _ in range(free):
            fs.append(-1)
        id += 1
    head = 0
    tail = len(fs) - 1
    while head < tail:
        # get file len
        while fs[tail] == -1:
            tail -= 1
        file_len = 0
        while fs[tail - file_len] == fs[tail]:
            file_len += 1

        # move to next free space
        while fs[head] != -1:
            head += 1
        if head >= tail:
            break

        # find large enough free space
        space_fit = head
        free_len = -1
        while file_len > free_len:
            if space_fit > tail:
                break
            # check next space
            space_fit += free_len
            free_len = 0
            # get to next free space
            while fs[space_fit] != -1:
                space_fit += 1
            # get space len
            while fs[space_fit + free_len] == -1:
                free_len += 1
                if space_fit + free_len > tail:
                    break
        if file_len > free_len:
            tail -= file_len
            continue
        if space_fit > tail:
            break

        if space_fit == head:
            head += file_len
        # move file to free space
        for _ in range(file_len):
            fs[space_fit] = fs[tail]
            fs[tail] = -1
            tail -= 1
            space_fit += 1

    total = 0
    for i in range(len(fs)):
        if fs[i] == -1:
            continue
        total += fs[i] * i
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
