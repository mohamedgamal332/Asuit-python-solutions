import copy

lst3 = [i for i in range(10, 1000000)]
lst4 = []

for x in lst3:
    for i in range(x):
        sum = (i * (i+1) // 2)
        if sum == x:
            lst4.append(i // x)
            break
        elif sum >= x:
            lst4.append((i -1) // x)
            break
        continue

print(lst4)