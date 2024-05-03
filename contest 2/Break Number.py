x = int(input())
y = [int(x) for x in input().split(" ")]
lst = []


for i in range(x):
    count = 0
    while( y[i] % 2 == 0):
        y[i] /= 2 
        count += 1
    lst.append(count)

print(max(lst))