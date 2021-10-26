# guess_number.py
# Short game for user to guess a number

import random                      # Import the random module 

# Get random number between [1 and 1000)
number = random.randrange(1, 1000) 
guess = int(input("Guess my number between 1 and 1000: "))
guesses = 1 

while guess != number:
    guesses = guesses + 1
    if guess > number:
        print(guess, "is too high.") 
    elif guess < number:
        print(guess, " is too low.")
    guess = int(input("Guess again: "))

print("\nGreat, you got it in", guesses,  "guesses!")
