all_words = list()
with open(f"game_files/expert.txt", "r") as file:
    for line in file:
        if len(line.strip()) >= 4:
            all_words.append(line.strip())
file.close()

word = "zwitterion".upper()
guesses = ""
progress = ""
rounds = 0
lives = 6

possible_words = list()
for possible_word in all_words:
    if len(word) == len(possible_word):
        possible_words.append(possible_word)
print(len(all_words))
print(len(possible_words))
while len(possible_words) > 1:
    print(possible_words)
    for character in word:
        if character in guesses:
            progress += " " + character + " "
        else:
            progress += " _ "

    letter_histogram = dict()
    for possible_word in possible_words:
        for letter in possible_word:
            if letter not in guesses.lower():
                letter_histogram[letter] = letter_histogram.get(letter, 0) + 1
    print(letter_histogram)
    guess = (max(letter_histogram.items(), key=lambda x: x[1]))[0].upper()
    guesses += guess
    print(guess)
    rounds += 1

    temp = list()
    if guess in word:
        for possible_word in list(possible_words):
            if guess.lower() in possible_word:
                i = [index for index, value in enumerate(word) if value == guess]
                ir = [index for index, value in enumerate(possible_word) if value == guess.lower()]
                if i == ir:
                    temp.append(possible_word)
                possible_words = temp

    if guess not in word:
        lives -= 1
        for possible_word in list(possible_words):
            if guess.lower() in possible_word:
                possible_words.remove(possible_word)

print(f"the word is {possible_words}")
print(lives)
