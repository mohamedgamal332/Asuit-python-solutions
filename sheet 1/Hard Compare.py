import math
a, b, c, d = [int(x) for x in input().split(" ")]


if ((b * math.log(a)) > (d * math.log(c))):
    print("YES")
else:
    print("NO")