# https://adventofcode.com/2024/day/19
from _helpers import get_input, make_trie


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


def is_design_possible(towels: list[str], design: str) -> bool:
    # print(f"{design} :: is_design_possible")

    for i in range(0, len(design)):
        pre, post = divide(design, i)
        # print(f"{design} :: division", pre, post)
        if post == "":
            return True
        if pre in towels:
            # print(f"{design} :: {pre} is in towels")
            result = is_design_possible(towels, post)
            # print(f"{design} :: result of recursion {result}")
            if result:
                return True

    return False


def solve(input):
    towels, designs = parse(input)
    print("TOWELS", towels)
    print("")

    count = 0

    trie = make_trie(towels)

    # for design in designs:
    #     print("\nTRYING DESIGN", design)
    #     possible = is_design_possible(towels, design)
    #     print("possible?", possible)
    #     if possible:
    #         count += 1

    return count


print("\npart 1 solution:", solve(get_input(use_real=False)))
