x = int(input())
lst =[]


for i in range(1, x + 1):
    if x % i == 0:
        lst.append(i)


for i in (lst):
    print(i)