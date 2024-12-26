# https://adventofcode.com/2024/day/24
from collections import defaultdict
from _helpers import get_input

operators = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}


def parse(inputStr):
    top, bottom = inputStr.split("\n\n")

    state = defaultdict(int)
    for line in top.split("\n"):
        label, value = line.split(":")
        state[label] = int(value)

    # (a, b, operator, output)
    connections = []
    z_prefixes = []
    for line in bottom.split("\n"):
        sources, dest = line.split(" -> ")
        a, operator, b = sources.split(" ")
        connections.append((a, b, operator, dest))
        if dest.startswith("z"):
            z_prefixes.append(dest)

    z_prefixes.sort(key=lambda s: int(s[1:]))

    return state, connections, z_prefixes


def is_computation_complete(state, z_prefixes):
    complete = True
    for item in z_prefixes:
        if item not in state:
            complete = False
    return complete


def get_sum(state, z_prefixes):
    buffer = ""
    for item in z_prefixes:
        buffer = str(state[item]) + buffer
    print("\nBUFFER", buffer)
    return int(buffer, 2)


def print_state(state):
    for item in state:
        print(item, state[item])


def solve(inputStr):
    state, connections, z_prefixes = parse(inputStr)

    print("\nINITIAL STATE")
    print_state(state)
    print("\nZ-PREFIXES", z_prefixes)
    print("")

    while not is_computation_complete(state, z_prefixes):
        for a, b, operator, output in connections:
            # print("running", a, b)
            if a in state and b in state:
                result = operators[operator](state[a], state[b])
                print(f"computing {a} {operator} {b}; {result} -> {output}")
                state[output] = result

    return get_sum(state, z_prefixes)


print("\npart 1 solution:", solve(get_input(use_real=True)))
