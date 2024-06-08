import math
# More on functions
# def greet():
#     print("Hello,")
#     print("How are you??")
#     print("What are you doing??")

# greet()

# Function with Input
# def greet(name):
#     print("Hello", name)

# greet("Nehanshu")

# Functions with multiple input
# def greet(name, location):
#     print("Name is", name)
#     print("Lives in", location)

# greet("Nehanshu", "Indore")

# positional arguments
# def greet(name, location):
#     print("Name is", name)
#     print("Lives in", location)

# greet("Nehanshu", "Indore")
# greet("Indore", "Nehanshu") # Positional arguments

# KeyWord Arguments
# def practice(a, b, c):
#     print("A is",a, "\nB is",b, "\nC is",c)

# practice(1, 2, 3)
# practice(c = 3, a = 1, b = 2) # keyword arguments

# WAP to get no. of can needed to paint a wall
# def cans_needed(height, width, cover):
#     area = height * width 
#     no_of_cans = math.ceil(area / cover)
#     print(no_of_cans)

# height = int(input("Height of wall. "))
# width = int(input("Width of wall. "))
# coverage = 5

# cans_needed(height=height, width=width, cover=coverage)

# WAP to know the prime number
# def get_prime(number):
#     for i in range(2, round(number / 2)):
#         if number % i == 0:
#             return False
#     return True

# num = int(input("Enter any number. "))
# print(get_prime(number = num))

# WAP to encrypt and decrypt the 

def encode(message, shift):
    for char in range(0, len(message)):
        if message[char] == "":
            print("")

dir = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
message = input("\nType yor message:\n").lower()
shift = int(input("\nType the shift number:\n"))

if dir == "encode":
    encode(message = message, shift = shift)