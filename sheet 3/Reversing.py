x = int(input())
y = [int(i) for i in input().split(" ")]

for i in range(x -1, -1, -1):
    print(y[i], end=" ")