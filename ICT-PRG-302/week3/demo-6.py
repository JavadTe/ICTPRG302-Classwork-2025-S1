import random
secret = random.randint( 0, 100 )


print(secret)
for number in range(10):
    print("you have used ", number, "of 9 attempted")
    print("Please enter number between 0 to 100")
    userinput = input("?")

    try:
        userinput = int(userinput)
    except:
        print("your did not use a number")
        continue

    if userinput == secret:
        print("well done")
        break
    elif userinput > secret:
        print("Go lower ")
    elif userinput < secret:
        print("Go higher")
    if number == 9:
        print("you lost. The answer was", secret)
        break