from ._type_aliases import Matrix


def copyMatrix(matrix: Matrix) -> Matrix:
    out = []
    for row in matrix:
        out.append(row[:])
    return out
