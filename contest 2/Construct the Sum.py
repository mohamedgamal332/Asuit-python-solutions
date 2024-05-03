import copy
lst = []

for i in range(int(input())):
    a, d = [int(x) for x in input().split(" ")]

    if ((a *(a +1)) / 2) < d:
        lst.append(-1)

    else:
        sum = 0
        coc = ""
        for z in range(a, 0, -1):
            if (sum + z) <= d:
                sum += z 
                coc += str(z)+" "
            if sum == d:
                break
        lst.append(coc)

print(*lst, sep="\n")



            

        
        
