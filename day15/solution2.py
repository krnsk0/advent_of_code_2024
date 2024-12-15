# https://adventofcode.com/2024/day/15
from _helpers import get_input, get_matrix, print_matrix


def parse_input(input):
    mapStr, moveStr = input.split("\n\n")
    matrix = get_matrix(mapStr)
    largerMatrix = [[] for _ in range(len(matrix))]
    for y in range(len(matrix)):
        row = largerMatrix[y]
        for x in range(len(matrix[0])):
            c = matrix[y][x]
            if c in (".", "#"):
                row.append(c + c)
            elif c == "@":
                row.append("@.")
            elif c == "O":
                row.append("[]")

    moves = list(moveStr.replace("\n", ""))
    return (largerMatrix, moves)


def find_robot(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == "@":
                return (x, y)
    return None


def get_next(x, y, dir):
    if dir == "^":
        return (x, y - 1)
    if dir == ">":
        return (x + 1, y)
    if dir == "v":
        return (x, y + 1)
    if dir == "<":
        return (x - 1, y)


def solve(input):
    matrix, moves = parse_input(input)
    print_matrix(matrix)
    print("")
    print("".join(moves))

    print("")
    print_matrix(matrix)

    return 0


print("\npart 1 solution:", solve(get_input(use_real=False)))
