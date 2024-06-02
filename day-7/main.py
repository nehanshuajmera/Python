# Hangman

import random

word_list = ["advark", "baboon", "camel"]

chosen_word = random.choice(word_list)

word = []
for blank in chosen_word:
    word += "_"

print(word)

guess = input("Guess any letter. ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
