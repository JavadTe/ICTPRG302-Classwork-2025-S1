#
file = open("romeo-juliet.txt","r")
for line_from_file in file:
    print(line_from_file.strip())
file.close()

file = open("romeo-juliet.txt","r")
quickdictionarie = {}
