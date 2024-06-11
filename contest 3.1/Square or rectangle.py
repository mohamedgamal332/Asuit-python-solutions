lst = []
for i in range(int(input())):
    a, b = [int(i) for i in input().split(" ")]
    if a == b:
        lst.append("Square")
    else:
        lst.append("Rectangle")

print(*lst, sep= "\n")