# https://adventofcode.com/2024/day/15
from _helpers import get_input, get_matrix, print_matrix


def parse_input(input):
    mapStr, moveStr = input.split("\n\n")
    matrix = get_matrix(mapStr)
    moves = list(moveStr.replace("\n", ""))
    return (matrix, moves)


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


def move(matrix, dir, x, y) -> bool:
    """
    returns a boolean signifying whether anything changed as a
    result of the move call
    """
    nx, ny = get_next(x, y, dir)
    next = matrix[ny][nx]

    if next == ".":
        matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
        return True
    if next == "O":
        changed = move(matrix, dir, nx, ny)
        if changed:
            return move(matrix, dir, x, y)


def get_coordinate_sum(matrix):
    total = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "O":
                total += 100 * y + x
    return total


def solve(input):
    matrix, moves = parse_input(input)
    print_matrix(matrix)
    print("")
    print("".join(moves))

    for dir in moves:
        move(matrix, dir, *find_robot(matrix))

    print("")
    print_matrix(matrix)

    return get_coordinate_sum(matrix)


print("\npart 1 solution:", solve(get_input(use_real=True)))
