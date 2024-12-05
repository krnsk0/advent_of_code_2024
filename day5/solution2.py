# https://adventofcode.com/2024/day/5
import random

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

    violatedRules = []

    for first, second in rules:
        if first in hash and second in hash:
            if hash[first] > hash[second]:
                valid = False
                violatedRules.append((first, second))

    return valid, violatedRules

def conform(update, violatedRules):
    for first, second in violatedRules:
        firstIndex = update.index(first)
        secondIndex = update.index(second)
        update[firstIndex], update[secondIndex] = update[secondIndex], update[firstIndex]

def randomizeRuleOrder(violatedRules):
    random.shuffle(violatedRules)


def getAnswer(updates, rules):
    total = 0
    for update in updates:
        valid, violatedRules = isUpdateValid(update, rules)
        initiallyValid = valid

        while not valid:
            conform(update, violatedRules)
            valid, violatedRules = isUpdateValid(update, rules)
            randomizeRuleOrder(violatedRules)

        if not initiallyValid:
            total += getMiddleUpdate(update)

    return total


useRealInput = True
rules, updates = parseInput(getInput(useRealInput))
print('part 2 answer', getAnswer(updates, rules))

