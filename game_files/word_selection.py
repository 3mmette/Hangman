import os
import random
from game_files.utility_functions import *
from game_files.text_art import *


# Options for the three provided lists, and an option to choose from custom lists.
word_list_options = [
    "Beginner",
    "   A collection of the most common words.",
    "   Score multiplied x 0.75!",
    "",
    "Intermediate",
    "   A collection of words you should know.",
    "   Score multiplied x 1.00!",
    "",
    "Expert",
    "   A collection of all English words.",
    "   Score multiplied x 1.25!",
    "",
    "Custom",
    "   Select from user uploaded lists.",
    "   Score multiplied x 1.00!"
    ]


def word_file_selection_box(height, width, user_name):
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
    line_count += text_line(inner_width, f"{user_name}, select one of the following collections.", "^")
    line_count += solid_line(width)
    line_count += menu(inner_width, word_list_options, 1, 4)
    for extra in range((height - line_count)):
        empty_line(inner_width)
    line_count += solid_line(width)


def custom_file_selection_box(height, width, user_name):
    """
    Prints a box with a header, text and each individual custom list selection
    Options come from a custom_word_lists directory
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :return custom_list_dir: list of all the custom files
    """
    clear_screen()
    inner_width = width - 4
    line_count = 2
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, f"{user_name}, please select a custom word collection.", "^")
    line_count += solid_line(width)
    custom_list_dir = os.listdir("custom_word_lists/")
    custom_list_dir_names = list()
    for i in custom_list_dir:
        custom_list_dir_names.append(i.removesuffix(".txt"))
    line_count += menu(inner_width, custom_list_dir_names, 1, 1)
    for extra in range((height - line_count)):
        empty_line(inner_width)
    text_line(line_count, f"0) {'To return to list selection':{inner_width - 3}}")
    solid_line(width)
    return custom_list_dir


def random_word(file):
    """
    Selects a random word from the chosen word list file
    :param file: the name that corresponds to the number selected from the menu
    :return word.upper(): uppercase random word from the selected file
    """
    words = list()
    with open(f"{file}", "r") as text:
        for word in text:
            if len(word.strip()) >= 4:
                words.append(word.strip())
    if len(words) > 0:
        word = random.choice(words)
        return word.upper()
    else:
        return None


def word_selection(height, width, user_name):
    """
    A combination of all the required functions to complete the version 1.2 upgrade
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :return word: random word from the selected file
    :return from_file: name of the file the word came from
    """
    word = None
    from_file = None
    while word is None or from_file is None:
        # Creates a display
        word_file_selection_box(height, width, user_name)

        # Input selection and attempt to change it to an integer.
        selection = try_integer("[ENTER] your select number: ")

        # Validates your selection. User is not allowed to continue until a valid option is entered.
        while True:
            if type(selection) is int:
                if 1 <= selection <= 4:
                    break
                else:
                    word_file_selection_box(height, width, user_name)
                    print("You failed to enter a valid number.")
                    selection = try_integer("[ENTER] your select number: ")
            else:
                word_file_selection_box(height, width, user_name)
                print("You entered something other than a number.")
                selection = try_integer("[ENTER] your select number: ")

        # Selects a random word for the above choice.
        if selection == 1:
            word = random_word("game_files/Beginner.txt")
            from_file = "Beginner"
            break
        if selection == 2:
            word = random_word("game_files/Intermediate.txt")
            from_file = "Intermediate"
            break
        if selection == 3:
            word = random_word("game_files/Expert.txt")
            from_file = "Expert"
            break

        # If the user wants to select from a custom uploaded file in the custom_word_lists folder.
        if selection == 4:

            # Creates a display
            custom_list_dir = custom_file_selection_box(height, width, user_name)

            # User is not allowed to continue until a valid option is entered.
            while word is None or from_file is None:

                # Input selection and attempt to change it to an integer.
                selection = try_integer("[ENTER] your select number: ")
                if type(selection) is int:

                    # If selection is 0, takes user back to main selection screen.
                    if selection == 0:
                        break

                    # If selection is valid.
                    elif 1 <= selection <= len(custom_list_dir):
                        for i in range(len(custom_list_dir)):
                            if selection == i + 1:
                                custom_file = custom_list_dir[i]

                                # Word selected
                                word = random_word(f"custom_word_lists/{custom_file}")

                                # If there are no words in the file.
                                if word is None:
                                    custom_file_selection_box(height, width, user_name)
                                    print("There were no words in your selection.")

                                # Sets the from_file variable to exit the loop.
                                else:
                                    from_file = custom_file.removesuffix(".txt")
                    else:
                        custom_file_selection_box(height, width, user_name)
                        print("You failed to enter a valid number.")
                else:
                    custom_file_selection_box(height, width, user_name)
                    print("You entered something other than a number.")

    return word, from_file
