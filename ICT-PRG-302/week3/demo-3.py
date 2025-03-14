count = 0
string = "javadjayjay"
for character in string:
    count = count +1

print(count)

string = input("Please provide some string")
target = input("Please provide a target letter")

found = False
for character in string:
    if character == target:
        found = True
        break

if found:
    print("found it")
else:
    print ("Not found")

