# https://adventofcode.com/2024/day/23
from collections import defaultdict
from _helpers import get_input


def parse_input(inputStr):
    return [tuple(pair.split("-")) for pair in inputStr.split("\n")]


def solve(inputStr):
    pairs = parse_input(inputStr)
    comps = set()
    connections = defaultdict(dict)

    # get list of all computers
    for first, second in pairs:
        if first not in comps:
            comps.add(first)
        if second not in comps:
            comps.add(second)

    # build up adjacendy matrix
    for first, second in pairs:
        connections[first][second] = 1
        connections[second][first] = 1

    print("CONNECTIONS:")
    for key, val in connections.items():
        print(key, val)

    groups = [[x] for x in list(comps)]

    # for each computer name, we want to check each existing group to see if the name is connected to all members of the group. if so, add it
    for name in comps:
        print("\nCHECKING", name)
        for group in groups:
            print("should join group?", group)
            add_to_group = True
            for member in group:
                if member not in connections or name not in connections[member]:
                    add_to_group = False
            if add_to_group:
                group.append(name)
                print("ADDED", group)

    groups.sort(key=lambda x: len(x), reverse=True)

    print("\nGROUPS")
    print(groups)

    largest = sorted(groups[0])
    return ",".join(largest)


print("\npart 1 solution:", solve(get_input(use_real=True)))
