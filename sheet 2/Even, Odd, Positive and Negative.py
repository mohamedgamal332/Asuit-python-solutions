y = input()
x = [int(x) for x in input().split(" ")]

even, odd, positive, negative = 0, 0, 0, 0

for i in x:
    if i > 0:
        if i % 2 == 0:
            even += 1
        elif (i +1) % 2 == 0:
            odd += 1
        positive += 1
    elif i < 0:
        if i % 2 == 0:
            even += 1
        elif (i +1) % 2 == 0:
            odd += 1
        negative += 1
    elif i == 0:
        even += 1


print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Positive: {positive}")
print(f"Negative: {negative}")
