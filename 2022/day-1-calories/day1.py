def objectSort(e):
    return e['calories']


file = open("input.txt", "r")
list = file.read().replace("\n\n", "-").replace("\n", ",").split("-")
output = []
for key, line in enumerate(list):
    output.append({
        "elf": key + 1,
        "calories": sum(map(int, filter(None, line.split(","))))
    })
file.close()
output.sort(reverse=True, key=objectSort)
print(output)
