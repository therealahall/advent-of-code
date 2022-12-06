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
        boxes = crane[startingStack - 1][-boxesToMove:]
        del crane[startingStack - 1][-boxesToMove:]
        crane[endingStack - 1].extend(boxes)

output = ''
for stack in crane:
    output += str(stack[-1])

print(output)