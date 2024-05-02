a, b = [int(x) for x in input().split(" ")]
lst1 = []
lst2 = []


for i in range(1, a + 1):
    if a % i == 0:
        lst1.append(i)


for i in range(1, b + 1):
    if b % i == 0:
        lst2.append(i)


print(max(list(set(lst1).intersection(lst2))))