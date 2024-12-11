# https://adventofcode.com/2024/day/0
import time
import math


def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def digits(number):
    if number == 0:
        return 1
    else:
        return math.floor(math.log10(abs(number))) + 1

def tick(arr):
    out = []
    for el in arr:
        if el == 0:
            out.append(1)
        elif digits(el) % 2 == 0:
            s = str(el)
            l = len(s)
            half = l // 2
            left = int(s[0:half])
            right = int(s[half:])
            out.append(left)
            out.append(right)
        else:
            out.append(el * 2024)
    return out

def solve(input):
    arr = [int(x) for x in input.split(' ')]
    for tickIdx in range(25):
        print(f"ticking {tickIdx}; len {len(arr)}")
        arr = tick(arr)
    return len(arr)

start_time = time.time()
useRealInput = True
print("\npart 1 solution:", solve(getInput(useRealInput)))
end_time = time.time()
print(f"took {end_time - start_time}")