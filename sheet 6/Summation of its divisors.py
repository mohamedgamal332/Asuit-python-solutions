x = int(input())
sumu = []


for i in range(1, int(x ** 0.5) +1):
    if x % i == 0:
        sumu.append(i)
        sumu.append(x // i)

print(sum(list(set(sumu))))
