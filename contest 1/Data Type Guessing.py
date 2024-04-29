import math


n, k, a = [int(x) for x in input().split(" ")]

res = (n * k) / a
 
if (res - math.floor(res) == 0):
    if abs(res) <= 2147483647:
        print("int")
    else:
        print("long long")
else:
    print("double")