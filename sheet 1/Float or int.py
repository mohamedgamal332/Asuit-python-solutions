import math

x = float(input())

flag = x - math.floor(x)


if flag:
    print(f"float {int(x)} {flag:.3f}")
else:
    print(f"int {int(x)}")