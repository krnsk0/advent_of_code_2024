# https://adventofcode.com/2024/day/4
import re

def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def countXmasInStrs(strs):
    count = 0
    for str in strs:
        count += len(re.findall(r"XMAS", str))
    return count

def getLeftToRight(input):
    return input.split('\n')

def getRightToLeft(input):
    return list(map(lambda x: x[::-1], input.split('\n')))

def getMatrix(input):
    matrix = list(map(lambda x: list(x), input.split('\n')))
    # (matrix, width/height)
    return (matrix, len(matrix))

def getTopToBottom(input):
    matrix, n = getMatrix(input)
    out = ['' for _ in range(n)]
    for y in range(n):
        for x in range(n):
            out[x] += matrix[y][x]
    return out

def getBottomToTop(input):
    val = getTopToBottom(input)
    return list(map(lambda x: x[::-1], val))

def getBottomLeftToTopRight(input):
    matrix, n = getMatrix(input)
    out = ['' for _ in range(n * 2 - 1)]
    for y in range(n - 1, -1, -1):
        for x in range(n):
            total = x + y
            out[total] += matrix[y][x]
    return out

def getTopRightToBottomLeft(input):
    val = getBottomLeftToTopRight(input)
    return list(map(lambda x: x[::-1], val))

def getTopLeftToBottomRight(input):
    # first flip horizontally in place
    matrix, n = getMatrix(input)
    for y in range(n // 2):
        for x in range(n):
            matrix[y][x], matrix[n - y - 1][x] = matrix[n - y - 1][x], matrix[y][x]

    # then get diagonals
    out = ['' for _ in range(n * 2 - 1)]
    for y in range(n - 1, -1, -1):
        for x in range(n):
            total = x + y
            out[total] += matrix[y][x]
    return out

def getBottomRightToTopLeft(input):
    val = getTopLeftToBottomRight(input)
    return list(map(lambda x: x[::-1], val))

def getAll(input):
    return [
        *getLeftToRight(input),
        *getRightToLeft(input),
        *getTopToBottom(input),
        *getBottomToTop(input),
        *getBottomLeftToTopRight(input),
        *getTopRightToBottomLeft(input),
        *getTopLeftToBottomRight(input),
        *getBottomRightToTopLeft(input),
    ]


useRealData = True
count = countXmasInStrs(getAll(getInput(useRealData)))
print('part 1 solution', count)
