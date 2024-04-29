x = int(input())
flag = True

for i in range(2, x + 1, 1):
    if(i % 2 == 0):
        flag = False
        print(i)
if (flag):
    print(-1)