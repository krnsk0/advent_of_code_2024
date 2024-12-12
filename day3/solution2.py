# https://adventofcode.com/2024/day/3

import re

useRealInput = True

with open('input_1.txt' if useRealInput else 'input_0.txt', 'r') as file:
    contents = file.read()

out = 0
enabled = True
matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", contents)
for match in matches:
    if match == "don't()":
        enabled = False

    if match == "do()":
        enabled = True

    if match[0:3] == 'mul' and enabled:
        pre, post = match.split(',')
        first = int(pre[4:])
        second = int(post[0:-1])
        product = first * second
        out += product

print("part 2 solution", out)

