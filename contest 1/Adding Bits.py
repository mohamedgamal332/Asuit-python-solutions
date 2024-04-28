x = input().split(" ")

for i in range(len(x)):
    x[i] = int(x[i])

str = ""
num1 = bin(x[0])[2:].zfill(32)
num2 = bin(x[1])[2:].zfill(32)

for i in range(32):
    if num1[i] == "1" and num2[i] == "1":
        str += "0"
    elif num1[i] == "0" and num2[i] == "1":
        str += "1"
    elif num1[i] == "1" and num2[i] == "0":
        str += "1"
    else:
        str += "0"

print(int(str, 2)) 