# https://adventofcode.com/2024/day/5

from _helpers import get_input


def getInput(useRealInput):
    with open('input_1.txt' if useRealInput else 'input_0.txt', 'r') as file:
        input = file.read()
    return input

def printMatrix(matrix):
    for row in matrix:
        print(''.join(row))

def getMatrix(input):
    matrix = list(map(lambda x: list(x), input.split('\n')))
    # matrix, width, height
    return (matrix, len(matrix[0]), len(matrix))

def initialize(matrix, width, height):
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == '^':
                return (x, y)

def getNextSquare(x, y, dir):
    nx, ny = x, y
    if dir == 0:
        ny -= 1
    elif dir == 1:
        nx += 1
    elif dir == 2:
        ny += 1
    else:
        nx -= 1
    return nx, ny

def isObstacle(matrix, width, height, x, y):
    if 0 <= x < width and 0 <= y < height:
        return matrix[y][x] == '#'
    else: return False

def solve(input):
    matrix, width, height = getMatrix(input)
    x, y = initialize(matrix, width, height)
    direction = 0
    seen = set()

    print('INPUT:')
    printMatrix(matrix)
    print('')

    while 0 <= x < width and 0 <= y < height:
        seen.add((x, y))
        nx, ny = getNextSquare(x, y, direction)
        blocked = isObstacle(matrix, width, height, nx, ny)
        if blocked:
            direction += 1
            if direction == 4: direction = 0
        nx, ny = getNextSquare(x, y, direction)
        matrix[y][x] = 'X'
        x, y, = nx, ny

    printMatrix(matrix)
    return len(seen)



solution = solve(get_input(use_real=True))
print("part 1 solution", solution)