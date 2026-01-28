#GUESS THE NUMBER:
import random
target = random.randint(1,100)


while True:
    userchoice = int(input("enter the number or QUIT(Q):"))
    if(userchoice == "Q"):
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("success!! correct guess.....")
        break
    elif(userchoice < target):
        print("number is too small take a bigger guess......")
    else:
        print("number is too big take a smaller guess...")

print("GAME OVER!!")



        


    




















