def GCD(a,b):
    if a == 0:
        return b
    return GCD(b % a, a)

a, b = [int(i) for i in input().split(" ")]

print(GCD(a,b), a*b // GCD(a,b))