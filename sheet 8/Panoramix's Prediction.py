a, b = [int(i) for i in input().split(" ")]


def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    else:
        return True

flag = False
for i in range(a +1, b):
    if is_prime(i):
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")