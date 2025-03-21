import datetime
current_time = datetime.datetime.now()
timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")

userscores = input("Enter your latest score?")


file = open("scores.txt", "a")
file.write("\n")
file.write(userscores + " recorded at: " + timestamp)
file.close()

file = open("scores.txt","r")
for line_from_file in file:
    print(line_from_file.strip())
file.close()