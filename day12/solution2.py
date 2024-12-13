# https://adventofcode.com/2024/day/12
from _helpers import copy_matrix, get_input, get_matrix, get_neighbors, print_matrix


def search_from_cell(matrix, x, y, global_seen):
    height = len(matrix)
    width = len(matrix[0])
    search_letter = matrix[y][x]
    stack = [(x, y)]
    area = 0
    perimeter = 0
    seen = set()

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in seen:
            continue
        seen.add((cx, cy))
        global_seen.add((cx, cy))
        neighbors = get_neighbors(cx, cy)
        area += 1
        thisPerimeter = 0

        # DEBUG
        copy = copy_matrix(matrix)
        copy[cy][cx] = "."
        print("walking", cx, cy)
        print("neighbors", neighbors)
        print_matrix(copy)

        for nx, ny in neighbors:
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                print("neighbor", (nx, ny), "is out of bounds; incrementing perimeter")
                thisPerimeter += 1
            elif matrix[ny][nx] != search_letter:
                print("neighbor", (nx, ny), "is another letter; incrementing perimeter")
                thisPerimeter += 1
            elif matrix[ny][nx] == search_letter:
                stack.append((nx, ny))
        perimeter += thisPerimeter

        # DEBUG
        print("perimeter of this cell", thisPerimeter)
        print("")

    print("TOTAL AREA", area)
    print("TOTAL PERIMETER", perimeter)
    return area * perimeter


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


print("\npart 1 solution:", solve(get_input(use_real=False)))
