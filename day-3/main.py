# if-else

# WAP to check if a number is odd or even.

# number = int(input("Enter any number: "))
# if number % 2 == 0:
#     print(number, "is a even number.")
# else:
#     print(number, "is a odd number.")

# ----------------X--------------------

# nested if-else

# WAP for BMI Calculator 2.0.

height = float(input("Enter you height(in m): "))
weight = float(input("Enter your weight(in kg): "))
bmi = round(weight / (height ** 2), 2)

if bmi <= 18.5:
    print("your BMI is", bmi, "and you are under weight.")
elif bmi > 18.5 and bmi <= 25:
    print("you BMI is", bmi, "and you are normal weight.")
elif bmi > 25 and bmi <= 30:
    print("your BMI is", bmi, "and you are over weight.")
else:
    print("your BMI is", bmi, "and you are clinically obese") 

# ----------------X--------------------

# WAP to determine that is given year is a leap yer or not.

# year = int(input("Enter any year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year.")
#         else:
#             print(year, "is not a leap year.")
#     else:
#         print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")