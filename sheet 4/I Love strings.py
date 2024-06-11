lst= []
for iteration in range(int(input())):
    x = input()
    iter = len(x) // 2 +1

    conc = ""
    for i in range(iter +1):
        if len(x) % 2 != 0:
            if i >= len(x) - iter:
                conc += (x[i])
                break
            conc += (x[i] + x[i+ iter])

        else:
            if i >= len(x) - iter:
                print(conc)
                conc += (x[-1])
                print(conc)
                break
            conc += x[i] + x[i+ iter -1]
    lst.append(conc)
print(*lst, sep= "\n")
