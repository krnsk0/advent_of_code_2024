import os

def get_input(use_real=False):
    """
    Reads input from the specified folder (relative path).
    :param use_real: bool - If True, uses 'input_1.txt'; otherwise 'input_0.txt'.
    :return: str - The content of the input file.
    """
    filename = "input_1.txt" if use_real else "input_0.txt"
    file_path = os.path.join('day' + os.getenv('DAY'), filename)
    print(f"loading {file_path}...")
    with open(file_path, 'r') as file:
        return file.read()
