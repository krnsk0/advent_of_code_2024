# https://adventofcode.com/2024/day/7

def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
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
                times = operand * result
                if times <= solution:
                    newResults.append(times)
                add = operand + result
                if add <= solution:
                    newResults.append(add)
                concat = int(str(result) + str(operand))
                if concat <= solution:
                    newResults.append(concat)
            results = newResults
        if solution in results:
            print('solved, adding', solution)
            total += solution

    return total

useRealInput = True
print("\npart 2 solution", solve(getInput(useRealInput)))