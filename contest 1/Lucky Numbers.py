a, b = [int(x) for x in input()]


if (a) and (b):
    if (a % b == 0) or (b % a == 0):
        print("YES")
    else:
        print("NO")
else:
    print("YES")