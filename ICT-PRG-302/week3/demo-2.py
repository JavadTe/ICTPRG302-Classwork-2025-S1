n = 10
import random
secret = random.randint( 0, 100 )

DEBUG = False

while n > 0:

    print("You have", n," times let to try to find the number")
    if n == 10:
        print("Chose a number from 0 to 100")
    else:
        print("Try again. Chose a number from 0 to 100")

    if DEBUG:
        print(secret)
    userinput = input("?")

    n = n - 1

    try:
        userinput = int(userinput)
    except:
        input("your did not use a number")
        quit()

    if userinput < secret:
        print("Guess higher ")
    elif userinput > secret:
        print("Guss lower")
    else:
        print("******** well done", userinput, " is the correct number. ********")
        break


# print ("your number is: ",userinput ," The secret number is ", secret)
