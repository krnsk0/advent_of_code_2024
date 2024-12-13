# https://adventofcode.com/2024/day/12
from _helpers import get_input, get_matrix

def solve(input):
    matrix = get_matrix(input)
    print(matrix)

use_real = False
print("\npart 1 solution:", solve(get_input(use_real=False)))