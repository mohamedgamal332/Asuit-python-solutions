import copy

x = int(input())
y = [int(i) for i in input().split(" ")]

mini = y.index(min(y))
maxi = y.index(max(y))
tmp = copy.copy(y[maxi])
y[maxi] = y[mini]
y[mini] = tmp

print(*y, sep=" ")