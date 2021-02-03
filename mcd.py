import random

#Moneycounter
moneycount = 0

#Gamestart
def start():
    print(" You have", moneycount,"DKK")
    user_input = input(":")
#Go to exit
    if user_input == "e" or user_input == "E":
        Exit()
#Go to desk
    elif user_input == "d" or user_input == "D":
        desk()
#Go to queue
    elif user_input == "q" or user_input == "Q":
        queue()
#Go to trashcan
    elif user_input == "t" or user_input == "T":
        trashcan()
#Go to empty table
    elif user_input == "m" or user_input == "M":
        empty_table()
#Go to old man
    elif user_input == "o" or user_input == "O":
        old_man()
#Go to cleaning staff
    elif user_input == "c" or user_input == "C":
        cleaning()
#Go to family
    elif user_input == "f" or user_input == "F":
        family()
    #Wrong key
    else:
        print("Try again")

#exit
def Exit():
    global moneycount
    global running
    print("You are at the exit. Give up? y=yes, n=no")
    user_input = input(":")
    if user_input == "y" or user_input == "Y":
        print("You gave up. You had ", moneycount, "DKK")
        running = False
    elif user_input == "n" or user_input == "N":
        pass

#desk
def desk():
    global moneycount
    print("You are at the desk. You have ", moneycount, "DKK.")
    if moneycount >= 65:
        print("You have enough money for a burger, do you wanna buy? y=yes, n=no.")
        user_input = input(":")
        if user_input == "y" or user_input == "Y":
            print("You have now bought a burger.")
            moneycount = moneycount-65
        elif user_input == "n" or user_input == "N":
            print("You have not bought a burger.")
    elif moneycount < 65:
        print("You cannot afford a burger.")

#Kø
def queue():
    global moneycount
    print("You are at the queue. Do you start begging for money (b) or du you start stealing (s)? ")
    user_input = input(":")
    if user_input == "b" or user_input == "B":
        print("You beg for money.")
        x = random.choice([1,1,0,2,3,0,0,0,0.5,0.5])
        moneycount = moneycount+x
        print("You got ", x, "DKK from begging")
    elif user_input == "s" or user_input == "S":
        print("You steal money.")
        x = random.choice([1,2,0,2,3,0,0,0,5,2])
        moneycount = moneycount+x
        print("You got ", x, "DKK from stealing")

#trashcan
def trashcan():
    global running
    print("You are at the trashcan. Are you looking for a burger (b)? Or are you looking for bottle deposit (d)?")
    user_input = input(":")
    if user_input == "d" or user_input == "D":
        print("You are looking for bottle deposit, unfortunately there are no bottle deposit at McDonalds.")
    elif user_input == "b" or user_input == "B":
        print("You are looking for a burger.")
        x = random.choice(["a mouse", "a burger", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing","a mouse","nothing"])
        if x == "a burger":
            print("YOU FOUND A BURGER AND WON THE GAME!")
            running = False
        else:
            print("You found ",x)

    
#empty table
def empty_table():
    global moneycount
    print("You are at the empty table. Du you wanna cry(c) or look for money(l)?")
    user_input = input(":")
    if user_input == "c" or user_input == "C":
        print("You cry.")
    elif user_input == "l" or user_input == "L":
        print("You look for money under the table.")
        x = random.choice([0,2,2,1,1,0.5,0.5,0,1,0.5])
        moneycount = moneycount+x
        print("You found",x,"DKK under the table.")

#The old man
def old_man():
    print("You are at the old man. Du you want to offer him a good time in your bedroom (b). Du you want to listen to him talking about the good old days (l)")
    user_input = input(":")
    if user_input == "b" or user_input == "B":
        print("You offer him a good time in your bedroom, he refuses ...")
    elif user_input == "l" or user_input == "L":
        print("You listen to him talking about the good old days, while you are hoping that he offers you a burger.")
        print("But he doesn't.")

#Cleaning staff
def cleaning():
    global moneycount
    print("You are at the cleaning staff and want to work. Do you want a legal (l) or illegal (i) job?")
    user_input = input(":")
    if user_input == "l" or user_input == "L":
        print("You offer to work legal. The cleaning staff tells you to wait for the boss to arrive. You wait for hours and die from hunger.")
    elif user_input == "i" or user_input == "I":
        x = random.choice(["wash the floor","empty the trashcan","wash the windows", "cleanse the toilets"])
        if x == "wash the floor":
            y = 3
        elif x == "empty the trashcan":
            y = 1
        elif x == "wash the windows":
            y = 4
        elif x == "cleanse the toilets":
            y = 6
        moneycount = moneycount+y
        print("You offer to work illegal. The cleaning staff tells you to ",x,".")
        print("You do, and the cleaning staff gives you", y, "DKK for the job")

#Family
def family():
    global moneycount
    print("You are at the family. Do you wanna take the children and blackmail the parents (b), or do you offer to take care of the children for the parents (c).")
    user_input = input(":")
    if user_input == "b" or user_input == "B":
        print("You take the children and blackmail the family.")
        print("How much do you want for the children?")
        user_input = input(":")
        user_input = int(user_input)
        if user_input <= 50:
            moneycount = moneycount + user_input
            print("The family gives you the money!")
        elif user_input > 50:
            print("The family do not want to pay that much for the children. They just leave you with the chying kids.")
    elif user_input == "c" or user_input == "C":
        print("You offer to take care of the children.")

#run game
running = True
while running:
    start()
