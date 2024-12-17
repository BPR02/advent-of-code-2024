import sys
from pathlib import Path

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from aoc_2024.util import run

YEAR = 2024
DAY = 17


class Operator:
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Reg:
    RA: int
    RB: int
    RC: int

    PC: int
    JMP: bool
    IO: list[int]

    def reset(): # type: ignore
        Reg.RA = 0
        Reg.RB = 0
        Reg.RC = 0

        Reg.PC = 0
        Reg.JMP = False
        Reg.IO = []


def solve_a(input: str) -> int | str | None:
    lines = input.splitlines()
    Reg.reset()
    Reg.RA = int(lines[0].removeprefix("Register A: "))
    Reg.RB = int(lines[1].removeprefix("Register B: "))
    Reg.RC = int(lines[2].removeprefix("Register C: "))

    ir = [int(x) for x in lines[4].removeprefix("Program: ").split(",")]

    while Reg.PC < len(ir):
        execute(ir[Reg.PC], ir[Reg.PC + 1])
        if not Reg.JMP:
            Reg.PC += 2
        else:
            Reg.JMP = False

    out = ""
    for n in Reg.IO:
        out += f"{n},"
    out = out[:-1]
    return out


def combo(operand: int):
    if operand == 7:
        print("ERROR: Combo Operand 7")
        return 7
    if operand <= 3:
        return operand
    match operand:
        case 4:
            return Reg.RA
        case 5:
            return Reg.RB
        case 6:
            return Reg.RC
        case _:
            print("ERROR: Combo Operand", operand)
    return -1


def execute(operator: int, operand: int):
    cmb: int = combo(operand)
    match operator:
        case Operator.ADV:  # RA ; RA, RB, RC, operand
            num = Reg.RA
            denom = pow(2, cmb)
            Reg.RA = num // denom
        case Operator.BXL:  # RB ; RB, operand
            Reg.RB = Reg.RB ^ operand
        case Operator.BST:  # RB ; RA, RB, RC, operand
            Reg.RB = cmb % 8
        case Operator.JNZ:  # PC ; RA
            if Reg.RA == 0:
                return
            Reg.PC = operand
            Reg.JMP = True
        case Operator.BXC:  # RB ; RB, RC
            Reg.RB = Reg.RB ^ Reg.RC
        case Operator.OUT:  # IO ; RA, RB, RC, operand
            Reg.IO.append(cmb % 8)
            # print(Reg.IO)
        case Operator.BDV:  # RB ; RA, RB, RC, operand
            num = Reg.RA
            denom = pow(2, cmb)
            Reg.RB = num // denom
        case Operator.CDV:  # RC ; RA, RB, RC, operand
            num = Reg.RA
            denom = pow(2, cmb)
            Reg.RC = num // denom
        case _:
            print("ERROR: Operator", operator)


def solve_b(input: str) -> int | str | None:
    Reg.reset()
    lines = input.splitlines()
    ir = [int(x) for x in lines[4].removeprefix("Program: ").split(",")]

    return find_bits(0, 0, ir)


def find_bits(running: int, index: int, ir: list[int]):
    # assumption that all inputs end with
    # dividing RA by 8 and looping to beginning
    index += 1
    for guess in range(8):
        guess += running << 3
        check = run_prog(ir, guess, 0, 0)
        if check == ir:
            return guess
        if check == ir[-index:]:
            # print(running)
            res = find_bits(guess, index, ir)
            if res is not None:
                return res
    return None


def run_prog(ir: list[int], ra: int, rb: int, rc: int):
    Reg.reset()
    Reg.RA = ra
    Reg.RB = rb
    Reg.RC = rc
    while Reg.PC < len(ir):
        execute(ir[Reg.PC], ir[Reg.PC + 1])
        if not Reg.JMP:
            Reg.PC += 2
        else:
            Reg.JMP = False
    return Reg.IO


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Advent of Code")
    parser.add_argument("--notest", action="store_true", required=False)
    parser.add_argument("--retest", action="store_true", required=False)
    parser.add_argument("--manual", action="store_true", required=False)
    parser.add_argument("--part", action="store", required=False)
    args = parser.parse_args()
    run(YEAR, DAY, solve_a, solve_b, ~args.notest, args.retest, args.manual, args.part)
