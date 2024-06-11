a, b = [int(i) for i in input().split(" ")]


y = input()
count = 0

for i in range(len(y)):
    if y[i] != "-":
        count += 1
if (y[a] == "-" and count == a +b):
    print("Yes")
else:
    print("No")