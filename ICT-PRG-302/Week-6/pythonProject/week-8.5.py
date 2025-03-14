value_dictionary ={
    1: "Hello",
    2: "goodbye",
    3: "Who is this?"
}
number = input("Write a number: \n")

if number in value_dictionary:
    value_dictionary[number] = value_dictionary[number]
print(value_dictionary)
print()

for key, message in value_dictionary.items():
    print(key, message)

    if key == number:
        print(message)
    else:
        print("the number is invalid")