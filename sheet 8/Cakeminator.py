import numpy as np


x, y = [int(i) for i in input().split(" ")]
mat = []
coor = []

for i in range(x):
    lst = list(input())
    for z in range(len(lst)):
        if lst[z] == "S":
            coor.append([i,z])
    mat.append(lst)

mat = np.array(mat)


print(mat)
print(coor)

