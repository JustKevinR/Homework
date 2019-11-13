import random
j = "y"
while j == "y":
    

    user = input("rock(r),paper(p) or scissors(s): ")
    pc_random = random.choice("rps")
    print (pc_random)


    if user == pc_random:
        print ("Draw")
    elif user == "r" and pc_random == "p" or user == "p" and pc_random == "s" or user == "s" and pc_random == "r":
        print ("PC win")
    else:
        print ("User win")

    j = input("Do you wanna play again ? y/n : ")
