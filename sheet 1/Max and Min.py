y = input().split(" ")

for i in range(len(y)):
    y[i] = int(y[i])

print(min(y), max(y))
