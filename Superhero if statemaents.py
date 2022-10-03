question1 = input ("Is this hero morally good?")
if question1 == "Y":
    question2 = input("Is their mothers name Martha?")
    if question2 == "Y":
        question3 = input("Is she dead?")
        if question3 == "Y":
            print ("Your hero is Batman")
        elif question3 == "N":
            print ("Your hero is superman")
        else:
            print ("You can only enter Y or N")    
elif question1 == "N":
    question4 = input("Were they born with their powers?")
    if question4 == "N":
        print ("Your hero is Homelamnder")
    elif question4 == "Y":
        print ("Your hero is Omni man")
        

    
