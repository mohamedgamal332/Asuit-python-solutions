x = int(input())
y = [int(i) for i in input().split(" ")]

flag = False

for i in range(int(x /2)):
    if y[i] != y[-(i + 1)]:
        flag = True

if (not flag):
    print("YES")
else:
    print("NO")