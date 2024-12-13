from ._type_aliases import Matrix


def print_matrix(matrix: Matrix, axes=False):
    if axes:
        # Print the column indices
        print("  " + "".join(str(i % 10) for i in range(len(matrix[0]))))

    for i, row in enumerate(matrix):
        if axes:
            # Print the row index
            print(str(i % 10) + " ", end="")
        print("".join(str(n) for n in row))
