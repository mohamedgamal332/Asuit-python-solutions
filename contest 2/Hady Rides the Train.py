x = int(input())

row = int((x - (x % 4)) / 4) 


if (row % 2 == 0):
        print(row, x %4)
else:
        print(row, 3 -(x %4))
