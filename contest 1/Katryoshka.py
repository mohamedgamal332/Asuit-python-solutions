x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

eyes, mouths, bodies = x[0], x[1], x[2]

count = min(eyes, mouths, bodies)
eyes -= count
mouths -= count
bodies -= count
count += min(eyes // 2, bodies)

print(count)
