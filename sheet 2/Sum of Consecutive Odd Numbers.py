lst = []

for i in range(int(input())):
    a, b = [int(x) for x in input().split(" ")]
    count = 0
    for i in range(min(a, b) +1, max(a, b)):
        if i % 2 != 0:
            count += i
    lst.append(count)

for i in lst:
    print(i)