x = input().split(" ")
for i in range(len(x)):
    x[i] = int(x[i])

l1, l2 = x[0], x[2]

sorted_list = []

for i in range(len(x)):
    sorted_list.append(min(x))
    x.remove(min(x))

if (sorted_list[0] == l1 and sorted_list[1] == l2) or (sorted_list[0] == l2 and sorted_list[1] == l1):
    print(f"{sorted_list[1]} {sorted_list[2]}")
else: 
    print(-1)
