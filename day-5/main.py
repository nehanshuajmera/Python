# loops

# 1. For loop
# fruits = ["apple", "mango", "orange"]

# for fruit in fruits:
#     print(fruit)

# ------------ X ---------------

# WAP to print average height of students

# height_list = input("Enter the height of students.\n").split(" ")
# print(height_list)
# length = len(height_list)
# sum = 0

# for height in height_list:
#     sum += int(height)

# average = round(sum / length)
# print(average)

# ------------ X ---------------

# WAP to print the maximum value present in the list

# values = input("Enter the elements.\n").split()
# print(values)

# max_val = 0
# for value in values:
#     if max_val < int(value):
#         max_val = int(value)

# print(max_val)

# ------------ X ---------------

# range

sum = 0
for number in range(1, 101):
    sum += number

print(sum)