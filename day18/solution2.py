# https://adventofcode.com/2024/day/18
from collections import deque
from _helpers import copy_matrix, get_input, get_neighbors, make_matrix, print_matrix


def parse_input(input):
    return [
        (int(line.split(",")[0]), int(line.split(",")[1])) for line in input.split("\n")
    ]


def search_for_path(matrix):
    """
    perform BFS
    """
    # holds (x, y, distance)
    queue = deque()
    queue.append((0, 0, 0))
    seen = set()
    height = len(matrix)
    width = len(matrix[0])

    while queue:
        x, y, distance = queue.popleft()
        # matrix[y][x] = "O"
        if y == height - 1 and x == width - 1:
            return True

        neighbors = get_neighbors(x, y, matrix)
        for neighbor in neighbors:
            if neighbor in seen:
                continue
            nx, ny = neighbor
            if matrix[ny][nx] == "#":
                continue
            seen.add(neighbor)
            queue.append((nx, ny, distance + 1))

    return False


def solve(input, size=7):
    bytes = parse_input(input)
    matrix = make_matrix(size, size)
    copy = copy_matrix(matrix)

    for x, y in bytes:
        copy = copy_matrix(copy)
        copy[y][x] = "#"
        print("\napplied byte", (x, y))
        print("starting state:")
        print_matrix(copy)

        # search
        print("\nsolving...")
        solved = search_for_path(copy)
        print("final state:")
        print_matrix(copy)
        print("solved?", solved)

        # return
        if not solved:
            return (x, y)


use_real = True
print(
    "\npart 2 solution:",
    solve(
        get_input(use_real),
        size=71 if use_real else 7,
    ),
)
