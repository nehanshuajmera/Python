# if-else

# WAP to check if a number is odd or even
# number = int(input("Enter any number: "))

# if number % 2 == 0:
#     print(number, "is a even number.")
# else:
#     print(number, "is a odd number.")

# ----------------X--------------------

# nested if-else
# WAP for BMI Calculator 2.0

height = float(input("Enter you height(in m): "))
weight = float(input("Enter your weight(in kg): "))

bmi = round(weight / (height ** 2), 2)

if bmi <= 18.5:
    print("your BMI is", bmi, "and you are under weight.")
elif bmi > 18.5 & bmi <= 25:
    print("you BMI is", bmi, "and you are normal weight.")
elif bmi > 25 & bmi <= 30:
    print("your BMI is", bmi, "and you are over weight.")
else:
    print("your BMI is", bmi, "and you are clinically obese") 