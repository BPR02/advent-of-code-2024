from aocd.models import Puzzle
from beet import Context, Draft, Function

YEAR = 2024


def get_puzzle_input(day: int):
    puzzle = Puzzle(year=YEAR, day=day)
    try:
        out = puzzle.input_data
    except:
        out = None
    return out


def parse_input(draft: Draft, input: str, day: int):
    data = input.splitlines()
    cmd = "data merge storage aoc:register {input:" + str(data) + "}"
    cmd = cmd.replace(", ", ",")
    draft.data[f"aoc_{YEAR}:load_input/day_{day}"] = Function(cmd)


def beet_default(ctx: Context):
    day = 1
    while 1:
        input = None
        try:
            with open(f"manual_input/day_{day}.txt", "r") as file:
                input = file.read()
        except:
            input = get_puzzle_input(day)
        if input is None:
            if day != 1:
                print(f"Downloaded data from Days 1-{day-1}")
            else:
                print("Unable to download data")
            return

        with ctx.generate.draft() as draft:
            draft.cache(f"aoc/{YEAR}_{day}", "")
            # generate only upon cache miss
            parse_input(draft, input, day)
        day += 1
