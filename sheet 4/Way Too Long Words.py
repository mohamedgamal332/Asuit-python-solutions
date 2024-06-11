lst = []
for i in range(int(input())):
    x = input()
    if len(x) > 10:
        lst.append(x[0] + str(len(x) -2) + x[-1  ])
    else:
        lst.append(x)

print(*lst, sep= "\n")