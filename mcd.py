import random

#Moneycounter
moneycount=0

#Gamestart
def start():
    print(" You have",moneycount,"DKK")
    user_input = input(":")
    #Go to exit
    if user_input == "u" or user_input == "U":
        udgang()
    #Gå til desk
    if user_input == "s" or user_input == "S":
        skrank()
    #Go to queue
    if user_input == "k" or user_input == "K":
        kø()
    #Wrong key
    else:
        print("Try again")

#exit
def Exit():
    print("You are at the exit. Give up? y=yes, n=no")
    user_input = input(":")
    if user_input == "y" or user_input == "Y":
        print("Yes")
    elif user_input == "n" or user_input == "N":
        print("No")

#desk
def desk():
    print("You are at the desk. You have ", moneycount, "DKK.")
    if moneycount >= 65:
        print("You have enough money for a burger, do you wanna buy? y=yes, n=no.")
        user_input = input(":")
        if user_input == "y" or user_input == "Y":
            print("You have bought a burger.") 
        elif user_input == "n" or user_input == "N":
            print("You have not bought a burger.")
    elif moneycount < 65:
        print("You cannot afford a burger.")

#Kø
def queue():
    print("You are at the queue. Do you start begging for money (b) or du you start stealing (s)? ")
    user_input = input(":")
    if user_input == "b" or user_input == "B":
        print("You beg for money.")
    elif user_input == "s" or user_input == "S":
        print("You steal money.")

#trashcan
def trashcan():
    print("You are at the trashcan. Are you looking for a burger (b)? Or are you looking for bottle deposit (d)?")
    user_input = input(":")
    if user_input == "d" or user_input == "D":
        print("You are looking for bottle deposit, unfortunately there are no bottle deposit at McDonalds.")
    elif user_input == "b" or user_input == "B":
        print("You are looking for a burger.")
    
#empty table
def empty_table():
    print("You are at the empty table. Du you wanna cry(c) or look for money(l)?")
    user_input = input(":")
    if user_input == "c" or user_input == "C":
        print("You cry.")
    elif user_input == "l" or user_input == "L":
        print("You look for money.")

#The old man
def old_man():
    print("You are at the old man. Du you want to offer him a good time in your bedroom (b). Du you want to listen to him talking about the good old days (l)")
    user_input = input(":")
    if user_input == "t" or user_input == "T":
        print("You offers him a good time in your bedroom, he refuses ...")
    elif user_input == "l" or user_input == "L":
        print("You listen to him talking about the good old days, while you are hoping that he offers you a burger.")

#Cleaning staff
def cleaning():
    print("You are at the cleaning staff and want to work. Do you want a legal (l) or illegal (i) job?")
    user_input = input(":")
    if user_input == "l" or user_input == "L":
        print("You offer to work legal.")
    elif user_input == "i" or user_input == "I":
        print("You offer to work illegal.")

#Family
def family():
    print("You are at the family. Do you wanna take the children and blackmail the parents (b), or do you offer to take care of the children for the parents (c).")
    user_input = input(":")
    if user_input == "b" or user_input == "B":
        print("You are blackmailing the family.")
    elif user_input == "c" or user_input == "C":
        print("You offer to take care of the children.")

#Run program
user_input = ""
while True:
    start()
