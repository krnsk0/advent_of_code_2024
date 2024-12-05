# https://adventofcode.com/2024/day/4


def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def asMatrix(input):
    matrix = list(map(lambda x: list(x), input.split('\n')))
    return matrix

def getInnerValues(matrix):
    out = []
    size = len(matrix)
    for y in range(size - 2):
        for x in range(size - 2):
            out.append((x + 1, y + 1))
    return out

def isMas(matrix, coord):
    x, y = coord
    if matrix[y][x] != 'A': return False
    val = matrix[y - 1][x - 1] + matrix[y - 1][x + 1] + matrix[y + 1][x - 1] + matrix[y + 1][x + 1]
    return val in ('MSMS', 'MMSS', 'SMSM', 'SSMM')


def getAnswer(input):
    matrix = asMatrix(input)
    inner = getInnerValues(matrix)
    count = 0
    for coord in inner:
        if isMas(matrix, coord):
            count += 1
    return count


useRealInput = True
print(getAnswer(getInput(useRealInput)))
