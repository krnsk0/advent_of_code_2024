import os

def get_input(use_real_input):
    """
    Reads input from the specified folder (relative path).
    :param use_real_input: bool - If True, uses 'input_1_real.txt'; otherwise 'input_0_test.txt'.
    :return: str - The content of the input file.
    """
    filename = "input_1_real.txt" if use_real_input else "input_0_test.txt"
    file_path = os.path.join('day' + os.getenv('DAY'), filename)
    print(f"loading {file_path}...")
    with open(file_path, 'r') as file:
        return file.read()
