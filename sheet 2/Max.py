x = input()
inputs = [int(i) for i in input().split(" ")]

max = 0

for i in inputs:
    if max < i:
        max = i

print(max)