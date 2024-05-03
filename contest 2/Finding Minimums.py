a, b = [int(x) for x in input().split(" ")]
lst = []


cases = [int(x) for x in input().split(" ")]

while cases:
    if len(cases) > b:
        x = min(cases[0:b])
        lst.append(x)
        del cases[:b]
    else:
        x = min(cases)
        lst.append(x)
        break


print(*lst)