#!/usr/local/bin/python3

"""
guessing_game.py

Generate a random number between 1 and 99
User must guess the number
"""

import random

def random_number(upper):
    r_number = random.randint(1, upper_limit)
    return r_number


upper_limit = 99
secret_number = random_number(upper_limit)
g_string="I'm thinking of a number between 1 and " + str(upper_limit) +". Guess what it is: "

print()
while True:
    try:
        guess = int(input(g_string))
    except ValueError:
        print("\nNo. I'm thinking of an integer...\n")
        continue
    if guess < 1 or guess > upper_limit:
        print("\nI said, between 1 and " + str(upper_limit) + "...\n")
    else:
        if guess == secret_number:
            print ("\nYou guessed correctly, the number was " + str(secret_number) + "\n")
            break
        elif guess < secret_number:
            g_string="\nGuess higher: "
        else:
            g_string="\nGuess lower: "

                
            

