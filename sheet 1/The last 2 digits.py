x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

tmp = str(x[0] * x[1] * x[2] * x[3])

print(tmp[-2] + tmp[-1]) 