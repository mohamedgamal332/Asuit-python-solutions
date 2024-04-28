x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

if (x[0] % x[2] == 0) and (x[1] % x[2] == 0):
    print("Both")
elif (x[0] % x[2] == 0) and (x[1] % x[2] != 0):
    print("Memo")
elif (x[0] % x[2] != 0) and (x[1] % x[2] == 0):
    print("Momo")
else:
    print("No One")
