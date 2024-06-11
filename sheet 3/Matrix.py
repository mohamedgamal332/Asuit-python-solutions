size = int(input())

mat_2d = []

for i in range(size):
    row = [int(x) for x in input().split(" ")]
    mat_2d.append(row)

main_d = 0
sec_d = 0

for i in range(size):
    for j in range(size):
        if i == j:
            main_d += mat_2d[i][j]
        if i + j == size -1:
            sec_d += mat_2d[i][j]

print(abs(main_d - sec_d))