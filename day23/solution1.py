# https://adventofcode.com/2024/day/23
from collections import defaultdict
from _helpers import get_input


def parse_input(inputStr):
    return [tuple(pair.split("-")) for pair in inputStr.split("\n")]


def solve(inputStr):
    pairs = parse_input(inputStr)
    connections = defaultdict(list)
    comps = set()

    for first, second in pairs:
        comps.add(first)
        comps.add(second)
        connections[first].append(second)
        connections[second].append(first)

    threes = set()

    for n1 in comps:
        for n2 in connections[n1]:
            for n3 in connections[n2]:
                if n1 in connections[n3]:
                    threes.add(tuple(sorted((n1, n2, n3))))

    threes_with_t = [t for t in threes if any([c.startswith("t") for c in t])]

    return len(threes_with_t)


print("\npart 1 solution:", solve(get_input(use_real=True)))
