x = input().split("=")

op = ["+", "-", "*", "/"]
y = []


for i in x[0]:
    if i in op:
        y = x[0].split(i)
        if i == "+":
            y.append(int(y[0]) + int(y[1]))
        elif i == "-":
            y.append(int(y[0]) - int(y[1]))
        if i == "*":
            y.append(int(y[0]) * int(y[1]))
        if i == "/":
            y.append(int(y[0]) / int(y[1]))
        
if int(x[-1]) == y[-1]:
    print("Yes")
else:
    print(y[-1])