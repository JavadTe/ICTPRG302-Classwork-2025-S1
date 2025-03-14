print("What is the weather today?")
weather = input("Rain (R), Hot (H)? ").upper()

if weather == "R" and weather == "r":
    print("It is raining today")
    print("Remember to take umbrella")
elif weather == "H":
    print("Remember to put sunblock on")
    print("Remember your hat")
else:
    print("I di not understand your weather condition")

print("Hope you have a lovely day")
