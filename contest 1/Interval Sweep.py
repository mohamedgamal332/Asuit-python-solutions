x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

if ((abs(x[0] - x[1]) == 1) or (x[0] == x[1])) and ((x[0] != 0) and (x[1] != 0)):
    print("YES")
else:
    print("NO")