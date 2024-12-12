# https://adventofcode.com/2024/day/1

from collections import Counter


with open('input.txt', 'r') as file:
    contents = file.read()

output = 0
list1 = []
list2 = []

for line in contents.split('\n'):
    n1, n2 = line.split('   ')
    list1.append(n1)
    list2.append(n2)


list1.sort()
list2.sort()

for i in range(len(list1)):
    output += abs(int(list1[i]) - int(list2[i]))

print("part 1 solution:", output)

l2Counter = Counter(list2)

for n in list1:
    score = int(n) * l2Counter[n]
    output += score

print("part 2 solution:", output)