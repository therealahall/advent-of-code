# https://adventofcode.com/2022/day/3

import string
def convertLetterToPriority(letter):
    return string.ascii_letters.index(letter) + 1

file = open("input.txt", "r")
list = file.read().replace("\n", ",").split(",")
score = 0
groupings = []
group = []

for i, line in enumerate(list):
    group.append(line)
    if((i + 1) % 3 == 0):
        groupings.append(group)
        group = []

for groups in groupings:
    commonalities = set(groups[0])&set(groups[1])&set(groups[2])
    for commonality in commonalities:
            score += convertLetterToPriority(commonality)
print(score)
