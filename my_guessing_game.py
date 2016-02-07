#!/usr/local/bin/python3

"""
guessing_game.py

Generate a random number between 1 and 99
User must guess the number
"""

import random

def random_number(upper):
    """Generate and return a randomly generated number beteen 1 and the value of an upper limit,
       and also calculate and return the maximum number of attempts it should take to guess the number."""
    secret_number = random.randint(1, upper_limit)
    max_attempts = 0
    while upper > 0:
        upper = int(upper/2)
        max_attempts += 1
    return secret_number, max_attempts


# TODO: Allow user specify upper_limit. For now, just follow the objective requirements, hard-code for 99
upper_limit = 99
secret_number, max_attempts = random_number(upper_limit)

num_guesses=0
print()
while True:
    try:
        guess = int(input("I'm thinking of a number between 1 and " + str(upper_limit) +". Guess what it is: "))
    except ValueError:
        print("\nNo. I'm thinking of an integer...\n")
        continue
    if guess < 1 or guess > upper_limit:
        print("\nI said, between 1 and " + str(upper_limit) + "...\n")
    else:
        if guess == secret_number:
            print ("Yay! You guessed correctly, the number was " + str(secret_number) + "\n")
            break
        else:
            num_guesses += 1
            if num_guesses == max_attempts:
                print("\nWah, wah, wah...you're out of guesses. I was thinking of the number " + str(secret_number) + "\n")
                break
            elif guess < secret_number:
                print("\nGuess higher.", end=" ")
            else:
                print("\nGuess lower.", end=" ")
            print("You have " + str(max_attempts-num_guesses) + " guesses remaining." + "\n")

                
            

