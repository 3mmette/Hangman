import random

# Create a list off all the possible words.
all_words = list()
with open(f"game_files/beginner.txt", "r") as file:
    for line in file:
        if len(line.strip()) >= 4:
            all_words.append(line.strip().upper())
file.close()

progress = "T-E-"
incorrect_guesses = "I"
correct_guesses = progress.replace("-", "")

possible_words = list()
for possible_word in list(all_words):
    if len(progress) == len(possible_word):
        possible_words.append(possible_word)

for possible_word in list(possible_words):
    for guess in incorrect_guesses:
        if guess in possible_word:
            possible_words.remove(possible_word)

for possible_word in list(possible_words):
    word = ""
    for letter in possible_word:
        if letter in correct_guesses:
            word += letter
        else:
            word += "-"
    if progress != word:
        possible_words.remove(possible_word)
print(possible_words)
print(len(possible_words))
