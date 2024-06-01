# loops

# 1. For loop
# fruits = ["apple", "mango", "orange"]

# for fruit in fruits:
#     print(fruit)

# ------------ X ---------------

# WAP to print average height of students

height_list = input("Enter the height of students.\n").split(" ")
print(height_list)
length = len(height_list)
sum = 0

for height in height_list:
    sum += int(height)

average = round(sum / length)
print(average)