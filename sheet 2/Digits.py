lst = []


for i in range(int(input())):
    lst.append(input())


for i in lst:
    for w in range(len(i)):
        print(i[-(w + 1)], end = " ")
    print()