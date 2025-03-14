hot = input("Is it hot today? (Y/N)").upper()
lecture = input("Do you have a lecture? (Y/N)").upper()

if hot == "Y":
    if lecture == "Y":
        print("Sorry, no swimming and surfing today.")
    else:
        print("What about going to the beach?")

# To reformat code in PyCharm use CTRL+ALT+L
