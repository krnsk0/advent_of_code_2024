# https://adventofcode.com/2024/day/19
from _helpers import get_input
from _helpers import Trie


def parse(input):
    t, d = input.split("\n\n")
    towels = [towel.strip() for towel in t.split(",")]
    designs = d.split("\n")
    return towels, designs


def divide(design, i):
    if len(design) == 1:
        return design, ""
    pre = design[0:i]
    post = design[i:]
    return pre, post


def is_design_possible(trie: Trie, design: str) -> bool:
    # print(f"{design} :: is_design_possible")

    for i in range(0, len(design)):
        pre, post = divide(design, i)
        # print(f"{design} :: division", pre, post)
        if pre == "":
            continue
        if post == "":
            return True
        if trie.has(pre):
            # print(f"{design} :: {pre} is in towels")
            result = is_design_possible(trie, post)
            # print(f"{design} :: result of recursion {result}")
            if result:
                return True

    return False


def solve(input):
    towels, designs = parse(input)
    print("TOWELS", towels)
    print("")

    count = 0

    trie = Trie(towels)

    for design in designs:
        print("\nTRYING DESIGN", design)
        possible = is_design_possible(trie, design)
        print("possible?", possible)
        if possible:
            count += 1

    return count


# runs forever on a single case for unknown reasons
# solution is either 399 or 400?
print("\npart 1 solution:", solve(get_input(use_real=True)))
