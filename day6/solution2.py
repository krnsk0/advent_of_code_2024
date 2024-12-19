# https://adventofcode.com/2024/day/5

from _helpers import copy_matrix, get_input, get_matrix, get_neighbors, print_matrix


def find_guard(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == "^":
                return (x, y)


def attempt_escape(matrix):
    x, y = find_guard(matrix)
    direction = 0
    walked = set()
    escape_path = set()
    escape_path.add((x, y))
    escape_path_ordered = []
    while True:
        if (x, y, direction) in walked:
            return (False, escape_path_ordered)
        walked.add((x, y, direction))
        if (x, y) not in escape_path:
            escape_path.add((x, y))
            escape_path_ordered.append((x, y))
        matrix[y][x] = "%"
        nx, ny = get_neighbors(x, y)[direction]
        if ny < 0 or ny >= len(matrix) or nx < 0 or nx >= len(matrix[0]):
            return (True, escape_path_ordered)
        if matrix[ny][nx] in ("#", "O"):
            # print("\nhit obstacle at", ny, nx, "dir is", direction)
            direction = (direction + 1) % 4
            # print_matrix(matrix)
            # print("new direction", direction)
            nx, ny = get_neighbors(x, y)[direction]
        x, y = nx, ny


def solve(inputStr):
    matrix = get_matrix(inputStr)
    print("INPUT:")
    print_matrix(matrix)
    print("")

    copy = copy_matrix(matrix)
    _, path = attempt_escape(copy)

    obstacle_position_count = 0

    for x, y in path:
        copy = copy_matrix(matrix)
        copy[y][x] = "O"
        print("\nput obstacle at", (x, y))
        escaped, _ = attempt_escape(copy)
        print("escaped?", escaped)
        if not escaped:
            print_matrix(copy)
            obstacle_position_count += 1

    return obstacle_position_count


# not working yet... 1519 is output?
print("\npart 2 solution", solve(get_input(use_real=True)))
