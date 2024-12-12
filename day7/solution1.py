# https://adventofcode.com/2024/day/7

from _helpers import get_input


def getInput(useRealInput):
    with open('input_1.txt' if useRealInput else 'input_0.txt', 'r') as file:
        input = file.read()
    return input

def solve(input):
    equations = []
    for line in input.split('\n'):
        solution, rest = line.split(': ')
        operands = rest.split(' ')
        equations.append((int(solution), [int(x) for x in operands]))

    total = 0

    for solution, operands in equations:
        print("")
        print(solution, operands)

        results = [operands[0]]
        for operand in operands[1:]:
            newResults = []
            for result in results:
                newResults.append(operand * result)
                newResults.append(operand + result)
            results = newResults
        if solution in results:
            total += solution

    return total


print("part 1 solution", solve(get_input(use_real=True)))