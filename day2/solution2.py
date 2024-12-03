# https://adventofcode.com/2024/day/2

useRealInput = True

with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
    contents = file.read()

totalSafe = 0


def isSafe(levels):
    print("checking", levels)
    inc = levels[0] < levels[-1]
    last = None
    for l in levels:
        if last != None:

            # all inc/dec?
            if l > last and not inc:
                return False
            if l < last and inc:
                return False

            # is jump ok?
            diff = abs(l - last)
            if diff < 1 or diff > 3:
                return False
        last = l
    return True

for line in contents.split('\n'):
    print("")
    levels = list(map(lambda x: int(x), line.split(' ')))

    # first attempt
    safe = isSafe(levels)

    # second attempt - brute force
    if not safe:
        for i in range(len(levels)):
            newLevels = [*levels]
            print(f"retrying without value {newLevels[i]}")
            del newLevels[i]
            if isSafe(newLevels):
                safe = True
                break;

    print(f"safe: {safe}")

    if safe:
        totalSafe += 1


print("\nPart 2 solution:", totalSafe)