from utility_functions import *
from text_art import *

winner = ["Congratulations on winning this game of Hangman.",
          "You played well, and are deserving of your freedom.",
          "Move on to see if your name will be immortalised.",
          "For now, enjoy the victory and your life.",
          "Next time you may not be so lucky."]

loser = ["Here hangs the remains of the defeated.",
         "They flew too close to the sun and lost.",
         "Move on to see the names of some sticks still living",
         "Maybe try an easier setting next time...",
         "Oh wait, your dead."]

quitter = ["Here hangs the remains of the quitter.",
           "Because quitting is worse than losing.",
           "Move on to see the names of some sticks still living",
           "Maybe try an easier setting next time...",
           "Oh wait, your dead."]


def game_over_box(height, width, user_name, picture, word, finish):
    """
    Prints a box using the following arguments to provide information to the user
    Different comments come from the lists, located at the top of this file, depending on the result
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :param picture: a visual representation of the win or loss
    :param word: the target word
    :param finish: a text concluding the game
    """
    clear_screen()
    inner_width = width - 4
    line_count = 1
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, f"GAME OVER {user_name.upper()}", "^")
    line_count += solid_line(width)
    line_count += text_line(inner_width, picture, "^")
    line_count += empty_line(inner_width)
    line_count += solid_line(width)
    line_count += text_line(inner_width, "Word of the Game", "^")
    line_count += text_line(inner_width, word, "^")
    line_count += solid_line(width)
    line_count += text_line(inner_width, finish)
    for extra in range((height - line_count)):
        empty_line(inner_width)
    line_count += solid_line(width)


def game_over(height, width, user_name, word, difficulty, result):
    """
    A combination of all the required functions to complete the version 1.5 enhancement
    selects a picture to use and finishing statement depending on the result
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :param word: the target word
    :param difficulty: the selected difficulty of the game, for picture selection
    :param result: True, False or None for how the game went
    """
    # Uses the difficulty setting to select the respective text art list.
    picture = None
    if difficulty == "Easy":
        picture = easy
    if difficulty == "Normal":
        picture = normal
    if difficulty == "Hard":
        picture = hard

    display_word = ""
    for character in word:
        display_word += " " + character + " "

    # Win.
    if result is True:
        finish = winner
        game_over_box(height, width, user_name, picture[0], display_word, finish)

    # Loss.
    if result is False:
        finish = loser
        game_over_box(height, width, user_name, picture[1], display_word, finish)

    # Quit.
    if result is None:
        finish = quitter
        game_over_box(height, width, user_name, picture[1], display_word, finish)

    # Dummy input to continue.
    input("[ENTER] to continue: ")
