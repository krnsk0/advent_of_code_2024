from typing import Union

def get_matrix(input: str, convert_to_num=False) -> list[list[Union[int, str]]]:
    return [[int(cell) if convert_to_num else cell for cell in list(row)] for row in input.split('\n')]
