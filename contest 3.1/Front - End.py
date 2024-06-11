x = int(input())

elements = [int(i) for i in input().split(" ")]

count = 0
if x % 2 != 0:
    while(count < (x // 2)):
        print(elements[count], end=" ")
        count = -(count +1)
        print(elements[count], end=" ")
        count = - count
    print(elements[count], end=" ")
else:
    while (count < (x // 2)):
        print(elements[count], end=" ")
        count = -(count +1)
        print(elements[count], end=" ")
        count = - count
