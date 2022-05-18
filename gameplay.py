import random
import time

from utility_functions import *
from text_art import *


qwerty_keys = [
    f"{'Q':>2} {'W':>5} {'E':>5} {'R':>5} {'T':>5} {'Y':>5} {'U':>5} {'I':>5} {'O':>5} {'P':>5}",
    f"{'A':>5.5} {'S':>5} {'D':>5} {'F':>5} {'G':>5} {'H':>5} {'J':>5} {'K':>5} {'L':>5}",
    f"{'Z':>8.5} {'X':>5} {'C':>5} {'V':>5} {'B':>5} {'N':>5} {'M':>5}"
]

correct_quotes = ["your one step closer to freedom!",
                  "was that luck or skill?",
                  "great guess, another letter in!",
                  "interesting.... but it worked.",
                  "amazing! Keep it up."
                  ]

incorrect_quotes = ["your better then that!",
                    "do you want to die?",
                    "why would you guess that?",
                    "that was stupid of you!",
                    "keep that up and you'll be swinging soon"
                    ]


def gameplay_box(height, width, user_name, comment, picture, progress, lives, keyboard):
    """
    Prints a box using the following arguments to provide information to the user
    Different comments come from the lists, located at the top of this file, depend on the if the guess was good or not
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :param comment: a varying text, commenting on how the game is going
    :param picture: a visual representation of the remaining lives
    :param progress: the word the user is trying to guess, '_' for any letters yet to be guessed
    :param lives: the number of incorrect guesses the user has to complete the game
    :param keyboard: representation of the qwerty keyboard for the game
    """
    clear_screen()
    inner_width = width - 4
    line_count = 2
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, f"{user_name}, {comment}", "^")
    line_count += solid_line(width)
    line_count += text_line(inner_width, picture, "^")
    line_count += empty_line(inner_width)
    line_count += text_line(inner_width, f"Lives Remaining: {lives}", "^")
    line_count += solid_line(width)
    line_count += text_line(inner_width, "Word Progress", "^")
    line_count += text_line(inner_width, progress, "^")
    line_count += solid_line(width)
    line_count += text_line(inner_width, "Available Letters", "^")
    line_count += text_line(inner_width, keyboard)
    line_count += solid_line(width)
    for extra in range((height - line_count)):
        empty_line(inner_width)
    text_line(inner_width, "To quit, simply guess 0 (Zero)", "^")
    line_count += solid_line(width)


def validate_character(height, width, user_name, picture, lives, progress, guesses, keyboard):
    while True:
        guess = input("Guess: ").upper()

        # if the user wants to quit.
        if guess == "0":
            break

        # If the user enters a single character.
        if len(guess) == 1:

            # If the guess is valid.
            if guess in str(keyboard):
                break

            # If they have already guessed that letter.
            elif guess in guesses:
                gameplay_box(height, width, user_name, "choose from available letters below!",
                             picture[lives + 2], progress, lives, keyboard)
                print("You have already guessed that letter!")

            # If the guess is invalid
            else:
                gameplay_box(height, width, user_name, "that isn't a letter!", picture[lives + 2], progress,
                             lives, keyboard)
                print("Invalid character")

        # If the user entered more than one character
        else:
            gameplay_box(height, width, user_name, "enter a single letter this time!", picture[lives + 2],
                         progress, lives, keyboard)
            print("You must enter a single character")
    return guess


def gameplay(height, width, user_name, word, difficulty, lives):
    """
    A combination of all the required functions to complete the version 1.4 enhancement
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :param word: the word the user is trying to guess
    :param difficulty: the difficulty setting, used to select the respective text art list
    :param lives: the number of incorrect guesses the user has to complete the game
    """
    # Overall result of the game.
    result = None
    # Result of the round, used to create comments on the game
    round_result = None
    # The respective text art list for displaying visual of lives.
    picture = None
    # The keyboard the game will use.
    keyboard = qwerty_keys

    # A string of all the letter guessed so far.
    guesses = ""

    # Uses the difficulty setting to select the respective text art list.
    if difficulty == "Easy":
        picture = easy
    if difficulty == "Normal":
        picture = normal
    if difficulty == "Hard":
        picture = hard

    # Start time of the game
    start = time.time()

    # Creates a loop
    while result is None:
        failed = 0
        progress = ""
        # ***Modified Original Code*** Creates a word with any characters not guessed replaced with an underscore.
        for character in word:
            if character in guesses:
                progress += " " + character + " "
            else:
                progress += " _ "
                failed += 1

        # If failed is equal to zero, the game is won so result is set to True and break stops the loop.
        if failed == 0:
            result = True
            gameplay_box(height, width, user_name, "the word has be revealed. You win.", picture[lives + 2],
                         progress, lives, keyboard)
            break

        # If it is the first round, tells the player time has started, otherwise comments on their progress.
        if round_result is None:
            comment = "your time starts now!"
        elif round_result is True:
            comment = random.choice(correct_quotes)
        elif round_result is False:
            comment = random.choice(incorrect_quotes)
        else:
            continue

        # Create the gameplay box.
        gameplay_box(height, width, user_name, comment, picture[lives + 2], progress, lives, keyboard)

        # Get and validate the guess. Needs so many arguments to call the gameplay box within it.
        guess = validate_character(height, width, user_name, picture, lives, progress, guesses, keyboard)

        # Quits the game if 0 (Zero) is entered.
        if guess == "0":
            gameplay_box(height, width, user_name, "quitting won't save you. You lose anyway.", picture[2],
                         progress, 0, keyboard)
            result = None
            break

        # Add the guess to the list of characters used so far.
        guesses += guess

        # A temporary keyboard made to allow the replace function to work on list items. Makes guessed letter blank.
        temp = list()
        for line in keyboard:
            if guess in line:
                temp.append(line.replace(guess, " "))
            else:
                temp.append(line)

        # New keyboard with guessed letter replaced.
        keyboard = temp

        # Sets round result variable for customizable text responses.
        if guess not in word:
            # lives counter decreases by 1
            lives -= 1
            round_result = False

        if guess in word:
            round_result = True

        # If the lives are equal to zero, result set to False and loop breaks
        if lives == 0:
            gameplay_box(height, width, user_name, "no more chances remain. You lose.", picture[lives + 2],
                         progress, lives, keyboard)
            result = False
            break

    # Stops time for the game, then calculates time taken to reach this point.
    stop = time.time()
    time_taken = int(stop) - int(start)
    input("[ENTER] to continue: ")
    return result, time_taken
