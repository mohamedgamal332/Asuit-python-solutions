x = int(input())
groups = 1
lst = []

for i in range(x):
    lst.append(int(input()[-1]))

for i in range(x -1):
    if lst[i] != lst[i +1]:
        groups += 1

print(groups)

"""
another solution:
x = int(input())


def rec(x, n, item):
    if x == 0:
        return n
    else:   
        tmp = int(input()[-1])
        if item != tmp:
            n += 1
        return rec(x -1, n, tmp)
    
print(rec(x -1, 1, int(input()[-1])))

"""