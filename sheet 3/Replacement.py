x = int(input())

y = [int(i) for i in input().split(" ")]

for i in range(x):
    if y[i] < 0:
        y[i] = 2
    elif y[i] > 0:
        y[i] = 1

print(*y, sep=" ")