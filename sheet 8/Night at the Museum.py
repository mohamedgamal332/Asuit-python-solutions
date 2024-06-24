word = list(input())

rotations = 0

start = ord("a")

for i in word:
    dis_i = ord(i) - ord("a")
    dis_start = start - ord("a")

    clockwize = abs(dis_start - dis_i)
    counterwize = 26 - clockwize

    start = ord(i)

    rotations += min(clockwize, counterwize)

print(rotations)

