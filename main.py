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

# Import individual game sections into the main program
from welcome_screens import welcome
from word_selection import word_selection
from difficulty_selection import difficulty_selection
from gameplay import gameplay
from game_over import game_over
from scoring import scoring

#########################################################################

# CONSTANTS
HEIGHT = 30
WIDTH = 61

#########################################################################
# THE MAIN PROGRAM
#########################################################################

if __name__ == "__main__":

    # Welcome screens and input the name of the user.
    user_name = welcome(HEIGHT, WIDTH)

    # Loop gameplay
    while True:

        # Selects a random secret word. Returns the word and the list it came from.
        word_selection_information = word_selection(HEIGHT, WIDTH, user_name)

        # Select a difficulty. Returns the number of lives and difficulty.
        difficulty_selection_information = difficulty_selection(HEIGHT, WIDTH, user_name)

        # The game itself. Returns the result and time taken to complete the game.
        gameplay_information = gameplay(HEIGHT, WIDTH, user_name, word_selection_information[0],
                                        difficulty_selection_information[1], difficulty_selection_information[0])

        # Concluded the game, differing information depending on the result.
        game_over(HEIGHT, WIDTH, user_name, word_selection_information[0], difficulty_selection_information[1],
                  gameplay_information[0])

        # Calculate the users score and update the leaderboard if applicable.
        scoring(HEIGHT, WIDTH, user_name, word_selection_information[0], word_selection_information[1],
                difficulty_selection_information[1], gameplay_information[0], gameplay_information[1])

        # Play again or exit.
        replay = input("[ENTER] or 0: ")
        if replay == "0":
            break

    # If player exits
    print("Goodbye " + user_name)

