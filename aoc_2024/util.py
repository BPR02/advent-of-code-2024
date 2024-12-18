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


MAX_INT = 2147483647


class Node:
    pos: tuple[int, int]
    val: str | None
    score: int
    dir: int
    prev: tuple[int, int] | None

    def __init__(
        self,
        pos: tuple[int, int],
        val: str | None = None,
        score: int = MAX_INT,
        dir: int = 0,
        prev: tuple[int, int] | None = None,
    ):
        self.pos = pos
        self.val = val
        self.score = score
        self.dir = dir
        self.prev = prev

    def x(self):
        return self.pos[0]

    def y(self):
        return self.pos[1]

    def __str__(self) -> str:
        return f"{'{'}'pos':{self.pos} [{self.val}], 'dir':{self.dir}, 'score':{self.score},'prev':{self.prev}{'}'}"


class Grid:
    width: int
    height: int
    nodes: list[list[Node]]
    queue: list[Node]
    visited: dict[tuple[tuple[int, int, int]], Node]

    def __init__(
        self,
        width: int | None = None,
        height: int | None = None,
        from_string: str | None = None,
    ):
        self.queue = []
        if from_string is not None:
            self.init_from_str(from_string)
        elif width is not None and height is not None:
            self.init_from_dim(width, height)

    def init_from_str(self, s: str):
        self.queue = []
        self.visited = {}

        self.nodes = []
        grid = s.splitlines()
        self.height = len(grid)
        self.width = len(grid[-1])
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if grid[y][x] != "#":
                    node = Node((x, y), grid[y][x])
                else:
                    node = Node((x, y))
                row.append(node)
            self.nodes.append(row)

    def init_from_dim(self, height: int, width: int):
        self.height = height
        self.width = width
        self.nodes = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Node((x, y), "."))
            self.nodes.append(row)

    def __str__(self):
        res = ""
        for y in range(self.height):
            s = ""
            for x in range(self.width):
                if self.nodes[y][x].val:
                    s += self.nodes[y][x].val  # type: ignore
                else:
                    s += "#"
            res += s + "\n"
        return res.removesuffix("\n")

    def find(self, val: str):
        for y in range(self.height):
            for x in range(self.width):
                if self.nodes[y][x].val == val:
                    return (x, y)

    def iternodes(self) -> list[Node]:
        l = []
        for y in range(self.height):
            for x in range(self.width):
                if self.nodes[y][x].val:
                    l.append(self.nodes[y][x])
        return l

    def get_node(self, pos: tuple[int, int] | None) -> Node | None:
        if pos is None:
            return None
        return self.nodes[pos[1]][pos[0]]

    def set_node(
        self,
        pos: tuple[int, int],
        val: str | None = "",
        score: int = -MAX_INT,
        prev: tuple[int, int] | None = (-MAX_INT, -MAX_INT),
    ):
        node = self.nodes[pos[1]][pos[0]]
        if val != "":
            node.val = val
        if score != -MAX_INT:
            node.score = score
        if prev != (-MAX_INT, -MAX_INT):
            node.prev = prev

    def get_neighbors(self, pos: tuple[int, int], ignore: str = "") -> list[Node]:
        x = pos[0]
        y = pos[1]
        l: list[Node] = []
        if (
            y - 1 > -1
            and self.nodes[y - 1][x].val is not None
            and self.nodes[y - 1][x].val != ignore
        ):
            l.append(self.nodes[y - 1][x])
        if (
            x + 1 < self.width
            and self.nodes[y][x + 1].val is not None
            and self.nodes[y][x + 1].val != ignore
        ):
            l.append(self.nodes[y][x + 1])
        if (
            y + 1 < self.height
            and self.nodes[y + 1][x].val is not None
            and self.nodes[y + 1][x].val != ignore
        ):
            l.append(self.nodes[y + 1][x])
        if (
            x - 1 > -1
            and self.nodes[y][x - 1].val is not None
            and self.nodes[y][x - 1].val != ignore
        ):
            l.append(self.nodes[y][x - 1])
        return l

    def ins(self, node: Node):
        if node is None:
            return
        if len(self.queue) == 0:
            self.queue = [node]
            return
        if node in self.queue:
            return
        w = node.score
        
        low = 0
        high = len(self.queue) - 1
        mid = low + (high - low) // 2
        while low < high:
            mid = low + (high - low) // 2
            c = self.queue[mid].score
            if w == c:
                break
            if w < c:
                high = mid - 1
            else:
                low = mid + 1
        self.queue.insert(mid+1, node)

    def find_path(
        self, start: tuple[int, int], end: tuple[int, int], avoid: str = ""
    ) -> list[Node] | None:
        self.set_node(start, score=0)
        pos = start
        s = self.get_node(pos)
        if s is None:
            return None
        self.ins(s)
        while pos != end:
            if len(self.queue) == 0:
                return None
            curr = self.queue.pop(0)
            pos = curr.pos
            next_score = curr.score + 1
            search = self.get_neighbors(pos, avoid)
            for n in search:
                check_score = n.score
                if check_score > next_score:
                    self.set_node(n.pos, score=next_score, prev=pos)
                    self.ins(n)

        last = self.get_node(end)
        if last is None:
            return None
        path = [last]
        prev = self.get_node(last.prev)
        while prev != None:
            path.insert(0, prev)
            prev = self.get_node(prev.prev)
        return path
