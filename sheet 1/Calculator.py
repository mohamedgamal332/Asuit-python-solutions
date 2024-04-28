import math

def Notoperator(i):
    if (i == "+") or (i == "-") or (i == "*") or (i == "/"):
        return False
    else:
        return True

x = input()
str = ""
lst = []
op = ""
for i in x:
    if (Notoperator(i)):
        str += i
    else:
        op = i
        lst.append(int(str))
        str = ""
lst.append(int(str))
if (op == "+"):
    print(lst[0] + lst[1])
elif (op == "-"):
    print(lst[0] - lst[1])
elif (op == "*"):
    print(lst[0] * lst[1])
else:
    print(math.floor(lst[0] / lst[1]))