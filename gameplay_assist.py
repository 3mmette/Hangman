import random

# Create a list off all the possible words.
all_words = list()
with open(f"game_files/Expert.txt", "r") as word_file:
    for line in word_file:
        if len(line.strip()) >= 4:
            all_words.append(line.strip().upper())

progress = input("Enter progress so far, with - for missing letters: ").upper()
incorrect_guesses = input("Enter any incorrect guesses: ").upper()
correct_guesses = progress.replace("-", "")
guesses = correct_guesses + incorrect_guesses

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
sorted_histogram = dict(sorted(letter_histogram.items(), key=lambda item: item[1], reverse=True))

total = sum(sorted_histogram.values())
for k, v in sorted_histogram.items():
    print(f"{k}: {round((v / total) * 100, 2)}%")

