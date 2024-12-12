# https://adventofcode.com/2024/day/8
from collections import defaultdict

from _helpers import get_input

def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def getMatrix(input):
    matrix = list(map(lambda x: list(x), input.split('\n')))
    # matrix, width, height
    return (matrix, len(matrix[0]), len(matrix))

def getAntennaMap(matrix, width, height):
    map = defaultdict(list)
    for y in range(height):
        for x in range(width):
            val = matrix[y][x]
            if val == '.': continue
            map[val].append((x, y))
    return map

def countAntinodes(map, width, height):
    antinodes = set()
    for antennas in map.values():
        for a1 in antennas:
            for a2 in antennas:
                if a1 == a2: continue
                xDiff = a1[0] - a2[0]
                yDiff = a1[1] - a2[1]
                nodeX = a1[0] + xDiff
                nodeY = a1[1] + yDiff
                if 0 <= nodeX < width and 0 <= nodeY < height:
                    antinodes.add((nodeX, nodeY))

    return len(antinodes)




def solve(input):
    matrix, width, height = getMatrix(input)
    map = getAntennaMap(matrix, width, height)
    return countAntinodes(map, width, height)

print("\npart 1 solution:", solve(get_input(use_real=True)))