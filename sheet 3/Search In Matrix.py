rows , columns = [int(i) for i in input().split(" ")]

matrix = ""
for i in range(rows):
    matrix += input()

mat = matrix.split(" ")

target = input()
if target in matrix:
    print("will not take number")
else:
    print("will take number")