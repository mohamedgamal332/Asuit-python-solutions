lst = []

for i in range(int(input())):
    lst.append(int(input()))

result = 1
for i in lst:
    for x in range(1, i + 1):
        result *= x
    print(result)
    result = 1


