from utility_functions import *
from text_art import *


# Values for each letter in the alphabet.
letter_score = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5,
                "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1,
                "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}


def final_scoreboard_box(height, width, word, from_file, difficulty, time_taken, placing,
                         word_score, list_multi, diff_multi, time_multi, score):
    """
    Prints a box using the following arguments to provide information to the user
    :param height: height of the box
    :param width: width of the box
    :param word: the target word
    :param from_file: the name of the file the word came from
    :param difficulty: the difficulty selected
    :param time_taken: time, in seconds, to complete the gameplay function
    :param placing: text based message on where the user placed
    :param word_score: the score from adding up the value of each letter
    :param list_multi: list selection score multiplier
    :param diff_multi: difficulty selection score multiplier
    :param time_multi: time score multiplier
    :param score: total score of the game
    """
    clear_screen()
    inner_width = width - 4
    line_count = 2
    line_count += solid_line(width)
    line_count += header(inner_width, hangman)
    line_count += solid_line(width)
    line_count += text_line(inner_width, "LEADERBOARD", "^")
    line_count += solid_line(width)
    line_count += scoreboard(inner_width)
    line_count += solid_line(width)
    line_count += text_line(inner_width, f"{'Word': <17} | {word.capitalize():<17} |    {word_score}")
    line_count += text_line(inner_width, f"{'Word List': <17} | {from_file:<17} | x  {list_multi}")
    line_count += text_line(inner_width, f"{'Difficulty': <17} | {difficulty:<17} | x  {diff_multi}")
    line_count += text_line(inner_width, f"{'Time in seconds': <17} | {time_taken:<17} | x  {time_multi}")
    line_count += text_line(inner_width, f"{'Total Score': <17} | {' ':<17} | = {score}")
    line_count += solid_line(width)
    line_count += text_line(inner_width, placing, "^")
    for extra in range((height - line_count)):
        empty_line(inner_width)
    text_line(inner_width, "Want another game, press [Enter], or 0 to exit.", "^")
    solid_line(width)


def calculate_score(word, from_file, difficulty, time_taken):
    """
    Using the parameters, calculates the total score the user achieved
    :param word: the target word
    :param from_file: the name of the file the word came from
    :param difficulty: the difficulty selected
    :param time_taken: time, in seconds, to complete the gameplay function
    :return word_score: the score from adding up the value of each letter
    :return list_multi: list selection score multiplier
    :return diff_multi: difficulty selection score multiplier
    :return time_multi: time score multiplier
    :return score: total score of the game
    """
    # Create histogram for each letter in the word.
    word_score = 0
    word_letters = dict()
    for letter in word:
        if letter not in word_letters:
            word_letters[letter] = 1
        else:
            word_letters[letter] = word_letters[letter] + 1
    # Calculate the word score by allocating each letter a value.
    for key in word_letters:
        word_score += word_letters[key] * letter_score[key]

    # Get score multiplier for the list selected.
    if from_file == "Beginner":
        list_score = 0.75
    elif from_file == "Intermediate":
        list_score = 1
    elif from_file == "Expert":
        list_score = 1.25
    else:
        list_score = 1

    # Get score multiplier for the difficulty selected.
    if difficulty == "Easy":
        difficulty_score = .75
    elif difficulty == "Normal":
        difficulty_score = 1
    elif difficulty == "Hard":
        difficulty_score = 1.25
    else:
        difficulty_score = 1

    # Get score multiplier from time take to complete the gameplay function.
    time_score = 1 / (time_taken / 120)

    # Calculate total score.
    score = word_score * list_score * difficulty_score * time_score

    return word_score, list_score, difficulty_score, round(time_score, 2), round(score, 2)


def write_high_score(user_name, from_file, score):
    """
    Opens the high_scores.txt file and checks if it should replace any of the high scores with the new score
    :param user_name: name of the user
    :param from_file: the name of the file the word came from
    :param score: total score of the game
    :return place: where the user place in the high scores, if any
    """
    lines = list()
    place = None
    custom = True
    count = 0
    with open("game_files/high_scores.txt", "r") as score_file:

        # If the user was using one of the three pre-made word collections.
        while count <= 2:
            for line in score_file.readlines(3):
                count += 1

                # Matches the word collection selected with the corresponding line in the high scores file.
                if line.startswith(from_file):

                    # Therefor it was not a custom list.
                    custom = False

                    new_line = ""
                    parts = line.strip().split(",")
                    new_line += parts[0] + ","

                    # If the user beat the first score.
                    if score > float(parts[1].split()[2]):
                        new_line += " 1st" + " " + user_name + " " + str(score) + ","
                        new_line += parts[1].replace("1st", "2nd") + ","
                        new_line += parts[2].replace("2nd", "3rd") + ","
                        place = "First"

                    # If the user the second score.
                    elif score > float(parts[2].split()[2]):
                        new_line += parts[1] + ","
                        new_line += " 2nd" + " " + user_name + " " + str(score) + ","
                        new_line += parts[2].replace("2nd", "3rd") + ","
                        place = "Second"

                    # If the user beat the third score.
                    elif score > float(parts[3].split()[2]):
                        new_line += parts[1] + ","
                        new_line += parts[2] + ","
                        new_line += " 3rd" + " " + user_name + " " + str(score) + ","
                        place = "Third"

                    # If the user didn't beat any of the top three scores.
                    else:
                        new_line += parts[1] + ","
                        new_line += parts[2] + ","
                        new_line += parts[3] + ","
                    lines.append(new_line)

                # If the line did not match the word collection selected.
                else:
                    lines.append(line.strip())

        for line in score_file.readlines(1):
            # If a custom file was selected.
            if custom is True:
                new_line = ""
                parts = line.strip().split(",")
                new_line += parts[0] + ","

                # If the user beat the first score.
                if score > float(parts[1].split()[2]):
                    new_line += " 1st" + " " + user_name + " " + str(score) + " using the list of words " + from_file + ","
                    new_line += parts[1].replace("1st", "2nd") + ","
                    new_line += parts[2].replace("2nd", "3rd") + ","
                    place = "First"

                # If the user the second score.
                elif score > float(parts[2].split()[2]):
                    new_line += parts[1] + ","
                    new_line += " 2nd" + " " + user_name + " " + str(score) + " using the list of words " + from_file + ","
                    new_line += parts[2].replace("2nd", "3rd") + ","
                    place = "Second"

                # If the user beat the third score.
                elif score > float(parts[3].split()[2]):
                    new_line += parts[1] + ","
                    new_line += parts[2] + ","
                    new_line += " 3rd" + " " + user_name + " " + str(score) + " using the list of words " + from_file + ","
                    place = "Third"

                # If the user didn't beat any of the top three scores.
                else:
                    new_line += parts[1] + ","
                    new_line += parts[2] + ","
                    new_line += parts[3] + ","
                lines.append(new_line)

            # If a custom file was not selected.
            else:
                lines.append(line.strip())

    # Write the updated scores to file if a new score added.
    if place is not None:
        with open("game_files/high_scores.txt", "w") as score_file:
            for line in lines:
                score_file.write(line + "\n")

    return place


def scoring(height, width, user_name, word, from_file, difficulty, result, time_taken):
    """
    A combination of all the required functions to complete the version 1.6 enhancement
    Only takes score into account if the result is True
    :param height: height of the box
    :param width: width of the box
    :param user_name: name of the user
    :param word: the target word
    :param from_file: the name of the file the word came from
    :param difficulty: the difficulty selected
    :param result: True, False or None for how the game went
    :param time_taken: time, in seconds, to complete the gameplay function
    """
    calculations = calculate_score(word, from_file, difficulty, time_taken)

    # If the game was won.
    if result is True:
        place = write_high_score(user_name, from_file, calculations[4])
        if place == "First":
            placing = f"Congratulations {user_name}, you took first place!"
        elif place == "Second":
            placing = f"Well done {user_name}, you took second place!"
        elif place == "Third":
            placing = f"Nice work {user_name}, your on the leaderboard!"
        else:
            placing = f"{user_name}, that's not high enough for the leaderboard!"

        final_scoreboard_box(height, width, word, from_file, difficulty, time_taken, placing,
                             calculations[0], calculations[1], calculations[2], calculations[3], calculations[4])

    # if the game was lost or quit.
    else:
        placing = f"That could have been your score {user_name}... Such a pity!"
        final_scoreboard_box(height, width, word, from_file, difficulty, time_taken, placing,
                             calculations[0], calculations[1], calculations[2], calculations[3], calculations[4])
