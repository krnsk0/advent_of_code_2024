# https://adventofcode.com/2024/day/8
from collections import defaultdict

from _helpers import get_input

def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def printMatrix(matrix):
    for row in matrix:
        print(''.join(row))

def getMatrix(input):
    matrix = list(map(lambda x: list(x), input.split('\n')))
    # matrix, width, height
    return (matrix, len(matrix[0]), len(matrix))

def copyMatrix(matrix):
    out = []
    for row in matrix:
        out.append(row[:])
    return out

def getAntennaMap(matrix, width, height):
    map = defaultdict(list)
    for y in range(height):
        for x in range(width):
            val = matrix[y][x]
            if val == '.' or val == '#': continue
            map[val].append((x, y))
    return map

def countAntinodes(map, width, height, matrix):
    antinodes = set()
    for antennas in map.values():
        for a1 in antennas:
            for a2 in antennas:
                antinodes.add(a2)
                if a1 == a2: continue
                yDiff = a1[1] - a2[1]
                xDiff = a1[0] - a2[0]
                count = 1
                while True:
                    nodeX = a1[0] + (xDiff * count)
                    nodeY = a1[1] + (yDiff * count)
                    count += 1
                    if 0 <= nodeX < width and 0 <= nodeY < height:
                        antinodes.add((nodeX, nodeY))
                    else:
                        break

    copy = copyMatrix(matrix)
    for x, y in antinodes:
        copy[y][x] = '#'
    printMatrix(copy)


    return len(antinodes)


def solve(input):
    matrix, width, height = getMatrix(input)
    map = getAntennaMap(matrix, width, height)
    return countAntinodes(map, width, height, matrix)

print("\npart 2 solution:", solve(get_input(use_real=True)))