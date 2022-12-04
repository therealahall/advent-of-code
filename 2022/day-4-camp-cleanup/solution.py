# https://adventofcode.com/2022/day/4

fullOverlap = 0
partialOverlap = 0
with open("input.txt", "r") as file:
    list = file.read().splitlines()
    for elfPairs in list:
        elfOne, elfTwo = elfPairs.split(",")
        elfOneStart, elfOneEnd = elfOne.split("-")
        elfTwoStart, elfTwoEnd = elfTwo.split("-")
        elfOneRange = range(int(elfOneStart), int(elfOneEnd)+1)
        elfTwoRange = range(int(elfTwoStart), int(elfTwoEnd)+1)
        if(set(elfOneRange).issubset(elfTwoRange) or set(elfTwoRange).issubset(elfOneRange)):
            fullOverlap += 1
        if(range(max(elfOneRange.start, elfTwoRange.start), min(elfOneRange.stop, elfTwoRange.stop))):
            partialOverlap += 1

print("Fully overlapping: " + str(fullOverlap))
print("Partially overlapping: " + str(partialOverlap))
