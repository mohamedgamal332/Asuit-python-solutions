a, b = [int(i) for i in input().split(" ")]

inputs = [int(i) for i in input().split(" ")]

freq = [0] * b
for i in inputs:
    if freq[i -1] == 0:
        freq[i -1] = 1
    else:
        freq[i -1] += 1

print(*freq, sep= "\n")