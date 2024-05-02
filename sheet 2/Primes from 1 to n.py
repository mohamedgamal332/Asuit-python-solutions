import math

x = int(input())
lst = []

for i in range(2, x + 1):
    flag = False
    for w in range(2, math.ceil(math.sqrt(i) + 1)):
        if i % w == 0 and i != w:
            flag = True
    if not flag:
        lst.append(i)

for i in (lst):
    print(i, end = " ")