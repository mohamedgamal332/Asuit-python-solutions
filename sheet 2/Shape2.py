x = int(input()) - 1

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
 
print(sec)