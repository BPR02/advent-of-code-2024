from aocd.models import Puzzle


def get_puzzle(year: int, day: int) -> Puzzle:
    return Puzzle(year=year, day=day)


def test_puzzle(puzzle: Puzzle, func, part: str = "a"):
    examples = puzzle.examples
    for example in examples:
        sol: int | str | None = func(example.input_data)
        if sol is None:
            return
        if isinstance(sol, int):
            sol = f"{sol}"

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

        print(f"---{sol}")


def run(
    year: int,
    day: int,
    solve_a,
    solve_b,
    test: bool = True,
    retest: bool = False,
    manual: bool = False,
    part: str | None = None,
):
    print(f"{year} - DAY {day}")
    if manual:
        with open(f"manual_input/day_{day}.txt", "r") as file:
            input = file.read()
        if part == "1" or part is None:
            solution_a = solve_a(input)
            print("Part 1:", solution_a)
        if part == "2" or part is None:
            solution_b = solve_b(input)
            print("Part 2:", solution_b)
        return
    puzzle: Puzzle = Puzzle(year=year, day=day)
    input = puzzle.input_data
    if (not puzzle.answered_a or retest) and (part == "1" or part is None):
        print("-Part 1")
        if test:
            print("--Testing")
            test_puzzle(puzzle, solve_a, "a")
            print("---Tests Passed")
        print("--Solving")
        solution_a = solve_a(input)
        if solution_a is not None and not retest:
            print(f"--Submitting {solution_a}")
            puzzle.answer_a = solution_a
    if ((puzzle.answered_a and not puzzle.answered_b) or retest) and (
        part == "2" or part is None
    ):
        print("-Part 2")
        if test:
            print("--Testing")
            test_puzzle(puzzle, solve_b, "b")
            print("---Tests Passed")
        print("--Solving")
        solution_b = solve_b(input)
        if solution_b is not None and not retest:
            print(f"--Submitting {solution_b}")
            puzzle.answer_b = solution_b
