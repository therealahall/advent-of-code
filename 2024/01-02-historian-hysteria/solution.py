left_list = []
right_list = []
with open("input.txt", "r") as file:
    for line in file:
        file_input = line.strip().split()
        left, right = map(int, file_input)
        left_list.append(left)
        right_list.append(right)

similarity = 0
for left in left_list:
    similarity += left * right_list.count(left)

print(similarity)
