#!/usr/local/bin/python3
#
# guess.py
#
""" 
Player must guess a secret number between 1-20 in 5 guesses or less.
"""

import random

secret_num = random.randint(1,20)
num_guesses = 0

while num_guesses < 5:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
        except ValueError:
            print("You must enter an integer...")
            continue
        else:
            if guess < 1 or guess > 20:
                print("Lets stay within 1 and 20...")
            else:
                break
    if guess == secret_num:
        print ("Yay! You guessed correctly, the number was " + str(secret_num))
        break
    else:
        num_guesses += 1
        if num_guesses == 5:
            print("Wah, wah, wah...you're out of guesses. It was " + str(secret_num))
            break
        elif guess < secret_num:
            print("Guess higher")
        else:
            print("Guess lower")

            


