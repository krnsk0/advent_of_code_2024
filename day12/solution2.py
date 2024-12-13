# https://adventofcode.com/2024/day/12
from collections import deque
from _helpers import copy_matrix, get_input, get_matrix, get_neighbors, print_matrix


def get_side_label(x, y, nx, ny):
    if x == nx:
        if ny < y:
            return f"U"
        else:
            return f"D"
    if y == ny:
        if nx < x:
            return f"L"
        else:
            return f"R"


assert get_side_label(1, 1, 1, 0) == "U"
assert get_side_label(1, 1, 1, 2) == "D"
assert get_side_label(1, 1, 0, 1) == "L"
assert get_side_label(1, 1, 2, 1) == "R"


def search_from_cell(matrix, x, y, global_seen):
    height = len(matrix)
    width = len(matrix[0])
    search_letter = matrix[y][x]
    queue = deque()
    queue.append((x, y))
    area = 0
    seen = set()
    copy = copy_matrix(matrix)

    sides = {
        "U": set(),
        "D": set(),
        "L": set(),
        "R": set(),
    }
    sideCount = 0

    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) in seen:
            continue
        seen.add((cx, cy))
        global_seen.add((cx, cy))
        neighbors = get_neighbors(cx, cy)
        area += 1

        # DEBUG
        copy[cy][cx] = "."

        for nx, ny in neighbors:
            side_label = get_side_label(cx, cy, nx, ny)

            # found a side
            if (
                nx < 0
                or nx >= width
                or ny < 0
                or ny >= height
                or matrix[ny][nx] != search_letter
            ):
                sideSet = sides[side_label]
                sideSet.add((nx, ny))
                if side_label in ("U", "D"):
                    if (nx + 1, ny) not in sideSet and (
                        nx - 1,
                        ny,
                    ) not in sideSet:
                        sideCount += 1
                elif side_label in ("R", "L"):
                    if (nx, ny - 1) not in sideSet and (
                        nx,
                        ny + 1,
                    ) not in sideSet:
                        sideCount += 1

            elif matrix[ny][nx] == search_letter:
                queue.append((nx, ny))

    # print_matrix(copy, axes=True)
    # print("FOR LETTER", search_letter)
    # print("TOTAL AREA", area)
    # print("TOTAL SIDES", sideCount)
    return area * sideCount


def solve(input):
    matrix = get_matrix(input)
    global_seen = set()
    total_value = 0
    width = len(matrix[0])
    height = len(matrix)

    for y in range(height):
        for x in range(width):
            if (x, y) not in global_seen:
                value = search_from_cell(matrix, x, y, global_seen)
                total_value += value

    return total_value


# not yet working
print("\npart 1 solution:", solve(get_input(use_real=False)))
