x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

print(f"{(x[1] / (1 - (x[0] / 100))):.2f}")
