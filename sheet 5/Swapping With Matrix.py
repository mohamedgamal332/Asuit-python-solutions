import numpy as np

def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]
    return matrix

def swap_columns(matrix, col1, col2):
    matrix[:,[col1, col2]] = matrix[:,[col2, col1]]
    return matrix

parameters = [int(x) for x in input().split()]

lst = []
for i in range(parameters[0]):
    tmp = [int(x) for x in input().split()]
    lst.append(tmp)
matrix = np.array(lst)
matrix = swap_rows(matrix, parameters[1] -1, parameters[2] -1)
matrix = swap_columns(matrix, parameters[1] -1  , parameters[2] -1)
print(matrix)