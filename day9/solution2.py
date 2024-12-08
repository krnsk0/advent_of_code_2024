# https://adventofcode.com/2024/day/9
from collections import defaultdict

def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input


def solve(input):
    pass

useRealInput = True
print("\npart 1 solution:", solve(getInput(useRealInput)))