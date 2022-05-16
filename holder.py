progress_index = dict()
count = 0
for i in progress:
    progress_index[count] = i
    count += 1
print(progress_index)
# Create a list of all words with the same length.
possible_words = list()
for possible_word in all_words:
    if len(progress) == len(possible_word):
        possible_words.append(possible_word)

temp = list()
for possible_word in possible_words:
    temp_dict = dict()
    count = 0
    for i in possible_word:
        temp_dict[count] = i
        count += 1
    for k, v in progress_index.items():
        for k1, v1 in temp_dict.items():
            if k == k1 and v == v1 and v1 not in guesses:
                temp.append(possible_word)
possible_words = temp

# Create a histogram to determine the likelihood of a letter being in a word.
letter_histogram = dict()
for possible_word in possible_words:
    no_doubles = "".join(set(possible_word))
    for letter in no_doubles:
        if letter not in guesses:
            letter_histogram[letter] = letter_histogram.get(letter, 0) + 1

# Get the most probable letter to guess.
guess = (max(letter_histogram.items(), key=lambda x: x[1]))[0].upper()
if letter_histogram[guess] == 1:
    print("It is now down to luck.")
    print(f"The word could be {possible_words}")
print(guess)
print(letter_histogram)
print(possible_words)
