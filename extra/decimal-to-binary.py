# Wap to print pinary representation of given number.

n = int(input())

ans = 0
i = 0

while (n != 0):
  bit = n & 1

  ans += (pow(10, i) * bit)

  n = n >> 1
  i += 1

print(ans)