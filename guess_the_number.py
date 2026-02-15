#GUESS THE NUMBER:
#importing random:
import random
target = random.randint(1,100)

#using loops:
while True:
    userchoice = int(input("enter the number or QUIT(Q):"))
    #using conditional statements for checking whether the target is greater or smaller:
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
#if guessed is correct print game over:
print("GAME OVER!!")



        


    





















