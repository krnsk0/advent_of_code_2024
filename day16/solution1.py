# https://adventofcode.com/2024/day/16
from collections import deque
import os
from _helpers import get_input, get_matrix, get_neighbors, print_matrix


def solve(inputStr):
    matrix = get_matrix(inputStr)
    height = len(matrix)
    width = len(matrix[0])
    print("INPUT:")
    print_matrix(matrix)
    print("")

    sx, sy = 1, height - 2
    ex, ey = width - 2, 1
    sched = set()  # x,y. don't scehdule twice
    sched.add((sx, sy))
    queue = deque()  # queue x,y,score,dir
    queue.append((sx, sy, 0, 1))
    scores = []

    while queue:
        print("")
        # os.system("clear")
        x, y, score, dir = queue.popleft()
        matrix[y][x] = "w"
        for new_dir, (nx, ny) in enumerate(get_neighbors(x, y)):
            if nx == ex and ny == ey:
                scores.append(score)
                continue
            if matrix[ny][nx] != "#" and (nx, ny) not in sched:
                matrix[ny][nx] = "s"
                sched.add((nx, ny))
                rotate_modifier = 1000 if new_dir != dir else 0
                queue.append((nx, ny, score + 1 + rotate_modifier, new_dir))
        # print_matrix(matrix)

    return min(scores) + 1


print("\npart 1 solution:", solve(get_input(use_real=True)))
