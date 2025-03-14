# Caesar-cipher
#
# With functions

# welcome function:
#   display program introduction message
#   obtain user name
#   welcome message with user name
#   return user name

def welcome():
    print("Caesar Cipher")
    username = input("enter your name : \n")
    print("welcome ", username)
    return username

# encrypt function:
#   parameters: letter and shift
#   determine encrypted character
#   return encrypted character

def encrypt(letter, shift):

    if letter.isalpha():
        answer = chr(ord(letter)+ shift)
    else:
        answer = letter
    return answer



# main program
#
# call welcome function
welcome()
# ask user for letter and shift
letter = input("Letter to encrypt")
# if shift cannot be converted to an integer

#   display error message,
#   encrypted character = letter
# else
#   call encrypted function
# display encrypted character