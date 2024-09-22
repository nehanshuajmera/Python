# Wap to print product - sum of digits of a number

n = int(input())

prod_of_digits = 1
sum_of_digits = 0

while(n != 0):
  digit = n % 10
  prod_of_digits *= digit
  sum_of_digits += digit
  n //= 10

print(prod_of_digits - sum_of_digits)