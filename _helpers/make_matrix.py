from ._type_aliases import Matrix


def make_matrix(width: int, height: int, char: str = ".") -> Matrix:
    """
    generate matrix of `width`, `height` initialized to `char`
    """
    return [[char for _ in range(width)] for _ in range(height)]
