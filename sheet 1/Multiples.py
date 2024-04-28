y = input().split(" ")

x = max(int(y[0]),int(y[1]))
y = min(int(y[0]),int(y[1]))

if int(x) % int(y) == 0:
    print("Multiples")
else:
    print("No Multiples")