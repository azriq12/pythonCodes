import random
"""
Your module description
"""
print("Welcome to GUESS THE NUMBER!")
print("The rules are simple. I'll think of a number, and you will try to guess it.") 
number=random.randint(73,111)
theGuess = False
while theGuess != True:
    guess = input("Guess a number between 73 and 111:")
    if int(guess)==88:
        print("You guessed {}. That is correct! You win!".format(guess))
        theGuess=True
    else:
        print("You guessed {}. Sorry, that is wrong. Please try again.".format(guess))