# https://adventofcode.com/2024/day/9
from collections import defaultdict

from _helpers import get_input

def getInput(useRealInput):
    with open('input_1.txt' if useRealInput else 'input_0.txt', 'r') as file:
        input = file.read()
    return input


def solve(input):
    pass

print("\npart 1 solution:", solve(get_input(use_real=True)))