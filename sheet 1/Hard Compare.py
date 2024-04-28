import math
x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

if (math.pow((x[0]), x[1]) > math.pow(x[2]), x[3]):
    print("YES")
else:
    print("NO")