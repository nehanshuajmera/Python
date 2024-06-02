# Hangman

import random

word_list = ["advark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
word = []
for blank in chosen_word:
    word += "_"

print(word)

guess = input("Guess any letter. ").lower()

for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
        print(guess)
        word[i] = guess
    else:
        print("Wrong")

print(word)