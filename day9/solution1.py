# https://adventofcode.com/2024/day/9
from collections import defaultdict

from _helpers import get_input



def getStr(input):
    out = ''
    id = 0
    for i, c in enumerate(input):
        n = int(c)
        if i % 2 == 0:
            out += str(id) * n
            id += 1
        else:
            out += '.' * n
    return out

def solve(input):
    print(getStr(input))
    i = 0
    while i < len(input):
        break


useRealInput = False
print("\npart 1 solution:", solve(get_input(use_real=True)))