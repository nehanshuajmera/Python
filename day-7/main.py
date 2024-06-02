# Hangman

import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
word = []
for blank in chosen_word:
    word += "_"

print(word)

end = False

while not end:
    guess = input("Guess any letter. ").lower()

    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            word[i] = guess

    print(word)

    if "_" not in word:
        end = True
        print("You Win!!!!!")
        