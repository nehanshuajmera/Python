# number = input("Enter any two digit number: ")

# No need to convert variable number to string because it is already in string format.
# print("Type of number is: ", type(number), "\n")
# string = str(number)
# line number 4 and 5 are unnecessary

# print("Type of string is: ",type(string), "\n")
# zeroth = int(string[0])
# first = int(string[1])
# print(type(zeroth), type(first))
# sum = zeroth + first
# print(sum)

# Mathematical operations
# print("sum: ", 5 + 4)
# print("substraction: ", 5 - 4)
# print("Multiplication: ", 5 * 4)
# print("Division: ", 5 / 4)
# print("Power: ", 5 ** 4)

# Priority
# ()
# **
# *  /  (left to right)
# +  -  (left to right)

# BMI calculator 
# height = float(input("Enter your height in m: "))
# weight = int(input("Enter you weight in kg: "))

# bmi = (weight / (height ** 2))
# print(int(bmi))

# f-string
age = int(input("What is your current age: "))
left = 90 - age
days = left * 365
weeks = left * 52
months = left * 12

print("you have", days,",", weeks, "weeks, and", months, "months left.")