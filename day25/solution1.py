# https://adventofcode.com/2024/day/25
from _helpers import get_input


def get_array(entry):
    matrix = entry.split("\n")
    out = [None] * 5
    for x in range(5):
        total = 0
        for y in range(7):
            if matrix[y][x] == "#":
                total += 1
        out[x] = total - 1
    return out


def parse(inputStr):
    entries = inputStr.split("\n\n")
    keys = []
    locks = []
    for entry in entries:
        if all([x == "#" for x in entry[0]]):
            locks.append(get_array(entry))
        else:
            keys.append(get_array(entry))
    return keys, locks


def does_key_fit(key, lock):
    for x in range(5):
        if key[x] + lock[x] >= 6:
            return False
    return True


def solve(inputStr):
    keys, locks = parse(inputStr)
    print("KEYS", keys)
    print("LOCKS", locks)

    count = 0
    for key in keys:
        for lock in locks:
            if does_key_fit(key, lock):
                count += 1

    return count


print("\npart 1 solution:", solve(get_input(use_real=True)))
