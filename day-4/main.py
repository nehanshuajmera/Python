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
toss = random.randint(1, 2)

if toss == 1:
    print("Heads")
else:
    print("Tails")