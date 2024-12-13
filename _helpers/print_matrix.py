from ._type_aliases import Matrix


def print_matrix(matrix: Matrix):
    for row in matrix:
        print("".join(str(n) for n in row))
