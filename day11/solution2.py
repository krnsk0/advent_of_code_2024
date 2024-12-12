# https://adventofcode.com/2024/day/0
import time
import math
from collections import defaultdict

from _helpers import get_input


def getInput(useRealInput):
    with open('input_1.txt' if useRealInput else 'input_0.txt', 'r') as file:
        input = file.read()
    return input

def digits(number):
    if number == 0:
        return 1
    else:
        return math.floor(math.log10(abs(number))) + 1

memo = {}
def process_stone(el):
    if el in memo: return memo[el]
    if el == 0:
        memo[el] = [1]
        return [1]
    elif digits(el) % 2 == 0:
        s = str(el)
        l = len(s)
        half = l // 2
        left = int(s[0:half])
        right = int(s[half:])
        memo[el] = [left, right]
        return [left, right]
    else:
        memo[el] = [el * 2024]
        return [el * 2024]


def solve(input):
    arr = [int(x) for x in input.split(' ')]
    dict = defaultdict(int)
    for n in arr:
        dict[n] += 1

    for tickIdx in range(75):
        print("")
        print(f"ticking {tickIdx}")
        nextDict = defaultdict(int)
        for stone, count in dict.items():
            result = process_stone(stone)
            for r in result:
                nextDict[r] += count
        dict = nextDict

    totalCount = 0
    for stone, count in dict.items():
        totalCount += count
    return totalCount

start_time = time.time()
solution = solve(get_input(use_real=True))
print("\npart 2 solution:", solution)
end_time = time.time()
print(f"took {end_time - start_time}")