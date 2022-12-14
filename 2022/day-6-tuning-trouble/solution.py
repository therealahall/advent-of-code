# https://adventofcode.com/2022/day/6

def findNonRepeatingCharacters(string, increment):
    counter = 0

    for i in string:
        substring = string[counter:counter+increment]
        if len(set(substring)) != len(substring):
            counter += 1
        else :
            return counter + increment

with open("input.txt", "r") as file:
    list = file.read().splitlines()
    for line in list:
        print(findNonRepeatingCharacters(line, 4))
        print(findNonRepeatingCharacters(line, 14))