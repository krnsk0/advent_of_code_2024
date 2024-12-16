# https://adventofcode.com/2024/day/15
from _helpers import get_input, get_matrix
import os

HIGHLIGHT = "\033[92m\033[1m"
ENDC = "\033[0m"


def print_matrix(matrix):
    for i, row in enumerate(matrix):
        print(
            "".join(str(n) if n != "@" else f"{HIGHLIGHT}{str(n)}{ENDC}" for n in row)
        )


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


def get_left_bracket(matrix, x, y):
    if matrix[y][x] == "]":
        return (x - 1, y)
    if matrix[y][x] == "[":
        return (x, y)


def get_right_bracket(matrix, x, y):
    if matrix[y][x] == "]":
        return (x, y)
    if matrix[y][x] == "[":
        return (x + 1, y)


def get_box_set(matrix, x, y, dir):
    # print(f"get_box_set {(x, y)}, dir {dir}")
    # only push left brackets
    s = set()
    left = get_left_bracket(matrix, x, y)
    right = get_right_bracket(matrix, x, y)

    # add self
    s.add(left)

    # get set above left bracket
    nextLeft = get_next(*left, dir)
    if matrix[nextLeft[1]][nextLeft[0]] in ("[", "]"):
        leftBracketBoxes = get_box_set(matrix, *nextLeft, dir)
        for box in leftBracketBoxes:
            s.add(box)

    # get set above right bracket
    nextRight = get_next(*right, dir)
    if matrix[nextRight[1]][nextRight[0]] in ("[", "]"):
        leftBracketBoxes = get_box_set(matrix, *nextRight, dir)
        for box in leftBracketBoxes:
            s.add(box)
    return s


def can_set_move(matrix, s, dir) -> bool:
    """
    given a set of boxes, find only those boxes in the set with no boxes
    in front of them, the "terminal" boxes in the direction we are moving
    """
    # print("can_set_move in dir", dir)

    # bx is always left bracket
    for bx, by in s:
        left_next = get_next(bx, by, dir)
        right_next = get_next(bx + 1, by, dir)
        if (
            matrix[left_next[1]][left_next[0]] == "#"
            or matrix[right_next[1]][right_next[0]] == "#"
        ):
            return False
    return True


def move_box_set(matrix, s, dir):
    # print(f"move_box_set called in dir {dir} with s", s)
    # first need to sort the set by y
    asc = sorted(list(s), key=lambda box: box[1])
    if dir == "v":
        asc = reversed(asc)

    dy = -1 if dir == "^" else 1
    # bx is always left bracket
    for bx, by in asc:
        matrix[by][bx] = "."
        matrix[by][bx + 1] = "."
        matrix[by + dy][bx] = "["
        matrix[by + dy][bx + 1] = "]"


def move_box_up_down(matrix, dir, x, y):
    # print(f"move_box_up_down {(x, y)}, dir {dir}, char {matrix[y][x]}")
    s = get_box_set(matrix, x, y, dir)
    # print("boxes in set:", s)
    can_move = can_set_move(matrix, s, dir)
    if can_move:
        move_box_set(matrix, s, dir)
        # print("DEBUG AFTER MOVE")
        # print_matrix(matrix)


def move(matrix, dir, x, y):
    # print(f"moved called for {dir}, {(x, y)}, chr {matrix[y][x]}")
    nx, ny = get_next(x, y, dir)

    # pushing for left/right moves is easy
    if dir in ("<", ">"):
        if matrix[ny][nx] in ("[", "]"):
            move(matrix, dir, nx, ny)

    # pushing for up/down moves
    if dir in ("^", "v"):
        if matrix[ny][nx] in ("[", "]"):
            move_box_up_down(matrix, dir, nx, ny)

    # do the actual move for this char
    cur = matrix[y][x]
    if cur == "@" or dir in ("<", ">"):
        # only check for next square free
        if matrix[ny][nx] == ".":
            matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]


def get_checksum(matrix):
    total = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            char = matrix[y][x]
            if char == "[":
                total += y * 100 + x

    return total


def solve(input_str):
    matrix, moves = parse_input(input_str)
    print("input", "".join(moves))
    print_matrix(matrix)

    for i, dir in enumerate(moves):
        move(matrix, dir, *find_robot(matrix))
        os.system("clear")
        print(f"\n************ Move {dir}; {i}:")
        print_matrix(matrix)

    print("\nfinal")
    print_matrix(matrix)

    return get_checksum(matrix)


print("\npart 2 solution:", solve(get_input(use_real=True)))
