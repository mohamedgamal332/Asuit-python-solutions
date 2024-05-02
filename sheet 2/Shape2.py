x = int(input()) - 1

cnc = " " * x 
sec = "*"
tot = ""

while cnc:
    tot += cnc + sec
    print(tot)
    for i in range(x):
        cnc = " " * i
    sec += "**"
    tot = ""
    x -= 1
 
print(sec)