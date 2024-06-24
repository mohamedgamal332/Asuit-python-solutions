x = input()

lst = [int(i) for i in input().split(" ")]

maxx = 00
minn = 101
first = 0
last = 0

for i in range(len(lst)):
    if lst[i] >= maxx:
        maxx = lst[i]
        first = i

    if lst[i] <= minn:
        minn = lst[i]
        last = i


sum = 0


if first > last:
    sum += first
    sum += (len(lst) -1 - last) -1

else:
    sum += first + (len(lst) -1 - last)

print(sum)