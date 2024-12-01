from aocd.models import Puzzle


def get_puzzle(year: int, day: int) -> Puzzle:
    return Puzzle(year=year, day=day)


def test_puzzle(puzzle: Puzzle, func, part: str = "a"):
    examples = puzzle.examples
    for example in examples:
        sol: str | None = func(example.input_data)
        if sol is None:
            return

        if part != "b":
            if sol != example.answer_a:
                raise AssertionError(
                    f"Solution does not match => {sol} != {example.answer_a}"
                )
        else:
            if example.answer_b is None:
                continue
            if sol != example.answer_b:
                raise AssertionError(
                    f"Solution does not match => {sol} != {example.answer_b}"
                )


def run(year: int, day: int, solve_a, solve_b):
    print(f"{year} - DAY {day}")
    puzzle: Puzzle = Puzzle(year=year, day=day)
    input = puzzle.input_data
    if not puzzle.answered_a:
        print("-Part 1")
        print("--Testing")
        test_puzzle(puzzle, solve_a, "a")
        print("--Solving")
        solution_a = solve_a(input)
        if solution_a is not None:
            print(f"--Submitting {solution_a}")
            puzzle.answer_a = solution_a
    elif not puzzle.answered_b:
        print("-Part 2")
        print("--Testing")
        test_puzzle(puzzle, solve_b, "b")
        print("--Solving")
        solution_b = solve_b(input)
        if solution_b is not None:
            print(f"--Submitting {solution_b}")
            puzzle.answer_b = solution_b
