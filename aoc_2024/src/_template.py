import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from aoc_2024.lib.util import run

YEAR = 2024
DAY = 1


def solve_a(input: str) -> int | str | None:
    return None


def solve_b(input: str) -> int | str | None:
    return None


if __name__ == "__main__":
    run(YEAR, DAY, solve_a, solve_b)
