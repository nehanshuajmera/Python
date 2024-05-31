# Randomness

import random

# Random Integer
# integer = random.randint(1, 10)
# print(integer)

# Random Float
# floating = random.random()
# print(floating)

# ------------ X ------------

# WAP to print head and tails (randomily)
# toss = random.randint(1, 2)

# if toss == 1:
#     print("Heads")
# else:
#     print("Tails")

# ------------ X ------------

# Lists

names = input("Enter everyone's name seperated by comma.\n")
names_list = names.split(", ")
print(names_list)
print(len(names_list))
random_card = random.randint(0, len(names_list)-1)
print(random_card)
print(names_list[random_card])