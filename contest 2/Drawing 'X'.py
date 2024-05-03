x = int(input())

for i in range(x):
    cont = ""
    for j in range(x):
        if (i == j) and (i == int(x/2)):
            cont += "X"
        elif (i == j) and (i != int(x/2)):
            cont += "\\"
        elif (i + j == x-1) and (i != int(x/2)):
            cont += "/"
        else:
            cont += "*"
    print(cont)