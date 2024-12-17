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


def debug(state):
    print(f"A: {state.a}\nB: {state.b}\nC: {state.c}")
    print(f"Pointer: {state.pointer}")
    # print(f"Output: {state.output}")
    print(f"Program: {state.program}")


def get_combo_operand(state, operand):
    result = None
    if 0 <= operand <= 3:
        result = operand
    if operand == 4:
        result = state.a
    if operand == 5:
        result = state.b
    if operand == 6:
        result = state.c
    if operand == 7:
        raise "7 is not valid combo operator"
    # print("get_combo_operand", state.a, state.b, state.c, "returning", result)
    return result


VERBOSE = True


def adv(state, operand):
    result = int(state.a / (2 ** get_combo_operand(state, operand)))
    VERBOSE and print("adv; result in A:", result)
    state.a = result


def bxl(state, operand):
    result = state.b ^ operand
    VERBOSE and print("bxl; result in B:", result)
    state.b = result


def bst(state, operand):
    result = get_combo_operand(state, operand) % 8
    VERBOSE and print("bst; result in B:", result)
    state.b = result


def jnz(state, operand):
    if state.a == 0:
        VERBOSE and print("jnz; no action")
        return None
    else:
        VERBOSE and print("jnz; jumping to", operand)
        state.pointer = operand
        return True


def bxc(state, operand):
    result = state.b ^ state.c
    VERBOSE and print("bxc; result in B:", result)
    state.b = result


def out(state, operand):
    result = get_combo_operand(state, operand) % 8
    VERBOSE and print("out; result in out", result)
    state.output.append(result)


def bdv(state, operand):
    result = int(state.a / (2 ** get_combo_operand(state, operand)))
    VERBOSE and print("bdv; result in B:", result)
    state.b = result


def cdv(state, operand):
    result = int(state.a / (2 ** get_combo_operand(state, operand)))
    VERBOSE and print("cdv; result in C:", result)
    state.c = result


opcode_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def get_output_at_halt(state):
    # print(f"Program: {state.program}\n")
    # debug(state)
    # print("")

    while state.pointer < len(state.program):
        # print("")
        opcode = state.program[state.pointer]
        operand = state.program[state.pointer + 1]
        jumped = opcode_map[opcode](state, operand)

        if jumped is None:
            state.pointer += 2
        # debug(state)
        # input("press any key")

    VERBOSE and print("")
    VERBOSE and print("HALTED")
    VERBOSE and debug(state)
    return state.output


def solve(inputStr):
    # website said 1_999_999 is too low
    # website said 9_990_000 is too low
    for i in range(37283687):
        state = get_initial_state(inputStr)
        state.a = i
        if i % 10_000 == 0:
            print(f"*** Trying", i)
        output = get_output_at_halt(state)
        if state.program == output:
            return i
    return None


# not working, brute force will take way too long here
print("\npart 2 solution:", solve(get_input(use_real=False)))
