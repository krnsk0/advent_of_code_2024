# https://adventofcode.com/2024/day/
from collections import defaultdict, deque

from _helpers import get_input

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

    queue = deque()
    seen = set()
    queue.append((startX, startY))
    nineCount = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        elevation = matrix[y][x]
        debug[y][x] = elevation


        if elevation == 9:
            nineCount += 1

        neighbors = getNeighbors(x, y, width, height)
        for nx, ny in neighbors:
            if matrix[ny][nx] == elevation + 1:
                queue.append((nx, ny))
    print('found nines:', nineCount)
    return nineCount


def solve(input):
    matrix = getMatrix(input)
    print("input")
    printMatrix(matrix)

    width = len(matrix[0])
    height = len(matrix)

    count = 0

    for startY in range(height):
        for startX in range(width):
            if matrix[startY][startX] == 0:
                count += walk(matrix, startX, startY)
    return count


print("\npart 1 solution:", solve(get_input(use_real=True)))