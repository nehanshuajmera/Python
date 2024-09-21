# Wap to print 
# 1 1 1 
# 2 2 2 
# 3 3 3 

# n = int(input())
# i = 1
# while (i <= n):
#   j = 1
#   while (j <= n):
#     print(i, end=" ")
#     j = j + 1
#   print("\n")
#   i = i + 1

#  --------------------------- X --------------- 

# Wap to print
# 1 2 3
# 4 5 6
# 7 8 9

n = int(input())

count = 1
i = 1

while (i <= n):
  j = 1
  while (j <= n):
    print(count, end=" ")
    count = count + 1
    j = j + 1
  print()
  i = i + 1