lst = []

for i in range(int(input())):
    elemNum = int(input())
    elements = [int(i) for i in input().split(" ")]
    even, odd = 0, 0

    if elemNum % 2 == 0:
        for i in elements:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        lst.append(abs((even - odd) // 2))
    else:
        lst.append(-1)

print(*lst, sep= "\n")