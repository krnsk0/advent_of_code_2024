from typing import Optional, Union


def get_neighbors(
    x: int, y: int, matrix: Optional[list[list[Union[int, str]]]] = None
) -> list[tuple[int, int]]:
    """
    Get the neighboring coordinates of a given coordinate in a 2D grid.

    Args:
      coord (tuple[int, int]): A tuple representing the (x, y) coordinate.
      matrix (Optional[list[list[Union[int, str]]]]): A 2D list representing the grid. If provided,
      the function will return only the neighbors that are within the bounds of the grid.

    Returns:
      list[tuple[int, int]]: A list of tuples representing the neighboring coordinates in the order of
      up, right, down, and left. If a matrix is provided, only valid neighbors within the
      grid bounds are returned.
    """
    neighbors = []

    potential_neighbors = [
        (x, y - 1),  # up
        (x + 1, y),  # right
        (x, y + 1),  # down
        (x - 1, y),  # left
    ]

    for nx, ny in potential_neighbors:
        if matrix is None or (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])):
            neighbors.append((nx, ny))

    return neighbors


assert get_neighbors(1, 1) == [(1, 0), (2, 1), (1, 2), (0, 1)]
assert get_neighbors(0, 0) == [(0, -1), (1, 0), (0, 1), (-1, 0)]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

assert get_neighbors(1, 1, matrix) == [(1, 0), (2, 1), (1, 2), (0, 1)]
assert get_neighbors(0, 0, matrix) == [(1, 0), (0, 1)]
assert get_neighbors(2, 2, matrix) == [(2, 1), (1, 2)]
