# https://adventofcode.com/2024/day/5

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
        return matrix[y][x] == '#' or matrix[y][x] == 'O'
    else: return False

def attemptEscape(matrix, width, height):
    x, y = initialize(matrix, width, height)
    initX, initY = x, y
    direction = 0
    obstaclePositions = set()
    pathPoints = set()


    while 0 <= x < width and 0 <= y < height:
        if (x, y) != (initX, initY):
            obstaclePositions.add((x, y))
        if (x, y, direction) in pathPoints:
            return (False, obstaclePositions)
        pathPoints.add((x, y, direction))
        nx, ny = getNextSquare(x, y, direction)
        blocked = isObstacle(matrix, width, height, nx, ny)
        if blocked:
            direction += 1
            if direction == 4: direction = 0
        nx, ny = getNextSquare(x, y, direction)
        matrix[y][x] = 'X'
        x, y, = nx, ny

    # escaped, obstaclePositions
    return (True, obstaclePositions)

def copyMatrix(matrix):
    out = []
    for row in matrix:
        out.append(row[:])
    return out

def solve(input):
    matrix, width, height = getMatrix(input)
    escaped, obstaclePositions = attemptEscape(copyMatrix(matrix), width, height)
    positions = 0

    for oX, oY in obstaclePositions:
        # print("\nputtting obstacle at", (oX, oY))
        copy = copyMatrix(matrix)
        copy[oY][oX] = 'O'
        # print("attempting escape...")
        escaped, _ = attemptEscape(copy, width, height)
        # printMatrix(copy)
        # print('escaped', escaped)
        if escaped == False:
            positions += 1
    return positions


useRealInput = True
# not working yet...
print("\npart 2 solution", solve(getInput(useRealInput)))