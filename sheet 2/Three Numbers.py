k, s = [int(x) for x in input().split(" ")]

count = 0

for x in range(k +1):
    for y in range(k +1):
        if (s - x - y >= 0) and (s - x - y <= k ):
            count += 1 

print(count)