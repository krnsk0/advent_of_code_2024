# https://adventofcode.com/2024/day/3
import re

useRealInput = True

with open('input_1.txt' if useRealInput else 'input_0.txt', 'r') as file:
    contents = file.read()

out = 0
pattern = r"mul\(\d+,\d+\)"
matches = re.findall(pattern, contents)
for match in matches:
    pre, post = match.split(',')
    first = int(pre[4:])
    second = int(post[0:-1])
    product = first * second
    print(first, second)
    out += product

print('first solution', out)