import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 5


def solve_a(input: str) -> int | str | None:
    ordering: dict[int, list[int]] = {}
    total = 0
    for line in input.splitlines():
        if "|" in line:
            t, p = line.split("|")
            target = int(t)
            prev = int(p)
            if target not in ordering:
                ordering[target] = [prev]
            else:
                ordering[target].append(prev)
        elif line != "":
            pages = line.split(",")
            first = int(pages[0])
            if first not in ordering:
                continue
            valid = [ordering[first]]
            correct = True
            for i in range(1, len(pages) - 1):
                page = int(pages[i])
                if page not in ordering:
                    correct = False
                    break
                for j in range(0, i):
                    if page not in valid[j]:
                        correct = False
                        break
                if not correct:
                    break
                valid.append(ordering[page])
            if correct:
                mid = len(pages) // 2
                total += int(pages[mid])
    return total


def solve_b(input: str) -> int | str | None:
    ordering: dict[int, list[int]] = {}
    total = 0
    for line in input.splitlines():
        if "|" in line:
            t, p = line.split("|")
            target = int(t)
            prev = int(p)
            if target not in ordering:
                ordering[target] = [prev]
            else:
                ordering[target].append(prev)
        elif line != "":
            pages = line.split(",")
            first = int(pages[0])
            if first not in ordering:
                continue
            valid = [ordering[first]]
            correct = True
            for i in range(1, len(pages) - 1):
                page = int(pages[i])
                if page not in ordering:
                    correct = False
                    break
                for j in range(0, i):
                    if page not in valid[j]:
                        correct = False
                        break
                if not correct:
                    break
                valid.append(ordering[page])
            if not correct:
                new_pages = []
                check_nodes: list[int] = []
                limited_ordering = {}
                for key, value in ordering.items():
                    keep = False
                    new_v = []
                    for v in value:
                        if f"{v}" in pages:
                            keep = True
                            new_v.append(v)
                    if keep:
                        limited_ordering[key] = new_v
                for page in pages:
                    node = int(page)
                    if node not in limited_ordering:
                        check_nodes.append(node)
                while len(check_nodes) > 0:
                    node = check_nodes.pop()
                    new_pages.insert(0, f"{node}")
                    pages.remove(f"{node}")
                    for key, value in limited_ordering.items():
                        for page in new_pages:
                            p = int(page)
                            if p in value:
                                value.remove(p)
                        if len(value) == 0 and f"{key}" in pages:
                            check_nodes.append(key)
                mid = len(new_pages) // 2
                total += int(new_pages[mid])
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
