left_list = []
right_list = []
with open("input.txt", "r") as file:
    for line in file:
        file_input = line.strip().split()
        left, right = map(int, file_input)
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

total_distance = 0
for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

print(total_distance)
