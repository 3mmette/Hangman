#########################################################################
#
#  Python Project - Hangman
#
#  File:       main.py
#  Project:    Apply introductory programming techniques, Portfolio
#  Author:     Emmette Taylor (emmette.taylor@hotmail.com)
#  Copyright:  © Copyright 2022, Emmette Taylor
#
#########################################################################

import time
from utility_functions import *
from welcome_screens import welcome
from word_selection import word_selection

#########################################################################
# CONSTANTS
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

MAX_LIVES = 10
SCORE_AMOUNT = 10
HEIGHT = 29
WIDTH = 61


##########################################################################
# INPUT FUNCTIONS

def askUserForSingleCharacter(options=[], prompt="Enter a character"):
    choice = ""
    if len(options) == 0:
        options = ALPHABET
    optionsList = ",".join(options)
    while options.count(choice) <= 0:
        print("Options are: " + optionsList)
        choice = input(prompt + ": ")
        if options.count(choice) <= 0:
            print("OOPS! You made an error...")
        # end if
    # end while
    return choice


#########################################################################
# THE MAIN PROGRAM
#########################################################################
# Welcome screens and get the name of the user.
user_name = welcome(HEIGHT, WIDTH)

# Welcome the user
print("\nHello, " + user_name, "\nTime to play Hangman!")
print()

# wait for 1 second
time.sleep(1)

# Selects a random secret word.
word = word_selection(HEIGHT, WIDTH, user_name)[0].lower()

print("Start guessing...")
time.sleep(0.5)
solid_line(WIDTH)

# create a guesses variable with an empty value
guesses = ''

# create a variable for the score
score = 0

# determine the number of lives
lives = MAX_LIVES

# list of letters not used
letters = ALPHABET

# Create a while loop
# check if the lives are more than zero
while lives > 0:
    # make a counter that starts with zero
    failed = 0

    print("\nGuess the word: ", end="")
    # for every character in the secret word
    for char in word:
        # see if the character is in the players guesses
        if char in guesses:
            # print then out the character
            print(char, end="")
        else:
            # if not found, print a dash
            print("-", end="")
            # and increase the failed counter by one
            failed += 1
    # if failed is equal to zero
    # print You Won
    if failed == 0:
        print("\nYou won")
        # exit the script
        break

    print("\n\n")
    # ask the user to guess a character
    guess = askUserForSingleCharacter(letters, "Enter a character")
    # add the guess to the list of characters used so far...
    guesses += guess

    # remove the guess from the list of available letters
    letters.remove(guess)

    # if the guess is not found in the secret word
    if guess not in word:
        # lives counter decreases by 1
        lives -= 1
        # print wrong
        print("Guessed Wrong!\n")
    else:
        # increase the player score
        score = score + SCORE_AMOUNT

    # how many lives are left
    print("You have", + lives, 'more guesses\n')

    # if the lives are equal to zero
    if lives == 0:
        # print "You Lose"
        print("You Lose")

# Press enter to quit
finish = input("Press enter to finish. Goodbye " + user_name)
