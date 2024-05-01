flag = True
lst = []

while(flag):
    if int(input()) == 1999:
        lst.append("Correct")
        flag = False
    else:
        lst.append("Wrong")

for i in lst:
    print(i)