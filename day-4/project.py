# Rock papers and scissors game

import random

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors.\t"))
choice_list = ["rock", "paper", "scissors"]
com_choice = random.choice(choice_list)
print("\nYou chose:",human)
print("\nComputer chose:",com_choice)

if (human == 0 and com_choice == "rock") or (human == 1 and com_choice == "paper") or (human == 2 and com_choice == "scissors"):
    print("\nDraw")
elif (human == 0 and com_choice == "scissors") or (human == 1 and com_choice == "rock") or (human == 2 and com_choice == "paper"):
    print("\nYou Win!!!")
else:
    print("\nYou Lose!!!")