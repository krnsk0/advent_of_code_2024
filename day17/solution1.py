# https://adventofcode.com/2024/day/17
from _helpers import get_input


def parse_input(input):
    split = input.split("\n")
    a = int(split[0].split(":")[1])
    b = int(split[1].split(":")[1])
    c = int(split[2].split(":")[1])
    programStr = split[4].split(":")[1]
    program = [int(x) for x in programStr.split(",")]
    return a, b, c, program


def debug(a, b, c, program):
    print(f"A: {a}\nB: {b}\nC: {c}")
    print("Program:", program)


def solve(input):
    a, b, c, program = parse_input(input)
    debug(a, b, c, program)


# sample out is 4,6,3,5,6,3,5,2,1,0
print("\npart 1 solution:", solve(get_input(use_real=False)))
