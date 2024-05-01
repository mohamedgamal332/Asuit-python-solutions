import math

   
flag = False
x = int(input())


for i in range(2, math.ceil(math.sqrt(x)) + 1):
    if x % i == 0 and x != i :
        flag = True


if not flag:
    print("YES")
else:
    print("NO")
