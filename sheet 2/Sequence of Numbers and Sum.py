lst = []

while(1):
    a, b = [int(x) for x in input().split(" ")]
    if (a > 0 and b > 0):
        conc = ""
        count = 0
        for i in range(min(a, b), max(a, b) +1):
             conc += str(i) + " "
             count += i
        lst.append(conc)
        lst.append(count)
    else:
        break

for i in range(0, len(lst), 2):
    print(f"{lst[i]}sum ={lst[i +1]}")
