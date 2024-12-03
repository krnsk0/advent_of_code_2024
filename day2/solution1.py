# https://adventofcode.com/2024/day/2


useRealInput = True

with open('input_1_real.txt' if useRealInput else 'input_0_test.txt', 'r') as file:
    contents = file.read()

totalSafe = 0

for line in contents.split('\n'):
    print("")
    levels = list(map(lambda x: int(x), line.split(' ')))
    print(levels)

    safe = True

    inc = levels[0] < levels[-1]

    last = None
    for l in levels:
        if last != None:
            if l > last and not inc:
                safe = False
                break
            if l < last and inc:
                safe = False
                break
            diff = abs(l - last)
            if diff < 1 or diff > 3:
                safe = False
        last = l

    if safe:
        totalSafe += 1
    print("safe?", safe)


print("\nPart 1 solution", totalSafe)