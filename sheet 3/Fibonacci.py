x = int(input())
lst = [0, 1]

for i in range(2, x):
    lst.append(lst[i - 1] + lst[i - 2])

print(lst[x-1])