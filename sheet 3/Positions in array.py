x = int(input())
y = [int(s) for s in input().split(" ")]

lst = []
for i in range(x):
    if y[i] <= 10:
        lst.append(i)

for i in range(len(lst)):
    print(f"A[{lst[i]}] = {y[lst[i]]}")
