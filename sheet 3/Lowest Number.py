x = int(input())
y = [int(i) for i in input().split(" ")]

low = 999999

for i in y:
    if low > i:
        low = i
print(low, y.index(low) + 1)