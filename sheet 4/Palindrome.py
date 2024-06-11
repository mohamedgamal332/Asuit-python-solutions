x = input()

length = len(x) // 2
flag = True

for i in range(length):
    if not (x[i] == x[-(i +1)]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")