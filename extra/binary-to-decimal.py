# Wap to print decimal number of given binary number.

n = int(input())

ans = 0
i = 0

while (n != 0):
  digit = n % 10

  if( digit & 1 ):
    ans += pow(2, i)

  i += 1
  n //= 10

print(ans)