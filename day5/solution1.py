# https://adventofcode.com/2024/day/5

from _helpers import get_input


def getInput(useRealInput):
    with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
        input = file.read()
    return input

def parseInput(input):
    (rawRules, rawUpdates) = input.split('\n\n')
    rules = list(map(lambda x: x.split('|'), rawRules.split('\n')))
    updates = list(map(lambda x: x.split(','), rawUpdates.split('\n')))
    return rules, updates

def getMiddleUpdate(update):
    if len(update) % 2 == 0: raise ValueError('even length')
    return int(update[len(update) // 2])


def isUpdateValid(update, rules):
    valid = True
    hash = {}
    for i, page in enumerate(update):
        hash[page] = i

    for first, second in rules:
        if first in hash and second in hash:
            if hash[first] > hash[second]:
                valid = False

    return valid

def getAnswer(updates, rules):
    total = 0
    for update in updates:
        if isUpdateValid(update, rules):
            total += getMiddleUpdate(update)
    return total



rules, updates = parseInput(get_input(use_real=True))
print('part 1 answer', getAnswer(updates, rules))

