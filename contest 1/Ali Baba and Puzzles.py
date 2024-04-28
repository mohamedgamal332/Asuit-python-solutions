x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

if (x[0] - x[1] + x[2] == x[3]):
    print("YES")
elif (x[0] - x[1] * x[2] == x[3]):
    print("YES")
elif (x[0] + x[1] - x[2] == x[3]):
    print("YES")
elif (x[0] + x[1] * x[2] == x[3]):
    print("YES")
elif (x[0] * x[1] - x[2] == x[3]):
    print("YES")
elif (x[0] * x[1] + x[2] == x[3]):
    print("YES")
else:
    print("NO")