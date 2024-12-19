# https://adventofcode.com/2024/day/17
from _helpers import get_input


def get_initial_state(input):
    class State:
        a = 0
        b = 0
        c = 0
        program = []
        pointer = 0
        output = []

    state = State()
    split = input.split("\n")
    state.a = int(split[0].split(":")[1])
    state.b = int(split[1].split(":")[1])
    state.c = int(split[2].split(":")[1])
    state.program = [int(x) for x in split[4].split(":")[1].split(",")]
    state.pointer = 0
    state.output = []
    return state


def decompiled(a):
    out = []
    a = a
    b = 0
    c = 0
    while a != 0:
        b = (a % 8) ^ 3
        c = int(a / (2**b))
        b = (b ^ c) ^ 3
        a = int(a / (2**3))
        out.append(b % 8)
    return out


# binary search found this is the first that
# outputs the required 16 digits
low = 35184372088832


# binary search found this is the last that
# outputs the required 16 digits
high = 281474976710656


def solve(inputStr):
    state = get_initial_state(inputStr)
    print("=============>", state.program)
    print("program length", len(state.program))

    # main brute force
    for i in range(low, high):
        output = decompiled(i)
        if output == state.program:
            return i
        if i % 1_000_000 == 0:
            print(i)

    # val = high + 1
    # output = decompiled(val)
    # print(f"\nout for {val} is {output}")
    # print("out length", len(output))

    return None


# website said 1_999_999 is too low
# website said 9_990_000 is too low
print("\npart 2 solution:", solve(get_input(use_real=True)))
