x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

copy = x[:]
lst = []

for i in range(len(x)):
    lst.append(min(copy))
    copy.remove(min(copy))

for i in range(3):
    print(lst[i])

print("")

for i in range(3):
    print(x[i])

