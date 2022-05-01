from utility_functions import *
from text_art import *


def welcome_scoreboard_name_box(height, width):
    """
    Prints a box with a header, the scoreboard and text. Uses multiple functions from the utility file
    :param height: height of the box
    :param width: width of the box
    """
    clear_screen()
    inner_width = width - 4
    line_count = 1
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, "WORD LIST LEADERBOARD", "^")
    line_count += solid_line(width)
    line_count += scoreboard(inner_width)
    line_count += solid_line(width)
    line_count += text_line(inner_width, "Please sign your life away below: ", "^")
    for extra in range((height - line_count)):
        empty_line(inner_width)
    solid_line(width)


def name_request(height, width):
    """
    Requests a name from the user and validates it to ensure something was entered, and it is not too long
    :param height: height of the box
    :param width: width of the box
    :return user_name: the name the user
    """
    user_name = input("[ENTER] your name here: ").capitalize()
    while True:
        if user_name == "":
            welcome_scoreboard_name_box(height, width)
            print("Your name must consist of at least one character.")
            user_name = input("[ENTER] your name here: ").capitalize()
        elif len(user_name) > 7:
            welcome_scoreboard_name_box(height, width)
            print("Your name is too long.")
            print("A maximum of 7 characters will fit.")
            user_name = input("[ENTER] your name here: ").capitalize()
        elif " " in user_name:
            welcome_scoreboard_name_box(height, width)
            print("Your name must not contain any spaces.")
            user_name = input("[ENTER] your name here: ").capitalize()
        else:
            break
    return user_name


def welcome_rules_box(user_name, height, width):
    """
    Prints a box with a header, text and the game rules. Uses multiple functions from the utility file
    :param user_name: name of the user
    :param height: height of the box
    :param width: width of the box
    """
    clear_screen()
    inner_width = width - 4
    line_count = 1
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, f"Read this carefully {user_name}, it may save your life.", "^")
    line_count += solid_line(width)
    text = open("game_files/rules.txt", "r")
    for line in text:
        line_count += text_line(inner_width, line.strip())
    for extra in range((height - line_count)):
        empty_line(inner_width)
    solid_line(width)


def welcome(height, width):
    """
    A combination of all the required functions to complete the version 1.1 upgrade
    :param height: height of the box
    :param width: width of the box
    :return user_name: the name the user inputted
    """
    # Displays the first screen.
    welcome_scoreboard_name_box(height, width)

    # Shown under the first screen.
    user_name = name_request(height, width)

    # Displayed once a valid name is entered.
    welcome_rules_box(user_name, height, width)

    # Dummy input to allow sufficient time to ready the rules.
    input("[ENTER] to continue: ")
    return user_name
