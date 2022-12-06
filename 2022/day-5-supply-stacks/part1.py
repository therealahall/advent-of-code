# https://adventofcode.com/2022/day/5

import crane
crane = crane.crane

with open("input.txt", "r") as file:
    list = file.read().splitlines()
    for line in list:
        line = line.replace('move', '').replace('from', ',').replace('to', ',')
        boxesToMove, startingStack, endingStack = line.split(',')
        boxesToMove = int(boxesToMove.strip())
        startingStack = int(startingStack.strip())
        endingStack = int(endingStack.strip())
        for i in range(1, boxesToMove + 1):
            box = crane[startingStack - 1].pop()
            crane[endingStack - 1].append(box)

output = ''
for stack in crane:
    output += str(stack[-1])

print(output)