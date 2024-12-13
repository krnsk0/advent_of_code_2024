from typing import Union

def get_matrix(input: str, convert_to_num=False) -> list[list[Union[int, str]]]:
    return [[int(cell) if convert_to_num else cell for cell in list(row)] for row in input.split('\n')]

assert(get_matrix('123\n456\n789') == [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
])

assert(get_matrix('123\n456\n789', convert_to_num=True) == [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])