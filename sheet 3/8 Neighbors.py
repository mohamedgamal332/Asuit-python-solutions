n ,m = [int(i) for i in input().split(" ")]
x = "0"

row = x * (m +2)
mat = []
mat.append(row)
for i in range(n):
    mat.append(x + input() + x)
mat.append(row)


inx , iny = [int(i) for i in input().split(" ")]


if (mat[inx -1][iny -1] != ".") and (mat[inx][iny -1] != ".") and (mat[inx +1][iny -1] != ".") and (mat[inx -1][iny] != ".") and (mat[inx +1][iny] != ".") and (mat[inx -1][iny +1] != ".") and (mat[inx][iny +1] != ".") and (mat[inx +1][iny +1] != "."):
    print("yes")
else:
    print("no")