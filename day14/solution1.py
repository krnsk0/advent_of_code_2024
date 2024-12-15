# https://adventofcode.com/2024/day/14
from _helpers import copy_matrix, get_input, make_matrix, print_matrix


def parse_input(input):
    # (x, y, dx, dy)
    out = []
    for line in input.split("\n"):
        ps, vs = line.split(" ")
        x, y = ps[2:].split(",")
        dx, dy = vs[2:].split(",")
        out.append([int(x), int(y), int(dx), int(dy)])
    return out


def place_robots(matrix, robots):
    for x, y, dx, dy in robots:
        if matrix[y][x] == ".":
            matrix[y][x] = 0
        matrix[y][x] += 1
    return matrix


def tick(robots, width, height):
    for robot in robots:
        x, y, dx, dy = robot
        robot[0] = (x + dx) % width
        robot[1] = (y + dy) % height


def get_safety_factor(matrix, width, height):
    factors = [0] * 4
    halfWidth = width // 2
    halfHeight = height // 2
    for y in range(height):
        for x in range(width):
            if matrix[y][x] != ".":
                # upper left
                if x < halfWidth and y < halfHeight:
                    factors[0] += int(matrix[y][x])
                # upper right
                if x > halfWidth and y < halfHeight:
                    factors[1] += int(matrix[y][x])
                # lower left
                if x < halfWidth and y > halfHeight:
                    factors[2] += int(matrix[y][x])
                # lower right
                if x > halfWidth and y > halfHeight:
                    factors[3] += int(matrix[y][x])
    factor = 1
    for f in factors:
        factor *= f
    return factor


def solve(input, width, height):
    print(f"width={width}")
    print(f"height={height}")
    print("")
    matrix = make_matrix(width, height)
    robots = parse_input(input)

    TICKS_TO_RUN = 10000
    SEARCH_SUM = 30

    for t in range(TICKS_TO_RUN):
        tick(robots, width, height)
        copy = place_robots(copy_matrix(matrix), robots)

        for y in range(height):
            nonZeroCount = 0
            for x in range(width):
                if copy[y][x] == ".":
                    nonZeroCount = 0
                else:
                    nonZeroCount += 1
                if nonZeroCount == SEARCH_SUM:
                    print_matrix(place_robots(copy_matrix(matrix), robots))
                    return t


use_real = True
print(
    "\npart 1 solution:",
    solve(get_input(use_real), 101 if use_real else 11, 103 if use_real else 7),
)
