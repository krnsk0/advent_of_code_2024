# https://adventofcode.com/2024/day/17
from _helpers import get_input


class State:
    a = 0
    b = 0
    c = 0
    program = []
    pointer = 0
    output = []


def get_initial_state(input):
    state = State()
    split = input.split("\n")
    state.a = int(split[0].split(":")[1])
    state.b = int(split[1].split(":")[1])
    state.c = int(split[2].split(":")[1])
    programStr = split[4].split(":")[1]
    state.program = [int(x) for x in programStr.split(",")]
    return state


def debug(state):
    print(f"A: {state.a}\nB: {state.b}\nC: {state.c}")
    print(f"Pointer: {state.pointer}")


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
    print("get_combo_operand", state.a, state.b, state.c, "returning", result)
    return result


def adv(state, operand):
    result = int(state.a / (2 ^ get_combo_operand(state, operand)))
    print("adv; result in A:", result)
    state.a = result


def bxl(state, operand):
    result = state.b ^ operand
    print("bxl; result in B:", result)
    state.b = result


def bst(state, operand):
    result = get_combo_operand(state, operand) % 8
    print("bst; result in B:", result)
    state.b = result


def jnz(state, operand):
    if state.a == 0:
        print("jnz; no action")
        return None
    else:
        print("jnz; jumping to", operand)
        state.pointer = operand
        return True


def bxc(state, operand):
    result = state.b ^ state.c
    print("bxc; result in B:", result)
    state.b = result


def out(state, operand):
    result = get_combo_operand(state, operand) * 8
    print("out; result in out", result)
    state.output.append(result)


def bdv(state, operand):
    result = int(state.a / (2 ^ get_combo_operand(state, operand)))
    print("bdv; result in B:", result)
    state.b = result


def cdv(state, operand):
    result = int(state.a / (2 ^ get_combo_operand(state, operand)))
    print("cdv; result in C:", result)
    state.c = result


opcode_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def solve(inputStr):
    state = get_initial_state(inputStr)
    print(f"Program: {state.program}\n")
    debug(state)
    print("")

    while state.pointer < len(state.program):
        opcode = state.program[state.pointer]
        operand = state.program[state.pointer + 1]
        jumped = opcode_map[opcode](state, operand)
        if jumped is None:
            state.pointer += 2
        # input("press any key")

    print("")
    print("HALTED")
    debug(state)
    print("Output:", state.output)


# sample out is 4,6,3,5,6,3,5,2,1,0
print("\npart 1 solution:", solve(get_input(use_real=False)))
