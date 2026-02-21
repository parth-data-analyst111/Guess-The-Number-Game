print("hellow python")

# Guess the Number (Game): [overall logic is based on loops]
import random

target = random.randint(1,100)

while True:
    Userchoice =input("Guess the target or Quit(Q) : ")
    if(Userchoice == "Q"):
        break

    Userchoice = int(Userchoice)
    if(Userchoice == target):
        print("success : correct guess!! ")
        break
    elif(Userchoice < target):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too Big. Take a Smaller guess...")

print("-----GAME OVER-----")    