x = input()


flag = True

for i in range(int(len(x) / 2)):
    if x[i] != x[- (i + 1)]:
        flag = False

reverse = ""

for i in range(len(x)):
    reverse += x[-(i + 1)]

print(int(reverse))
if flag:
    print("YES")
else:
    print("NO")