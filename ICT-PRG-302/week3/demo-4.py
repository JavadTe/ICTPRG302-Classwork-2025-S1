count = 0


string = input("Please provide some string")
target = input("Please provide a target letter")


found = False
for character in string:
    if character == target:
        found = True
        count = count + 1


if found:
    print("found the " + target + " in " + string )
    print("There are " + str(count) + " in the string")
else:
    print ("Not found")