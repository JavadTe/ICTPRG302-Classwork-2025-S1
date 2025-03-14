
import random
secret = random.randint( 0, 100 )

DEBUG = True



print("Chose a number from 0 to 100")
if DEBUG:
    print(secret)
userinput = input("?")


try:
    userinput = int(userinput)
except:
    input("your did not use a number")
    quit()

if userinput < secret:
    print("Guess lower")
elif userinput > secret:
    print("Guss higher")
else:
    print("well done", userinput , " is the corect number")

print ("your number is: ",userinput ," The secret number is ", secret)
