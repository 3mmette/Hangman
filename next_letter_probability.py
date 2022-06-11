def next_letter(progress, guesses):
    """
    Gives you the possible letters and their respective probabilities for a word in progress
    :param progress: The progress you have made, with any missing letters shown with a '-' symbol
    :param guesses: All the letters you have guessed so far
    :return: Histogram of probabilities
    """

    # Create a list off all the possible words.
    all_words = list()
    with open(f"game_files/Expert.txt", "r") as word_file:
        for line in word_file:
            if len(line.strip()) >= 4:
                all_words.append(line.strip().upper())

    # Create a sting of correct and incorrect guesses.
    correct_guesses = progress.replace("-", "")
    incorrect_guesses = ""
    if correct_guesses not in guesses:
        incorrect_guesses += guesses

    # Gets all the words with the same length.
    possible_words = list()
    for possible_word in list(all_words):
        if len(progress) == len(possible_word):
            possible_words.append(possible_word)

    # Removes all words with incorrectly guessed letters.
    for possible_word in list(possible_words):
        if any(guess in incorrect_guesses for guess in possible_word):
            possible_words.remove(possible_word)

    # Uses correct letters to match word progress
    for possible_word in list(possible_words):
        word = ""
        for letter in possible_word:
            if letter in correct_guesses:
                word += letter
            else:
                word += "-"
        if progress != word:
            possible_words.remove(possible_word)

    # Creates a histogram of the possible words.
    letter_histogram = dict()
    for possible_word in possible_words:
        no_doubles = "".join(set(possible_word))
        for letter in no_doubles:
            if letter not in guesses:
                letter_histogram[letter] = letter_histogram.get(letter, 0) + 1

    # Sort histogram so the highest number is at the top.
    sorted_histogram = dict(sorted(letter_histogram.items(), key=lambda item: item[1], reverse=True))

    # Prints the percentage chance of each letting being in the word.
    total = sum(sorted_histogram.values())
    for k, v in sorted_histogram.items():
        print(f"{k}: {round((v / total) * 100, 2)}%")


if __name__ == "__main__":
    current_progress = input("Enter progress so far, with - for missing letters: ").upper()
    all_guesses = input("Enter all guesses: ").upper()
    next_letter(current_progress, all_guesses)
