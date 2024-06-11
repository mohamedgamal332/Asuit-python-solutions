x = int(input())
y = [int(i) for i in input().split(" ")]

first = ""
sec = ""
last = ""
count = 0

for i in y:
    if i == 0:
        count += 1
        continue

    if count == 0:
        first += str(i)
        first += " "
    if count == 1:
        sec += str(i)
        sec += " "
    if count == 2:
        last += str(i)
        last += " "

print(sec + "0 " + first + "0 " + last)
