n, a, b = [int(x) for x in input().split(" ")]
lst = []

for i in range(n + 1):
    count = 0
    for x in str(i):
        count += int(x)
    if (count >= a) and (count <= b):
        lst.append(i)
print(sum(lst))