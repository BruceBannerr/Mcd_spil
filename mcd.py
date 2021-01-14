import random

#Moneycounter
moneycount=0

#Starten af spillet
def start():
    print("Du er på mcd. Du har",moneycount,"kroner")
    user_input = input(":")
    
    #Gå til udgang
    if user_input == "u" or user_input == "U":
        udgang()
    #Gå til skrank
    if user_input == "s" or user_input == "S":
        skrank()
    #Gå til kø
    if user_input == "k" or user_input == "K":
        kø()
    #Forkert tast
    else:
        print("Prøv lige igen")

#Udgang
def udgang():
    print("Du er ved udgangen. Vil du give op? y=ja, n=nej")
    user_input = input(":")
    if user_input == "y" or user_input == "Y":
        print("Ja")
    elif user_input == "n" or user_input == "N":
        print("Nej")

#Skranken 
def skrank():
    print("Du står ved skranken. Du har ", moneycount, "kroner.")
    if moneycount >= 65:
        print("Du har penge nok til en burger. Vil du købe? tast y for ja, tast n for nej.")
        user_input = input(":")
        if user_input == "y" or user_input == "Y":
            print("Jaa, du har købt en burger.") 
        elif user_input == "n" or user_input == "N":
            print("Du har ikke købt en burger")
    elif moneycount < 65:
        print("Du har ikke penge til en burger")

#Kø
def kø():
    print("Du er ved køen. Vil du tigge om penge, tast t. Vil du stjæle, tast s.")
    user_input = input(":")
    if user_input == "t" or user_input == "T":
        print("Du tigger om penge.")
    elif user_input == "s" or user_input == "S":
        print("Du stjæler")

#Skraldespand
def Skraldespand():
    print("Du står ved skraldespanden. Vil du lede efter pant, tast p. Vil du lede efter en burger, tast b.")
    user_input = input(":")
    if user_input == "p" or user_input == "P":
        print("Du leder efter pant.")
    elif user_input == "b" or user_input == "B":
        print("Du leder efter en burger.")
    
#Tomt bord
def tomt_bord():
    print("Du er ved det tomme bord. Vil du græde, tast g. Vil du lede efter småpenge, tast l.")
    user_input = input(":")
    if user_input == "g" or user_input == "G":
        print("Du græder.")
    elif user_input == "l" or user_input == "L":
        print("Du leder efter småpenge.")

#Gammel mand
def gammel_mand():
    print("Du står ved den gamle mand. Vil du tilbyde ham en omgang på toilettet, tast t. Vil du lytte til de gode gamle dage, tast l.")
    user_input = input(":")
    if user_input == "t" or user_input == "T":
        print("Du tilbyder ham en omgang på toilettet.")
    elif user_input == "l" or user_input == "L":
        print("Du hører om de gode gamle dage og håber at han giver dig en burger.")

#Rengøring
def rengøring():
    print("Du står ved rengøringspersonalet og vil tilbyde arbejde, vil du arbejde hvidt, tast h, eller sort, tast s?")
    user_input = input(":")
    if user_input == "h" or user_input == "H":
        print("Du tilbyder at arbejde hvidt.")
    elif user_input == "s" or user_input == "S":
        print("Du tilbyder at arbejde sort.")

#Familie
def familie():
    print("Du er gået hen til familien. Vil du tage børnene som gidsler og afpresse familien, tast a. Vil du tilbyde børnepasning, tast b.")
    user_input = input(":")
    if user_input == "a" or user_input == "A":
        print("Du afpresser familien.")
    elif user_input == "b" or user_input == "B":
        print("Du tilbyder at passe børnene.")

#Kør programmet
user_input = ""
while True:
    start()
