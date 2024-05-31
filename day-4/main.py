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

# names = input("Enter everyone's name seperated by comma.\n")
# names_list = names.split(", ")
# print(names_list)
# print(len(names_list))
# random_card = random.randint(0, len(names_list)-1)
# print(random_card)
# print(names_list[random_card])

# ------------ X ------------

# nested lists
row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

tmap = [row1, row2, row3]
print("\n",row1,"\n",row2,"\n",row3,"\n")
position = input("where do you want to put the treasure.\t")
col = int(position[0])
row = int(position[1])
print(col)
print(row)
final_row = tmap[row-1]
print(final_row)
final_row[col-1] = "X"

print("\n",row1,"\n",row2,"\n",row3,"\n")