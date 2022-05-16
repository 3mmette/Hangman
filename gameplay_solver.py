import random

# Create a list off all the possible words.
all_words = list()
with open(f"game_files/expert.txt", "r") as file:
    for line in file:
        if len(line.strip()) >= 4:
            all_words.append(line.strip().upper())
file.close()

# Select a random word.
word = random.choice(all_words).upper()
print(word)

# Create a list of all words with the same length.
possible_words = list()
for possible_word in all_words:
    if len(word) == len(possible_word):
        possible_words.append(possible_word)

# Loop progress.
guesses = ""
progress = ""
incorrect_guesses = 0

# Start loop
while True:
    print(len(possible_words))
    # Create word progress.
    for character in word:
        if character in guesses:
            progress += character
        else:
            progress += "-"

    if len(possible_words) == 1:
        print(f"The word is {possible_words}")
        print(f"{incorrect_guesses} incorrect guesses were needed to solve this word.")
        break

    # Create a histogram to determine the likelihood of a letter being in a word.
    letter_histogram = dict()
    for possible_word in possible_words:
        no_doubles = "".join(set(possible_word))
        for letter in no_doubles:
            if letter not in guesses:
                letter_histogram[letter] = letter_histogram.get(letter, 0) + 1
    print(letter_histogram)
    # Get the most probable letter to guess.
    guess = (max(letter_histogram.items(), key=lambda x: x[1]))[0].upper()
    if letter_histogram[guess] == 1:
        print("It is now down to luck.")
        print(f"The word could be {possible_words}")
        print(f"{incorrect_guesses} incorrect guesses were needed to get to this point.")
        break
    guesses += guess
    print(guess)

    temp = list()
    if guess in word:
        for possible_word in list(possible_words):
            if guess in possible_word:
                i = [index for index, value in enumerate(word) if value == guess]
                ir = [index for index, value in enumerate(possible_word) if value == guess]
                if i == ir:
                    temp.append(possible_word)
                possible_words = temp

    if guess not in word:
        incorrect_guesses += 1
        for possible_word in list(possible_words):
            if guess in possible_word:
                possible_words.remove(possible_word)


