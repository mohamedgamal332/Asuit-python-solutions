a, b = [int(x) for x in input().split(" ")]
lst = []


for i in range(a, b+1):
    x = set(str(i))
    if not (x.difference({'4', '7'})) or not (x.difference({'4'})) or not (x.difference({'7'})):
        lst.append(i)

if lst:
    for i in lst:
        print(i, end =" ")
else:
    print(-1)


        