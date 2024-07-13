# Calculator

# Functions
# addition
def add(num1, num2):
    """ Add two numbers """
    return num1 + num2

# subtract
def subtract(num1, num2):
    """ Subtract two numbers """
    return num1 - num2

# multiply
def multiply(num1, num2):
    """ Multiply two numbers """
    return num1 * num2

# divide
def divide(num1, num2):
    """ Divide teo numbers """
    return num1 / num2

# Dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

number1 = int(input("\nEnter the first number: "))
number2 = int(input("\nEnter the second number: "))

for symbol in operations:
    print(symbol)
operation = input("\nSelect any operation to perform: ")

calculate_function = operations[operation]
answer = calculate_function(number1, number2)

print(answer)