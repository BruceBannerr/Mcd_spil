#Starten af spillet
def start():
    print("Du er på mcd, men har ingen penge. Vil du gå til udgangen, tast u. Vil du gå til skranken, tast s.")
    user_input = input(":")
    
    #Gå til udgang
    if user_input == "u" or user_input == "U":
        udgang()
    #Gå til skrank
    if user_input == "s" or user_input == "S":
        skrank()
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
    print("Du står ved skranken. Du har et eller andet antal penge. Vil du købe en burger, tast k, vil du gå tilbage, tast t.")
    user_input = input(":")
    if user_input == "k" or user_input == "K":
        print("Du kan ikke købe, for du har ingen penge.")
    elif user_input == "t" or user_input == "T":
        pass

#Kør programmet
user_input = ""
while True:
    start()

#lololololol
#skidiski papPAP