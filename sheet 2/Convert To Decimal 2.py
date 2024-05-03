lst = []
for i in range(int(input())):
    x = bin(int(input())).count("1")
    com = "0b"
    for i in range(x):
        com += "1"
    lst.append(int(com, 2))
    
for i in lst:
    print(i)