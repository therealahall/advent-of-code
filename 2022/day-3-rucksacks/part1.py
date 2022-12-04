# https://adventofcode.com/2022/day/3

import string
def convertLetterToPriority(letter):
    return string.ascii_letters.index(letter) + 1

file = open("input.txt", "r")
list = file.read().replace("\n", ",").split(",")
score = 0
for line in list:
    compartmentOne = line[:len(line)//2]
    compartmentTwo = line[len(line)//2:]
    commonalities = set(compartmentOne)&set(compartmentTwo)
    for commonality in commonalities:
        score += convertLetterToPriority(commonality)

print(score)
