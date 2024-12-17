import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 16

MAX_INT = 2147483647


class Node:
    pos: tuple[int, int]
    val: str | None
    score: int = MAX_INT
    dir: int = 0
    prev: tuple[int, int] = None

    def __init__(self, pos, val, score, prev):
        self.pos = pos
        self.val = val
        self.score = score
        self.dir = 0
        self.prev = prev

    def __init__(self, pos, val):
        self.pos = pos
        self.val = val
        self.score = MAX_INT
        self.dir = 0

    def __init__(self, pos, val):
        self.pos = pos
        self.val = val

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
    visited: dict[tuple[tuple[int,int,int]],Node]

    def __init__(self, from_string: str):
        self.queue = []
        self.visited = {}
        
        self.nodes = []
        grid = from_string.splitlines()
        self.height = len(grid)
        self.width = len(grid[-1])
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if grid[y][x] != "#":
                    node = Node((x, y), grid[y][x])
                else:
                    node = Node((x, y), None)
                row.append(node)
            self.nodes.append(row)

    def __str__(self):
        res = ""
        for y in range(self.height):
            s = ""
            for x in range(self.width):
                if self.nodes[y][x].val:
                    s += self.nodes[y][x].val
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

    def get_node(self, pos: tuple[int, int]) -> Node:
        return self.nodes[pos[1]][pos[0]]

    def get_neighbors(self, pos: tuple[int, int]) -> list[Node]:
        x = pos[0]
        y = pos[1]
        l: list[Node] = []
        if self.nodes[y - 1][x].val:
            l.append(self.nodes[y - 1][x])
        if self.nodes[y][x + 1].val:
            l.append(self.nodes[y][x + 1])
        if self.nodes[y + 1][x].val:
            l.append(self.nodes[y + 1][x])
        if self.nodes[y][x - 1].val:
            l.append(self.nodes[y][x - 1])
        return l
    
    def get_turns_pos(self, pos: tuple[int, int], dir: int) -> list[Node]:
        x, y = pos
        pf = (x, y)
        pl = (x, y)
        pr = (x, y)
        l = [None,None,None]
        match dir:
            case 0:  # north
                pf = (x, y - 1)
                pl = (x - 1, y)
                pr = (x + 1, y)
            case 1:  # east
                pf = (x + 1, y)
                pl = (x, y - 1)
                pr = (x, y + 1)
            case 2:  # south
                pf = (x, y + 1)
                pl = (x + 1, y)
                pr = (x - 1, y)
            case 3:  # west
                pf = (x - 1, y)
                pl = (x, y + 1)
                pr = (x, y - 1)
        if self.nodes[pf[1]][pf[0]].val:
            l[0] = self.nodes[pf[1]][pf[0]]
        if self.nodes[pl[1]][pl[0]].val:
            l[1] = self.nodes[pl[1]][pl[0]]
        if self.nodes[pr[1]][pr[0]].val:
            l[2] = self.nodes[pr[1]][pr[0]]
        return l
    
    def get_turns(self, node: Node) -> list[Node]:
        return self.get_turns_pos(node.pos, node.dir)
    
    def ins(self, node: Node):
        if node is None:
            return        
        if len(self.queue) == 0:
            self.queue = [node]
            return
        if node in self.queue:
            return
        w = node.score
        i = 0
        while i < len(self.queue):
            c = self.queue[i].score
            if w < c:
                break
            i += 1
        self.queue.insert(i, node)

    def process(self):
        node = self.queue.pop(0)
       # print("pop", node)
        self.visited[(node.pos)] = node
        turns = self.get_turns(node)
        # for n in turns:
           # print("  ", n)
        if turns[0] is not None:
            compare = turns[0].score
            if turns[0].pos in self.visited: 
               # print("!!!")
                check_dir = turns[0].dir
                if check_dir != node.dir:
                    compare += 1000
            if compare > node.score:
                turns[0].dir = node.dir
                turns[0].score = node.score + 1
                turns[0].prev = node.pos
            else:
                turns[0] = None
        if turns[1] is not None:
            compare = turns[1].score
            if turns[1].pos in self.visited:
                check_dir = turns[1].dir
                if check_dir != node.dir:
                    compare += 1000
            if compare > node.score:
                turns[1].dir = (node.dir-1) % 4
                turns[1].score = node.score + 1001
                turns[1].prev = node.pos
            else:
                turns[1] = None
        if turns[2] is not None:
            compare = turns[2].score
            if turns[2].pos in self.visited:
                check_dir = turns[2].dir
                if check_dir != node.dir:
                    compare += 1000
            if compare > node.score:
                turns[2].dir = (node.dir+1) % 4
                turns[2].score = node.score + 1001
                turns[2].prev = node.pos
            else:
                turns[2] = None
        for n in turns:
            if n is None:
                continue
            if n.val == "E":
                return True
           # print("  (", turns.index(n),")", n)
            self.ins(n)
        # return True
        return len(self.queue) == 0

def solve_a(input: str) -> int | str | None:
    grid = Grid(input)
    pos = grid.find("S")
   # print(grid)
   # print(pos)
   # print()
    start = grid.get_node(pos)
    start.dir = 1
    start.score = 0
    grid.ins(start)
    
    # for _ in range(10):
    #     if grid.process():
    #         break
    #     for n in grid.queue:
    #        # print(n)
    #    # print()
    while not grid.process():
        # for n in grid.queue:
           # print(n)
       # print()
        continue
    
    end = grid.get_node(grid.find("E"))
    # print(end)
    
    return end.score



def solve_b(input: str) -> int | str | None:
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
