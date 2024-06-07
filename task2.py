from random import *
def number_guesser():
    num = randint(1,100)
    userGuess = int(input("Guess the number:\n"))
    while userGuess != num:
    
        if userGuess < num:
            print("Try Higher")
        
        elif userGuess > num:
            print("Try Lower")
        userGuess = int(input("Guess the number:\n"))

    print("You guessed correct")    

    
number_guesser()
