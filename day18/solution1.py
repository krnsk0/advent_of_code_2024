# https://adventofcode.com/2024/day/18
from collections import deque
from _helpers import get_input, get_neighbors, make_matrix, print_matrix


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
    path_length = 0
    seen = set()
    height = len(matrix)
    width = len(matrix[0])

    while queue:
        x, y, distance = queue.popleft()
        matrix[y][x] = "O"
        if y == height - 1 and x == width - 1:
            return distance, True

        neighbors = get_neighbors(x, y, matrix)
        for neighbor in neighbors:
            if neighbor in seen:
                continue
            nx, ny = neighbor
            if matrix[ny][nx] == "#":
                continue
            seen.add(neighbor)
            queue.append((nx, ny, distance + 1))

    return 0, False


def solve(input, size=7, bytes_to_fall=12):
    bytes = parse_input(input)
    matrix = make_matrix(size, size)

    # apply bytes to map
    for x, y in bytes[0:bytes_to_fall]:
        matrix[y][x] = "#"
    print("starting state:")
    print_matrix(matrix)

    # search
    path_length, solved = search_for_path(matrix)
    print("\nfinal state:")
    print_matrix(matrix)
    print("solved?", solved)
    return path_length


use_real = True
print(
    "\npart 2 solution:",
    solve(
        get_input(use_real),
        size=71 if use_real else 7,
        bytes_to_fall=1024 if use_real else 12,
    ),
)
