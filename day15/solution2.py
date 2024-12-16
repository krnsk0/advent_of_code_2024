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
                row.append(c)
                row.append(c)
            elif c == "@":
                row.append("@")
                row.append(".")
            elif c == "O":
                row.append("[")
                row.append("]")

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


def move(matrix, dir, x, y):
    print(f"moved called for {dir}, {(x, y)}, chr {matrix[y][x]}")
    nx, ny = get_next(x, y, dir)

    # left/right moves are easy
    if dir in ("<", ">"):
        if matrix[ny][nx] in ("[", "]"):
            move(matrix, dir, nx, ny)
    if matrix[ny][nx] == ".":
        matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]


def solve(input):
    matrix, moves = parse_input(input)
    print_matrix(matrix)
    print("")
    print("".join(moves))

    move(matrix, "<", *find_robot(matrix))

    print("")
    print_matrix(matrix)

    return 0


print("\npart 1 solution:", solve(get_input(use_real=False)))
