# https://adventofcode.com/2024/day/12
from _helpers import get_input, get_matrix, get_neighbors


def search_from_cell(matrix, x, y):
    height = len(matrix)
    width = len(matrix[0])
    search_letter = matrix[y][x]
    stack = [(x, y)]
    area = 0
    perimeter = 0
    seen = []

    while stack:
        cx, cy = stack.pop()
        seen.append((cx, cy))
        neighbors = get_neighbors(cx, cy)
        area += 1

        for nx, ny in neighbors:
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                perimeter += 1
            elif matrix[ny][nx] != search_letter:
                perimeter += 1
            elif matrix[ny][nx] == search_letter:
                if (nx, ny) not in seen:
                    stack.append((nx, ny))

    print("area", area)
    print("perimeter", perimeter)
    return area * perimeter


def solve(input):
    matrix = get_matrix(input)

    # this is R, with area 12 and perimeter 18, value 216
    value = search_from_cell(matrix, 0, 0)
    print("value", value)


print("\npart 1 solution:", solve(get_input(use_real=False)))
