lst = []

for i in range(int(input())):
    x = input()
    flag = False
    for i in range(len(x) -2):
        if x[i] == "0" and x[i +1] == "1" and x[i +2] == "0" :
            flag = True
        elif x[i] == "1" and x[i +1] == "0" and x[i +2] == "1" :
            flag = True
        else:
            continue
    if flag:
        lst.append("Good")
    else:
        lst.append("Bad")

print(*lst, sep="\n")