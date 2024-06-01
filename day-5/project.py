# password generator
import random

alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']

alphabets = int(input("Enter the number of alphabets you want in your password.\t"))
numbers = int(input("Enter the number of numbers you want in your password.\t"))
symbols = int(input("Enter the number of symbols you want in your password.\t"))

password = []

for alphabet in range(1, alphabets + 1):
    password += random.choice(alphabets_list)

for number in range(1, numbers + 1):
    password += random.choice(numbers_list)

for symbol in range(1, symbols + 1):
    password += random.choice(symbols_list)

random.shuffle(password)

new_pass = ""
for char in password:
    new_pass += char

print("Your password is:",new_pass)