x = int(input())
num = 4 * x 


for i in range(1, num + 1 ):
    if (num):
        if (i) % 4 == 0:
            print("PUM")
        else:
            print(i, end = " ")
    else:
        break
    num -= 1