# Hangman

import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
word = []
for blank in chosen_word:
    word += "_"

lives = 6
end = False

while not end:
    guess = input("\nGuess any letter. ").lower()

    for i in range(0, len(chosen_word)):
        if lives != 0 and chosen_word[i] == guess:
            word[i] = guess

    # print(word)
    print("\n",' '.join(word))
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end = True
            print("\nYou Lose!!!!!")

    print("\nYou have", lives, "lives left")

    if "_" not in word:
        end = True
        print("\nYou Win!!!!!")
        