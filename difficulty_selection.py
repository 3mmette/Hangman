from utility_functions import *
from text_art import *


# Options for the three difficulties.
difficulty_options = [
    "EASY",
    "   Living that easy stick life, bribe the executioner?",
    "   You have 7 lives. Score multiplied x 0.75!",
    "",
    "NORMAL",
    "   Normal stick person living that normal sticky life?",
    "   You have 6 lives. Score multiplied x 1!",
    "",
    "HARD",
    "   Been doing it hard there sticky??? Even lost a leg?",
    "   You have 5 lives. Score multiplied x 1.25!"
    ]


def difficulty_selection_box(height, width, user_name):
    """
    Prints a box with a header, text and pre-made list selections or go to custom list selection
    Options come from a list, located at the top of this file
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    """
    clear_screen()
    inner_width = width - 4
    line_count = 1
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, f"{user_name}, choose your Avatar", "^")
    line_count += solid_line(width)
    line_count += text_line(inner_width, difficulty_art, "^")
    line_count += solid_line(width)
    line_count += menu(inner_width, difficulty_options, 1, 4)
    for extra in range((height - line_count)):
        empty_line(inner_width)
    line_count += solid_line(width)


def difficulty_selection(height, width, user_name):
    """
    A combination of all the required functions to complete the version 1.3 enhancement
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :return lives: number of incorrect guesses the user will have
    :return difficulty: string to be matched in later functions
    """
    # Creates a display
    difficulty_selection_box(height, width, user_name)

    # Input selection and attempt to change it to an integer.
    selection = try_integer("[ENTER] your select number: ")

    # Validates your selection. User is not allowed to continue until a valid option is entered.
    while True:
        if type(selection) is int:
            if 1 <= selection <= 3:
                break
            else:
                difficulty_selection_box(height, width, user_name)
                print("You failed to enter a valid number.")
                selection = try_integer("[ENTER] your select number: ")
        else:
            difficulty_selection_box(height, width, user_name)
            print("You entered something other than a number.")
            selection = try_integer("[ENTER] your select number: ")

    # Set lives and difficulty
    lives = None
    difficulty = None
    if selection == 1:
        lives = 7
        difficulty = "Easy"
    if selection == 2:
        lives = 6
        difficulty = "Normal"
    if selection == 3:
        lives = 5
        difficulty = "Hard"

    return lives, difficulty
