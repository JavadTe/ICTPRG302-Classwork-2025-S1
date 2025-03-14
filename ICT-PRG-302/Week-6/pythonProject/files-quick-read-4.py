file_quick = open("quick.txt", "r")

quicklist = []

for line in file_quick:
    quicklist.append(line.strip())

print(quicklist)

