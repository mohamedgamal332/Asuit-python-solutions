x = int(input())

lst = [0, 1]

if x > 2:
    for i in range(2, x):
        lst.append(lst[i -1] + lst[i -2])
else:
     if x == 1:
          lst.remove(1)
          
for i in lst:
        print(i, end = " ")