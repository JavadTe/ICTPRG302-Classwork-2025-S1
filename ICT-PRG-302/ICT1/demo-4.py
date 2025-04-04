print("Welcome to Caesar cipher program")
name = input("What is your name? ")
print(name, "Hope you enjoy encrypting and decrypting words.")
letter =  input("Please give a letter to encrypt ")
shift = input("shift with how many characters: ")

try:
    shift = int(shift)
except:
    input("invalid shift, press any key to exit")
    quit()

if letter.isalpha():
    ord_value = ord(letter)
    ord_value = ord_value + shift
    answer = chr(ord_value)
    print("Caesar cypher letter is :", answer)
else:
    print("You entered a non alpha character.")

