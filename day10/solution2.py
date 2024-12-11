# https://adventofcode.com/2024/day/
from collections import defaultdict, deque

def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def getMatrix(input):
    return [[int(c) if c != '.' else '.' for c in row] for row in input.split('\n')]


def printMatrix(matrix):
    height = len(matrix)
    for y in range(height):
        print("".join(str(n) for n in matrix[y]))

def copyMatrix(matrix):
    height = len(matrix)
    out = []
    for y in range(height):
        out.append(matrix[y][:])
    return out

def getNeighbors(x, y, width, height):
    neighbors = []
    if y > 0:
        neighbors.append((x, y - 1)) # up
    if y < height - 1:
        neighbors.append((x, y + 1)) # down
    if x > 0:
        neighbors.append((x - 1, y)) # left
    if x < width - 1:
        neighbors.append((x + 1, y)) # right
    return neighbors


def walk(matrix, startX, startY):
    print("")
    print("Walk started from 0 at", (startX, startY))
    width = len(matrix[0])
    height = len(matrix)

    debug = [['.' for _ in range(width)] for _ in range(height)]
    pathsToNine = 0
    stack = [(startX, startY)]
    seen = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in seen:
            continue
        elevation = matrix[y][x]
        debug[y][x] = elevation
        neighbors = getNeighbors(x, y, width, height)

        if elevation == 9:
            pathsToNine += 1

        for nx, ny in neighbors:
            if matrix[ny][nx] == elevation + 1:
                stack.append((nx, ny))

    return pathsToNine


def solve(input):
    matrix = getMatrix(input)
    print("input")
    printMatrix(matrix)

    width = len(matrix[0])
    height = len(matrix)

    count = 0

    # print(walk(matrix, 2, 0))
    for startY in range(height):
        for startX in range(width):
            if matrix[startY][startX] == 0:
                count += walk(matrix, startX, startY)
    return count

useRealInput = True
print("\npart 1 solution:", solve(getInput(useRealInput)))