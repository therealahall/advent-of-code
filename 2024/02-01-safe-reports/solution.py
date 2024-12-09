def is_safe(report):
    if all(
        report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3
        for i in range(len(report) - 1)
    ):
        return True
    if all(
        report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3
        for i in range(len(report) - 1)
    ):
        return True
    return False


safe_reports = 0
with open("input.txt", "r") as file:
    for line in file:
        file_input = line.strip().split()
        numbers = list(map(int, file_input))
        if is_safe(numbers):
            safe_reports += 1

print(safe_reports)
