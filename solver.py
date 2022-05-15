import time

from gameplay import qwerty_keys


all_words = list()
with open(f"game_files/intermediate.txt", "r") as file:
    for line in file:
        if len(line.strip()) >= 4:
            all_words.append(line.strip())
file.close()

result = None
round_result = None
picture = None
keyboard = qwerty_keys
guesses = ""
lives = 6
word = "MATE"
possible_words = list()
for possible_word in all_words:
    if len(word) == len(possible_word):
        possible_words.append(possible_word)

while result is None:
    time.sleep(1)
    failed = 0
    progress = ""
    # **Modified Original Code** Creates a word with any characters not guessed replaced with an underscore.
    for character in word:
        if character in guesses:
            progress += " " + character + " "
        else:
            progress += " _ "
            failed += 1

    # If failed is equal to zero, the game is won so result is set to True and break stops the loop.
    if failed == 0:
        result = True
        break

    # If it is the first round, tells the player time has started, otherwise comments on their progress.

    letter_histogram = dict()
    for possible_word in possible_words:
        for letter in possible_word:
            if letter not in guesses.lower():
                letter_histogram[letter] = letter_histogram.get(letter, 0) + 1
    print(letter_histogram)
    guess = (max(letter_histogram.items(), key=lambda x: x[1]))[0].upper()
    print(guess)

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
    temp = list()
    if guess not in word:
        # lives counter decreases by 1
        lives -= 1
        round_result = False
        for possible_word in list(possible_words):
            if guess.lower() in possible_word:
                possible_words.remove(possible_word)

    if guess in word:
        round_result = True
        for possible_word in list(possible_words):
            if guess.lower() in possible_word:
                i = [index for index, value in enumerate(word) if value == guess]
                ir = [index for index, value in enumerate(possible_word) if value == guess.lower()]
                if i == ir:
                    temp.append(possible_word)
    print(temp)
    # If the lives are equal to zero, result set to False and loop breaks
    if lives == 0:
        result = False
        break



