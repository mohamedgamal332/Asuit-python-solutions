import copy

x = int(input()) - 1
num = copy.copy(x)

cnc = " " * x 
sec = "*"
tot = ""

while cnc:
    tot += cnc + sec
    print(tot)
    cnc = " " * (x - 1)
    sec += "**"
    tot = ""
    x -= 1
 
cnc = ""
w = num
print(sec)
while x != (num + 1):
    tot += cnc + sec
    print(tot)
    cnc = " " * (x +1)
    sec = "*" * (2 * w - 1)
    tot = "" 
    x += 1
    w -= 1



print(sec)