lst = []
for i in range(int(input())):
    a, b = [int(x) for x in input().split(" ")]

    lst.append((((max(b,a) *(max(b,a) +1))//2) - ((min(b,a)-1) *((min(b,a)-1) +1))//2))
print(*lst, sep='\n')

